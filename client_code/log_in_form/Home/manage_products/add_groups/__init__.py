from ._anvil_designer import add_groupsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form

class add_groups(add_groupsTemplate):
  def __init__(self,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products')
 

  def button_1_click(self, **event_args):
        # Get the text value from text_box_1
        text_value = self.text_box_1.text
        # Call the server function to set the group name
        anvil.server.call('set_group_name', text_value)
        # Open the manage_products1 form
        open_form('log_in_form.Home.manage_products.manage_products1')