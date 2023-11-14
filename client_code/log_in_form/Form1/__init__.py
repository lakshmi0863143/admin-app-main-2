from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
if self.text_box_1.text == "" or self.text_box_2.text == "" or  self.text_box_3.text == "" or not self.date_picker_1.date or not self.drop_down_1.selected_value or not self.drop_down_2.selected_value:
      Notification("Fill All Required Details").show()
    else:
      data = tables.app_tables.admin_teams.search()
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