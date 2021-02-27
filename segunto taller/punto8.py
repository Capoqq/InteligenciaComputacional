numeroHoras = int(input("Escriba el numero de horas a pagar: "))
cajaAhorro = (numeroHoras*20000)*0.05
total= (numeroHoras*20000) - cajaAhorro
print(f"Este es el descuento por caja de ahorro {cajaAhorro}")
print(f"Es es el total a pagarle al profesor {total}") 