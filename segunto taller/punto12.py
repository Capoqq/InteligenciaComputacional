numeroDvd = int(input("Escriba el numero de peliculas que desea rentar: "))
numeroDias = int(input("Cuantos dias lo quieres rentar: "))
if numeroDvd > 1:
    numeroDvd = numeroDvd - 1
    total = numeroDvd * numeroDias*1500
    print(total)
else: 
    total = numeroDvd * numeroDias*1500
    print(total)
print(total)