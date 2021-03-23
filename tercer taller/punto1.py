lista1 = [1,4,6,2,3,5]
suma = 0
i = 0
productoria = 1
for n in lista1:
    suma += n 
    print(suma)
    

while i < len(lista1):
    productoria = productoria * lista1[i]
    i +=1
print(productoria)

print(max([ int(num) for num in lista1]))
print(min([ int(num) for num in lista1]))