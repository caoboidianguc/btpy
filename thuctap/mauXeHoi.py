

class XeHoi():
    def __init__(self, kieuXe, namSanXuat, mauSac, km):
        self.kieuXe = kieuXe
        self.namSanXuat = namSanXuat
        self.mauSac = mauSac
        self.km = km

    def tangToc(self,tocDo):
        xechay = f'xe chay {tocDo} Km/h'

        return xechay







honda = XeHoi('Accoss', 2020, 'xanh da troi')
tangtoc = honda.tangToc(5)
print(tangtoc)