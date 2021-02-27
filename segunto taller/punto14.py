numeroDias = int(input("Escriba cuantos dias se va a quedar: "))
if numeroDias > 1:
    dia1 = 100000
    total = (numeroDias - 1)*200000 + dia1
    print(total)
else:
    total = numeroDias*100000
print(total)