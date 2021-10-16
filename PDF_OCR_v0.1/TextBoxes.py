import re
import cv2
import pandas as pd
import pytesseract
from pytesseract import Output
import pandas
import sqlite3


OIL_TYPE = '([A-Z]{5}[T][A][R])|([A-Z]{5}[U][E])'
CAR_PLATE = '^[0-9]{4}.?[A-Z]{3}$'
DATE_PATTERN = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
GAS_STATION = '^[0-9]{8}$'


def readImage():
    img = cv2.imread('Pending/girado.png')
    return pytesseract.image_to_data(img, output_type=Output.DICT)


def getPositionInArrayForRegex(data, regex):
    for i in range(len(data['text'])):
        if (re.match(regex, data['text'][i])):
            return i
        # (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return None


def printValue(data, regex):
    position = getPositionInArrayForRegex(data, regex)
    if position:
        print(data['text'][position])
    else:
        print('Element not found in the image provided')


def getValue(data, regex):
    position = getPositionInArrayForRegex(data, regex)
    if position:
        return data['text'][position]
    else:
        return('NULL')

def getFloatNumber(data, position):
    dotIndex = data['text'][position].index('.')
    return data['text'][position][:dotIndex + 3]


def getLiterPrice(liter, totalPrice):
    return float(totalPrice) / float(liter)


data = readImage()
# keys = list(data.keys())
# cv2.imshow('img', img)
# cv2.waitKey(0)

positionOilType = getPositionInArrayForRegex(data, OIL_TYPE)
positionLit = getPositionInArrayForRegex(data, OIL_TYPE) + 1
# print(getFloatNumber(data, positionLit))
positionPrice = getPositionInArrayForRegex(data, OIL_TYPE) + 2
# print(getFloatNumber(data, positionPrice))
# print(round(getLiterPrice(getFloatNumber(data, positionLit), getFloatNumber(data, positionPrice)), 4))

# printValue(data, OIL_TYPE)
# printValue(data, GAS_STATION)
# printValue(data, CAR_PLATE)
# printValue(data, DATE_PATTERN)


LITER_DATA = float(getFloatNumber(data, positionLit))
PRICE_DATA = float(getFloatNumber(data, positionPrice))
LITER_PRICE_DATA = float(round(getLiterPrice(getFloatNumber(data, positionLit), getFloatNumber(data, positionPrice)), 4))
OIL_TYPE_DATA = getValue(data, OIL_TYPE)
GAS_STATION_DATA = int(getValue(data, GAS_STATION))
CAR_PLATE_DATA = getValue(data, CAR_PLATE)
DATE_PATTERN_DATA = getValue(data, DATE_PATTERN)
dfDictionary = {'Liter': LITER_DATA,
          'Cost': PRICE_DATA,
          'CostPerLiter': LITER_PRICE_DATA,
          'OilType': OIL_TYPE_DATA,
          'GasStationID': GAS_STATION_DATA,
          'CarPlate': CAR_PLATE_DATA,
          'Date': DATE_PATTERN_DATA}

df = pd.DataFrame(dfDictionary, index=[0])
df.index.name = 'RecordID'
# df.to_csv('TicketData.csv')

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
df.to_sql('TicketData', conn, if_exists='append', index = False)

c.execute('''  SELECT distinct * FROM TicketData ''')

for row in c.fetchall():
    print (row)