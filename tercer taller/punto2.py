lista2 = [1,8,4,6,10,5]
contadorPar = 0
contadorImpar = 0
for i in lista2:
    if i % 2 == 0:
        contadorPar +=1
    else:
        contadorImpar += 1
print(contadorImpar,contadorPar)

