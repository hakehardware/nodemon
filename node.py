import json
from api import GRPCAPI
from time import time

class Node:
    def __init__(self, config):
        self.node_data = {
            "name": config['name'],
            "public": config['public'],
            "private": config['private'],
            "host": config['public'].split(':')[0],
            "highest_atx": None,
            "version": None,
            "build": None,
            "connected_peers": None,
            "synced": None,
            "synced_layer": None,
            "top_layer": None,
            "verified_layer": None,
            "first_genesis": None,
            "epoch_size": None,
            "effective_genesis": None,
            "smeshing": None,
            "node_id": None,
            "coinbase": None,
            "post_state": None,
            "post_data_dir": None,
            "provider_id": None,
            "max_file_size_gib": None,
            "space_units": None,
            "size_gib": None,
            "available_providers": None,
            "assigned_layers": None,
            "assigned_layers_count": None,
            "heartbeat": None,
            "current_epoch": None
        }
        self.event_stream = None
    # Setters
    def set_highest_atx(self):
        self.node_data["highest_atx"] = GRPCAPI.get_highest_atx(self.node_data["public"])

    def set_version(self):
        self.node_data["version"] = GRPCAPI.get_version(self.node_data["public"])

    def set_build(self):
        self.node_data["build"] = GRPCAPI.get_build(self.node_data["public"])

    def set_node_status(self):
        node_status = GRPCAPI.get_node_status(self.node_data["public"])
        if node_status:
            self.node_data["connected_peers"] = node_status.get("status", {}).get("connectedPeers", "None")
            self.node_data["synced"] = node_status.get("status",  {}).get("isSynced", False)
            self.node_data["synced_layer"] = node_status.get("status",  {}).get("syncedLayer",  {}).get("number", "0")
            self.node_data["top_layer"] = node_status.get("status",  {}).get("topLayer",  {}).get("number", "0")
            self.node_data["verified_layer"] = node_status.get("status",  {}).get("verifiedLayer",  {}).get("number", "0")

            if self.node_data["synced"]:
                self.node_data["current_epoch"] = self.node_data["top_layer"] // 4032
        else:
            #TODO: Handle Error
            pass

    def set_node_info(self):
        node_info = GRPCAPI.get_node_info(self.node_data["public"])

        if node_info:
            self.node_data["first_genesis"] = node_info.get("firstGenesis", "0")
            self.node_data["epoch_size"] = node_info.get("epochSize", "0")
            self.node_data["effective_genesis"] = node_info.get("effectiveGenesis", "0")
        else:
            #TODO: Handle Error
            pass

    def set_is_smeshing(self):
        is_smeshing = GRPCAPI.get_is_smeshing(self.node_data["private"])
        self.node_data["smeshing"] = is_smeshing.get("isSmeshing", False)

    def set_smesher_id(self):
        smesher_id = GRPCAPI.get_smesher_id(self.node_data["private"])
        self.node_data["node_id"] = smesher_id.get("publicKey")

    def set_coinbase(self):
        coinbase = GRPCAPI.get_coinbase(self.node_data["private"])
        self.node_data["coinbase"] = coinbase.get("accountId",  {}).get("address", "None")

    def set_post_setup_status(self):
        post_setup_status = GRPCAPI.get_post_setup_status(self.node_data["private"])
        if post_setup_status:
            self.node_data["post_state"] = post_setup_status.get("status",  {}).get("state", "None")
            self.node_data["post_data_dir"] = post_setup_status.get("status",  {}).get("opts",  {}).get("dataDir", "None")
            self.node_data["provider_id"] = post_setup_status.get("status",  {}).get("opts",  {}).get("providerId", "None")

            max_file_size = post_setup_status.get("status",  {}).get("opts",  {}).get("maxFileSize", None)
            if(max_file_size):
                self.node_data["max_file_size_gib"] = int(int() / 1024**3)
            else:
                self.node_data["max_file_size_gib"] = "0"

            self.node_data["space_units"] = post_setup_status.get("status",  {}).get("opts",  {}).get("numUnits", 0)
            if self.node_data["space_units"] > 0:
                self.node_data["size_gib"] = self.node_data["space_units"] * 64

        else:
            #TODO: Handle Error
            pass

    def set_post_setup_status_providers(self):
        post_setup_status_providers = GRPCAPI.get_post_setup_status_providers(self.node_data["private"])
        if post_setup_status_providers:
            providers = []
            for provider in post_setup_status_providers["providers"]:
                providers.append(provider["model"])

            self.node_data["available_providers"] = providers
        else:
            #TODO: Handle Error
            pass

    def set_assigned_layers_count(self):
        if not self.event_stream:
            self.get_event_stream()
        
        assigned_layers_count = 0


        for event in self.event_stream:
            eligibilities = event.get("eligibilities", None)
            if eligibilities and eligibilities['epoch'] == self.node_data['current_epoch']:
                self.node_data['assigned_layers'] = eligibilities['eligibilities']
                for layer in eligibilities['eligibilities']:
                    assigned_layers_count = layer['count'] + assigned_layers_count

        self.node_data['assigned_layers_count'] = assigned_layers_count

    def set_assigned_layers(self):
        if not self.event_stream:
            self.get_event_stream()

        for event in self.event_stream:
            eligibilities = event.get("eligibilities", None)
            if eligibilities and eligibilities['epoch'] == self.node_data['current_epoch']:
                self.set_assigned_layers = [item['layer'] for item in eligibilities['eligibilities'] for _ in range(item['count'])]

    def get_event_stream(self):
        self.event_stream = GRPCAPI.get_event_stream(self.node_data["private"])

    def set_heartbeat(self, heartbeat):
        self.node_data["heartbeat"] = heartbeat
        
    def get_node_data(self):
        return self.node_data
    
    def print_node_data(self):
        print(json.dumps(self.node_data))

    def load_all_data(self):
        self.set_highest_atx()
        self.set_version()
        self.set_build()
        self.set_node_status()
        self.set_node_info()
        self.set_is_smeshing()
        self.set_smesher_id()
        self.set_coinbase()
        self.set_post_setup_status()
        self.set_post_setup_status_providers()
        self.set_assigned_layers()
        self.set_assigned_layers_count()
        self.set_heartbeat(time())
