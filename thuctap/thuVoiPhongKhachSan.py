import datetime
from room import Rooms




class hotel ():
    def __init__(self, name, rating, phong1, phong2, phong3):
        self.name = name
        self.rating = rating
        self.rooms = Rooms(phong1, phong2, phong3)
        self.gym = False
        self.pool = False
        self.khach = []
        
    def checkAvailability(self):
        tongPhong = self.rooms.tinhtong()
        ro = str(tongPhong)
        if self.gym == True:
            self.gym = 'Co San'
        else:
            self.gym = "Khong co"
        if self.pool == True:
            self.pool = 'Co san'
        else: self.pool = 'khong'
        tongket = "Khach San hien co "+ ro + " phong trong! \nPhong Tap The Thao "+ self.gym +'\nHo Boi '+ self.pool
        return tongket

    def booking(self, room, ten, sdt, ngayvao, ngayRa):
        tg = datetime.datetime.now()
        thoigian = tg.strftime('%x')

        if room == "phong don":
            room = self.rooms.phong1(1)
        elif room == "phong doi":
            room = self.rooms.phong2(1)
        elif room == "nha":
            room = self.rooms.house(1)
        else:
            return "Ma phong khong dung! \nXin chon:\nphong don\n phong doi \n nha"
        
        tenkhach = {'hoten': ten, 'sdt' : sdt, 'ngay den': ngayvao,
         'ngay ra': ngayRa, 'thoi gian book':thoigian}
        self.khach.append(tenkhach)
        return ('Da duoc dat cho ' + ten)

    def cancelbooking(self, tenhuy, dienthoai, ma):
        for kha in self.khach:
            if kha["hoten"] == tenhuy and kha["sdt"] == dienthoai:
                huy = kha
                self.rooms.traPhong(ma)
                self.khach.remove(huy)
    
    def makeKey(self, ten, sdt):
        mabam = ""
        for kha in self.khach:
            if kha['hoten'] == ten and kha['sdt'] == sdt:
                vao = kha['ngay den']
                ra = kha['ngay ra']
                bam = ten + ra
                mabam = hash(bam)
                print(f'khoa cua ban co ngay han tu {vao} den ngay {ra}')
        return mabam



hoatham = hotel('Hoa But', '5 star', 6, 9, 12)


hoatham.booking("phong don",'Thong',8033399070,'12-1-2021', '15-1-2021')
hoatham.booking("phong doi",'Linh',8032628775,'10-1-2021','15-1-2020')
hoatham.booking("nha",'Quang', 8032132387, '20-02-2010','26-02-2010')
#hoatham.cancelbooking('Quang',8032132387, "nha")


key = hoatham.makeKey("Thong", 8033399070)
print(key)

print(hoatham.name)
print(hoatham.khach)
ktra = hoatham.checkAvailability()
print(ktra)


