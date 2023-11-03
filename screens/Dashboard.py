from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Markdown,TabbedContent, TabPane, Placeholder
from textual.reactive import reactive
from textual.containers import Container, ScrollableContainer

welcome = """
### Welcome to Nodemon
Nodemon is a textual user interface (TUI) for go-spacemesh created by Hake Hardware. 
If you found this useful consider contributing by sending some SMH:

https://explorer.spacemesh.io/accounts/sm1qqqqqqxgw2e4qw9q9gzyqmqu92u9t5p22k9p7rg82v9n4

Or subscribe to my YouTube channel where I talk a lot about Spacemesh, clean old GPUs, and do generally nerdy stuff: 
https://www.youtube.com/channel/UCakvG7QQp4oL0Rtpiei1yKg

### Set Up
If you haven't already, create your config with 
`cp example.config.json config.json`. 

Then for each node you have, create an entry that mimicks the example. 
Make sure that the config.mainnet.json for each node has the private grpc IP 
set to accept connections outside local host: `grpc-private-listener": "0.0.0.0:9093`

Depending on how you have your nodes set up, you could be done. But more complex setups will require more configurations. But as long as you have ports open and accessible you
should be able to hook up nodes on your local network.

### Usage
When you start up Nodemon, you will see the dashboard. On the left hand side is an aggregate
view of all of your nodes. And then you will see announcements and other information where you
are reading this now.

You can always return to the dashboard by pressing 'd' or by clicking the 'D' in the footer. 

To view the nodes screen, press 'n' or click the 'N' in the footer. This will bring you to
a table with all of your nodes. You can click in to each node to view additional details about
the node. To return to the main table, simply press 'b' for back. 

On the Nodes screen you can also view a table of all of your layers by selecting the tab. You
can toggle between the tabs by clicking them. If you want to return to the dashboard press 'd'
at any time.

The last screen is for Settings. Right now this is empty. But in the future you can update
things like refresh rate.
"""

class DashboardScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id='side-bar'):
            yield Markdown(""" ## Overview """, id='overview')
        with ScrollableContainer():
            yield Markdown(welcome, id='home')
        yield Footer()

    # def watch_node_data(self, data) -> None:
    #     self.query_one('#overview').update(data)

    def update_components(self, data, layers):
        parsed_data = self.parse_data(data, layers)
        self.query_one('#overview').update(parsed_data)

    def parse_data(self, data, layers):
        total_su = 0
        not_synced = []
        total_gib = 0
        total_nodes = len(data)
        total_layers = 0
        last_layer = layers[0]['number']
        layers = []
        completed_layers = []
        incomplete_layers = []
        next_layer = None

        for node in data:
            # Calculate total Space Units
            su = node['smeshing']['space_units']
            total_su += su if su else 0

            # Calculate total Synced Nodes
            synced = node['network']['is_synced']
            if not synced:
                not_synced.append(node['info']['node_name'])

            # Calculate total GiB
            gib = node['smeshing']['size_gib']
            total_gib += gib if gib else 0

            # Calculate total Layers
            total_layers += node['smeshing']['assigned_layers_count']

            if node['smeshing']['assigned_layers_count'] > 0:
                layers.extend(node['smeshing']['assigned_layers'])

                layers.sort()

                for layer in layers:
                    if layer > last_layer:
                        incomplete_layers.append(layer)
                    else:
                        completed_layers.append(layer)

            # completed_layers.sort()
            # incomplete_layers.sort()

            if len(incomplete_layers) > 0:
                approximate_time_to_next_layer_min = incomplete_layers[0]-last_layer*5
                next_layer = incomplete_layers[0]
            else:
                approximate_time_to_next_layer_min = None

        return f"""
## Overview

**Total Nodes:** {total_nodes}

**Total Space Units:** {total_su} ({total_gib}GiB) 

**Total Assigned Layers:** {total_layers}

**Assigned Layers Left:** {total_layers-len(completed_layers)} 

**Next Assigned Layer:** {next_layer}

{f"TTNL: {approximate_time_to_next_layer_min} minutes ({last_layer - incomplete_layers[0]} layers)" if approximate_time_to_next_layer_min else ""}

"""
            

        # return {
        #     'Total SU': total_su,
        #     'Not Synced': len(not_synced),
        #     'Total GiB': total_gib,
        #     'Total Nodes': total_nodes,
        #     'Total Layers': total_layers,
        #     'Completed Layers': completed_layers,
        #     'Incomplete Layers': incomplete_layers,
        #     'Last Layer': last_layer,
        #     'TTNL': approximate_time_to_next_layer_min
        # }
