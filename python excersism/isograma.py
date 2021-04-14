def isograma(palabra):
    
    alfabeto = set(list('abcdefghijklmnopqrstuvwxyz'))
    palabra = filter(lambda x: x in alfabeto, list(palabra.lower()))
    letra = set(palabra)
    return len(letra) == len(palabra)