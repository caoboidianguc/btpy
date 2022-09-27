import copy
original = [['conco', 'con Cong'],['con Ga','con ca']]
deepCo = copy.deepcopy(original)
shadow = original[:]

original.append('CON THAN LAN')
original[0].append(['Thuc An'])

print('-----------Shadow Copy---------')  #shadow copy khong tu copy them index,
print(shadow)
print()
print('------------Original Copy-----------')
print(original)
print()
print('------------deep Copy------------')
print(deepCo)

