dinero = int(input("Cantidad:"))

uno = dinero // 200
restouno = dinero % 200
dos = restouno // 100
restodos = restouno % 100
tres = restodos // 50
restotres = restodos % 50
cuatro = restotres // 20
restocuatro = restotres % 20
cinco = restocuatro // 10
restocinco = restocuatro % 10
seis = restocinco // 5
restoseis = restocinco % 5
siete=restoseis//2
restosiete=restoseis % 2
ocho=restosiete//1
ocho=restosiete % 2

"""clase base"""
if dinero==0:
    print("0")
else:
    if uno >= 1: print(uno,"Billete de 200 pesos")
    if dos >= 1: print (dos, "Billete de 100 pesos")
    if tres >= 1: print (tres,"Billete de 50 pesos")
    if cuatro >= 1: print (cuatro, "moneda de 20 pesos")
    if cinco >= 1:print (cinco, "moneda de 10 pesos")
    if seis >= 1: print (seis,"Moneda de 5 pesos")
    if siete>=1:print(siete,"Moneda de 2 pesos")
    if ocho>=1: print(ocho,"moneda de 1 pesos")