#Determina la cantidad de dias que has vivido
from datetime import date,timedelta
import calendar
ahora=date.today()
#ingresamos la fecha nacimiento
print("Ingresa la fecha de nacimiento ")
agno=int(input("Digite el año :"))
mes=int(input("Digite el mes :"))
dia=int(input("Digite el dia :"))
fecha_nace=date(agno,mes,dia)
#Fecha en que nacimiento fue :
print('La Fecha de nacimiento fue :\t',fecha_nace.strftime('%A %d, %B %Y'))
#Fecha actual de referencia es :
print('Fecha actual de referencia :\t',ahora.strftime('%A %d, %B %Y'))
#cantidad de dias que vivimos por año
print('='*70)
print('Imprimiremos los dias que vivimos por año')
print('='*70)
fecha_nace_aux=fecha_nace
comprobar=0
for i in range(fecha_nace.year,ahora.year):
    aux=date(i+1,1,1)
    print('Del año %d, vivimos esta cantidad de dias : %d '%(i,(aux-fecha_nace_aux).days))
    comprobar+=(aux-fecha_nace_aux).days
    fecha_nace_aux=date(i+1,1,1)
print('Del año %d, vivimos esta cantidad de dias : %d '%(i+1,(ahora-fecha_nace_aux).days))
comprobar+=(ahora-fecha_nace_aux).days
print('Total Comprobado : ',comprobar)
print('='*70)
#hallamos la cantidad de dias
todaydias=(ahora-fecha_nace).days
print("La cantidad de dias vividos son : ",todaydias)
#La cantidad de dias que viviras en los siguientes meses
print('='*70)
print('Imprimiremos los dias que viviremos por mes entorno a este año')
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