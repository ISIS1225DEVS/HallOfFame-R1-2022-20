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
from prettytable import PrettyTable,ALL

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController(ListType = "SINGLE_LINKED"):
    """
        Se crea una instancia del controlador
    """
    control = controller.newController(ListType)
    return control
def selector():
    ints = input("Ingrese el tipo de lista:\nLINKED_LIST:0\nARRAY_LIST:1\n")
    if ints == "0":
        control = newController()
        ints = "SINGLE_LINKED"
    elif ints == "1":
        control = newController("ARRAY_LIST")
        ints = "ARRAY_LIST"
    else:
        control = None
    size = input("Ingrese el tamaño de la muestra:(-5pct,-10pct,-20pct,-30pct,-50pct,-80pct,-small,-large)\n")
    if size[0] != "-":
        size = None
    algorithm = input("Ingrese el algoritmo deseado:\nSelection:0\nInsertion:1\nShell:2\nMerge:3\nQuick:4\n")
    return control,size,int(algorithm),ints
def sortbydate(control,algorithm,ListType):
    sorted_catalog,deltatime = controller.sortbydate(control,algorithm,ListType)
    print("Tiempo de ejecución:",str(deltatime))
def loadData(control,size):
    Amazon,Disney,Hulu,Netflix = controller.loadData(control,size)

    return Amazon,Disney,Hulu,Netflix

def PrintStreamingData(Data):
    index = ("Amazon","Disney+","Hulu","Neflix")
    i = 0
    Amazon,Disney,Hulu,Netflix= Data
    size_Amazon, amazon_list = Amazon
    size_Disney, disney_list = Disney
    size_Hulu, hulu_list = Hulu
    size_Netflix, netflix_list = Netflix  
    table1 = PrettyTable()
    table1.hrules = ALL
    table1.field_names = ["service_name","count"]
    table1.add_row(["Amazon",size_Amazon])
    table1.add_row(["Disney",size_Disney])
    table1.add_row(["Hulu",size_Hulu])
    table1.add_row(["Netflix",size_Netflix])
    print(table1)
    table = PrettyTable()
    for stream in (amazon_list,disney_list,hulu_list,netflix_list):
        print("Primeros y últimos titulos de",index[i]+":")
        i+=1
        table.field_names = ["type","release_year","title",
        "director","country","date_added","rating","duration","listed_in","description"]
        table._max_width = {"title":8,"description":10,"listed_in":6,"director":10}
        table.hrules = ALL
        for title1 in lt.iterator(stream):
            table.add_row([title1["type"],title1["release_year"],title1["title"],title1["director"]
            ,title1["country"],title1["date_added"],title1["rating"],title1["duration"],title1["listed_in"],title1["description"][0:50]])
        print(table)
        table.clear()

def printReq1(control,first_year,last_year):
    titles_list = controller.TitlesByYear(control,first_year,last_year)
    print("Hay "+ str(lt.size(titles_list)),"películas entre los años",first_year,"y",last_year,".")
    tabla = PrettyTable()
    tabla.hrules = ALL
    tabla._max_width = {"cast":12,"title":15}
    tabla.field_names = ["type","release_year","title","duration","stream_service","director","cast"]
    if lt.size(titles_list) >= 6:
        print("Primeras y últimas 3 películas:")
        first = lt.subList(titles_list,1,3)
        last = lt.subList(titles_list,lt.size(titles_list)-2,3)
        for i in lt.iterator(first):
            tabla.add_row([i["type"],i["release_year"],i["title"],i["duration"],i["streaming_service"],i["director"],i["cast"]])
        for i in lt.iterator(last):
            tabla.add_row([i["type"],i["release_year"],i["title"],i["duration"],i["streaming_service"],i["director"],i["cast"]])
    else:
        for i in lt.iterator(titles_list):
            tabla.add_row([i["type"],i["release_year"],i["title"],i["duration"],i["streaming_service"],i["director"],i["cast"]])
    print(tabla)
def printReq2(control,date1,date2):
    size,list1 = controller.TitleByTime(control.copy(),date1,date2)
    list = list1.copy()
    print("Hay "+ str(size)+" 'TV SHOW' entre "+date1 + " y " + date2+".")
    print("Los Primeros y Últimos 3 programas son:")
    #for i in lt.iterator(list):
     #   for key in i:
      #      if i[key] == "":
       #         i[key] = "Unknown"
    tabla = PrettyTable()
    tabla.field_names = ["type", "date_Added", "title", "duration", "release_year", "stream_service", "director", "cast"]
    tabla._max_width = {"cast":25}
    tabla.hrules = ALL
    tabla.horizontal_char = "="
    if size >= 6:
        first3 = lt.subList(list, 1, 3)
        last3 = lt.subList(list, lt.size(list)-2, 3)
        for title in lt.iterator(first3):
            tabla.add_row([title["type"],title["date_added"],title["title"],title["duration"],title["date_added"],
            title["streaming_service"],title["director"],title["cast"]])
        for title in lt.iterator(last3):
            tabla.add_row([title["type"],title["date_added"],title["title"],title["duration"],title["date_added"],
            title["streaming_service"],title["director"],title["cast"]])
    else:
        for title in lt.iterator(list):
            tabla.add_row([title["type"],title["date_added"],title["title"],title["duration"],title["date_added"],
            title["streaming_service"],title["director"],title["cast"]])
    print(tabla)
