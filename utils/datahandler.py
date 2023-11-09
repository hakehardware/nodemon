import asyncio
from node import Node
from api import ExplorerAPI, DatabaseAPI
from datetime import datetime, timedelta

class DataHandler:
    @staticmethod
    async def handle_data(config,verbose = True):
        # Instantiate All Drives
        nodes = [Node(node) for node in config['nodes']]

        # Create tasks for asyncio
        tasks = [node.refresh_data() for node in nodes]

        # Run tasks
        await asyncio.gather(*tasks)

        # Get data from nodes
        node_data = [node.get_data() for node in nodes]
        layers = ExplorerAPI.get_layers()
        # print(len(layers))

        # Get Layer Data
        last_network_layer = DataHandler.get_last_network_layer(layers)
        print(last_network_layer) if verbose else False

        last_network_layer_start_time = DataHandler.get_last_network_layer_start_time(last_network_layer)
        print(last_network_layer_start_time) if verbose else False

        # This data stores node-specific data
        total_space_units = 0
        total_not_synced = 0
        total_post_gib = 0
        total_offline = 0
        total_nodes = len(node_data)
        all_assigned_layers = []

        for node in node_data:
            if node['info']['status'] == "Online":

                # Space Units
                if node['smeshing']['space_units']:
                    total_space_units+=node['smeshing']['space_units']

                # Sync State
                if not node['network']['is_synced']:
                    total_not_synced+=1

                # PoST GiB
                if node['smeshing']['size_gib']:
                    total_post_gib+=node['smeshing']['size_gib']

                # Assigned Layers
                assigned_layers = DataHandler.get_assigned_layers(
                    node, 
                    last_network_layer_start_time,
                    last_network_layer['Number'])
                all_assigned_layers.extend(assigned_layers)
                print(assigned_layers) if verbose else False
            else:
                total_offline+=1

        all_assigned_layers = sorted(all_assigned_layers, key=lambda x:x['Layer'])
        print(f"All Assigned Layers: {len(all_assigned_layers)}") if verbose else False

        rewards = DataHandler.get_rewards(all_assigned_layers, last_network_layer['Epoch'], config)

        DataHandler.append_rewards(rewards, all_assigned_layers)

        next_layer = DataHandler.get_next_layer(all_assigned_layers)

        return {
            'Node Data': node_data,
            'All Assigned Layers': all_assigned_layers,
            'Last Network Layer': last_network_layer,
            'Total Space Units': total_space_units,
            'Total Not Synced': total_not_synced,
            'Total PoST GiB': total_post_gib,
            'Total Nodes': total_nodes,
            'Total Offline': total_offline,
            'Next Layer': next_layer,
            'Rewards': rewards
        }
        


    @staticmethod
    def get_last_network_layer(layers):
        """The last network layer that was completed"""
        if not layers:
            return None
        
        layers = sorted(layers, key=lambda x: x['number'], reverse=True)
        return {
            'Number': layers[0]['number'],
            'Status': layers[0]['status'],
            'Transactions': layers[0]['txs'],
            'Start Time': layers[0]['start'],
            'End Time': layers[0]['end'],
            'Transactions Amount': layers[0]['txsamount'],
            'ATX Num Units': layers[0]['atxnumunits'],
            'Rewards': layers[0]['rewards'],
            'Epoch': layers[0]['epoch'],
            'Smeshers': layers[0]['smeshers'],
            'Hash': layers[0]['hash'],
            'Blocks Number': layers[0]['blocksnumber'],
        }
            
    
    @staticmethod
    def get_last_network_layer_start_time(last_network_layer):
        """Takes in the last network layer and returns the start time"""
        if not last_network_layer:
            return None
        return datetime.fromtimestamp(last_network_layer['Start Time'])
    
    @staticmethod
    def get_next_layer(all_assigned_layers):
        for layer in all_assigned_layers:
            if layer['State'] == 'Current':
                return layer
            if layer['State'] == 'Waiting':
                return layer
        
        return None
    
    @staticmethod
    def get_assigned_layers(node, last_network_layer_start_time, last_layer):
        raw_layers = node['smeshing']['assigned_layers']
        assigned_layers = []
        if raw_layers:
            for layer in raw_layers:

                min_to_layer = (layer - last_layer)*5
                current_layer = last_layer + 1
                state = None

                if current_layer + 1 == layer:
                    state = 'Current'
                elif layer > current_layer:
                    state = 'Waiting'
                elif layer < current_layer:
                    state = 'Old'

                assigned_layers.append({
                    'Node Name': node['info']['node_name'],
                    'Coinbase': node['smeshing']['coinbase'],
                    'Layer': layer,
                    'Layer Time': (last_network_layer_start_time + timedelta(minutes=min_to_layer)),
                    'State': state,
                    'Layers to Layer': layer - last_layer,
                    'Minutes to Layer': (layer - last_layer)*5,
                    'Reward': None
                })

        assigned_layers = sorted(assigned_layers, key=lambda x: x['Layer'])
        return assigned_layers
    
    @staticmethod
    def get_rewards(layers, epoch, config):
        #print(layers)
        try:
            coinbases = set(entry['Coinbase'] for entry in layers)
            rewards = []

            for coinbase in coinbases:
                rewards.extend(DatabaseAPI.get_rewards(coinbase, epoch, config['state_file']))

            return rewards
        except:
            return None
    
    @staticmethod
    def append_rewards(rewards, layers):
        if not rewards:
            for layer in layers:
                layer['Reward'] = 'N/A'
            return None
        
        for reward in rewards:
            coinbase = reward['Coinbase']
            layer = reward['Layer']
            nodes = list(filter(lambda entry: entry.get('Layer') == layer and entry.get('Coinbase') == coinbase, layers))

            if len(nodes) == 1:
                nodes[0]['Reward'] = reward['Reward']

            if len(nodes) > 1:
                for node in nodes:
                    if not node['Reward']:
                        node['Reward'] = reward['Reward']
    
