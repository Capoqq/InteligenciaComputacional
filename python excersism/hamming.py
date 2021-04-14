def distancia(lado_a, lado_b):
    len_a = len(lado_a)
    len_b = len(lado_b)
    if len_a != len_b:
        raise ValueError("Deben tener el mismo tamaño")
    dist = 0
    i = 0
    while i < len_a:
        if lado_a[i] != lado_b[i]:
            dist += 1
        i += 1
    return dist