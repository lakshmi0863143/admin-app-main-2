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
    specific_issues = self.drop_down_2.selected_value
    user_discription = self.text_area_1.text
    image = self.file_loader_1.file
    feedback_form = self.text_area_2.text

    if product_name == "" or membership_type == "" or processing_fee == "" or extension_fee == "" or interest_type == "" or max_days == "" or min_days == ""  or discount_coupons == "" or roi == "" or product_group == "" or product_categories == "" :
      Notification("Fill All Required Details").show()
    else:
     anvil.server.call('product_details', self.id,product_name,processing_fee,extension_fee,membership_type,interest_type,max_days,min_days,roi,discount_coupons,product_group,product_categories)
     alert("Submited successfull")
     open_form('log_in_form.Home.manage_products')
 
 
  
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

    
    
