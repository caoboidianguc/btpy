

class Rooms():
    def __init__(self, oneRoom, two, house):
        self.oneRoom = oneRoom
        self.twoRoom = two
        self.houseWithThreeRoom = house

    def tinhtong (self):
        tong = self.oneRoom + self.twoRoom + self.houseWithThreeRoom
        return tong

    def phong1 (self, chon):
        self.oneRoom = self.oneRoom - chon
        return self.oneRoom
    
    def phong2 (self, chon):
        self.twoRoom = self.twoRoom - chon
        return self.twoRoom

    def house (self, chon):
        self.houseWithThreeRoom = self.houseWithThreeRoom - chon
        return self.houseWithThreeRoom

    def traPhong (self, tra):
        if tra == "mot":
            self.oneRoom += 1
        elif tra == "hai":
            self.twoRoom += 1
        elif tra == "nha":
            self.houseWithThreeRoom += 1
        else:
            return "Ma nhap khong dung"





hibi = Rooms(5,7,9)
hibi.phong1(1)
hibi.traPhong("mot")
tong = hibi.tinhtong()
print(tong)
#print(hibi.oneRoom)