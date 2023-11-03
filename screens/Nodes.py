from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, DataTable, Header

HEADERS = ["Name", "Version", "IP", "Peers", "Synced", "Top", "Verified", "Synced", "Smeshing", "PoST State", "SU", "GiB", "Layers"]

class NodesScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True

        # Add headers to table
        for index, header in enumerate(HEADERS):
            table.add_column(header, key=str(index))

    def action_back(self):
        pass

    def update_table(self, data):
        table = self.query_one(DataTable)

        for index, node_data in enumerate(data):
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
                    node_data['smeshing']['assigned_layers_count'], 
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
                table.update_cell( str(index), "12", node_data['smeshing']['assigned_layers_count'])

