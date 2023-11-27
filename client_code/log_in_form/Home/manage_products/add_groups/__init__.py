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
    open_form('log_in_form.Home.manage_products', items=self.get_dynamic_items())

  def button_1_click(self, **event_args):
        text_value = self.text_box_1.text

        # Open the manage_products1 form
        manage_products_form = open_form('log_in_form.Home.manage_products.manage_products1', items=self.get_dynamic_items())

        # Call the method to set drop_down_1 value
        manage_products_form.set_drop_down_1(text_value)

  def get_dynamic_items(self):
        # Return a list of items dynamically
        return ['Item 1', 'Item 2', 'Item 3']  # Update this with your logic
