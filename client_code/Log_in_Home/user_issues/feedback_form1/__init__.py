from ._anvil_designer import feedback_form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class feedback_form1(feedback_form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.data = tables.app_tables.user_profile.search()
    
    self.email_user = []

    a = -1
    for i in self.data:
      a+=1
      self.email_user.append(i['email_user'])

    if a == -1:
      alert("No Data Available Here!!")
    else:
      self.label_8.text = self.email_user[a]


    self.data = tables.app_tables.user_issues_bugreports.search()
    
    self.user_issues = []
    self.specific_issue = []
    self.user_discription = []
    self.image = []
    self.feedback_form = []

    a = -1
    for i in self.data:
      a+=1
      self.user_issues.append(i['user_issues'])
      self.specific_issue.append(i['specific_issue'])
      self.user_discription.append(i['user_discription'])
      self.image.append(i['image'])
      self.feedback_form.append(i['feedback_form'])


    if a == -1:
      alert("No Data Available Here!!")
    else:     

      self.label_10.text = self.user_issues[a]
      self.label_11.text = self.specific_issue[a]
      self.label_12.text = self.user_discription[a]
      self.image_2.source = self.image[a]
      self.label_13.text = self.feedback_form[a]

    


  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form')
