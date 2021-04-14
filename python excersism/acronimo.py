import re


def abbreviate(palabras):
    return "".join(palabra[0].upper() for palabra in
                   re.findall(r"([a-zA-Z0-9]+(?:'\w+)?)", palabras))