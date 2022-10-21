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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*100)
import csv
csv.field_size_limit(2147483647)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar las películas estrenadas en un periodo de tiempo ")
    print("3- Listar programas de televisión agregados en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un género especifico")
    print("6- Encontrar contenido producido en un país")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el TOP (N) de los géneros con más contenido")
    print("9- Seleccionar tipo de algoritmo de ordenamiento")
    print("10- Listar el TOP (N) de los actores con más participaciones en contenido")
    print("11- Seleccionar tipo de representación de la lista")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 11:
            tipo_lista = input("Que tipo de representacion de la lista quiere? (ARRAY_LIST o SINGLE_LINKED)\n")
            inputs=1
    else:
            tipo_lista = "ARRAY_LIST"
    if int(inputs)== 1:
            opcion = int(inputs)
            print("Cargando información de los archivos ....")
            tamanio_datos = input("Elija el tamaño de la muestra que desea: (-5pct, -10pct, -20pct, -30pct, -50pct, -80pct, -large o -small)\n")
            catalogo=controller.inicializarCatalogo(tipo_lista)
            controller.loadData(catalogo,tamanio_datos)

            listaNetflix=catalogo['listaNetflix']
            size=lt.size(listaNetflix)
            result = controller.sortTitles(catalogo, 'listaNetflix', int(size))
            delta_time = f"{result[1]:.3f}"
            sorted_listN = result[0]
            print("Para", size, "elementos, delta tiempo: ", str(delta_time))

            primeros3Netflix=controller.primeros3(sorted_listN,opcion)

            print("                                                        NETFLIX: ")
            print("----------------------------------------------Los primeros 3 contenidos son-----------------------------------------------------")
            for nombre in lt.iterator(primeros3Netflix):
                print(nombre)

            print("\n----------------------------------------------Los ultimos 3 contenidos son-----------------------------------------------------")
            ultimos3Netflix=controller.ultimos3(sorted_listN,opcion)
            for nombre in lt.iterator(ultimos3Netflix):
                print(nombre)
            size=lt.size(listaNetflix)  
            print("\nEl total de contenidos es " + str(size))
            

            listaHulu= catalogo['listaHulu']
            size=lt.size(listaHulu)
            result = controller.sortTitles(catalogo, 'listaHulu', int(size))
            delta_time = f"{result[1]:.3f}"
            sorted_listH = result[0]
            print("Para", size, "elementos, delta tiempo:", str(delta_time))
            primeros3Hulu=controller.primeros3(sorted_listH,opcion)
            print("\n                                                       HULU: ")
            print("----------------------------------------------Los primeros 3 contenidos son-----------------------------------------------------")
            for nombre in lt.iterator(primeros3Hulu):
                print(nombre)

            print("\n----------------------------------------------Los ultimos 3 contenidos son-----------------------------------------------------")
            ultimos3Hulu=controller.ultimos3(sorted_listH,opcion)
            for nombre in lt.iterator(ultimos3Hulu):
                print(nombre)
            print("\nEl total de contenidos es " + str(size))

            listaDisney= catalogo['listaDisney']
            size=lt.size(listaDisney)
            result = controller.sortTitles(catalogo, 'listaDisney', int(size))
            delta_time = f"{result[1]:.3f}"
            sorted_listD = result[0]
            print("Para", size, "elementos, delta tiempo:", str(delta_time))
            primeros3Disney=controller.primeros3(sorted_listD,opcion)
            print("\n                                                        DISNEY: ")
            print("----------------------------------------------Los primeros 3 contenidos son-----------------------------------------------------")
            for nombre in lt.iterator(primeros3Disney):
                print(nombre)

            print("\n--------------------------------------------Los ultimos 3 contenidos son------------------------------------------------------")
            ultimos3Disney=controller.ultimos3(sorted_listD,opcion)
            for nombre in lt.iterator(ultimos3Disney):
                print(nombre)
            print("\nEl total de contenidos es " + str(size))

            listaPrime= catalogo['listaPrime']
            size=lt.size(listaPrime)
            result = controller.sortTitles(catalogo, 'listaPrime', int(size))
            delta_time = f"{result[1]:.3f}"
            sorted_listP = result[0]
            print("Para", size, "elementos, delta tiempo:", str(delta_time))
            primeros3Prime=controller.primeros3(sorted_listP,opcion)
            print("\n                                                      AMAZON PRIME: ")
            print("------------------------------------------------Los primeros 3 contenidos son------------------------------------------------------")
            for nombre in lt.iterator(primeros3Prime):
                print(nombre)
            
            print("\n----------------------------------------------Los ultimos 3 contenidos son------------------------------------------------------")
            ultimos3Prime=controller.ultimos3(sorted_listP,opcion)
            for nombre in lt.iterator(ultimos3Prime):
                print(nombre)
            print("\nEl total de contenidos es " + str(size)+"\n")
            
            listaTotal=catalogo['listaTotal']
            size=lt.size(listaTotal)
            result = controller.sortTitles(catalogo, 'listaTotal', int(size))
            sorted_listT = result[0]
            
            listaTotal=catalogo['listaTotal']
            size=lt.size(listaTotal)
            result = controller.sortSeries(catalogo, 'listaTotal', int(size))
            sorted_listSeries = result[0]

            listaTotal=catalogo['listaTotal']
            size=lt.size(listaTotal)
            result = controller.sortDirector(catalogo, 'listaTotal', int(size))
            sorted_listDirector = result[0]

            listaTotal=catalogo['listaTotal']
            size=lt.size(listaTotal)
            result = controller.sortActores(catalogo, 'listaTotal', int(size))
            sorted_listActores = result[0]

    elif int(inputs) == 2:
            opcion = int(inputs)
            inicial = input ("Introduzca el año inicial que del rango que desea consultar: ")
            final = input ("Introduzca el año final que del rango que desea consultar: ")
            periodo = controller.periodo_tiempo_peliculas(inicial,final,sorted_listT)

            print("----------------------------------------------Los primeros 3 contenidos son------------------------------------------------------")
            primeros3anio=controller.primeros3(periodo,opcion)

            for nombre in lt.iterator(primeros3anio):
                print(nombre)

            print("\n--------------------------------------------Los ultimos 3 contenidos son------------------------------------------------------")
            ultimos3anio=controller.ultimos3(periodo,opcion)
            for nombre in lt.iterator(ultimos3anio):
                print(nombre)

            size = lt.size(periodo)
            print("\n--------------------------------------------------------------------------------------------------------------------------------")
            print("El total de peliculas que esta entre los años " + str(inicial) + " y " + str(final) + " es " +str(size))
            print("--------------------------------------------------------------------------------------------------------------------------------")
            
            size=lt.size(periodo)
            result = controller.sortReleaseYear(periodo, int(size))
            delta_time = f"{result[1]:.3f}"
            print("Para", size, "elementos, delta tiempo:", str(delta_time))

    elif int(inputs) == 3:
        opcion = int(inputs)
        inicial = input ("Introduzca la fecha inicial que del rango que desea consultar: \n")
        final = input ("Introduzca la fecha final que del rango que desea consultar: \n")
        periodo = controller.periodo_tiempo_series(inicial,final,sorted_listSeries)

        print("----------------------------------------------Los primeros 3 contenidos son------------------------------------------------------")
        primeros3anio=controller.primeros3(periodo,opcion)
        print("\n" +str(periodo))

        for nombre in lt.iterator(primeros3anio):
            print(nombre)

        print("\n---------------------------------------------Los ultimos 3 contenidos son------------------------------------------------------")
        ultimos3anio=controller.ultimos3(periodo,opcion)
        for nombre in lt.iterator(ultimos3anio):
            print(nombre)

        size = lt.size(periodo)
        print("\n-------------------------------------------------------------------------------------------------------------------------------")
        print("El total de programas de television que esta entre los años " + str(inicial) + " y " + str(final) + " es " +str(size))
        print("------------------------------------------------------------------------------------------------------------------------------------\n")
        
        size=lt.size(periodo)
        result = controller.sortDateAdded(periodo, int(size))
        delta_time = f"{result[1]:.3f}"
        print("Para", size, "elementos, delta tiempo:", str(delta_time))

    elif int(inputs)== 4:
        opcion = int(inputs)
        actor = input("Introduzca el nombre del actor del cuál le gustaria encontrar contenido: ")
        peliculas, series, lista_actor = controller.contenido_por_actor( actor ,sorted_listActores)
        cont_peliculas = lt.size(peliculas)
        cont_series = lt.size(series)
        print("\n-------------------------------------------------------------------------------------------------------------------------------")
        print("Peliculas en las que el actor aparece: " + str(cont_peliculas)+ ". ")
        print("Programas en los que el actor aparece: " + str(cont_series)+ ". ")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        cantidad_titulos = lt.size(lista_actor)
        if cantidad_titulos>5:
            primeros3T = controller.primeros3(lista_actor, opcion)
            for titulo in lt.iterator(primeros3T):
                print (titulo)
                print("\n-------------------------------------------------------------------------------------------------------------------------------")
            ultimos3T = controller.ultimos3(lista_actor, opcion)
            for titulo in lt.iterator(ultimos3T):
                print (titulo)
                print("--------------------------------------------------------------------------------------------------------------------------------")

        else :
            listar = controller.listar(lista_actor)
            for titulo in lt.iterator(listar):
                print (titulo)
                print("--------------------------------------------------------------------------------------------------------------------------------")


    elif int(inputs) == 5:
            opcion = int(inputs)
            i = 1
            genero = input("Inserte el genero de películas y programas desea ver \n")
            gen, peliculas, series = controller.contenido_por_genero(genero,sorted_listDirector)
            
            print("----------------------------------------------Los primeros 3 contenidos son------------------------------------------------------")
            primeros3T=controller.primeros3(gen,opcion)

            for nombre in lt.iterator(primeros3T):
                print(nombre)

            print("\n---------------------------------------------Los ultimos 3 contenidos son------------------------------------------------------")
            ultimos3T=controller.ultimos3(gen,opcion)
            for nombre in lt.iterator(ultimos3T):
                print(nombre)
            
            size = lt.size(gen)
            print("\n-------------------------------------------------------------------------------------------------------------------------------")
            print("El total de contenidos que pertenece al genero " + str(genero) + " es " + str(size) + ". De las cuales, " +str(peliculas)+ " son peliculas y " + str(series)+ " son series")
            print("------------------------------------------------------------------------------------------------------------------------------------\n")

    elif int(inputs) == 6:
            opcion = int(inputs)
            i = 1
            pais = input("Inserte el país del que desea ver sus películas y programas \n")
            lista_pais, peliculas, series = controller.contenido_por_pais(pais,sorted_listDirector)
            
            size = lt.size(lista_pais)
            print("\n--------------------------------------------------------------------------------------------------------------------------------")
            print("El total de contenidos que pertenece al país " + str(pais) + " es " + str(size) + ". De las cuales, " +str(peliculas)+ " son peliculas y " + str(series)+ " son series.")
            print("------------------------------------------------------------------------------------------------------------------------------------\n")

            if size>5:
                primeros3T = controller.primeros3(lista_pais, opcion)
                print("----------------------------------------------Los primeros 3 contenidos son------------------------------------------------------")
                for titulo in lt.iterator(primeros3T):
                    print (titulo)
                    print("--------------------------------------------------------------------------------------------------------------------------------")
                print("\n-------------------------------------------------------------------------------------------------------------------------------")
                ultimos3T = controller.ultimos3(lista_pais, opcion)
                print("\n---------------------------------------------Los ultimos 3 contenidos son------------------------------------------------------")
                for titulo in lt.iterator(ultimos3T):
                    print (titulo)
                    print("--------------------------------------------------------------------------------------------------------------------------------")
            else :
                listar = controller.listar(lista_pais)
                for titulo in lt.iterator(listar):
                    print (titulo)
                    print("--------------------------------------------------------------------------------------------------------------------------------")

    elif int(inputs) == 7:
        opcion = int(inputs)
        director = input("Inserte el nombre del director del cual sea ver contenido \n")
        contenido_por_director, peliculas, programas, listastreaming, listasgenero = controller.contenido_director(director,sorted_listT)
        size = lt.size(contenido_por_director)
        print("\n--------------------------------------------------------------------------------------------------------------------------------")
        print("El numero total de películas y programas dirigidos por " + str(director)+ " es: " +str(size))
        print("--------------------------------------------------------------------------------------------------------------------------------")
        if peliculas != 0 and programas != 0:
            print("De las cuales " +str(peliculas)+ " son peliculas  y " +str(programas)+ " son programas.")
            print("---------------------------------------------------")
        elif peliculas !=0:
            print("De las cuales " +str(peliculas)+ " son peliculas.")
            print("---------------------------------------------------")
        else:
            print("De las cuales " +str(programas)+ " son progrmas.")
            print("---------------------------------------------------")

        for key, value in listastreaming.items():
            print("|"+ str(value) + " | "+str(key)+(" | "))
 

        if len(listasgenero)<6: 
            print("\nLos primeros 3 y ultimos 3 tags estan listados bajo: ")
            print("---------------------")
            for key, value in listasgenero.items():
                print("|"+ str(value) +" | "+str(key)+" | ")

        else:
            print("----------------------------------------------Los primeros 3 tags son------------------------------------------------------")
            i=1
            for key, value in listasgenero.items():
                if i <= 3:
                    print("|"+ str(key) +" | "+str(value)+" | ")
                i+=1

            print("\n----------------------------------------------Los ultimos 3 tags son------------------------------------------------------")            
            i=0
            lenght = len(listasgenero)-3
            for key, value in listasgenero.items():
                i+=1
                if i > lenght:
                    print("|"+ str(key) +" | "+str(value)+" | ")


        if lt.size(contenido_por_director)<=3:
            print("\nLos primeros y ultimos 3 contenidos son: ")
            primeros3T=controller.primeros3(contenido_por_director,opcion)

            for nombre in lt.iterator(primeros3T):
                print(nombre + "\n")
        else:
            print("----------------------------------------------Los primeros 3 contenidos son------------------------------------------------------")
            primeros3T=controller.primeros3(contenido_por_director,opcion)

            for nombre in lt.iterator(primeros3T):
                print(nombre + "\n")

            print("\n----------------------------------------------Los ultimos 3 contenidos son------------------------------------------------------")
            ultimos3T=controller.ultimos3(contenido_por_director,opcion)
            for nombre in lt.iterator(ultimos3T):
                print(nombre + "\n")

    elif int(inputs) == 8:
        top = int(input("Indique el numero de generos que desea ordenar en el TOP \n"))
        listafinaltags, listafinalnumeros, listaMovies, listaTV, listaN, listaH, listaA, listaD = controller.top_generos(top,sorted_listT)
        print("--------------------------------------------------------------------------------------------------------------------------------")
        i=1

        print("El TOP " + str(top)+ " tiene los sigues tags \n")

        while i <= top:
            print(str(lt.getElement(listafinaltags,i))+ " | " + str(lt.getElement(listafinalnumeros,i)))
            print("----------------------\n ")
            i+=1
        i=1    
        while i <= top:
            print(str(i)+") "+str(lt.getElement(listafinaltags,i))+ " | " + str(lt.getElement(listafinalnumeros,i)))
            print("Movies: "+ str(lt.getElement(listaMovies,i))+ " | TV Shows: " + str(lt.getElement(listaTV,i)))
            print("Netflix: " + str(lt.getElement(listaN,i))+ " | Hulu: " + str(lt.getElement(listaH,i))+ " | Amazon:"+ str(lt.getElement(listaA,i)) + " | Disney:"+ str(lt.getElement(listaD,i)))
            print("----------------------\n ")
            i+=1
        


    elif int(inputs) == 9:
        tipo_alg = input("Que tipo de algoritmo de ordenamiento desea usar? (selection, insertion, shell, merge o quick)\n")
        tiempo = controller.ordenamiento(catalogo,tipo_alg)
        delta_time = f"{tiempo:.3f}"
        size=int(lt.size(listaNetflix))+int(lt.size(listaDisney))+int(lt.size(listaHulu))+int(lt.size(listaPrime))
        print("Para el algoritmo " +tipo_alg+ " el tiempo de ordenamiento es " +str(delta_time)+" milisegundos para "+str(size)+" datos")
        print("--------------------------------------------------------------------------------------------------------------------------------")
    
    elif int(inputs) == 10:
        top = int(input("Indique el numero de actores que desea ordenar en el TOP \n"))
        listafinaltags, listafinalnumeros, listaMovies, listaTV, listaN, listaH, listaA, listaD = controller.top_actores(top,sorted_listT)


    else:
            sys.exit(0)
sys.exit(0)
