from ._anvil_designer import feedback_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class feedback_form(feedback_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Log_in_Home')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_issues = self.drop_down_1.selected_value
    user_discription = self.text_area_1.text
    image = self.file_loader_1.file
    feedback_form = self.text_area_2.text

  

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value == 'Account Inquiries':
            # Add items to the dropdown dynamically
      items_to_add = [ 'Balance Inquiries', 'Transaction History' ]
      self.drop_down_2.items = items_to_add
    elif self.drop_down_1.selected_value == 'Loan and Mortgage Inquiries':
            # Add items to the dropdown dynamically
      items_to_add = ['Loan Application Status ', 'Mortgage Payment Inquiries']
      self.drop_down_2.items = items_to_add  
    elif self.drop_down_1.selected_value == 'Account Management':
            # Add items to the dropdown dynamically
      items_to_add = ['Account Closure','Change of Contact Information']
      self.drop_down_2.items = items_to_add  
    elif self.drop_down_1.selected_value == 'Financial Planning and Advice':
            # Add items to the dropdown dynamically
      items_to_add = ['Inquiries About Investment Options', 'Retirement Planning Assistance']
      self.drop_down_2.items = items_to_add  

    
    
