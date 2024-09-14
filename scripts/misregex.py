import re

def esNumero(input):
    patron = "^\\d+$"
    if re.match(patron, input):
        return True
    else:
        return False

if "__name__" =="__main__":
    esNumero()
