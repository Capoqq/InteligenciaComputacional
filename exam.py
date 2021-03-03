#Punto 1
llantas = int(input("Ingrese su numero de llantas a comprar: "))
if llantas < 5:
    valorUnidad = 300
    valorTotal = llantas * valorUnidad
elif llantas >= 5 and llantas <= 10:
    valorUnidad = 250
    valorTotal = llantas * valorUnidad
elif llantas > 10:
    valorUnidad = 200
    valorTotal = llantas * valorUnidad
print(f"Este es el valor por llantas {valorUnidad}")
print(f"Este es el valor total {valorTotal}")

#Punto 2
print("Digite el valor total de su compra: ")
valor = int(input())
print("Digite su numero de cedula: ")
cedula = input()
ultimos = cedula[len(cedula)-2]+cedula[len(cedula)-1]
print(f"Los dos ultimos digitos son {ultimos}")
if ultimos == "01":
   valor = valor - (valor * 0.1)
   print(f'El valor a final a pagar es: {valor}')
else:
    if ultimos == "25":
        valor = valor - (valor * 0.2)
        print(f'El valor a final a pagar es: {valor}')
    else:
        if ultimos == "44":
            valor = valor - (valor * 0.35)
            print(f'El valor a final a pagar es: {valor}')
        else:
            if ultimos == "57":
                valor = valor - (valor * 0.5)
                print(f'El valor a final a pagar es: {valor}')
            else:
                print(f'El valor a final a pagar es: {valor}'
#Punto 3
numeroColchones = int(input("Ingrese la cantidad de colchones a comprar: "))
valorColchon = 100000
if numeroColchones > 0 and numeroColchones <=3:
    valorFinal = valorColchon*numeroColchones
elif numeroColchones > 3 and numeroColchones <=6:
    valorFinal = (valorColchon*numeroColchones) - (valorColchon*numeroColchones)*0.2
elif numeroColchones > 6 and numeroColchones < 8:
    valorFinal = (valorColchon*numeroColchones) - (valorColchon*numeroColchones)*0.25
elif numeroColchones >= 8:
    valorFinal = (valorColchon*numeroColchones) - (valorColchon*numeroColchones)*0.3
print(valorFinal)

#Punto 4
numeroEstudiantes = int(input("Ingresa la cantidad de estudiantes: "))
if numeroEstudiantes < 20:
    muestra = numeroEstudiantes*0.5
elif numeroEstudiantes >= 20 and numeroEstudiantes <= 30:
    muestra = numeroEstudiantes*0.6
elif numeroEstudiantes > 30:
    muestra = numeroEstudiantes*0.7
print(muestra)