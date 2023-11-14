from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

   
    self.user_id = []
    self.name = []
    self.password = []
    self.mobile_no = []
    self.mail_id = []
    self.pincode = []
    

    data = tables.app_tables.users.search()
    for row in data:
      self.user_id.append(row['user_id'])
      self.name.append(row['name'])
      self.password.append(row['passward'])
      self.mobile_no.append(row['mobile_no'])
      self.mail_id.append(row['mail_id'])
      self.pincode.append(row['pincode'])
      
    
    self.label_3.text = self.user_id[-1]
    self.label_5.text = self.name[-1]
    self.label_7.text = self.password[-1]
    self.label_9.text = self.mobile_no[-1]
    self.label_11.text = self.mail_id[-1]
    self.label_13.text = self.pincode[-1]
    print(self.pincode)

