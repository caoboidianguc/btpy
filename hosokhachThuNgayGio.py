import sqlite3
import datetime


conn = sqlite3.connect('hoso.sqlite')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS Khach')
#cur.execute('''CREATE TABLE Khach (
#    Ten TEXT,
#    sdt INTEGER UNIQUE,
#    email TEXT,
#    lancuoi DATE,
#    homnay DATE,
#    ngaysosanh DATE,
#    count INTEGER

#)''')
#hnay = datetime.date.today()
#cur.execute(''' ALTER TABLE Khach ADD ngayhnay DATE  ''')




while True:
    hnay = datetime.date.today()
    print(hnay)
    ten = input('Ho ten: ')
    if ten == 'giamgia': break
    sdt = input('So dien thoai: ')
    mail = input('Email: ')
    cur.execute('SELECT count FROM Khach WHERE sdt = ? ',(sdt, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Khach (ten, sdt, email, homnay, ngaysosanh, count)
        VALUES ( ? , ? , ? , ? , ? , 1 )''', ( ten, sdt, mail ,hnay, hnay, ))
    else :
        cur.execute(''' UPDATE Khach SET count = count +1 WHERE homnay != ngaysosanh AND sdt = ?''', (sdt, ))
        #cur.execute(''' UPDATE Khach SET count = count + 1 WHERE sdt = ?''', ( sdt, ))
        cur.execute("UPDATE Khach SET lancuoi = homnay , homnay = ? where sdt = ?", (hnay, sdt))
        #cur.execute("UPDATE Khach SET homnay = ? where sdt = ?", (hnay, sdt))
    conn.commit()

giamgia = input('Nhap sdt: ')
if giamgia == '': exit()
try:
    cur.execute(''' UPDATE Khach SET count = count - 3 WHERE sdt = ?
''', (giamgia, ))
except:
    print('khong tim thay sdt nay!')

conn.commit()

cur.execute('SELECT ten, sdt, email, count FROM Khach WHERE sdt = ?', (giamgia, ))
lay = cur.fetchone()
print('da giam 3 diem cho:', lay)
cur.close()
