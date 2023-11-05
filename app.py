from screens.Dashboard import DashboardScreen
from screens.Nodes import NodesScreen
from screens.Layers import LayersScreen
from screens.Settings import SettingsScreen
from utils.datahandler import DataHandler

from textual.app import App
from textual import work

import json

import asyncio

class Nodemon(App):
    def __init__(self, config) -> None:
        self.config = config
        super().__init__()

    BINDINGS = [
        ("d", "switch_screen('dashboard')", "Dashboard"),  
        ("n", "switch_screen('nodes')", "Nodes"),
        ("l", "switch_screen('layers')", "Layers"),
        ("s", "switch_screen('settings')", "Settings"),
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
            data = await DataHandler.handle_data(self.config, False)

            self.SCREENS['dashboard'].update_components(data)
            self.SCREENS['nodes'].update_table(data)
            self.SCREENS['layers'].update_table(data)

            await asyncio.sleep(300)

if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    Nodemon(config).run()