valor = 11000
computadores = int(input("Cuantas computadoras desea comprar?: "))
if computadores < 5:
    total = (computadores*valor) - (computadores*valor)*0.1
    print(computadores*valor)
elif computadores >= 5 and computadores < 10:
    total = (computadores*valor) -(computadores*valor)*0.2
elif computadores >= 10:
    total = (computadores*valor) - (computadores*valor)*0.4
print(total)
