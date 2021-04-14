def convert(number):
    sonido = ""
    num_snd = { "3" : "Pling" , "5" : "Plang" , "7" : "Plong"}
    for key in num_snd:
        if number % int(key) == 0:
            sonido = sonido + num_snd[key]
    return sonido if sonido else str(number)