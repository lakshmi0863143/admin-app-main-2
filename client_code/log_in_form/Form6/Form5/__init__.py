from ._anvil_designer import Form5Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.loan_details.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []
    self.list_6 = []
    
    
    for i in self.data:
      a+=1
      self.list_1.append(i['max_amount'])
      self.list_2.append(i['min_amount'])
      self.list_3.append(i['appication_status'])
      self.list_4.append(i['timestamp'])
      self.list_5.append(i['total_repayment_amount'])
      self.list_6.append(i['tenure'])

    print(a)

    self.result = []
    self.index = []
    if a == -1:
      alert("No Data Available Here!")
          
      for i in self.index:
        self.result.append({'coustmer_id' : self.list_1[i], 'full_name' : self.list_2[i], 'profile_status' : self.list_3[i], 'gender' : self.list_4[i], 'user_age' : self.list_5[i],
                          'date_of_birth' : self.list_6[i], 'mobile' : self.list_7[i], 'aadhaar_no' : self.list_8[i]})

      self.repeating_panel_1.items = self.result

      print(self.list_1, self.list_2, self.list_3)
      print(self.result)
      print(a)












  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form()
