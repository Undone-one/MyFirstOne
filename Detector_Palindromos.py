import unicodedata
import sys

print("DETECTOR DE PALINDROMOS")

palabra = input("Palabra o frase:").lower().replace(" ","").replace(",","").replace(".","")
caracteres = dict.fromkeys (c for c in range (sys.maxunicode) if unicodedata.combining(chr(c)))
cadena_normalizada = unicodedata.normalize('NFD', palabra)
palabra = cadena_normalizada.translate(caracteres)

rever = ""
for i in palabra:
    rever= i + rever
print("Palabra/Frase invertida y simplificada:", rever)    
if rever == palabra:
   print("La palabra/frase ingresada es un palindromo")
else:
   print("La palabra/frase ingresada no es un palindromo.")