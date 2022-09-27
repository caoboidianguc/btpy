import collections
import datetime

#Immutable Data Structures: namedtuple

khach = collections.namedtuple("khahang", ['ten',"sdt",'email',"ngayden" ])

#nếu sử dụng list như dưới đay thì thông tin khong bị sua doi nhung co the xoá.
listkhach = [khach('Thong',8033399070,'hibiscus@hotmail.com.vn','09-02-2020'),
        khach('Linh',8032628775, 'hoadambutxinh@icloud.com','12-02-2019'),
        khach('hibi',8033098890,'hibi@gmail.com','04-09-2015')
        ]

layten = listkhach[1].ten
del(listkhach[0])

doiten = listkhach[0].ten
print(doiten)

#voi tuple thi thong tin khong the bi xoa nua
tuplekhach = (khach('Thong',8033399070,'hibiscus@hotmail.com.vn','09-02-2020'),
        khach('Linh',8032628775, 'hoadambutxinh@icloud.com','12-02-2019'),
        khach('hibi',8033098890,'hibi@gmail.com','04-09-2015')
        )

def khachHang():
    dskhachHang = []
    ten = input('Nhap ten ban')
    sdt = input('Nhap SDT')
    email = input('Nhap Email')
    lucden = datetime.datetime.now()
    den = lucden.strftime('%x')
    kha = khach(ten, sdt,email,den)
    dskhachHang.append(kha)
    return dskhachHang


