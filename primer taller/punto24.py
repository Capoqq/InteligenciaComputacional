numero1 = int(input("Escriba su numero 1: "))
numero2 = int(input("Escibra su numero 2: "))
if numero1 == numero2:
    resultado = numero1*numero2
elif numero1 > numero2:
    resultado = numero1 - numero2
elif numero1 < numero2:
    resultado = numero1 + numero2
print(resultado)