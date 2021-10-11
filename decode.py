import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sqlliteconnect as sql


import os
from datetime import datetime

def sql_markAttendance(code):
    db = 'Attendance.db'
    #con = sql.sql_connection(db)
    now = datetime.now()
    data = code+","+now.strftime('%d/%m/%y')+","+now.strftime('%H:%M:%S')
    entities = tuple(data.split(','))
    #print(entities, type(entities))

    query = """INSERT INTO tblAtendace(code, date, time) VALUES ( ?, ?, ?)"""
    print(query)
    sql.sql_insert(db, query, entities)

def markAttendance(code):
    with open('Attendace.csv','r+') as f:
        myDataList = f.readline()
        for line in myDataList:
            entry = line.split(',')
        now = datetime.now()
        dateString = now.strftime('%d/%m/%y')
        timeString = now.strftime('%H:%M:%S')
        f.writelines(f'\n{code},{dateString},{timeString}')

def decode_img(img):
    gray_img = cv2.cvtColor(img, 0)
    for barcode in decode(gray_img):
        myData = barcode.data.decode("utf-8")
        #print(myData)
        myData = str.replace(myData,'(',"")
        myData = str.replace(myData, ')', "")
        myData = str.replace(myData, "'", "")
        myData = tuple(myData.split(","))
        #print(myData, type(myData))
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myData[0], (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

        # Lưu dữ liệu SQL
        sql_markAttendance(myData[0])
        # Lưu dữ liệu Excel
        markAttendance(myData[0])
    return img