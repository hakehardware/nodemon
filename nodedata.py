from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Static, Label, LoadingIndicator, Button, Log
from textual.containers import Container
from textual.binding import Binding
from textual import work
from textual import on

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