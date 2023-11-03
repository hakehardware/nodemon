from screens.Dashboard import DashboardScreen
from screens.Nodes import NodesScreen
from screens.Settings import SettingsScreen
from node import Node
from api import ExplorerAPI

from textual.app import App
from textual import work
from textual import on

import json

import asyncio

class Nodemon(App):
    def __init__(self, config) -> None:
        self.config = config
        super().__init__()

    BINDINGS = [
        ("d", "switch_screen('dashboard')", "Dashboard"),  
        ("n", "switch_screen('nodes')", "Nodes"),
        ("s", "switch_screen('settings')", "Settings"),
        ("q", "app.quit", "Quit")
    ]

    SCREENS = {
        'dashboard': DashboardScreen(),
        'nodes': NodesScreen(),
        'settings': SettingsScreen()
    }

    CSS_PATH = "nodemon.tcss"
    
    def on_mount(self) -> None:
        self.push_screen('settings')
        self.push_screen('nodes')
        self.push_screen('dashboard')
        self.node_worker()

    @work(exclusive=True)
    async def node_worker(self):
        nodes = [Node(node) for node in self.config['nodes']]

        # for node in self.config['nodes']:
        #     node_instance = Node(node)
        #     nodes.append(node_instance)

        while True:
            tasks = [node.refresh_data() for node in nodes]
            await asyncio.gather(*tasks)
            node_data = [node.get_data() for node in nodes]
            layers = await ExplorerAPI.get_layers()

            self.SCREENS['dashboard'].update_components(node_data, layers)
            self.SCREENS['nodes'].update_table(node_data)

            await asyncio.sleep(5)

if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    Nodemon(config).run()