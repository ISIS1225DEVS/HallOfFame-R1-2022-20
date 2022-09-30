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

from datetime import datetime
from marshal import load
from re import A
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from prettytable import PrettyTable
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#Función del lab 4 para validar la entrada del tipo de estructura a usar (no se usa)

def convertirTipo(eleccion):
    eleccion=eleccion.upper()
    resultado = "DEFAULT"
    if eleccion == "A":
        resultado = "ARRAY_LIST"
    elif eleccion == "S":
        resultado = "SINGLE_LINKED"
    return resultado

#Función que imprime el menú principal para el usuario

def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar programas de televisión agregados en un periodo de tiempo")
    print("3- Encontrar contenido donde participa un actor")
    print("4- Encontrar contenido por un género especifico")
    print("5- Encontrar contenido producido en un país")
    print("6- Encontrar contenido con un director involucrado")
    print("7- Listar el TOP (N) de los géneros con más contenido")
    print("8- Listar el TOP (N) de los actores con más participaciones en contenido ")
    print("9- Listar películas agregadas en un periodo de tiempo")
    print("0- Salir")

#Funciones del lab 4 que imprimen los menús de carga personalizada para el usuario (no se usan)

def printMenuMuestra():
    print("1 - 5%")
    print("2 - 10%")
    print("3 - 20%")
    print("4 - 30%")
    print("5 - 50%")
    print("6 - 80%")
    print("7 - 100%")
    print("8 - 0.5%")

def printMenuAlgoritmo():
    print("1 - Selection")
    print("2 - Insertion")
    print("3 - Shell")
    print("4 - Merge")
    print("5 - Quick")

#Función del lab 4 que imprime los tiempos de ejección luego de cada carga personalizada (no se usa)

def printSortData(data):
    sizePercent = "100" if data[1] == "large" else "0.5" if data[1] == "small" else data[1][:-3]
    size = data[2]
    time = data[0]
    print(f'Muestra del {sizePercent}% o {size} elementos tuvo una duracion de: {time:.2f} ms')

#Función del lab 4 para validar la entrada del tamaño de muestra a usar (no se usa)

def convertirMuestra(input):
    try:
        input=int(input)
    except:
        input = 0
    resultado = "DEFAULT"
    if input == 1:
        resultado="5pct"
    elif input == 2:
        resultado="10pct"
    elif input == 3:
        resultado="20pct"
    elif input == 4:
        resultado="30pct"
    elif input == 5:
        resultado="50pct"
    elif input == 6:
        resultado="80pct"
    elif input == 7:
        resultado="large"
    elif input == 8:
        resultado="small"
    return resultado

#Función del lab 4 para validar la entrada del tipo de algorítmo a usar (no se usa)

def convertirAlgoritmo(num):
    try:
        num=int(num)
    except:
        num = 0
    resultado = "DEFAULT"
    if num == 1:
        resultado = "SELECTION"
    elif num == 2:
        resultado = "INSERTION"
    elif num == 3:
        resultado = "SHELL"
    elif num == 4:
        resultado = "MERGE"
    elif num == 5:
        resultado = "QUICK"
    return resultado 

#Función que se encarga de imprimir cada plataforma por separado

def printLoadedData(amazon, disney, hulu, netflix):
    printStreamingData(amazon)
    printStreamingData(disney)
    printStreamingData(hulu)
    printStreamingData(netflix)

#Funciones que se encargan de crear los parámetros de la función de tabulación usando la información filtrada de cada requerimiento

def printStreamingData(service):
    headers = ["Platform", "Title", "Realease Year", "Duration", "Type Duration", "Type"]
    keys = ["platform", "title", "release_year", "duration", "type_duration", "type"]
    data = controller.getElements(service)
    printTabulate(headers, keys, data)

