from ._anvil_designer import AnmeldenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class Anmelden(AnmeldenTemplate):
  def __init__(self, data_row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    return_value = anvil.server.call('get_alle_mitglieder_nicht_im_kurs', data_row["kurs_id"])
    for value in return_value:
      value["kurs_id"] = data_row["kurs_id"]
      value["date"] = datetime.today().strftime('%Y-%m-%d')
    self.repeating_panel_mitglieder.items = return_value

  @handle("button_back", "click")
  def button_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Kursuebersicht')
