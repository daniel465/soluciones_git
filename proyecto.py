#Determina la cantidad de dias que has vivido
from datetime import date,timedelta
import calendar
#Mostrar el menu de opciones
def Menu():
    print('='*70,'\n\tMenu adoptivo\n','='*70)
    print('1).Imprimir la cantidad de dias Vividos')
    print('2).Imprimir la cantidad de dias Vividos por Años')
    print('3).Imprimir la cantidad de dias que Viviriamos por Mes en el Año')
    print('0).Salir. ("Terminar")')
    return int(input('Digite la opcion,Elige --> '))
#Hallamos la cantidad de dias
def Mostrar_cant_dias_vividos(fecha_nace,ahora):
    todaydias=(ahora-fecha_nace).days
    print('='*70,"\n\tLa cantidad de dias vividos son : ",todaydias)
    return todaydias
#Cantidad de dias que vivimos por año
def Mostrar_cant_dias_vividos_anual(fecha_nace,ahora):
    print('='*70,'\n\tImprimiremos los dias que vivimos por año\n','='*70)
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
#La cantidad de dias que viviras en los siguientes meses
def Mostrar_cant_dias_que_viviriamos(cant_dias_vividos,ahora):
    print('='*70,'\n\tImprimiremos los dias que viviremos por mes entorno a este año\n','='*70)
    acumular=0
    fecha_aux=ahora
    for i in range(ahora.month,13):
        fecha_aux=fecha_aux.replace(month=i, day=calendar.monthrange(fecha_aux.year,i)[1])
        cant_dias=(fecha_aux-ahora).days
        acumular+=cant_dias
        print("Para el año %d/%d, la cant de dias q vivirias es :%d, cant dias mes : %d/ %d"%(fecha_aux.year,i,cant_dias_vividos+acumular,cant_dias,acumular))
        ahora=ahora.replace(month=i,day=calendar.monthrange(ahora.year,i)[1])
    print('Total de dias que podriasmos vivir en este año seria : ',(acumular+cant_dias_vividos))

if __name__ == '__main__':
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
    cant_dias=Mostrar_cant_dias_vividos(fecha_nace,ahora)
    opcion=1
    while(opcion):
        opcion=Menu()
        if opcion==1:
            g=Mostrar_cant_dias_vividos(fecha_nace,ahora)
        elif opcion==2:
            Mostrar_cant_dias_vividos_anual(fecha_nace,ahora)
        elif opcion==3:
            Mostrar_cant_dias_que_viviriamos(cant_dias,ahora)
        else:
            break;
