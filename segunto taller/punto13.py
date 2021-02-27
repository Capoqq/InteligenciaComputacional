familiares = int(input("Cuantos familiares van a ir?: "))
dias = int(input("Cuantos dias se van a quedar?: "))

totalSin = (familiares*25000)*dias
total = totalSin*0.12 + totalSin
print(total)
