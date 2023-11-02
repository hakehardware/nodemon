from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Static, Label, LoadingIndicator, Button, Log
from textual.containers import Container
from textual.binding import Binding
from textual import work
from textual import on
"""
The dashboard shows aggregate data such as:
1. The next 3 layers for the current EPOCH along with date and time
1. Total SU
1. Total GiB
1. Total Layers
1. Percentage of Epoch Complete
1. Total Rewards for current Epoch
1. Total Rewards
"""
class Dashboard(Container):

    def compose(self) -> ComposeResult:
        with Container(classes='box', id='dashboard'):
            yield Static("Dashboard (coming soon)")