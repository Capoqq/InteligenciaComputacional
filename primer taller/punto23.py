dineroInicial = 1000000
compra = int(input("De cuento es el valor de su compra: "))
if compra < 500:
    dineroInvertido = compra*0.7
    credito = compra*0.3
    interes = credito*0.2
    print(f"Esta es la cantidad de dinero a invertir {dineroInvertido} ")
    print(f"Este es el valor del credito { credito }")
    print(f"Este es el valor del interes {interes}")
elif compra > 500000:
    dineroInvertido = compra*0.55
    prestamo = compra*0.3
    credito = compra*0.15
    interes = credito*0.2
    print(f"Esta es la cantidad de dinero a invertir {dineroInvertido}")
    print(f"Este es el valor del prestamo {prestamo}")
    print(f"Este es el valor del credito {credito}")
    print(f"Este es el interes del credito {interes}")
elif compra >= 500 and compra < 500000:
    dineroInvertido = compra
    print(f"La empresa paga todo el valor de la compra {dineroInvertido}")