import sys

with open(str(sys.argv[1]) , "r") as file:
    texto = file.read()

caracteres = ""
palabras = set(texto.split())

for i in texto:
    if i not in caracteres:
        caracteres += i

print("El número de caracteres distintos es: ", len(caracteres))
print("El número de palabras distintas es: ", len(palabras))