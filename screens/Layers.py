from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, DataTable, Header, Placeholder, TabbedContent, LoadingIndicator, TabPane, Button
from textual.containers import ScrollableContainer, Container

from components.nodeloading import NodeLoading

LAYER_TABLE_HEADERS = ["Layer", "Node", "State", "Coinbase", "Layers to Layer", "Minutes to Layer", "Layer Time"]

class LayersScreen(Screen):
    def __init__(self) -> None:
        self.first_load = True
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id='container-layer-table', classes='-hidden'):
            yield DataTable(id='layer-table')

        yield NodeLoading(id='layer-screen-loading')
        yield Footer()

    def on_mount(self) -> None:
        # Layer Table
        layer_table = self.query_one('#layer-table')
        layer_table.cursor_type = "row"
        layer_table.zebra_stripes = True

        for index, header in enumerate(LAYER_TABLE_HEADERS):
            layer_table.add_column(header, key=str(index))

    def update_table(self, data):
        table = self.query_one('#layer-table')

        if self.first_load:
            self.query_one('#container-layer-table').remove_class('-hidden')
            self.query_one('#layer-screen-loading').add_class('-hidden')

        for index, layer in enumerate(data['All Assigned Layers']):
            if not table.is_valid_row_index(index):
                table.add_row( *[
                    layer['Layer'], 
                    layer['Node Name'], 
                    layer['State'],
                    f"{layer['Coinbase'][:4]}....{layer['Coinbase'][-4:]}",
                    layer['Layers to Layer'],
                    layer['Minutes to Layer'],
                    layer['Layer Time'].strftime("%b %d, %Y %H:%M:%S")], key=str(index)
                )
                self.first_load = False
            else:
                table.update_cell( str(index), "0", layer['Layer'])
                table.update_cell( str(index), "1", layer['Node Name'])
                table.update_cell( str(index), "2", layer['State'])
                table.update_cell( str(index), "3", f"{layer['Coinbase'][:4]}....{layer['Coinbase'][-4:]}")
                table.update_cell( str(index), "4", layer['Layers to Layer'])
                table.update_cell( str(index), "5", layer['Minutes to Layer'])
                table.update_cell( str(index), "6", layer['Layer Time'].strftime("%b %d, %Y %H:%M:%S"))