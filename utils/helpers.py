from datetime import datetime, timedelta
from dateutil import tz
import bech32

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
