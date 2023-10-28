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
import pyperclip

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
            yield Static("Loading...", classes='light-background', id='node-data-smesher-id')
            yield Static("Loading...", classes='light-background', id='node-data-network')
            yield Static("Loading...", classes='light-background', id='node-data-smeshing')
            yield Static("Loading...", classes='light-background', id='node-data-layers')
            yield Button("Copy Layers", id='btn-copy-layers')



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

    @work(thread=True)
    def node_worker(self):

        table = self.query_one(DataTable)

        nodes = []
        for node in self.config['nodes']:
            node_instance = Node(node)
            nodes.append(node_instance)

        while True:
            threads = []

            for node in nodes:
                thread = threading.Thread(target=node.load_all_data)
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

            if self.first_load:
                self.query_one(NodeLoading).add_class('-hidden')
                self.query_one('#node-container').remove_class('-hidden')
                self.is_loading = False

            # For each node add a row
            for index, node in enumerate(nodes):
                node_data = node.get_node_data()
                
                self.node_data.append(node_data)

                if not table.is_valid_row_index(index):
                    table.add_row(node_data['name'], node_data['version'], node_data['host'], node_data['connected_peers'], str(node_data['synced']), str(node_data['top_layer']), str(node_data['verified_layer']), str(node_data['synced_layer']), str(node_data['smeshing']), str(node_data['post_state']), str(node_data['space_units']), str(node_data['size_gib']), str(node_data['assigned_layers_count']), key=str(index))
                else:
                    table.update_cell(str(index), "0", str(node_data['name']))
                    table.update_cell(str(index), "1", str(node_data['version']))
                    table.update_cell(str(index), "2", str(node_data['host']))
                    table.update_cell(str(index), "3", str(node_data['connected_peers']))
                    table.update_cell(str(index), "4", str(node_data['synced']))
                    table.update_cell(str(index), "5", str(node_data['top_layer']))
                    table.update_cell(str(index), "6", str(node_data['verified_layer']))
                    table.update_cell(str(index), "7", str(node_data['synced_layer']))
                    table.update_cell(str(index), "8", str(node_data['smeshing']))
                    table.update_cell(str(index), "9", str(node_data['post_state']))
                    table.update_cell(str(index), "10", str(node_data['space_units']))
                    table.update_cell(str(index), "11", str(node_data['size_gib']))
                    table.update_cell(str(index), "12", str(node_data['assigned_layers_count']))

            sleep(60)

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
        self.query_one('#node-data-layers').update(f"[b]Layers:[/b] {'None' if not self.selected_node['assigned_layers'] else ', '.join(map(str, self.selected_node['assigned_layers'].sort()))}")

    @on(Button.Pressed, '#btn-copy-layers')
    def on_copy(self):
        pyperclip.copy('None' if not self.selected_node['assigned_layers'] else ', '.join(map(str, self.selected_node['assigned_layers'])))
        self.query_one(Button).label = "COPIED"

if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    Nodemon(config).run()
