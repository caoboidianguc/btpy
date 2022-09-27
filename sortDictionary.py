#sorted(iterable, key= , reserved=True or False) return new list
#  .sort() giu nguyen list cu va sort no


doan = "what are all the basics which i should complete before going to ml The expression is executed and the result is returned"
chiadoan = doan.split()
#xapxep = sorted(chiadoan)
#print(xapxep)

def nhoDenLon (dsach):
    hopTuDien = {}
    for item in dsach:
        if item not in hopTuDien:
            hopTuDien[item] = len(item)
    trave = sorted(hopTuDien, key=(lambda x: hopTuDien[x]))
    
    return trave



hopTu = nhoDenLon(chiadoan)

#print(hopTu)

tudien = {}
tudien['kho'] = 2
tudien['chu'] = 1

print(sorted(tudien ,key=(lambda x: tudien[x])))