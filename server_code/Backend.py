import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_alle_kurse():
  with sqlite3.connect(data_files["Reichart_Tobias_fitnessstudio.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("SELECT k.kurs_id, k.bezeichnung AS kurs, k.wochentag, k.uhrzeit, t.nachname || ' ' || t.vorname AS trainer, COUNT(a.mitglied_id) || '/' || k.maxteilnehmer AS teilnehmer FROM kurs k JOIN trainer t ON t.trainer_id = k.trainer_id LEFT JOIN anmelden a ON a.kurs_id = k.kurs_id GROUP BY k.kurs_id;").fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def get_alle_mitglieder_nicht_im_kurs(kurs_id: int):
  with sqlite3.connect(data_files["Reichart_Tobias_fitnessstudio.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql = "SELECT mitglied_id, nachname || ' ' || vorname AS mitglied FROM mitglied WHERE mitglied_id NOT IN (SELECT mitglied_id FROM anmelden WHERE kurs_id = ?)"
    result = cur.execute(sql, (kurs_id,)).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def add_mitglied_to_kurs(kurs_id: int, mitglied_id: int, date:str):
  with sqlite3.connect(data_files["Reichart_Tobias_fitnessstudio.db"]) as conn:
    cur = conn.cursor()
    cur.execute(f"INSERT INTO anmelden (kurs_id, mitglied_id, anmeldedatum) VALUES ({kurs_id}, {mitglied_id}, '{date}')")
    conn.commit()
  return