from ._anvil_designer import Form6Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form6(Form6Template):
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
      self.list_1.append(i['customer_id'])
      self.list_2.append(i['email_id'])
      self.list_3.append(i['full_name'])
      self.list_4.append(i['interest_rate'])
      self.list_5.append(i['loan_id'])
      self.list_6.append(i['loan_status'])
    print(a)

    self.result = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      for i in range(len(self.list_1)):
        print(self.list_2[i])
        self.result.append({'customer_id' : self.list_1[i], 'email_id' : self.list_2[i], 'full_status' : self.list_3[i], 'inetrest_rate' : self.list_4[i], 'loan_id' : self.list_5[i],
                          'loan_status' : self.list_6[i]})

      self.repeating_panel_1.items = self.result
      print(self.result)
    
