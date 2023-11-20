from ._anvil_designer import Form9Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form9(Form9Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

    product_id = self.text_box_1.text
    product_name = self.text_box_2.text
    product_description = self.text_area_1.text
    product_categories = self.drop_down_1.selected_value
    processing_fee = self.text_box_3.text
    extension_fee = self.text_box_4.text
    discount_coupons = self.radio_button_3.selected
    max_days = self.drop_down_4.selected_value
    print(max_days)
    