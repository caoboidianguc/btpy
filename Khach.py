


class Khach:
    def __init__(self, ten, sdt):
        self.ten = ten
        self.sdt = sdt
        self.tongGia = 0

    def chonDichVu(self, dichvu, danhMuc):
        self.dichvu = dichvu
        
        if dichvu in danhMuc.keys():
            gia = danhMuc[dichvu]
            self.tongGia += gia
            
        return self.tongGia

    def tinhTien(self):
        print(f"Tong so tien la: {self.tongGia}")
        self.tongGia = 0
    
    def huyDichVu(self, dichvu, danhMuc):
        self.dichvu = dichvu
        if dichvu in danhMuc.keys():
            huy = danhMuc[dichvu]
            self.tongGia -= huy
            return self.tongGia


listGia = {"tay": 25, 
            "chan": 40,
            "fullSet": 55,
            "pinkWhite": 65,
            "gel": 15,
            "fillIn":45,
            "dip": 50}




thong = Khach("thong", 803)
thong.chonDichVu("chan",listGia)
thong.chonDichVu("tay",listGia)
thong.huyDichVu("tay",listGia)
thong.tinhTien()

