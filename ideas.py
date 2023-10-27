"""https://github.com/Textualize/textual/discussions/3026"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import TabbedContent, TabPane, Button, Footer

class BasePane(TabPane):

    BINDINGS = [
        Binding("f1", "something", "First thing"),
        Binding("f2", "another_thing", "Second thing"),
    ]

class FirstPane(BasePane):

    def compose(self) -> ComposeResult:
        yield Button("This is the first pane")

class SecondPane(BasePane):

    BINDINGS = [
        Binding("f3", "one_more_thing", "Also this too")
    ]

    def compose(self) -> ComposeResult:
        yield Button("This is the second pane")

class TabbedContentBindings(App[None]):

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield FirstPane("First")
            yield SecondPane("Second")
        yield Footer()

if __name__ == "__main__":
    TabbedContentBindings().run()