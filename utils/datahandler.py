import asyncio
from node import Node
from api import ExplorerAPI
from datetime import datetime, timedelta
from dateutil import tz

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
        layers = await ExplorerAPI.get_layers()

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
            print
            if node['info']['status'] == "Online":
                # Space Units
                total_space_units+=node['smeshing']['space_units']

                # Sync State
                if not node['network']['is_synced']:
                    total_not_synced+=1

                # PoST GiB
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
            'Next Layer': next_layer
        }
        


    @staticmethod
    def get_last_network_layer(layers):
        """The last network layer that was completed"""
        layers = sorted(layers, key=lambda x: x['number'], reverse=True)
        print(layers)
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
        return datetime.fromtimestamp(last_network_layer['Start Time'])
    
    @staticmethod
    def get_next_layer(all_assigned_layers):
        for layer in all_assigned_layers:
            if layer['State'] == 'Current':
                return layer
            if layer['State'] == 'Pending':
                return layer
    
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
                    state = 'Pending'
                elif layer < current_layer:
                    state = 'Old'

                assigned_layers.append({
                    'Node Name': node['info']['node_name'],
                    'Layer': layer,
                    'Layer Time': (last_network_layer_start_time + timedelta(minutes=min_to_layer)),
                    'State': state,
                    'Layers to Layer': layer - last_layer,
                    'Minutes to Layer': (layer - last_layer)*5
                })

        assigned_layers = sorted(assigned_layers, key=lambda x: x['Layer'])
        return assigned_layers