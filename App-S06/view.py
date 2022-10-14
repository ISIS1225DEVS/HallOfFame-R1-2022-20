"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


from model import cmpMoviesByReleaseYear as m
from model import cmpalphabetically as a
import config as cf
import sys
import controller
from tabulate import tabulate
from prettytable import PrettyTable
from prettytable import ALL
from DISClib.ADT import list as lt
assert cf
import time


default_limit=1000
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def loadData(control,tamaño):
    services,total= controller.loadData(control,tamaño)
    return  services,total
def loadFirst(control):
    controller.first(control)
    
def getTime():
    return float(time.perf_counter()*1000)

def deltaTime(start, end):
    elapsed = float(end - start)
    return elapsed

def printMenu():
    print("-"*130)
    print("\nBienvenido")
    print("1- Cargar información en el catálogo, seleccionar tipo de estructura de datos y tamaño de la muestra")
    print("2- Listar las películas estrenadas en un periodo de tiempo")
    print("3- Listar programas de televisión agregados en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un género especifico")
    print("6- Encontrar contenido producido en un país ")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el TOP (N) de los géneros con más contenido")
    print("9- : Listar el TOP (N) de los actores con más participaciones en contenido")
    print("10- Seleccionar el algoritmo para ordenar los datos")


"""
Menu principal
"""

def newController(estructura):
    """
    Se crea una instancia del controlador
    """
    control = controller.newController(estructura)
    return control
control=newController(estructura="ARRAY_LIST")



