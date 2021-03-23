productoria = 1
i = 0
suma = 0
lista7 = [1,2,3,4,5,6]
B = lista7[:len(lista7)//2]
C = lista7[len(lista7)//2:]
print(B)
print(C)
for n in C:
    suma += n 
    print(suma)
while i < len(B):
    productoria = productoria * B[i]
    i +=1
print(productoria)