def printTopActores(dataActores):
    headers = ["Rank", "Nombre", "Amazon", "Disney Plus", "Hulu", "Netflix", "Movies", "Tv Shows", "Directores", "Compañeros"]
    keys = ["index", "name", "Amazon_Prime", "Disney_Plus", "Hulu", "Netflix", "movies", "tv_shows", "directores@name", "mates@name"]
    data = controller.getElements(dataActores)
    for x in range(len(data)):
        data[x]["index"] = x + 1
    configTable = { "hrules": 1, "vrules": 1, "max_table": 450, "min_table": 200, "max_col": 450//8}
    printTabulate(headers, keys, data, all=True, configTable=configTable)
    
def printTopCategorias(dataCategorias):
    headers = ["Rank", "Listed In", "Total", "Movies", "Tv Shows", "Amazon", "Disney Plus", "Hulu", "Netflix"]
    keys = ["index", "name", "total", "movies", "tv_shows", "Amazon_Prime", "Disney_Plus", "Hulu", "Netflix"]
    data = controller.getElements(dataCategorias)
    for x in range(len(data)):
        data[x]["index"] = x + 1
    printTabulate(headers, keys, data, all=True)

def printPaisVideos(dataPais):
    print(f'\n{"="*30} {dataPais["name"]} {"="*30}\n')
    print(f'Peliculas: {dataPais["movies"]}')
    print(f'Programas: {dataPais["tv_shows"]}')
    headers = ["Título", "Año de lanzamiento", "Director", "Plataforma", "Duración", "Tipo de duración", "Actores", "País", "Generos", "Descripción"]
    keys = ["title", "release_year", "director", "platform", "duration", "type_duration", "cast", "country", "listed_in", "description"]
    data = controller.getElements(dataPais["videos"])
    configTable = { "hrules": 1, "vrules": 1, "max_table": 170, "min_table": 150 }
    printTabulate(headers, keys, data, configTable)

def printDirectorVideos(dataDirector):
    print(f'\n{"="*30} {dataDirector["name"]} {"="*30}\n')
    headers = ["Tipo", "Cantidad"]
    keys= ["Tipo", "Cantidad"]
    dataTipo= [{"Tipo": "Movies", "Cantidad": dataDirector["movies"]},{"Tipo": "TV_shows", "Cantidad": dataDirector["tv_shows"]}]
    print("Cantidad por tipo")
    printTabulate(headers, keys, dataTipo)

    headers = ["Plataforma", "Cantidad"]
    keys = ["Plataforma", "Cantidad"]
    dataPlataformas= [{"Plataforma": "Netflix", "Cantidad": dataDirector[controller.model.NETFLIX]},
    {"Plataforma": "Amazon", "Cantidad": dataDirector[controller.model.AMAZON_PRIME]},
    {"Plataforma": "Hulu", "Cantidad": dataDirector[controller.model.HULU]},
    {"Plataforma": "Disney", "Cantidad": dataDirector[controller.model.DISNEY_PLUS]}]
    configTable = { "hrules": 1, "vrules": 1, "max_table": 170, "min_table": 150 }
    print("Cantidad por plataforma")
    printTabulate(headers, keys, dataPlataformas, configTable)

    headers = ["Genero", "Cantidad"]
    keys = ["name", "total"]
    dataCategorias = controller.getElements(dataDirector["generos"])
    print("Cantidad por categoria")
    printTabulate(headers, keys, dataCategorias)

    headers = ["Año de lanzamiento", "Titulo", "Duración", "Tipo de duración", "Plataforma", "Director", "Actores",  "País", "Generos", "Descripción"]
    keys = ["release_year", "title", "duration", "type_duration", "platform", "director", "cast", "country", "listed_in", "description"]
    data = controller.getElements(dataDirector["videos"])
    configTable = { "hrules": 1, "vrules": 1, "max_table": 170, "min_table": 150 }
    print("Lista")
    printTabulate(headers, keys, data, configTable)

def printCategoriasVideos(dataCategoria):
    print(f'\n{"="*30} {dataCategoria["name"]} {"="*30}\n')
    print(f'Peliculas: {dataCategoria["movies"]}')
    print(f'Programas: {dataCategoria["tv_shows"]}')
    headers = ["Platform", "Title", "Director", "Release Year", "Actores", "Pais", "Generos", "Descripción"]
    keys = ["platform", "title", "director", "release_year", "cast", "country", "listed_in", "description"]
    data = controller.getElements(dataCategoria["videos"])
    configTable = { "hrules": 1, "vrules": 1, "max_table": 170, "min_table": 150 }
    printTabulate(headers, keys, data, configTable)
    
def printActorsVideos(dataActor):
    print(f'\n{"="*30} {dataActor["name"]} {"="*30}\n')
    print(f'Peliculas: {dataActor["movies"]}')
    print(f'Programas: {dataActor["tv_shows"]}')
    headers = ["Platform", "Title", "Director", "Actores", "Duracion", "Pais", "Generos"]
    keys = ["platform", "title", "director", "cast", "duration", "country", "listed_in"]
    data = controller.getElements(dataActor["videos"])
    configTable = { "hrules": 1, "vrules": 1, "max_table": 170, "min_table": 150 }
    printTabulate(headers, keys, data, configTable)
    
def printProgramas(data):
    print(f'\n{"="*30} {data["periodo"]} {"="*30}\n')
    print(f'TV Shows: {data["tv_shows"]}')
    headers = ["Título", "Año de adición", "Duración", "Tipo de duración", "Año de lanzamiento", "Plataforma", "Director", "Actores"]
    keys = ["title", "date_added", "duration", "type_duration", "release_year", "platform", "director", "cast"]
    data = controller.getElements(data["videos"])
    configTable = { "hrules": 1, "vrules": 1, "max_table": 170, "min_table": 150 }
    printTabulate(headers, keys, data, configTable)
    
def printPeliculas(data):
    print(f'\n{"="*30} {data["periodo"]} {"="*30}\n')
    print(f'Peliculas: {data["movies"]}')
    headers = ["Año de lanzamiento", "Título","Duración", "Tipo de duración",  "Plataforma", "Director", "Actores"]
    keys = ["release_year", "title", "duration", "type_duration", "platform", "director", "cast",]
    data = controller.getElements(data["videos"])
    configTable = { "hrules": 1, "vrules": 1, "max_table": 170, "min_table": 150 }
    printTabulate(headers, keys, data, configTable)

#Función que se encarga de tabular e imprimir la información al usuario en cada requerimiento

def printTabulate(headers=[], keys=[], data=[], configTable={}, all=False):
    row = []
    index = 1
    size = len(data)
    table = PrettyTable(headers)
    table.max_width = configTable.get("max_col", configTable.get("max_table", 170)//len(headers))
    table.min_table_width = configTable.get("min_table", 170)
    table.max_table_width = configTable.get("max_table", 170)
    table.hrules = configTable.get("hrules", 0)
    table.vrules = configTable.get("vrules", 1)
    for d in data:
        if ((index < 4 or index > (size - 3)) or all):
            for key in keys:
                mainKey = key.split("@")[0]
                subkeys = key.split("@")[1:]
                value = d[mainKey]
                if not isinstance(value, str):
                    if isinstance(value, type(datetime)):
                        row.append(value.strftime('%Y-%m-%d'))
                    elif isinstance(value, dict):
                        row.append(",".join(controller.getElements(value, subkeys)))
                    else:
                        row.append(d[key])
                else:
                    row.append(d[key])
            table.add_row(row)
            row = []
        index += 1
    print(table)

#Inicialización de la variable catalog
catalog = {}

"""
Menu principal
"""

while True:

    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = controller.newCatalog(structure="ARRAY_LIST" ,sortAlgorithm="MERGE",sampleSize="large")
        print("\nCargando información de los archivos ....")
        amazon, disney, hulu, netflix = controller.loadData(catalog)
        printLoadedData(amazon, disney, hulu, netflix)

    elif int(inputs[0]) == 2:
        inputInicial = input("Ingrese la fecha inicial del periodo a buscar (Algo de la forma 'September 17, 2013'): ")
        inputFinal = input("Ingrese la fecha final del periodo a buscar (Algo de la forma 'September 17, 2013'): ")
        try:
            inputToDateInicial = datetime.strptime(inputInicial, "%B %d, %Y")
            inputToDateFinal = datetime.strptime(inputFinal, "%B %d, %Y")
            dateModelInicial =  datetime.strptime(datetime.strftime(inputToDateInicial, '%Y-%m-%d'), '%Y-%m-%d')
            dateModelFinal = datetime.strptime(datetime.strftime(inputToDateFinal, '%Y-%m-%d'), '%Y-%m-%d')
            data = controller.filterProgramas(catalog, dateModelInicial, dateModelFinal)
            if data == None:
                print("\nUps! No encontramos programas en ese periodo")
            else:
                printProgramas(data)
        except:
            print("\nUps! Las fechas consultadas no son válidas")
  
    elif int(inputs[0]) == 3:
        actor = input("Ingrese el nombre del actor a buscar: ")
        dataActor = controller.filterByActor(catalog, actor)
        if dataActor == None:
            print("\nUps! el actor consultado no ha sido encontrado")
        else:
            printActorsVideos(dataActor)

    elif int(inputs[0]) == 4:
        genero = input("Ingrese el genero a filtrar: ")
        dataCategoria = controller.filterByCategoria(catalog, genero)
        if dataCategoria == None:
            print("\nUps! la categoria consultada no ha sido encontrada")
        else:
            printCategoriasVideos(dataCategoria)  
            
    elif int(inputs[0]) == 5:
        pais = input("Ingrese elnombre del país a buscar: ").title()
        dataPais = controller.filterByPais(catalog, pais)
        if dataPais == None:
            print("\nUps! el país consultado no ha sido encontrado")
        else:
            printPaisVideos(dataPais)

    elif int(inputs[0]) == 6:
        director = input("Ingrese el nombre del director a buscar: ").title()
        dataDirector = controller.filterByDirector(catalog, director)
        if dataDirector == None:
            print("\nUps! el director consultado no ha sido encontrado")
        else:
            printDirectorVideos(dataDirector)
            
    elif int(inputs[0]) == 7:
        top = int(input("Top N(int) de generos a buscar: "))
        dataCategorias = controller.findTopCategorias(catalog, top)
        printTopCategorias(dataCategorias)
        
    elif int(inputs[0]) == 8:
        top = int(input("Top N(int) de actores a buscar: "))
        dataActores = controller.findTopActores(catalog, top)
        printTopActores(dataActores)
            
    elif int(inputs[0]) == 9:
        aInicial = input("Ingrese el año inicial del periodo a buscar: ")
        aFinal = input("Ingrese el año final del periodo a buscar: ")
        data = controller.filterPeliculas(catalog, aInicial, aFinal)
        if data == None:
            print("\nUps! el periodo consultado no es válido")
        else:
            printPeliculas(data)

    else:
        sys.exit(0)
sys.exit(0)
