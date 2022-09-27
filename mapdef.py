def demso(danhsach):
    lan = 0
    tong = 0
    trungbinh = 0
    for so in danhsach:
        tong += so
        lan += 1
    trungbinh = tong/lan
    return trungbinh

dayso = [9,12,34,2,5,6,8,9,0,23,45,67,54,2,3]
thu = map(demso,dayso)


thukhac = lambda lit : lit[0] +1
cai = thukhac(dayso)
#print(type(cai))
#print(cai)

#list comprehension: neu muon tao list moi dua tren list cu voi dieu kien nao do

daysoMoi = [so for so in dayso if so%2 == 0]

print(daysoMoi)