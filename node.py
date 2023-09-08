import json

class Node:
    def __init__(self):
        self.node_data = {
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
    def set_highest_atx(self, highest_atx):
        self.node_data["highest_atx"] = highest_atx

    def set_version(self, version):
        self.node_data["version"] = version

    def set_build(self, build):
        self.node_data["build"] = build

    def set_node_status(self, node_status):
        node_status = node_status
        if node_status:
            self.node_data["connected_peers"] = node_status["status"]["connectedPeers"]
            self.node_data["synced"] = node_status["status"]["isSynced"]
            self.node_data["synced_layer"] = node_status["status"]["syncedLayer"]["number"]
            self.node_data["top_layer"] = node_status["status"]["topLayer"]["number"]
            self.node_data["verified_layer"] = node_status["status"]["verifiedLayer"]["number"]
        else:
            #TODO: Handle Error
            pass

    def set_node_info(self, node_info):
        node_info = node_info

        if node_info:
            self.node_data["first_genesis"] = node_info["firstGenesis"]
            self.node_data["epoch_size"] = node_info["epochSize"]
            self.node_data["effective_genesis"] = node_info["effectiveGenesis"]
        else:
            #TODO: Handle Error
            pass

    def set_is_smeshing(self, is_smeshing):
        self.node_data["smeshing"] = is_smeshing["isSmeshing"]

    def set_smesher_id(self, smesher_id):
        self.node_data["node_id"] = smesher_id["publicKey"]

    def set_coinbase(self, coinbase):
        self.node_data["coinbase"] = coinbase["accountId"]["address"]

    def set_post_setup_status(self, post_setup_status):
        if post_setup_status:
            self.node_data["post_state"] = post_setup_status["status"]["state"]
            self.node_data["post_data_dir"] = post_setup_status["status"]["opts"]["dataDir"]
            self.node_data["provider_id"] = post_setup_status["status"]["opts"]["providerId"]
            self.node_data["max_file_size_gib"] = int(int(post_setup_status["status"]["opts"]["maxFileSize"]) / 1024**3)
            self.node_data["space_units"] = post_setup_status["status"]["opts"]["numUnits"]
        else:
            #TODO: Handle Error
            pass

    def set_post_setup_status_providers(self, post_setup_status_providers):
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