while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:

        rta=int(input("\nSeleccione el tipo de estructura de datos:\n1. Array List\n2. Linked_list\nSeleccione una opción para continuar: "))
        if rta==1:
            control=newController("ARRAY_LIST")
        elif rta==2:
            control=newController("SINGLE_LINKED")
        else: 
            print("Opción invalida")
        
        t=input("\nSeleccione el tamaño de la muestra:\n-5pct\n-10pct\n-20pct\n-30pct\n-50pct\n-80pct\n-Large\n-Small\n Seleccione una opción para continuar: ")
        print("\nCargando información de los archivos ....\n")
        start_time=getTime()
        servicios,total=loadData(control,t)
        end_time= getTime()
        
        
        print("Loaded streaming service info\n\nTotal loaded titles: ",total,"\n","-"*130)
        print(tabulate(servicios,headers="keys",tablefmt="github"),"\n\n")
        filas,columnas=controller.load_data_req1(control["model"]["total"])
        controller.imprimirTabla(columnas,filas)
        print(round((deltaTime(start_time, end_time)),2))

        
    elif int(inputs[0]) == 2:
        start_year=input("Digite el año inicial (formato AAAA): ")
        end_year=input("Digite el año final (formato AAAA): ")
        start_time=getTime()
        filas, columnas, numero =controller.req1(control["model"], start_year, end_year)
        end_time= getTime()
        print(f"\nMovies released between {start_year} and {end_year}","\n","-"*130)
        print(f"There are {numero} Tv show between {start_year} and {start_year}","\n","-"*130)
        controller.imprimirTabla(columnas,filas)
        print(round((deltaTime(start_time, end_time)),2))


    elif int(inputs[0]) == 3:
        start_date=input("Digite la fecha inicial (formato year-month-day): ")
        end_date=input("Digite la fecha final (formato year-month-day): ")
        start_time=getTime()
        filas,titulos,numero=controller.req2(control["model"],start_date, end_date)
        print(f"There are {numero} Tv show between {start_date} and {end_date}","\n","-"*130)
        controller.imprimirTabla(titulos,filas)
        print(round((deltaTime(start_time, end_time)),2))
    
    elif int(inputs[0]) == 4:
        actor=input("Escriba el nombre del actor a buscar: ")
        start_time=getTime()
        var=controller.req3(control["model"], actor)
        end_time= getTime()
        print(f"\nContent with {actor} in the cast","\n","-"*130)
        print(f"{actor} cast parcticipation count: ","\n","-"*130)
        print(tabulate(var[1],headers="keys",tablefmt="github"),"\n\n")
        filas,columnas=var[0]
        controller.imprimirTabla(columnas,filas)
        print(round((deltaTime(start_time, end_time)),2))
        
    elif int(inputs[0]) == 5:
        genero=input("Digite el genero que desea consultar: ")
        start_time=getTime()
        n_movies,n_shows,filas,columnas,a=controller.req4(control["model"],genero)
        end_time= getTime()
        print(deltaTime(start_time, end_time))
        print(tabulate([["Movies",n_movies],["Tv_Shows",n_shows]],headers=["type","count"],tablefmt="github"))
        controller.imprimirTabla(columnas,filas)
        print(round((deltaTime(start_time, end_time)),2))

    elif int(inputs[0]) == 6:
        pais= input("Escriba el nombre del pais a buscar:")
        start_time=getTime()
        bpais=controller.req5(control["model"], pais)
        end_time= getTime()
        print(deltaTime(start_time, end_time))
        print(f"\nContent produced in {pais}","\n","-"*130)
        
        print(tabulate(bpais[1],headers="keys",tablefmt="github"),"\n\n")
        filas,columnas=bpais[0]
        controller.imprimirTabla(columnas,filas)
        print(round((deltaTime(start_time, end_time)),2))

    elif int(inputs[0]) == 7:
        director=input("Escriba el nombre del director a buscar: ")
        start_time=getTime()
        var=controller.req6(control["model"], director)
        end_time= getTime()
        print(deltaTime(start_time, end_time))
        print(f"\n{director} content type count: \n")
        print(tabulate(var[0],headers="keys",tablefmt="github"),"\n\n")
        print(f"\n{director} Streaming content type count: \n")
        print(tabulate(var[1],headers="keys",tablefmt="github"),"\n\n")
        print(f"\n{director} tags in (listed in) count: \n")
        print(tabulate(var[4],headers="keys",tablefmt="github"),"\n\n")
        print(f"\nThere are only {len(var[2])} IPs with {director} as director: \n")
        filas,columnas=var[2], var[3]
        controller.imprimirTabla(columnas, filas)
        print(round((deltaTime(start_time, end_time)),2))
        
    elif int(inputs[0]) == 8:
        top=int(input("Digite el top que desea buscar: "))
        start_time=getTime()
        tablas=controller.req7(control["model"],top)
        end_time= getTime()
        print(deltaTime(start_time, end_time))
        print("\n",tabulate(tablas[0],headers="keys",tablefmt="github"),"\n")
        print(tabulate(tablas[1],headers="keys",tablefmt="grid"))
        print(round((deltaTime(start_time, end_time)),2))

    elif int(inputs[0]) == 9:
        top=int(input("Digite el top que desea buscar: "))
        tabla,tabla2,tabla3=controller.req8(control["model"],top)
        
        print(tabulate(tabla,headers="keys",tablefmt="grid"),"\n\n")
        print(tabulate(tabla2,headers="keys",tablefmt="grid"),"\n\n")
        print(tabulate(tabla3,headers="keys",tablefmt="grid",showindex="always"))
    elif int(inputs[0])==10:
        ordenamiento=int(input("Selecione el algoritmo para ordenar los datos:\n1. selection\n2. insertion\n3. shell\n4. merge\n5. quick\n"))
        type_sort=""
        print("\nEl tiempo es de : ",)
        if ordenamiento==1:
            type_sort="selection"
            print(controller.sorting(control["model"]["movies"],type_sort))
        elif ordenamiento==2:
            type_sort="insertion"
            print(controller.sorting(control["model"]["movies"],type_sort))
        elif ordenamiento==3:
            type_sort="shell"
            print(controller.sorting(control["model"]["movies"],type_sort))
        elif ordenamiento==4:
            type_sort="merge"
            print(controller.sorting(control["model"]["movies"],type_sort))
        elif ordenamiento==5:
            type_sort="quick"
            print(controller.sorting(control["model"]["movies"],type_sort))

            
    else:
        sys.exit(0)
sys.exit(0)
