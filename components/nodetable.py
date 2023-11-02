from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Static, Label, LoadingIndicator, Button, Log
from textual.containers import Container
from textual.binding import Binding
from textual import work
from textual import on

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