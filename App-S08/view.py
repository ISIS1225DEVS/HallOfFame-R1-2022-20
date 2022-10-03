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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar peliculas en un intervalo de tiempo")
    print("3- Buscar series en un intervalo de tiempo")
    print("4- Buscar contenido de un actor especifico")
    print("5- Buscar contenido de un género especifico")
    print("6- Buscar contenido producido en un país en especifico")
    print("7- Encontrar un contenido con un director")
    print("8- Listar top de generos con mas contenidos")

catalog = None

def newController(ordenamiento):
    catalog=controller.newCatalog(ordenamiento)
    return catalog

def loadCatalog(catalog):
    catalog= controller.loadContentCatalog(catalog)
    return catalog

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=newController("ARRAY_LIST")
        cargar= loadCatalog(catalog)
        atributos=["show_id", "type", "title", "director", "cast", "country", "date_added", "release_year", "rating", "duration", "listed_in", "stream_service", "description"]
        nodesc=newController("ARRAY_LIST")
        for plataforma in catalog:
            elemento=controller.escogeratributos(catalog[plataforma], atributos)
            nodesc[plataforma]=elemento
        primerosultimos=lt.newList("ARRAY_LIST")
        print(controller.tabla_carga_datos(catalog))
        for plataforma in nodesc:
            elemento=controller.first3last3(nodesc[plataforma])
            lt.addLast(primerosultimos,elemento)
        for catalogo in lt.iterator(primerosultimos):
            print(lt.getElement(catalogo,1)["stream_service"])
            print(controller.creartablas(catalogo))
            

    elif int(inputs[0]) == 2:
        desde=input("digite año inicial: ")
        hasta=input("digite año final: ")
        inicio=controller.getTime()
        print("Buscando las peliculas estrenadas entre " + desde + " y " + hasta)
        atributos=["release_year", "title", "duration", "stream_service", "director", "cast"]
        peliculas=controller.requerimiento1(desde,hasta,catalog)
        peliculas=controller.escogeratributos(peliculas, atributos)
        primerosultimos=controller.first3last3(peliculas)
        print(controller.creartablas(primerosultimos))
        final=controller.getTime()
        print(final-inicio)

    elif int(inputs[0]) == 3:
        desde=input("digite fecha inicial (en formato YYYY-MM-DD): ")
        hasta=input("digite fecha final (en formato YYYY-MM-DD): ")
        inicio=controller.getTime()
        print("Buscando las series estrenadas entre " + desde + " y " + hasta)
        atributos=["title", "date_added", "duration", "release_year", "stream_service", "director", "cast"]
        series=controller.requerimiento2(desde,hasta,catalog)
        series=controller.escogeratributos(series, atributos)
        primerosultimos=controller.first3last3(series)
        print(controller.creartablas(primerosultimos))
        final=controller.getTime()
        print(final-inicio)
        
    elif int(inputs[0])==4:
        actorbuscar=input("digite el actor/actiz a buscar: ")
        inicio=controller.getTime()
        print("Buscando los shows en donde participa "+actorbuscar)
        showsytabla=controller.requerimiento3(actorbuscar,catalog)
        shows=showsytabla[0]
        tabla=showsytabla[1]
        atributos=["title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
        shows=controller.escogeratributos(shows, atributos)
        primerosultimos=controller.first3last3(shows)
        print(controller.creartablas(tabla))
        print(controller.creartablas(primerosultimos))
        final=controller.getTime()
        print(final-inicio)

    elif int(inputs[0])==5:
        generobuscar=input("digite el genero a buscar: ")
        inicio=controller.getTime()
        print("Buscando los shows en donde que tienen el genero "+generobuscar)
        showsytabla=controller.requerimiento4(generobuscar,catalog)
        shows=showsytabla[0]
        tabla=showsytabla[1]
        atributos=["title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
        shows=controller.escogeratributos(shows, atributos)
        primerosultimos=controller.first3last3(shows)
        print(controller.creartablas(tabla))
        print(controller.creartablas(primerosultimos))
        final=controller.getTime()
        print(final-inicio)
    
    elif int(inputs[0])==6:
        paisbuscar=input("digite el pais a buscar: ")
        inicio=controller.getTime()
        print("Buscando los contenidos hechos en "+paisbuscar)
        showsytabla=controller.requerimiento5(paisbuscar,catalog)
        shows=showsytabla[0]
        tabla=showsytabla[1]
        atributos=["title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
        shows=controller.escogeratributos(shows, atributos)
        primerosultimos=controller.first3last3(shows)
        print(controller.creartablas(tabla))
        print(controller.creartablas(primerosultimos))
        final=controller.getTime()
        print(final-inicio)

    elif int(inputs[0]) == 7:
        director=input("digite el director a buscar: ")
        inicio=controller.getTime()
        tablas=controller.requerimiento6(director, catalog)
        atributos=["release_year", "title", "duration","stream_service", "director", "cast", "country", "listed_in", "description"]
        tabla1=tablas[0]
        tabla2=tablas[1]
        tabla3=tablas[2]
        tabla4=tablas[3]
        tabla4=controller.escogeratributos(tabla4, atributos)
        tabla4=controller.first3last3(tabla4)
        print(controller.creartablas(tabla1))
        print(controller.creartablas(tabla2))
        print(controller.creartablas(tabla3))
        print(controller.creartablas(tabla4))
        final=controller.getTime()
        print(final-inicio)
        

    elif int(inputs[0]) == 8:
        num=int(input("digite el tamaño del top de generos: "))
        inicio=controller.getTime()
        tablas=controller.requerimiento7(catalog, num)
        tabla1=tablas[0]
        tabla2=tablas[1]
        print(controller.creartablas(tabla1))
        print(controller.creartablas(tabla2))
        final=controller.getTime()
        print(final-inicio)

        pass

    else:
        sys.exit(0)
sys.exit(0)
