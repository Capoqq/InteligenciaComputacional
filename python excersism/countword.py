from collections import Counter
import re


def cuenta_palabra(oracion):
    return Counter(re.findall(r"[a-z]+'[a-z]|[0-9]|[a-z]+", oracion.lower()))