import re
import pandas as pd
import sqlite3
import os
import PDFtoIMG as pdfToImg
import WA as wa
import shutil


OIL_TYPE = '([A-Z]{5}[T][A][R])|([A-Z]{5}[U][E])'
CAR_PLATE = '^[0-9]{4}.?[A-Z]{3}$'
DATE_PATTERN = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
GAS_STATION = '^[0-9]{8}$'
carpetatemp = "PDF"



def readImage(file):
    return pdfToImg.convertPDFToImage(file)

def readImage2(file):
    return wa.WAToImage(file)


def getPositionInArrayForRegex(data, regex):
    for i in range(len(data)):
        if (re.match(regex, data[i])):
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
        return data[position]
    else:
        return('NULL')

def getFloatNumber(data, position):
    try:
        dotIndex = data[position].index('.')
        return float(data[position][:dotIndex + 3])
    except:
        return 0


def getLiterPrice(liter, totalPrice):
    try:
        return float(totalPrice) / float(liter)
    except:
        return 0

def getDatabaseConnection():
    return sqlite3.connect('ocr_pombo.db')


def checkIfTableExists(connection):
    c = connection.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='%s'".format("TicketData"))
    result = c.fetchone()
    if result == None:
        return False
    else:
        return True

def createDatabase(connection):
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS TicketData (Liter float, '
              'Cost float, '
              'CostPerLiter float, '
              'OilType varchar(10), '
              'GasStationID int, '
              'CarPlate varchar(10), '
              'Date date)')
    connection.commit()

def storeInformationInDatabase(connection, dataframe):
    dataframe.to_sql('TicketData', connection, if_exists='append', index=False)

def getDataFromDatabase(connection):
    c = connection.cursor()
    return c.execute('''  SELECT * FROM TicketData ''')

def printDataFromDatabase(connection):
    data = getDataFromDatabase(connection)
    for row in data.fetchall():
        print(row)


file = 'PDF/' + file_name
converted_file = 'PDF_Converted/' + file_name
error_file = 'Errors/' + file_name

try:
    if __name__ == "__main__":
        connection = getDatabaseConnection()
        if not checkIfTableExists(connection):
            createDatabase(connection)
        for file_name in os.listdir(carpetatemp):
            if not file_name.endswith(".pdf"):
                continue
            data = readImage(file_name)
            positionOilType = getPositionInArrayForRegex(data, OIL_TYPE)
            positionLit = getPositionInArrayForRegex(data, OIL_TYPE) + 1
            positionPrice = getPositionInArrayForRegex(data, OIL_TYPE) + 2
            LITER_DATA = getFloatNumber(data, positionLit)
            PRICE_DATA = getFloatNumber(data, positionPrice)
            LITER_PRICE_DATA = float(
                round(getLiterPrice(getFloatNumber(data, positionLit), getFloatNumber(data, positionPrice)), 4))
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
            storeInformationInDatabase(connection, df)
except Exception:
    print(f"{filename} value error")
    shutil.move(file, error_file)
finally:
    shutil.move(file, converted_file)
    # printDataFromDatabase(connection)