import qrcode


def generalqrcode(id, data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(image_factory=None)
    img.save("DataQR/"+id+".png")

#if __name__ == '__main__':
    #db = 'Attendance.db'
    #con = sql.sql_connection(db)
    #query = 'SELECT * FROM tblEmployees'
    #rows = sql.sql_fetch(con, query)
    #for row in rows:
        #generalqrcode(row[0], row)