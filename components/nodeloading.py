from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Static, Label, LoadingIndicator, Button, Log
from textual.containers import Container
from textual.binding import Binding
from textual import work
from textual import on

class NodeLoading(Container):
    def compose(self) -> ComposeResult:
        yield Static('🥔  Harvesting Potatoes (please wait) 🥔', id='loading-message')
        yield LoadingIndicator(id="loading-indicator", name="Loading Node Data")