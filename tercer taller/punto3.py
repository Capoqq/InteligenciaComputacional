lista3 = [1,5,3,6,8]
lista4 = [3,5,7,9,10]
lista5 = []
for i in range(len(lista3)):
    lista5.append(lista3[i] + lista4[i])

print(lista5)
for i in range(len(lista3)):
    lista5.append(lista3[i] - lista4[i])

print(lista5)