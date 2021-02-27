sueldoSin = int(input("Escriba el sueldo sin el descuento: "))
politicaPublica = sueldoSin*0.01
seguroSocial = sueldoSin*0.04
cajaAhorro = sueldoSin*0.05
sueldoFinal = sueldoSin - politicaPublica - seguroSocial - cajaAhorro
print(f"Eso se debe descontar por politica publica {politicaPublica}")
print(f"Esto se debe descontar por seguroSocial {seguroSocial}")
print(f"Esto se debe descontar por caja de ahorro {cajaAhorro}")
print(f"Esto es lo que se debe pagar al empleado {sueldoFinal}")
