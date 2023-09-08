from node import Node
from time import sleep,time
from api import GRPCAPI,DynamoAPI


def main():
    print('starting..')
    node = Node()

    while True:
        print('Updating Node')
        node.set_highest_atx(GRPCAPI.get_highest_atx())
        node.set_version(GRPCAPI.get_version())
        node.set_build(GRPCAPI.get_build())
        node.set_node_status(GRPCAPI.get_node_status())
        node.set_node_info(GRPCAPI.get_node_info())
        node.set_is_smeshing(GRPCAPI.get_is_smeshing())
        node.set_smesher_id(GRPCAPI.get_smesher_id())
        node.set_coinbase(GRPCAPI.get_coinbase())
        node.set_post_setup_status(GRPCAPI.get_post_setup_status())
        node.set_post_setup_status_providers(GRPCAPI.get_post_setup_status_providers())
        node.set_heartbeat(time.time())
        
        print('Sending Update')
        response = DynamoAPI.send_update(node.get_node_data())
        if not response:
            print('Error Updating Dynamo')
        break
        sleep(5)


if __name__ == "__main__":
    main()