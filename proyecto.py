#Determina la cantidad de dias que has vivido
#importamos date
from datetime import date
import calendar
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
#La cantidad de dias que viviras en los siguientes meses
print('='*70)
print('Impresion de cantidad de dias que viviremos')
print('='*70)
acumular=0
fecha_aux=ahora
for i in range(ahora.month,13):
    fecha_aux=fecha_aux.replace(month=i, day=calendar.monthrange(fecha_aux.year,i)[1])
    cant_dias=(fecha_aux-ahora).days
    acumular+=cant_dias
    print("Para el año %d/%d, la cant de dias q vivirias es :%d, cant dias mes : %d/ %d"%(fecha_aux.year,i,todaydias+acumular,cant_dias,acumular))
    ahora=ahora.replace(month=i,day=calendar.monthrange(ahora.year,i)[1])
print('='*70)
print('Total de dias que podriasmos vivir en este año seria : ',(acumular+todaydias))