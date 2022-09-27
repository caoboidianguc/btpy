from tenThoNail import ThoNail



class Nailspa:
    def __init__(self, tenTiem, sdtTiem):
        self.tentiem = tenTiem
        self.sdttiem = sdtTiem
        self.diadiem = ""
        self.dsKhach = []
        self.tongTho = []
        
        
    
    def tuyentho(self, tennail, sdt):
        tho = ThoNail(tenNailTech=tennail, sdt=sdt)
        self.tongTho.append(tho)
        for tho in self.tongTho:
            print(f"Tien hien co : {tho.ten}")

   
    def booking(self,tenkh, sdtkh, thGian, dichVu):
        
        khach = {'ten khach': tenkh, 'sdtkh': sdtkh, 'thoi gian': thGian, 'can lam': dichVu}
        self.dsKhach.append(khach)


    def cancel(self, tiem, ten, sdt):
        for kh in self.dsKhach:
            if kh['ten Tiem'] == tiem and kh['ten khach'] == ten and kh['sdtkh'] == sdt:
                self.dsKhach.remove(kh)




#dang ki ten tiem
spar = Nailspa('sparkle', 8039997642)

spar.tuyentho('Thong', 803)
spar.tuyentho("Quang", 800)







'''
supernail = Nailspa('Top Nails', 8033399070)

supernail.booking('Quang', 8039840980, '12-02-2020', 'bo moi')
supernail.booking('Linh', 803123456, '15-03-2020', 'lam dep')
supernail.booking('Vu', 8032628775, '02-07-2020', 'den choi')

supernail.booking('thong', 803123123, '12-02-2020', 'bo moi')
supernail.booking('pham', 803123456, '15-03-2020', 'lam dep')
supernail.booking('ngoc', 8039089080, '02-07-2020', 'den choi')

#dung filter de loc nhung muc minh can, no se tra ve 1 ds iterator
locds = filter(lambda x: x['can lam'] == 'bo moi',supernail.dsKhach)

for khach in locds:
    print(khach)
'''