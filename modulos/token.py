import random

def token():
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    letras_min = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z"]
    letras_may = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","W","Y","Z"]

    vacio_1 = []
    vacio_2 = []
    vacio_3 = []
    vacio = []

    token = ""
    token_1 = ""
    token_2 = ""
    token_3 = ""

    for x in range(12):
        token_1 += random.choice(letras_min)
    
    for x in range(12):
        token_2 += random.choice(letras_may)

    for x in range(16):
        token_3 += random.choice(numeros)

    caracteres = token_1 + token_2 + token_3

    for x in range(40):
        token += random.choice(caracteres)
     
    return token

