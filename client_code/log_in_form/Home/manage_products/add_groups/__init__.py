from ._anvil_designer import add_groupsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class add_groups(add_groupsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)


    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      text_bo