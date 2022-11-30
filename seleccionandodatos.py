#ENTRADAS DEL PROBLEMA
niveldeagua= int(input ("digita el nivel de agua"))

#EVALUANDO CAMINOS MULTIPLES (MAS DE 2)
if niveldeagua<=100:
    print("bajo nivel de agua")
elif niveldeagua>100 and niveldeagua<400:
    print("operación optima")
elif niveldeagua>=400:
    print("peligro.....")
else:
    print("nivel de agua no valido")
