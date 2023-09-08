from node import Node
from time import sleep
from api import API

def main():
    print('starting..')
    node = Node()

    while True:
        print('Updating Node')
        node.set_highest_atx(API.get_highest_atx())
        node.set_version(API.get_version())
        node.set_build(API.get_build())
        node.set_node_status(API.get_node_status())
        node.set_node_info(API.get_node_info())
        node.set_is_smeshing(API.get_is_smeshing())
        node.set_smesher_id(API.get_smesher_id())
        node.set_coinbase(API.get_coinbase())
        node.set_post_setup_status(API.get_post_setup_status())
        node.set_post_setup_status_providers(API.get_post_setup_status_providers())
        node.print_node_data()
        break


if __name__ == "__main__":
    main()