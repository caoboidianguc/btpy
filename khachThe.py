import os
import csv

class Khach():
    point = 0

    def __init__(self, hoten, email, sdt):
        self.hoten = hoten
        self.email = email
        self.sdt = sdt
        #self.bday = bday
    
    def tangdiem(self):
        self.point += 1
        return self.point

nguoi = Khach('Thong q Vu', 'caoboidianguc@yahoo.com', 8033399070)

with open('tenkhach.csv','w') as file:
    ghi = csv.writer(file)
    ghi.writerows(nguoi)


print(os.path.exists('tenkhach.txt'))
#os.rename('tenkhach.txt', 'khachhang.txt')
#os.remove('tenfile')
print(os.path.getsize('khachhang.txt'))
print(os.path.abspath('khachhanh.txt')) #tim duong dan file
