import json
from api import GRPCAPI

class Node:
    def __init__(self, config):
        self.node_data = {
            "name": config['name'],
            "public": config['public'],
            "private": config['private'],
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
            "available_providers": None,
            "heartbeat": None
        }

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
            self.node_data["connected_peers"] = node_status.get("status", {}).get("connectedPeers", None)
            self.node_data["synced"] = node_status.get("status",  {}).get("isSynced", False)
            self.node_data["synced_layer"] = node_status.get("status",  {}).get("syncedLayer",  {}).get("number", None)
            self.node_data["top_layer"] = node_status.get("status",  {}).get("topLayer",  {}).get("number", None)
            self.node_data["verified_layer"] = node_status.get("status",  {}).get("verifiedLayer",  {}).get("number", None)
        else:
            #TODO: Handle Error
            pass

    def set_node_info(self):
        node_info = GRPCAPI.get_node_info(self.node_data["public"])

        if node_info:
            self.node_data["first_genesis"] = node_info.get("firstGenesis", None)
            self.node_data["epoch_size"] = node_info.get("epochSize", None)
            self.node_data["effective_genesis"] = node_info.get("effectiveGenesis", None)
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
        self.node_data["coinbase"] = coinbase.get("accountId",  {}).get("address", None)

    def set_post_setup_status(self):
        post_setup_status = GRPCAPI.get_post_setup_status(self.node_data["private"])
        if post_setup_status:
            self.node_data["post_state"] = post_setup_status.get("status",  {}).get("state", None)
            self.node_data["post_data_dir"] = post_setup_status.get("status",  {}).get("opts",  {}).get("dataDir", None)
            self.node_data["provider_id"] = post_setup_status.get("status",  {}).get("opts",  {}).get("providerId", None)

            max_file_size = post_setup_status.get("status",  {}).get("opts",  {}).get("maxFileSize", None)
            if(max_file_size):
                self.node_data["max_file_size_gib"] = int(int() / 1024**3)
            else:
                self.node_data["max_file_size_gib"] = None

            self.node_data["space_units"] = post_setup_status.get("status",  {}).get("opts",  {}).get("numUnits", None)
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

    def set_heartbeat(self, heartbeat):
        self.node_data["heartbeat"] = heartbeat
        
    def get_node_data(self):
        return self.node_data
    
    def print_node_data(self):
        print(json.dumps(self.node_data))