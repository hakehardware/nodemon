from screens.Dashboard import DashboardScreen
from screens.Nodes import NodesScreen
from screens.Layers import LayersScreen
from screens.Settings import SettingsScreen
from utils.datahandler import DataHandler

from textual import on
from textual.app import App, ComposeResult
from textual import work
from textual.widgets import Label, Checkbox, Button
from textual.screen import ModalScreen
from textual.containers import Grid

import json
import csv
import asyncio

class ExportScreen(ModalScreen):

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("What would you like to export?", id="question"),
            Checkbox("Layers (JSON)", id='layers-json'),
            Checkbox("Layers (CSV)", id='layers-csv'),
            Checkbox("Nodes (JSON)", id='nodes-json'),
            Checkbox("Nodes (CSV)", id='nodes-csv'),
            Button("Export", id="export-btn", variant="primary"),
            Button("Close", id="cancel-btn"),
            id="dialog",
        )

class Nodemon(App):
    def __init__(self, config) -> None:
        self.config = config
        super().__init__()

    BINDINGS = [
        ("d", "switch_screen('dashboard')", "Dashboard"),  
        ("n", "switch_screen('nodes')", "Nodes"),
        ("l", "switch_screen('layers')", "Layers"),
        ("s", "switch_screen('settings')", "Settings"),
        ("e", "export()", "Export"),
        ("q", "app.quit", "Quit")
    ]

    SCREENS = {
        'dashboard': DashboardScreen(),
        'nodes': NodesScreen(),
        'layers': LayersScreen(),
        'settings': SettingsScreen(),
    }

    CSS_PATH = "nodemon.tcss"

    def on_mount(self) -> None:
        self.push_screen('settings')
        self.push_screen('nodes')
        self.push_screen('layers')
        self.push_screen('dashboard')
        self.node_worker()

    @work(exclusive=True)
    async def node_worker(self):

        while True:
            try:
                data = await DataHandler.handle_data(self.config, False)

                self.SCREENS['dashboard'].update_components(data)
                self.SCREENS['nodes'].update_table(data)
                self.SCREENS['layers'].update_table(data)
            except:
                pass

            await asyncio.sleep(300)

    def action_export(self) -> None:
        self.push_screen(ExportScreen())

    @on(Button.Pressed, '#cancel-btn')
    def cancel_button_pressed(self) -> None:
        self.app.pop_screen()

    @on(Button.Pressed, '#export-btn')
    def export_button_pressed(self) -> None:
        layers_csv = self.query_one('#layers-csv').value
        layers_json = self.query_one('#layers-json').value
        nodes_csv = self.query_one('#nodes-csv').value
        nodes_json = self.query_one('#nodes-csv').value

        self.SCREENS['nodes'].export_node_data({
            'Layers CSV': layers_csv,
            'Layers JSON': layers_json,
            'Nodes CSV': nodes_csv,
            'Nodes JSON': nodes_json
        })

        self.app.pop_screen()

if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    Nodemon(config).run()