def printReq3(control,actor):
    titles, TV_count, Movie_count = controller.TitlesByActor(control,actor)
    tabla0 = PrettyTable()
    tabla0.field_names = ["type","count"]
    tabla0.add_row(["Movie",Movie_count])
    tabla0.add_row(["TV SHOW",TV_count])
    print(tabla0)
    tabla1 = PrettyTable()
    tabla1.field_names = ["type", "title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
    tabla1._max_width = {"cast":30,"description":10,"listed_in":15}
    tabla1.hrules = ALL
    if lt.size(titles) >= 6:
        first3 = lt.subList(titles, 1, 3)
        last3 = lt.subList(titles, lt.size(titles)-2, 3)

        for title in lt.iterator(first3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])

        for title in lt.iterator(last3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    else:
        for title in lt.iterator(titles):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    print(tabla1)

def printreq4(control,generos):
    titles, TV_count, Movie_count = controller.TitlesByGenres(control,generos)
    tabla0 = PrettyTable()
    tabla0.field_names = ["type","count"]
    tabla0.add_row(["Movie",Movie_count])
    tabla0.add_row(["TV SHOW",TV_count])
    print(tabla0)
    tabla1 = PrettyTable()
    tabla1.field_names = ["type", "title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
    tabla1._max_width = {"cast":30,"description":10,"listed_in":15}
    tabla1.hrules = ALL
    if lt.size(titles) >= 6:
        first3 = lt.subList(titles, 1, 3)
        last3 = lt.subList(titles, lt.size(titles)-2, 3)

        for title in lt.iterator(first3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])

        for title in lt.iterator(last3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    else:
        for title in lt.iterator(titles):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    print(tabla1)

def printreq5(control,country):
    movies,TV_Shows,country_catalog = controller.TitlesByCountry(control,country)
    tabla0 = PrettyTable()
    tabla0.field_names = ["type","count"]
    tabla0.add_row(["Movie",movies])
    tabla0.add_row(["TV SHOW",TV_Shows])
    tabla1 = PrettyTable()
    tabla1.field_names = ["title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
    tabla1._max_width = {"title":10,"release_year":4,"stream_service":5,"cast":12,"country":61,"description":10,"listed_in":15}
    tabla1.hrules = ALL
    
    if lt.size(country_catalog) >= 6:
        first_three = lt.subList(country_catalog,1,3)
        last_three = lt.subList(country_catalog,(lt.size(country_catalog)-2),3)

        for title in lt.iterator(first_three):
                tabla1.add_row([title["title"],title["release_year"],title["director"],title["streaming_platform"],
                    title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
        for title in lt.iterator(last_three):
                tabla1.add_row([title["title"],title["release_year"],title["director"],title["streaming_platform"],
                    title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    else:
        for title in lt.iterator(country_catalog):
                tabla1.add_row([title["title"],title["release_year"],title["director"],title["streaming_platform"],
                    title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
  
    tabla0.hrules = ALL
    tabla1.hrules = ALL
    print(tabla0)
    print(tabla1)


def printreq6(control,director):
    directorTitles,type_count,streaming_count,listed_in_count = controller.TitlesByDirector(control,director)
    tabla1 = PrettyTable()
    tabla1.field_names = ["type","count"]
    for i in type_count:
        tabla1.add_row([i,type_count[i]])
    tabla2 = PrettyTable()
    tabla2.field_names = ["service_name","Movie","TV Show"]
    for i in streaming_count:
        tabla2.add_row([i,streaming_count[i]["Movie"],streaming_count[i]["TV Show"]])
    tabla3 = PrettyTable()
    tabla3.field_names = ["listed_in","count"]
    if len(listed_in_count) <= 6:
        for i in listed_in_count:
            tabla3.add_row([i,listed_in_count[i]])
    else:
        i = 1
        for key in listed_in_count:
            if i <= 3 or (i >= len(listed_in_count)-2 and i <= len(listed_in_count)):
                tabla3.add_row([key,listed_in_count[key]])
            i += 1
    tabla4 = PrettyTable()
    tabla4.field_names = ["title","release_year","director","stream_name","type","duration","cast", "country","rating","listed_in","description"]
    tabla4._max_width = {"title":12,"cast":20,"description":13,"listed_in":15,"country":12}
    if lt.size(directorTitles) <= 6:
        for i in lt.iterator(directorTitles):
            tabla4.add_row([i["title"],i["release_year"],i["director"],i["streaming_platform"],i["type"],
            i["duration"],i["cast"],i["country"],i["rating"],i["listed_in"],i["description"][0:100]+"(...)"])
    else:
        first = lt.subList(directorTitles,1,3)
        last = lt.subList(directorTitles,lt.size(directorTitles)-2,3)
        for i in lt.iterator(first):
            tabla4.add_row([i["title"],i["release_year"],i["director"],i["streaming_platform"],i["type"],
            i["duration"],i["cast"],i["country"],i["rating"],i["listed_in"],i["description"][0:100]+"(...)"])
        for i in lt.iterator(last):
            tabla4.add_row([i["title"],i["release_year"],i["director"],i["streaming_platform"],i["type"],
            i["duration"],i["cast"],i["country"],i["rating"],i["listed_in"],i["description"][0:100]+"(...)"])
    tabla1.hrules = ALL
    tabla2.hrules = ALL
    tabla3.hrules = ALL
    tabla4.hrules = ALL
    print(tabla1)
    print(tabla2)
    print(tabla3)
    print(tabla4)
def printreq7(control, TopN):
    top_num,size = controller.GenresTop(control, TopN)
    print('Hay', str(size), 'generos.')
    tabla1 = PrettyTable()
    tabla1.field_names = ['listed_in', 'count']
    tabla2 = PrettyTable()
    tabla2.field_names = ['rank','listed_in', 'count', 'type', 'stream_service']
    tabla1.hrules = ALL
    tabla2.hrules = ALL
    rank = 1
    for i in lt.iterator(top_num):
        genre,type_counter,streaming_counter,genreSize = i
        tabla1.add_row([genre,genreSize])
        tabla2.add_row([rank,genre,genreSize,type_counter,streaming_counter])
        rank += 1
    print(tabla1)
    print(tabla2)

def printreq8(control,N):
    toplist,actorsize = controller.ActorsTop(control,N)
    print("Hay " + str(actorsize)+" actores.")
    print("Top",N,"actores con más participaciones:")
    tabla1 = PrettyTable()
    tabla1.field_names = ["actor","count","top_listed_in"]
    tabla2 = PrettyTable()
    tabla2.field_names = ["actor","content_type"]
    tabla2._max_width = {"content_type":30}
    tabla3 = PrettyTable()
    tabla3.field_names = ["actor","colaborations"]
    tabla3._max_width = {"colaborations":120}
    tabla1.hrules = ALL
    tabla2.hrules = ALL
    tabla3.hrules = ALL
    str_actores = ""
    for i in lt.iterator(toplist):
        name,colaborations,stream_show_tvCount,max_genre,size = i
        tabla1.add_row([name,size,max_genre[0]])
        tabla2.add_row([name,stream_show_tvCount])
        for actores in range (1, lt.size(colaborations)+1):
            x = lt.getElement(colaborations, actores)
            if x.strip() != "":
                if actores == lt.size(colaborations):
                    str_actores += x + "."
                else:
                    str_actores += x + ","
        tabla3.add_row([name,str_actores])
        str_actores = ""
    print(tabla1)
    print(tabla2)
    print(tabla3) 
def printTimes(control):
    list = controller.ReqsTimeCounts(control)
    a = 1
    for i in lt.iterator(list):
        print("Tiempo de requerimiento",str(a)+":",str(i))
        a += 1
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista de las películas estrenadas en un periodo de tiempo")
    print("3- Lista de programas de televisión agregados en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un género especifico")
    print("6- Encontrar contenido producido por país")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el top de géneros con más contenido")
    print("9-  Listar el top de los actores con más participaciones en contenido")
    print("10- Definir lista,tamaño y algoritmo")
    print("11- Ordenar Listas por año de lanzamiento.")
    print("12-Mostrar Tiempos de Ejecución")
    print("0- Salir")

control = None
size = "-20pct"
algorithm = 0
ListType = "SINGLE_LINKED"
"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        if control == None:
            control = newController()
        print("Cargando información de los archivos ....")
        Data = loadData(control,size)
        PrintStreamingData(Data)
    elif int(inputs) == 2:
        f = input("Ingrese el primer año: ")
        l = input("Ingrese el último año: ")
        printReq1(control,f,l)
    elif int(inputs) == 3:
       date1 = input("Ingrese la primera fecha: ")
       date2 = input("ingrese la segunda fecha: ")
       printReq2(control,date1,date2)
    elif int(inputs) == 4:
        actor = input("Ingrese el nombre del actor/actriz: ")
        printReq3(control,actor)
    elif int(inputs) == 5:
        generos = input("Ingrese el genero: ")
        printreq4(control,generos)
    elif int(inputs) == 6:
        pais = input("Ingrese el nombre del pais: ")
        printreq5(control,pais)
    elif int(inputs) == 7:
        director = input("Ingrese el nombre del director: ")
        printreq6(control,director)
    elif int(inputs) == 8:
        N = input("Ingrese el número N para el top: ")
        printreq7(control,N)
    elif int(inputs) == 9:
        N = input("Ingrese el número N para el top: ")
        printreq8(control,N)
    elif int(inputs) == 10:
        control,size,algorithm,ListType = selector()
    elif int(inputs) == 11:
        sortbydate(control,algorithm,ListType)
    elif int(inputs) == 12:
        printTimes(control)
    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        sys.exit(0)
sys.exit(0)
