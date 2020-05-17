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
#Fecha en que nacimiento fue :
print('La fecha de nacimiento fue :')
print('\t',fecha_nace.strftime('%A %d, %B %Y'))
#Fecha actual de referencia es :
print('Fecha actual de referencia :')
print('\t',ahora.strftime('%A %d, %B %Y'))
#hallamos la cantidad de dias
todaydias=(ahora-fecha_nace).days
print("La cantidad de dias vividos son : ",todaydias)
#cantidad de dias por año
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