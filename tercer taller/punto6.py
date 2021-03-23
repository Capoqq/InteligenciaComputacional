def Union(lista1, lista2): 
    final_lista = list(set(lista1) | set(lista2)) 
    return final_lista 
def interseccion(lista1, lista2):
    lista3 = [value for value in lista1 if value in lista2]
    return lista3
def Diferencia1(lista1, lista2):
    return (list(list(set(lista1)-set(lista2)) + list(set(lista2)-set(lista1))))
def Diferencia2(lista1, lista2):
    return (list(list(set(lista2)-set(lista1)) + list(set(lista1)-set(lista2))))
lista1 = [23, 15, 2, 14, 14, 16, 20 ,52] 
lista2 = [2, 48, 15, 12, 26, 32, 47, 54] 
print(Union(lista1, lista2))
print(interseccion(lista1, lista2))
print(Diferencia1(lista1, lista2))
print(Diferencia2(lista1, lista2))