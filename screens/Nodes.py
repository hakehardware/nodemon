from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, DataTable, Button, Header, Static, Label, Markdown
from textual.containers import Container, ScrollableContainer
from textual import on
from textual.binding import Binding
from datetime import datetime
import csv
from components.nodeloading import NodeLoading
from utils.helpers import Helpers

NODE_TABLE_HEADERS = ["Name", "Status", "Version", "IP", "Peers", "Synced", "Top", "Verified", "Synced", "Smeshing", "PoST State", "SU", "GiB", "Layers"]
class NodeData(Container):
    def compose(self) -> ComposeResult:
        # with Container(id='log-container'):
        #     yield RichLog(markup=True, wrap=True)
        with Container(id='node-data-info', classes='box'):
            with Container(id='status-bar'):
                yield Button('<<< Back (b)', id='back-to-table-btn')
                yield Markdown("""**Last Updated:** None""", id='node-status-bar')
            with ScrollableContainer():
                yield Markdown("Coming Soon")
            with ScrollableContainer():
                yield Markdown("Loading...", id='node-data-markdown')

class NodeTable(Container):
    def compose(self) -> ComposeResult:
        yield Static('Last Updated: N/A', id='table-status')
        yield DataTable(id='node-table')

class NodesScreen(Screen):

    BINDINGS = [
        Binding("b", "back()", "Back", show=False),
        Binding("left", "move_page('left')", show=False),
        Binding("right", "move_page('right')", show=False)
    ]

    def __init__(self) -> None:
        self.first_load = True
        self.selected_node = 0
        self.node_data = None
        self.assigned_layers = None
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        yield NodeTable(id='container-node-table', classes='-hidden')
        yield NodeData(id='container-node-data', classes='-hidden')
        yield NodeLoading(id='node-screen-loading')
        yield Footer()

    def on_mount(self) -> None:
        # Node Table
        node_table = self.query_one('#node-table')
        node_table.cursor_type = "row"
        node_table.zebra_stripes = True

        for index, header in enumerate(NODE_TABLE_HEADERS):
            if header == 'Status':
                node_table.add_column(header, key=str(index), width=8)
            else:
                node_table.add_column(header, key=str(index))

    def action_move_page(self, direction):
        if direction == 'left':
            if self.selected_node == 0:
                self.selected_node = len(self.node_data)-1
            else:
                self.selected_node -=1
        elif direction == 'right':
            if (self.selected_node + 1) == len(self.node_data):
                self.selected_node = 0
            else:
                self.selected_node +=1

        self.title = f"Nodemon > {self.node_data[self.selected_node]['info']['node_name']}"

        self.update_node()

    @on(Button.Pressed, '#back-to-table-btn')
    def pressed_back(self) -> None:
        self.action_back()
    
    def on_focus(self):
        self.update_node()

    def action_back(self):
        if not self.first_load:
            self.query_one('#container-node-table').remove_class('-hidden')
            self.query_one('#container-node-data').add_class('-hidden')
            self.query_one('#node-table').focus()
            self.title = "Nodemon"

    @on(DataTable.RowSelected)
    def show_node_data(self, event):
        self.query_one('#container-node-table').add_class('-hidden')
        self.query_one('#container-node-data').remove_class('-hidden')

        self.selected_node = event.data_table.get_row_index(event.row_key)

        self.title = f"Nodemon > {self.node_data[self.selected_node]['info']['node_name']}"
        self.update_node()

    def update_node(self):
        node_data = Helpers.generate_node_info(self.node_data[self.selected_node])
        self.query_one('#node-data-markdown').update(node_data)

    def export_node_data(self, options_selected):
        Helpers.write_csv(self.assigned_layers, self.node_data, options_selected)


    def update_table(self, data):
        table = self.query_one('#node-table')
        self.node_data = data['Node Data']
        self.assigned_layers = data['All Assigned Layers']

        current_time = datetime.now().strftime("%b %d, %Y %H:%M:%S")

        if self.first_load:
            self.query_one('#container-node-table').remove_class('-hidden')
            self.query_one('#node-screen-loading').add_class('-hidden')

        self.query_one('#node-status-bar').update(f"""**Last Updated:** {current_time}""")
        self.query_one('#table-status').update(f"Last Updated: {current_time}")

        for index, node_data in enumerate(data['Node Data']):

            if not table.is_valid_row_index(index):
                table.add_row( *[
                    node_data['info']['node_name'],
                    node_data['info']['status'], 
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
                    node_data['smeshing']['assigned_layers_count'], 
                    ], key=str(index))
                
                self.first_load = False
            else:
                table.update_cell( str(index), "0", node_data['info']['node_name'])
                table.update_cell( str(index), "1", node_data['info']['status'])
                table.update_cell( str(index), "2", node_data['info']['version'])
                table.update_cell( str(index), "3", node_data['network']['host'])
                table.update_cell( str(index), "4", node_data['network']['peers'])
                table.update_cell( str(index), "5", node_data['network']['is_synced'])
                table.update_cell( str(index), "6", node_data['network']['top_layer'])
                table.update_cell( str(index), "7", node_data['network']['verified_layer'])
                table.update_cell( str(index), "8", node_data['network']['synced_layer'])
                table.update_cell( str(index), "9", node_data['smeshing']['is_smeshing'])
                table.update_cell( str(index), "10", node_data['smeshing']['post_state'])
                table.update_cell( str(index), "11", node_data['smeshing']['space_units'])
                table.update_cell( str(index), "12", node_data['smeshing']['size_gib'])
                table.update_cell( str(index), "13", node_data['smeshing']['assigned_layers_count'])