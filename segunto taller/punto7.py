añosAntiguedad = int(input("Escriba sus años de antiguedad"))
if añosAntiguedad >= 1:
    bonoInicio = 100000
    bonofinal = (añosAntiguedad - 1)*120000 + bonoInicio
else:
    print("No tienes la antiguedad necesaria")
print(bonofinal)
