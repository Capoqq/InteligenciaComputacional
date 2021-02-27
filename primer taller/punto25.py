numero1 = int(input("Ingrese su numero 1: "))
numero2 = int(input("Ingrese su numero 2: "))
numero3 = int(input("Ingrese su numero 3: "))
if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
elif numero3 > numero1 and numero3 > numero2:
    print(numero3)

