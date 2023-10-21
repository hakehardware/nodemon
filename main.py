from node import Node
from time import sleep,time
from api import GRPCAPI
import json

def main():
    # Open and load the JSON config file
    with open('example.config.json', 'r') as config_file:
        config = json.load(config_file)
        
    nodes = []
    print('starting nodes')

    for node in config['nodes']:
        print(f'Node {node["name"]}')
        node_instance = Node(node)
        nodes.append(node_instance)

    while True:
        node_data = []
        for node in nodes:
            print('Updating Node')
            node.set_highest_atx()
            node.set_version()
            node.set_build()
            node.set_node_status()
            node.set_node_info()
            node.set_is_smeshing()
            node.set_smesher_id()
            node.set_coinbase()
            node.set_post_setup_status()
            node.set_post_setup_status_providers()
            node.set_heartbeat(time())
        
            print('Sending Update')
            node_data.append(node.get_node_data())

        print(node_data)
        sleep(60)


if __name__ == "__main__":
    main()