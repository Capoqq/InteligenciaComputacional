monto = int(input("Cual es el monto para la fianza: "))
if monto > 50000:
    cuota = monto*0.02
    print(f"Su cuota a pagar es del 2% del monto inicial {cuota}")
else:
    cuota = monto*0.03
    print(f"Su cuota a pagar es del 3% {cuota}")