from collections import Counter
lista6 = [1,1,1,1,3,4,9,6,7,5,8,8,8]
""" contador = 0 """
print(Counter(lista6).most_common()[0][0])
print(max(set(lista6), key=lista6.count))
""" contador = 0
for i in lista6:
    lista6.count(i)
print( lista6.count(i)) """
""" for i in lista6:
    if lista6.count(i) > 1:
        print(i)
 """
""" for i in lista6:
     if i == i:
         contador +=1
print(contador)
 """