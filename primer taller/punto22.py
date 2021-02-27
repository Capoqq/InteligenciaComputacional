descuento = 0.1
desnosy = 0.05
producto = int(input("Aqui va el precio de tu producto: "))
marca = input("Que marca es su producto: ")
if producto >= 2000 and marca != "nosy":
    total = producto - producto*0.1
    total = total + total*0.16
elif producto >= 2000 and marca == "nosy":
    total = producto - producto*0.1
    total = total - total*0.05
    total = total + total*0.16
elif producto < 2000 and marca == "nosy":
    total = producto - producto*0.05
    total = total + total*0.16
else:
    total = producto + producto*0.16
print(total)