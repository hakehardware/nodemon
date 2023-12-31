from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Markdown,TabbedContent, TabPane, Placeholder
from textual.reactive import reactive
from textual.containers import ScrollableContainer

from components.nodeloading import NodeLoading


welcome = """
### Welcome to Nodemon
Nodemon is a textual user interface (TUI) for go-spacemesh created by Hake Hardware. 
If you found this useful consider contributing by sending some SMH:

https://explorer.spacemesh.io/accounts/sm1qqqqqqxl2phuunmsp8dm7hpywszakex34ce52zgdu205q

Or subscribe to my YouTube channel where I talk a lot about Spacemesh, clean old GPUs, and do generally nerdy stuff: 
https://www.youtube.com/channel/UCakvG7QQp4oL0Rtpiei1yKg

### Updates
- 11/11/2023: Big update to add exporting. You must wait for your nodes to load in order to export. Export will be to the directory nodemon is in. You can upload the Layers (JSON) file to the Spacemesh Reward Tracker to track your layers and rewards there as well. 
- 11/6/2023: Updated README and example config. Users can also not connect a db and still use the app
- 11/6/2023: Added Rewards (If you get two rewards on the same layer, it will aggregate them together and show the wrong value). I will fix this in a future version.
- 11/5/2023: Added coinbase to layers.

### TODO:
- The UI may freeze a bit when initially loading data. This will be fixed in the refactor. 
- Refactor will begin shortly so mostly bug fixes for the time being. Nodemon V4 will come with lots of big improvements but expect a release date mid-December.

### Set Up
If you haven't already, create your config with 
`cp example.config.json config.json` (linux) 

Then for each node you have, create an entry that mimicks the example. If you have a local state.sql file you can connect to it and view rewards by updating the state_file entry in the config.

**NOTE:** Make sure that the config.mainnet.json for each node has the private grpc IP 
set to accept connections outside local host: `grpc-private-listener": "0.0.0.0:9093"`

Depending on how you have your nodes set up, you could be done. But more complex setups will require more configurations. But as long as you have ports open and accessible you
should be able to hook up nodes on your local network.

### Usage
When you start up Nodemon, you will see the dashboard. On the left hand side is an aggregate
view of all of your nodes. 

- Total Nodes: Total nodes from your config
- Total Space Units: Sum of Space Units from all nodes
- Total PoST GiB: Total space of all your nodes
- Total Offline: Number of nodes that are offline
- Total Not Synced: Number of nodes that are not syced
- Total Assigned Layers: Sum of assigned layers from all nodes
- Last Completed Layer: Last layer the network completed
- Next Assigned Layer: The next layer from all connected nodes that will be reached
- Next Layer Time: Approximate time the next layer will be reached
- Layers to Layer: How many layers until your next assigned layer

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
loading = """
## Overview

Loading Data..

"""
class DashboardScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        with ScrollableContainer(id='side-bar'):
            yield Markdown(loading, id='overview')

        with ScrollableContainer():
            yield Markdown(welcome, id='home')
        yield Footer()

    def update_components(self, data):
        self.query_one('#overview').update(self.build_update(data))

    def build_update(self, data):
        return f"""
## Overview

### General
**Total Nodes:** {data['Total Nodes']}

**Total Space Units:** {data['Total Space Units']}

**Total PoST GiB:** {data['Total PoST GiB']}

**Epoch Rewards:** {data['Epoch Rewards']}

**Total Offline:** {data['Total Offline']}

**Total Not Synced:** {data['Total Not Synced']}

**Total Assigned Layers:** {len(data['All Assigned Layers'])}

**Last Completed Layer:** {data['Last Network Layer']['Number']}

### Assigned Layers

**Next Assigned Layer:** {data['Next Layer']['Layer'] if data['Next Layer'] else "None"}

**Next Layer Time:** {data['Next Layer']['Layer Time'].strftime("%b %d, %Y %H:%M:%S") if data['Next Layer'] else "None"}

**Layers to Layer:** {data['Next Layer']['Layers to Layer'] if data['Next Layer'] else "None"}
"""
