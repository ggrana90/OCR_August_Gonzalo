import sqlite3
import pandas as pd

conn = sqlite3.connect('ocr_pombo.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS TicketData (Liter float, '
          'Cost float, '
          'CostPerLiter float, '
          'OilType varchar(10), '
          'GasStationID int, '
          'CarPlate varchar(10), '
          'Date date)')
conn.commit()