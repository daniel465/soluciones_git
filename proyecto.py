#Determina la cantidad de dias que has vivido
#importamos date
from datetime import date
ahora=date.today()
#ingresamos la fecha nacimiento
print("Ingresa la fecha de nacimiento ")
agno=int(input("Digite el año :"))
mes=int(input("Digite el mes :"))
dia=int(input("Digite el dia :"))
fecha_nace=date(agno,mes,dia)
#hallamos la cantidad de dias
todaydias=(ahora-fecha_nace).days
print("La cantidad de dias vividos son : ",todaydias)