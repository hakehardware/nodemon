from grpc_lib import ActivationClient, AdminClient, NodeClient, SmesherClient
from utils.helpers import Helpers
import traceback
import asyncio
import sqlite3
import requests
import binascii
import base64

class GRPCAPI:
    @staticmethod
    async def get_highest_atx(ip):
        try:
            activation_client = ActivationClient(ip)
            results = await asyncio.to_thread(activation_client.get_highest_atx)

            data = {
                'highest_atx': results
            }

            return data
        except Exception as e:
            print(e)
            return "Error getting highest ATX"
        
    @staticmethod
    async def get_version(ip):
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_version)

            data = {
                'version': results
            }

            return data
        
        except Exception as e:
            print(e)
            return "Error getting App Version"
        
    @staticmethod
    async def get_build(ip):
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_build)

            data = {
                'build': results
            }

            return data
        
        except Exception as e:
            print(e)
            return "Error getting App Build"
        
    @staticmethod
    async def get_node_status(ip):
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_node_status)

            data = {
                'peers': results.get("status", {}).get("connectedPeers", "None"),
                'is_synced': results.get("status",  {}).get("isSynced", False),
                'synced_layer': results.get("status",  {}).get("syncedLayer",  {}).get("number", "0"),
                'top_layer': results.get("status",  {}).get("topLayer",  {}).get("number", "0"),
                'verified_layer': results.get("status",  {}).get("verifiedLayer",  {}).get("number", "0"),
                'current_epoch': None
            }

            if data['is_synced']:
                data['current_epoch'] = data["top_layer"] // 4032

            return data
        
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    async def get_node_info(ip):
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_node_info)

            data = {
                'first_genesis': results.get("firstGenesis", "0"),
                'epoch_size': results.get("epochSize", "0"),
                'effective_genesis': results.get("effectiveGenesis", "0")
            }

            return data
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    async def get_is_smeshing(ip):
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_is_smeshing)

            data = {
                'is_smeshing': results.get("isSmeshing", False)
            }

            return data

        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    async def get_smesher_id(ip):
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_smesher_id)
            node_id = results.get("publicKey", None)
            base64_bytes = base64.b64decode(node_id)
            node_id_hex = binascii.hexlify(base64_bytes).decode('utf-8')

            data = {
                'node_id': node_id,
                'node_id_hex': node_id_hex,
            }

            return data
        
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    async def get_coinbase(ip):
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_coinbase)

            data = {
                'coinbase': results.get("accountId",  {}).get("address", None)
            }

            return data
        
        except Exception as e:
            print(e)
            return False

    @staticmethod
    async def get_post_setup_status(ip):
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_post_setup_status)

            post_state = results.get("status",  {}).get("state", None)
            post_data_dir = results.get("status",  {}).get("opts",  {}).get("dataDir", None)
            provider_id = results.get("status",  {}).get("opts",  {}).get("providerId", None)
            max_file_size = results.get("status",  {}).get("opts",  {}).get("maxFileSize", None)
            space_units = results.get("status",  {}).get("opts",  {}).get("numUnits", 0)

            data = {
                'max_file_size_gib': int(int(max_file_size) / 1024**3) if max_file_size else 0,
                'space_units': space_units,
                'size_gib': space_units * 64 if space_units > 0 else 0,
                'post_state': post_state,
                'post_data_dir': post_data_dir,
                'provider_id': provider_id
            }

            return data
        except Exception as e:
            print(e)
            return False

    @staticmethod
    async def get_post_setup_status_providers(ip):
        return None # Not needed but don't want to do a big refactor
        try:

            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_post_setup_status_providers)
            providers = []

            for provider in results["providers"]:
                providers.append(provider["model"])

            data = {
                'available_providers': providers
            }

            return data
        
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    async def get_event_stream(ip):
        # TODO: Implement Stream Parser

        try:
            admin_client = AdminClient(ip)
            results = await asyncio.to_thread(admin_client.get_event_stream)

            events = []

            for event in results:
                eligibilities = event.get("eligibilities", None)
                poetwaitproof = event.get("poetWaitProof", None)
                beacon = event.get("beacon", None)
                init_start = event.get("initStart", None)
                init_complete = event.get("initComplete", None)

                if eligibilities:
                    # and eligibilities['epoch'] == self.node_data['current_epoch']:
                    layers = [item['layer'] for item in eligibilities['eligibilities'] for _ in range(item['count'])]
                    log = ""
                    events.append({
                        'event_name': 'Layer Eligibilities',
                        'epoch': eligibilities['epoch'],
                        'log': event['help'],
                        'timestamp': Helpers.get_date(event['timestamp']),
                        'layers': layers,
                        'eligibilities': eligibilities['eligibilities']
                    })
                    
                elif poetwaitproof:
                    events.append({
                        'event_name': 'PoET Wait Proof',
                        'target_epoch': event['poetWaitProof']['target'],
                        'publish_epoch': event['poetWaitProof']['publish'],
                        'wait': int(event['poetWaitProof']['wait'].split('.')[0]),
                        'log': event['help'],
                        'timestamp': Helpers.get_date(event['timestamp'])
                    })

                elif beacon:
                    pass

                elif init_start:
                    pass

                elif init_complete:
                    pass
                    
                else:
                    events.append({
                        'timestamp': Helpers.get_date(event['timestamp']),
                        'log': event['help'],
                    })
                    
            return events


        except Exception as e:
            print(e)
            traceback.print_exc()
            return False
        


class ExplorerAPI:      
    def get_layers():
        url = "https://mainnet-explorer-1-api.spacemesh.network/layers"
        response = requests.get(url)
        data = None

        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data['data']
        
        return data


class DatabaseAPI:
    @staticmethod
    def get_rewards(coinbase, epoch, db_location):
        hex_coinbase = Helpers.bech32_to_hex(coinbase)

        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()
        query = f'select * from rewards where lower(hex(coinbase)) = "{hex_coinbase}"'

        cursor.execute(query)
        results = cursor.fetchall()

        rewards = []
        for r in results:
            reward_epoch = int(r[1]/4032)
            reward = round(r[2] / 1000000000, 3)
            if epoch == reward_epoch:
                rewards.append({
                    'Coinbase': Helpers.hex_to_bech32(r[0]), 
                    'Epoch': reward_epoch, 
                    'Layer': r[1],
                    'Reward': reward
                })

        return rewards

    async def get_transactions(coinbase):
        pass

    