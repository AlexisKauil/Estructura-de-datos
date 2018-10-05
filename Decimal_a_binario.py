#Programam para convertir un numero decimal a binario.
#Kauil Dzib Alexis

print('PROGRAMA QUE DETERMINA UN NUMERO DECIMAL A BINARIO')
num = int(input("Digite un numero decimal:"))
 # Metodo recursivo
def binario(bi):
	if bi == 0:
		return " "
	else:
		return str (binario(bi//2))+str(bi%2)

print (binario(num))# llamar la funciom binario
