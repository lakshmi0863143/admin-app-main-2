from ._anvil_designer import manage_form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_form1(manage_form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Log_in_Home.manage_products')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Log_in_Home.manage_products.view_product')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Log_in_Home.Form11.view_categories')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Log_in_Home')
