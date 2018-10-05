#Programa para saber si una palabra es un palindromo.
# Kaui Dzib Alexis
print ("PROGRAMA QUE DETERMINA SI UNA PALABRA O FRASEES UN PALINDROMO")
frase= input("Ingresa una palabra o una frase: ")

frase_sin_espacios = frase.replace(" ","")

def palindromo(texto):
	if len(texto)<=1:
		return True
	else:
		return texto[0] == texto[-1] and palindromo(texto[1: -1])

if palindromo(frase_sin_espacios) == True:
	print("LA FRASE: "+str(frase)+"  Es palindromo")
else:
	print("LA FRASE: "+str(frase)+" No es Palindromo")