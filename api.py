from grpc_lib import ActivationClient, AdminClient, NodeClient, SmesherClient, DebugClient, GlobalStateClient, MeshClient
import traceback

class GRPCAPI:
    @staticmethod
    def get_highest_atx(ip):
        try:
            activation_client = ActivationClient(ip)
            return activation_client.get_highest_atx()
        except Exception as e:
            print(e)
            return "Error getting highest ATX"
        
    @staticmethod
    def get_version(ip):
        try:
            node_client = NodeClient(ip)
            return node_client.get_version()
        except Exception as e:
            print(e)
            return "Error getting App Version"
        
    @staticmethod
    def get_build(ip):
        try:
            node_client = NodeClient(ip)
            return node_client.get_build()
        except Exception as e:
            print(e)
            return "Error getting App Build"
        
    @staticmethod
    def get_node_status(ip):
        try:
            node_client = NodeClient(ip)
            return node_client.get_node_status()
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    def get_node_info(ip):
        try:
            node_client = NodeClient(ip)
            return node_client.get_node_info()
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def get_is_smeshing(ip):
        try:
            smesher_client = SmesherClient(ip)
            return smesher_client.get_is_smeshing()
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def get_smesher_id(ip):
        try:
            smesher_client = SmesherClient(ip)
            return smesher_client.get_smesher_id()
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def get_coinbase(ip):
        try:
            smesher_client = SmesherClient(ip)
            return smesher_client.get_coinbase()
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_post_setup_status(ip):
        try:
            smesher_client = SmesherClient(ip)
            return smesher_client.get_post_setup_status()
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_post_setup_status_providers(ip):
        try:
            smesher_client = SmesherClient(ip)
            return smesher_client.get_post_setup_status_providers()
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def get_event_stream(ip):
        try:
            admin_client = AdminClient(ip)
            return admin_client.get_event_stream()
        except Exception as e:
            print(e)
            traceback.print_exc()
            return False