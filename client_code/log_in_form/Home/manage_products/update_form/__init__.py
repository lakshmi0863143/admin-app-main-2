from ._anvil_designer import update_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class update_form(update_formTemplate):
  def __init__(self, get_customer_id_value, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.get = get_customer_id_value

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

    if  self.text_box_2.text == ""  or self.text_box_3.text == "" or self.drop_down_1.selected_value == "" or self.text_box_4.text  == "" or  self.drop_down_2.selected_value == "" or   self.drop_down_3.selected_value == "" or self.drop_down_4.selected_value == "" or self.text_box_5.text == "" or  self.radio_button_3.text == "" or self.radio_button_1.text == "" :

      Notification("Fill All Required Details").show()
    else:
      data = tables.app_tables.product_details.search()
      id_list = []
      for i in data:
        id_list.append(i['product_id'])

      if self.get in id_list:
        a = id_list.index(self.get)
        data[a]['product_name'] = self.text_box_2.text
        data[a]['product_categories'] = self.drop_down_1.selected_value 
        data[a]['processing_fee'] =  int(self.text_box_3.text)
        data[a]['extension_fee'] = int(self.text_box_4.text)
        data[a]['membership_type'] = self.drop_down_2.selected_value
        data[a]['interest_type'] = self.radio_button_1.text 
        data[a]['max_days'] = int(self.drop_down_3.selected_value)
        data[a]['min_days'] = int(self.drop_down_4.selected_value) 
        data[a]['roi'] = int(self.text_box_5.text)
        data[a]['discount_coupons'] = self.radio_button_3.text
      
        open_form('log_in_form.Home.manage_products.view_product')


  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.view_product')
