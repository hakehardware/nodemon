import json
from api import GRPCAPI
from time import time
from datetime import datetime
import asyncio
import traceback

class Node:
    def __init__(self, config) -> None:
        self.info = {
            "node_name": config['name'],
            "version": None,
            "build": None,
            "heartbeat": None
        }

        self.network = {
            "public_address": config['public'],
            "private_address": config['private'],
            "host": config['public'].split(':')[0],
            "peers": None,
            "is_synced": False,
            "synced_layer": None,
            "top_layer": None,
            "verified_layer": None,
            "highest_atx": None,
            "current_epoch": None
        }

        self.genesis = {
            "first_genesis": None,
            "epoch_size": None,
            "effective_genesis": None
        }

        self.smeshing = {
            "is_smeshing": None,
            "node_id": None,
            "coinbase": None,
            "post_state": None,
            "post_data_dir": None,
            "provider_id": None,
            "max_file_size_gib": None,
            "space_units": None,
            "size_gib": None,
            "assigned_layers": None
        }

        self.rewards = None #TODO

        self.atx = None #TODO

    async def refresh_data(self):

        try:
            tasks = [
                GRPCAPI.get_version(self.network["public_address"]),
                GRPCAPI.get_build(self.network["public_address"]),
                GRPCAPI.get_highest_atx(self.network["public_address"]),
                GRPCAPI.get_node_status(self.network["public_address"]),
                GRPCAPI.get_node_info(self.network["public_address"]),
                GRPCAPI.get_is_smeshing(self.network["private_address"]),
                GRPCAPI.get_smesher_id(self.network["private_address"]),
                GRPCAPI.get_coinbase(self.network["private_address"]),
                GRPCAPI.get_post_setup_status(self.network["private_address"]),
                GRPCAPI.get_post_setup_status_providers(self.network["private_address"]),
                GRPCAPI.get_event_stream(self.network["private_address"])
            ]

            results = await asyncio.gather(*tasks)

            # Set Info
            self.info['version'] = results[0]['version']
            self.info['build'] = results[1]['build']
            self.info['heartbeat'] = datetime.now()

            # Set Network
            self.network['peers'] = results[3]['peers']
            self.network['is_synced'] = results[3]['is_synced']
            self.network['synced_layer'] = results[3]['synced_layer']
            self.network['top_layer'] = results[3]['top_layer']
            self.network['verified_layer'] = results[3]['verified_layer']
            self.network['highest_atx'] = results[2]['highest_atx']
            self.network['current_epoch'] = results[3]['current_epoch']

            # Set Genesis
            self.genesis['first_genesis'] = results[4]['first_genesis']
            self.genesis['epoch_size'] = results[4]['epoch_size']
            self.genesis['effective_genesis'] = results[4]['effective_genesis']

            # Set Smeshing
            self.smeshing['is_smeshing'] = results[5]['is_smeshing']
            self.smeshing['node_id'] = results[6]['node_id']
            self.smeshing['coinbase'] = results[7]['coinbase']
            self.smeshing['post_state'] = results[8]['post_state']
            self.smeshing['post_data_dir'] = results[8]['post_data_dir']
            self.smeshing['provider_id'] = results[8]['provider_id']
            self.smeshing['max_file_size_gib'] = results[8]['max_file_size_gib']
            self.smeshing['space_units'] = results[8]['space_units']
            self.smeshing['size_gib'] = results[8]['size_gib']
            self.smeshing['assigned_layers'] = results[10]

        except Exception as e:
            traceback.print_exc()

        
