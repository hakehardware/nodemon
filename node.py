import json

class Node:
    def __init__(self):
        self.node_data = {
            "Highest ATX": None,
            "Version": None,
            "Build": None,
            "Connected Peers": None,
            "Synced": None,
            "Synced Layer": None,
            "Top Layer": None,
            "Verified Layer": None,
            "First Genesis": None,
            "Epoch Size": None,
            "Effective Genesis": None,
            "Smeshing": None,
            "Smesher ID": None,
            "Coinbase": None,
            "PoST State": None,
            "PoST Dat Dir": None,
            "Provider ID": None,
            "Max File Size GiB": None,
            "Space Units (SU)": None,
            "Available Providers": None
        }

    # Setters
    def set_highest_atx(self, highest_atx):
        self.node_data["Highest ATX"] = highest_atx

    def set_version(self, version):
        self.node_data["Version"] = version

    def set_build(self, build):
        self.node_data["Build"] = build

    def set_node_status(self, node_status):
        node_status = node_status
        if node_status:
            self.node_data["Connected Peers"] = node_status["status"]["connectedPeers"]
            self.node_data["Synced"] = node_status["status"]["isSynced"]
            self.node_data["Synced Layer"] = node_status["status"]["syncedLayer"]["number"]
            self.node_data["Top Layer"] = node_status["status"]["topLayer"]["number"]
            self.node_data["Verified Layer"] = node_status["status"]["verifiedLayer"]["number"]
        else:
            #TODO: Handle Error
            pass

    def set_node_info(self, node_info):
        node_info = node_info

        if node_info:
            self.node_data["First Genesis"] = node_info["firstGenesis"]
            self.node_data["Epoch Size"] = node_info["epochSize"]
            self.node_data["Effective Genesis"] = node_info["effectiveGenesis"]
        else:
            #TODO: Handle Error
            pass

    def set_is_smeshing(self, is_smeshing):
        self.node_data["Smeshing"] = is_smeshing["isSmeshing"]

    def set_smesher_id(self, smesher_id):
        self.node_data["Smesher ID"] = smesher_id["publicKey"]

    def set_coinbase(self, coinbase):
        self.node_data["Coinbase"] = coinbase["accountId"]["address"]

    def set_post_setup_status(self, post_setup_status):
        if post_setup_status:
            self.node_data["PoST State"] = post_setup_status["status"]["state"]
            self.node_data["PoST Data Dir"] = post_setup_status["status"]["opts"]["dataDir"]
            self.node_data["Provider ID"] = post_setup_status["status"]["opts"]["providerId"]
            self.node_data["Max File Size GiB"] = int(post_setup_status["status"]["opts"]["maxFileSize"]) / 1024**3
            self.node_data["Space Units (SU)"] = post_setup_status["status"]["opts"]["numUnits"]
        else:
            #TODO: Handle Error
            pass

    def set_post_setup_status_providers(self, post_setup_status_providers):
        if post_setup_status_providers:
            providers = []
            for provider in post_setup_status_providers["providers"]:
                providers.append(provider["model"])

            self.node_data["Available Providers"] = providers
        else:
            #TODO: Handle Error
            pass

    def get_node_data(self):
        return self.node_data
    
    def print_node_data(self):
        print(json.dumps(self.node_data))