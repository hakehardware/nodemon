from itertools import cycle
import asyncio
from textual.app import App, ComposeResult
from textual.widgets import DataTable
from textual import work
import json
from node import Node
from time import sleep,time

HEADERS = ["Name", "Version", "IP", "Peers", "Synced", "Top Layer", "Verified Layer", "Synced Layer", "Smeshing", "PoST State", "Space Units", "GiB"]

class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True

        for index, header in enumerate(HEADERS):
            table.add_column(header, key=str(index))

        table.zebra_stripes = True
        self.update_node_data()


    @work(thread=True)
    def update_node_data(self) -> None:
        with open('example.config.json', 'r') as config_file:
            config = json.load(config_file)

        nodes = []
        for node in config['nodes']:
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
                node_data.append(node.get_node_data())


            table = self.query_one(DataTable)
            for index, data in enumerate(node_data):
                #HEADERS = ["Name", "Version", "IP", "Peers", "Synced", "Top Layer", "Verified Layer", "Synced Layer", "Smeshing", "PoST State", "Space Units", "GiB"]

                if not table.is_valid_row_index(index):
                    table.add_row(data['name'], data['version'], data['host'], data['connected_peers'], str(data['synced']), str(data['top_layer']), str(data['verified_layer']), str(data['synced_layer']), str(data['smeshing']), str(data['post_state']), str(data['space_units']), str(data['size_gib']), key=str(index))
                else:
                    table.update_cell(str(index), "0", str(data['name']))
                    table.update_cell(str(index), "1", str(data['version']))
                    table.update_cell(str(index), "2", str(data['host']))
                    table.update_cell(str(index), "3", str(data['connected_peers']))
                    table.update_cell(str(index), "4", str(data['synced']))
                    table.update_cell(str(index), "5", str(data['top_layer']))
                    table.update_cell(str(index), "6", str(data['verified_layer']))
                    table.update_cell(str(index), "7", str(data['synced_layer']))
                    table.update_cell(str(index), "8", str(data['smeshing']))
                    table.update_cell(str(index), "9", str(data['post_state']))
                    table.update_cell(str(index), "10", str(data['space_units']))
                    table.update_cell(str(index), "11", str(data['size_gib']))

            sleep(5)


app = TableApp()
if __name__ == "__main__":
    app.run()