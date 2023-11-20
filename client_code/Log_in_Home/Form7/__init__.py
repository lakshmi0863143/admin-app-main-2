from ._anvil_designer import Form7Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    membership_type = self.drop_down_2.selected_value
    print(membership_type)
    interest_type = self.radio_button_1.selected
    print(interest_type)
    min_days = self.drop_down_3.selected_value
    print(min_days)
    max_days = self.drop_down_4.selected_value
    print(max_days)
    roi = self.text_box_5.text
    print(roi)

    interest_type = self.column_panel_2.add_component(membership_type = self.drop_down_2.selected_value,
                                                      interest_type = self.radio_button_1.selected,
                                                      min_days = self.drop_down_3.selected_value,
                                                      max_days = self.drop_down_4.selected_value,
                                                      roi = self.text_box_5.text)
    
    print(membership_type, interest_type, min_days, max_days,roi)