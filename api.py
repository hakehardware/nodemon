from grpc_lib import ActivationClient, AdminClient, NodeClient, SmesherClient, DebugClient, GlobalStateClient, MeshClient

class API:
    @staticmethod
    def get_highest_atx():
        try:
            activation_client = ActivationClient("localhost:9092")
            return activation_client.get_highest_atx()
        except Exception as e:
            print(e)
            return "Error getting highest ATX"
        

    def get_version():
        try:
            node_client = NodeClient("localhost:9092")
            return node_client.get_version()
        except Exception as e:
            print(e)
            return "Error getting App Version"
    
    def get_build():
        try:
            node_client = NodeClient("localhost:9092")
            return node_client.get_build()
        except Exception as e:
            print(e)
            return "Error getting App Build"

    def get_node_status():
        try:
            node_client = NodeClient("localhost:9092")
            return node_client.get_node_status()
        except Exception as e:
            print(e)
            return False

    def get_node_info():
        try:
            node_client = NodeClient("localhost:9092")
            return node_client.get_node_info()
        except Exception as e:
            print(e)
            return False
        
    def get_is_smeshing():
        try:
            smesher_client = SmesherClient("localhost:9093")
            return smesher_client.get_is_smeshing()
        except Exception as e:
            print(e)
            return False
        
    def get_smesher_id():
        try:
            smesher_client = SmesherClient("localhost:9093")
            return smesher_client.get_smesher_id()
        except Exception as e:
            print(e)
            return False
        

    def get_coinbase():
        try:
            smesher_client = SmesherClient("localhost:9093")
            return smesher_client.get_coinbase()
        except Exception as e:
            print(e)
            return False

    def get_post_setup_status():
        try:
            smesher_client = SmesherClient("localhost:9093")
            return smesher_client.get_post_setup_status()
        except Exception as e:
            print(e)
            return False


    def get_post_setup_status_providers():
        try:
            smesher_client = SmesherClient("localhost:9093")
            return smesher_client.get_post_setup_status_providers()
        except Exception as e:
            print(e)
            return False






# activation_client = ActivationClient("localhost:9092")
# admin_client = AdminClient("localhost:9093")
# node_client = NodeClient("localhost:9092")
# smesher_client = SmesherClient("localhost:9093")
# debug_client = DebugClient("localhost:9092")
# global_state_client = GlobalStateClient("localhost:9092")
# mesh_client = MeshClient("localhost:9092")

# print(mesh_client.get_genesis_id())