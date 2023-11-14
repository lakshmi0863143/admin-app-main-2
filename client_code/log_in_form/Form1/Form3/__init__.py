from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if self.text_box_2.text == "" or  self.text_box_3.text == "" or self.text_box_4.text == "" or self.text_box_5.text == "" or self.text_box_6.text == "" or self.text_box_7.text == "" or self.text_box_8.text == "" or self.text_box_9.text == "" or self.text_box_10.text == "" or self.text_box_11.text == "" or self.text_box_12.text == "" or self.text_box_13.text == "" or self.text_box_14.text == "" or self.text_box_15.text == "" or self.text_box_16.text == "" or self.text_box_17.text == "" or self.text_box_18.text == "" or self.text_box_19.text == "" or self.text_box_20.text == "" or self.text_box_21.text == "" or self.text_box_22.text == "" or self.text_box_23.text == "" or self.text_box_24.text == "" or self.text_box_25.text == "" or self.text_box_26.text == "" or self.text_box_27.text == "" or self.text_box_28.text == "" or self.text_box_29.text == "" or self.text_box_30.text == "" or self.text_box_32.text == "" or self.text_box_33.text == "" or self.text_box_34.text == "" or self.text_box_35.text == "" :
      Notification("Fill All Required Details").show()
    else:
      data = tables.app_tables.user_profile.search()
      a = -1
      for row in data:
        a += 1

      if a == -1:
        alert("No Data Available Here")
      else:
        data[a]['name'] = self.text_box_1.text
        data[a]['email'] = self.text_box_2.text
        data[a]['number'] = self.text_box_3.text
        data[a]['joining_date'] = self.date_picker_1.date
        data[a]['role'] = self.drop_down_1.selected_value
        data[a]['permission'] = self.drop_down_2.selected_value
        
        print(a)