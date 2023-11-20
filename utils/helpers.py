from datetime import datetime, timedelta
from dateutil import tz
import bech32
import csv
import json

class Helpers:
    @staticmethod
    def get_date(data):

        # Define UTC and your local time zone
        utc_zone = tz.tzutc()
        local_zone = tz.tzlocal()

        # Remove the fractional seconds and 'Z' from the input string
        data = data.split('.')[0]
        data = data.rstrip('Z')

        # Convert the input string to a datetime object with UTC time zone
        utc_datetime = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S")
        utc_datetime = utc_datetime.replace(tzinfo=utc_zone)

        # Convert the UTC datetime to the local time zone
        local_datetime = utc_datetime.astimezone(local_zone)

        return local_datetime.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def round_to_nearest_minute(data):
        data_seconds = data.second

        if data_seconds > 0 and data_seconds < 30:
            data = data - timedelta(seconds=data_seconds)
        else:
            seconds_off = 60-data_seconds
            data = data + timedelta(seconds=seconds_off)

        return data
    
    @staticmethod
    def generate_node_info(data):
        if data['info']['status'] == 'Online':

            return f"""\
| Top Layer | Verified Layer | Synced Layer | Peers | Synced |
| --------- | -------------- | ------------ | ----- | ------ |
| {data['network']['top_layer']} | {data['network']['verified_layer']} | {data['network']['synced_layer']} | {data['network']['peers']} | {data['network']['is_synced']}

**Node ID:** {data['smeshing']['node_id']}

**Node ID Hex:** {data['smeshing']['node_id_hex']}

**Coinbase:** {data['smeshing']['coinbase']}

### Smeshing

**Assigned Layers:** {", ".join(map(str, data['smeshing']['assigned_layers'])) if data['smeshing']['assigned_layers'] else "None"}

**Post State:** {data['smeshing']['post_state']}

**PoST Directory:** {data['smeshing']['post_data_dir']}

**Space Units:** {data['smeshing']['space_units']}

**Size:** {data['smeshing']['size_gib']}


"""
        else:
            return """Node Offline"""
        
    @staticmethod
    def bech32_to_hex(bech32_string):
        """Decode a bech32 encoded string into its hex representation."""
        hrp, words = bech32.bech32_decode(bech32_string)
        data = bech32.convertbits(words, frombits=5, tobits=8, pad=False)
        return bytes(data).hex()
    
    @staticmethod
    def hex_to_bech32(hex_string):
        """Encode a hexadecimal string as a Bech32 string."""
        # Convert the hex string to bytes
        data = hex_string
        
        # Convert bytes to a list of integers
        byte_list = list(data)

        # Convert the byte list to words with 5-bit encoding
        words = bech32.convertbits(byte_list, frombits=8, tobits=5, pad=True)
        
        # Encode the words as Bech32 with the specified HRP
        bech32_string = bech32.bech32_encode("sm", words)
        
        return bech32_string

    @staticmethod
    def write_csv(layers, node_data, options_selected):
        if options_selected['Layers CSV']:
            export_layers = []
            for layer in layers:
                export_layers.append([
                    layer['Node Name'],
                    layer['Coinbase'],
                    layer['Layer'],
                    layer['Layer Time'].strftime("%b %d, %Y %H:%M:%S"),
                    layer['State'],
                    layer['Layers to Layer'],
                    layer['Minutes to Layer'],
                    layer['Reward'] if layer['Reward'] else 0
                ])
            with open('layers.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(export_layers)

        if options_selected['Layers JSON']:
            export_layers = {}
            for node in node_data:
                node_id = node['smeshing']['node_id_hex']
                result = next(filter(lambda d: d.get('event_name') == 'Layer Eligibilities' and node_data['network']['current_epoch'] == d.get('epoch'), node['logs']), None)
                if result:
                    export_layers[node_id] = result['eligibilities']
                

            with open('layers.json', 'w') as json_file:
                json.dump(export_layers, json_file, indent=4)

        if(options_selected['Nodes JSON']):
            export_node = {}
            for node in node_data:
                node_id = node['smeshing']['node_id_hex']
                export_node[node_id] = {
                    'Node Name': node['info']['node_name'],
                    'Node ID': node['smeshing']['node_id'],
                    'Status': node['info']['status'], 
                    'Version': node['info']['version'], 
                    'Host': node['network']['host'], 
                    'Peers': node['network']['peers'], 
                    'Is Synced': node['network']['is_synced'],
                    'Top Layer': node['network']['top_layer'], 
                    'Verified Layer': node['network']['verified_layer'], 
                    'Synced Layer': node['network']['synced_layer'], 
                    'Is Smeshing': node['smeshing']['is_smeshing'], 
                    'PoST State': node['smeshing']['post_state'], 
                    'Space Units': node['smeshing']['space_units'], 
                    'Size GiB': node['smeshing']['size_gib'], 
                    'Assigned Layers Count': node['smeshing']['assigned_layers_count'],
                    'Assinged Layers': node['smeshing']['assigned_layers']
                }
            with open('nodes.json', 'w') as json_file:
                json.dump(export_node, json_file, indent=4)

        if(options_selected['Nodes CSV']):
            export_nodes = []
            for node in node_data:
                export_nodes.append([                    
                    node['info']['node_name'],
                    node['info']['status'], 
                    node['info']['version'], 
                    node['network']['host'], 
                    node['network']['peers'], 
                    node['network']['is_synced'],
                    node['network']['top_layer'], 
                    node['network']['verified_layer'], 
                    node['network']['synced_layer'], 
                    node['smeshing']['is_smeshing'], 
                    node['smeshing']['post_state'], 
                    node['smeshing']['space_units'], 
                    node['smeshing']['size_gib'], 
                    node['smeshing']['assigned_layers_count']
                ])
            with open('nodes.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(export_nodes)