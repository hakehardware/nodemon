from grpc_lib import ActivationClient, AdminClient, NodeClient, SmesherClient, DebugClient, GlobalStateClient, MeshClient
from dotenv import dotenv_values
import boto3
import botocore.exceptions
import requests
import json

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

class DynamoAPI:
    @staticmethod
    def get_session_token():
        creds = dotenv_values(".env")
        username = creds["username"]
        password = creds["password"]

        # Cognito Client information
        client_id = '871tds7bo65vp67aiqthk8cab'

        # Initialize Cognito client
        cognito = boto3.client('cognito-idp', region_name='us-west-2')

        try:
            # Sign in using the username and password
            response = cognito.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': password
                },
                ClientId=client_id
            )

            return response["AuthenticationResult"]["IdToken"]


        except botocore.exceptions.ClientError as e:
            print(f"Login failed: {e}")
            return False


    @staticmethod
    def send_update(node_data):


        session_token = DynamoAPI.get_session_token()

        if session_token:
            # Replace with the URL of your API Gateway endpoint
            api_url = 'https://i35gx8ssbe.execute-api.us-west-2.amazonaws.com/dev/update-node'

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {session_token}'
            }

            try:
                print(node_data)
                response = requests.post(api_url, json=node_data, headers=headers)

                if response.status_code == 200:
                    print("Request was successful")
                    return True
                else:
                    print(f"Request failed with status code: {response.status_code}")
                    return False

            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                return False


# activation_client = ActivationClient("localhost:9092")
# admin_client = AdminClient("localhost:9093")
# node_client = NodeClient("localhost:9092")
# smesher_client = SmesherClient("localhost:9093")
# debug_client = DebugClient("localhost:9092")
# global_state_client = GlobalStateClient("localhost:9092")
# mesh_client = MeshClient("localhost:9092")

# print(mesh_client.get_genesis_id())