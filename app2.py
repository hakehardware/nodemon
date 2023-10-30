from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Static, Label, LoadingIndicator, Button, Log
from textual.containers import Container
from textual.binding import Binding
from textual import work
from textual import on

import json
from time import sleep
from node import Node
import threading
import asyncio

HEADERS = ["Name", "Version", "IP", "Peers", "Synced", "Top", "Verified", "Synced", "Smeshing", "PoST State", "SU", "GiB", "Layers"]

class NodeTable(Container):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True

        # Add headers to table
        for index, header in enumerate(HEADERS):
            table.add_column(header, key=str(index))



class NodeData(Container):
    def compose(self) -> ComposeResult:
        with Container(classes='box', id='node-data-logs'):
            yield Static("Logs (coming soon)")
        with Container(classes='box', id='node-data-info'):
            yield Label("Loading...", classes='light-background', id='node-data-smesher-id')
            yield Label("Loading...", classes='light-background', id='node-data-network')
            yield Label("Loading...", classes='light-background', id='node-data-smeshing')
            yield Label("Loading...", classes='light-background', id='node-data-layers')
            #yield Button("Copy Layers", id='btn-copy-layers')



class NodeLoading(Container):
    def compose(self) -> ComposeResult:
        yield Static('🥔  Harvesting Potatoes (please wait) 🥔', id='loading-message')
        yield LoadingIndicator(id="loading-indicator", name="Loading Node Data")


class Nodemon(App):

    BINDINGS = [
        Binding("h", "home()", "Home", show=True),
        Binding("q", "app.quit", "Quit", show=True)
    ]
    CSS_PATH = "nodemon.tcss"

    def __init__(self, config) -> None:
        self.node_data = []
        self.config = config
        self.is_loading = True
        self.first_load = True
        self.selected_node = None
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Container(id='node-container', classes='-hidden'):
            yield NodeTable(id='node-table')
            yield NodeData(id='node-data', classes='-hidden')

        yield NodeLoading(id='node-loading')
        yield Footer()

    def on_mount(self) -> None:
        self.node_worker()

    def action_home(self):
        if not self.is_loading:
            self.query_one(NodeData).add_class('-hidden')
            self.query_one(NodeTable).remove_class('-hidden')
            self.query_one(DataTable).focus()
            self.title = "Nodemon"

    @work(exclusive=True)
    async def node_worker(self):

        table = self.query_one(DataTable)

        nodes = []
        for node in self.config['nodes']:
            node_instance = Node(node)
            nodes.append(node_instance)

        while True:
            tasks = []

            for node in nodes:
                tasks.append(node.refresh_data())

            results = await asyncio.gather(*tasks)

            if self.first_load:
                self.query_one(NodeLoading).add_class('-hidden')
                self.query_one('#node-container').remove_class('-hidden')
                self.is_loading = False

            # For each node add a row
            for index, node in enumerate(nodes):
                node_data = node.get_data()
                self.node_data.append(node_data)

                if not table.is_valid_row_index(index):
                    table.add_row( *[
                        node_data['info']['node_name'], 
                        node_data['info']['version'], 
                        node_data['network']['host'], 
                        node_data['network']['peers'], 
                        node_data['network']['is_synced'],
                        node_data['network']['top_layer'], 
                        node_data['network']['verified_layer'], 
                        node_data['network']['synced_layer'], 
                        node_data['smeshing']['is_smeshing'], 
                        node_data['smeshing']['post_state'], 
                        node_data['smeshing']['space_units'], 
                        node_data['smeshing']['size_gib'], 
                        node_data['smeshing']['assign_layers_count'], 
                        ], key=str(index))
                else:
                    table.update_cell( str(index), "0", node_data['info']['node_name'])
                    table.update_cell( str(index), "1", node_data['info']['version'])
                    table.update_cell( str(index), "2", node_data['network']['host'])
                    table.update_cell( str(index), "3", node_data['network']['peers'])
                    table.update_cell( str(index), "4", node_data['network']['is_synced'])
                    table.update_cell( str(index), "5", node_data['network']['top_layer'])
                    table.update_cell( str(index), "6", node_data['network']['verified_layer'])
                    table.update_cell( str(index), "7", node_data['network']['synced_layer'])
                    table.update_cell( str(index), "8", node_data['smeshing']['is_smeshing'])
                    table.update_cell( str(index), "9", node_data['smeshing']['post_state'])
                    table.update_cell( str(index), "10", node_data['smeshing']['space_units'])
                    table.update_cell( str(index), "11", node_data['smeshing']['size_gib'])
                    table.update_cell( str(index), "12", node_data['smeshing']['assign_layers_count'])

            asyncio.sleep(60)

    # Displays data about the node that was selected
    @on(DataTable.RowSelected)
    def show_node_data(self, event):
        self.query_one(NodeTable).add_class('-hidden')
        self.query_one(NodeData).remove_class('-hidden')
        index = event.data_table.get_row_index(event.row_key)
        
        self.selected_node = self.node_data[index]
        name = f"{self.selected_node['name']} ({self.selected_node['version']})"
        self.title = f"Nodemon > {name}"

        self.query_one('#node-data-smesher-id').update(f"[b]Smesher ID:[/b] {self.selected_node['node_id']}")
        self.query_one('#node-data-network').update(f"{self.selected_node['host']} | {self.selected_node['connected_peers']} Peers | {'Synced' if self.selected_node['synced'] else 'Not Synced'} | T {self.selected_node['top_layer']} | S {self.selected_node['synced_layer']} | V {self.selected_node['verified_layer']}")
        self.query_one('#node-data-smeshing').update(f"{self.selected_node['post_state']} | {self.selected_node['size_gib']} GiB ({self.selected_node['space_units']} SU) | {self.selected_node['assigned_layers_count']} Layers")
        self.query_one('#node-data-layers').update(f"[b]Layers:[/b] {'None' if not self.selected_node['assigned_layers'] else ', '.join(map(str, self.selected_node['assigned_layers']))}")

    # @on(Button.Pressed, '#btn-copy-layers')
    # def on_copy(self):
    #     pyperclip.copy('None' if not self.selected_node['assigned_layers'] else ', '.join(map(str, self.selected_node['assigned_layers'])))
    #     self.query_one(Button).label = "COPIED"

if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    Nodemon(config).run()
