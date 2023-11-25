from ._anvil_designer import manage_products1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_products1(manage_products1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    self.id = 'A' + str(1000000)  
    self.label_1.text = self.id
    self.data = tables.app_tables.product_details.search()

    a = -1
    self.list_1 = []
 
    for i in self.data:
      a+=1
      self.list_1.append(i['product_id']) 
    if a == -1 :
      self.id = 'A' + str(1000000)
      self.label_1.text = self.id
      
    else:
      self.id = 'A'+ str(int(self.list_1[-1][1:])+1)
      self.label_1.text = self.id
   
  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""


    product_name = self.text_box_2.text
    product_discription = self.text_area_1.text
    product_group = self.drop_down_1.selected_value
    self.list_1 = []
    product_categories = self.drop_down_5.selected_value or  self.drop_down_6.selected_value or  self.drop_down_7.selected_value or  self.drop_down_8.selected_value
    if self.list_1.get == 'Home Loan':
      self.label_2.visible = True
      self.drop_down_1.visible = True
      self.label_3.visible = False
      self.drop_down_2.visible = False
      self.label_4.visible = False
      self.drop_down_3.visible = False
      self.label_5.visible = False
      self.drop_down_4.visible = False
    elif self.list_1.get == 'Personal Loan':
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.label_3.visible = True
      self.drop_down_2.visible = True
      self.label_4.visible = False
      self.drop_down_3.visible = False
      self.label_5.visible = False
      self.drop_down_4.visible = False
    elif self.list_1.get == 'Vehicle Loan':
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.label_3.visible = False
      self.drop_down_2.visible = False
      self.label_4.visible = True
      self.drop_down_3.visible = True
      self.label_5.visible = False
      self.drop_down_4.visible = False
    elif self.list_1.get == 'Business Loan':
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.label_3.visible = False
      self.drop_down_2.visible = False
      self.label_4.visible = False
      self.drop_down_3.visible = False
      self.label_5.visible = True
      self.drop_down_4.visible = True
    processing_fee = int(self.text_box_3.text)
    extension_fee = int(self.text_box_4.text)
    discount_coupons = self.radio_button_3.text
    membership_type = self.drop_down_2.selected_value
    print(membership_type)
    interest_type = self.radio_button_1.text
    if interest_type :
      print(self.radio_button_1.text)
    else :
      print(self.radio_button_2.text)
    min_days = int(self.drop_down_3.selected_value)
    print(min_days)
    max_days = int(self.drop_down_4.selected_value)
    print(max_days)
    roi = int(self.text_box_5.text)
    print(roi)

    if product_name == "" or membership_type == "" or processing_fee == "" or extension_fee == "" or interest_type == "" or max_days == "" or min_days == ""  or discount_coupons == "" or roi == "":
      Notification("Fill All Required Details").show()
    else:
     anvil.server.call('product_details',self.id,product_name,processing_fee,extension_fee,membership_type,interest_type,max_days,min_days,roi,discount_coupons)
     product_id = self.label_1.text
     open_form('log_in_form.Home.manage_products.add_groups',product_id)
 

  def check_box_3_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    product_visibility = self.check_box_3.checked
    if  product_visibility :
      self.label_1.visible = True
      self.text_box_2.visible = True
      self.text_area_1.visible = True
      self.text_box_3.visible = True
      self.text_box_4.visible = True
      self.drop_down_2.visible = True
      self.radio_button_1.visible = True
      self.drop_down_3.visible = True
      self.drop_down_4.visible =True
      self.text_box_5.visible = True
      self.radio_button_3.visible = True
      self.radio_button_4.visible = True
    else:
      self.text_box_2.visible = False
      self.text_area_1.visible = False
      self.text_box_3.visible = False
      self.text_box_4.visible = False
      self.drop_down_2.visible = False
      self.radio_button_1.visible = False
      self.drop_down_3.visible = False
      self.drop_down_4.visible =False
      self.text_box_5.visible = False
      self.radio_button_3.visible = False
      self.radio_button_4.visible = False


