# Se entiende que cada camisa cuesta 20.000 pesos
camisas = int(input("Cuantas camisas desea comprar?: "))
valor = 20000
if camisas >= 3:
    total = (valor*camisas) - (valor*camisas)*0.3
else:
    total = (valor*camisas) - (valor*camisas)*0.1
print(total)

