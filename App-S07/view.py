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

from tabulate import tabulate


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    print("Bienvenido")
    print("0 - Cargar información en el catálogo")
    print("1 - Listar las películas estrenadas en un periodo de tiempo")
    print("2 - Listar programas de televisión agregados en un periodo de tiempo")
    print("3 - Encontrar contenido donde participa un actor")
    print("4 - Encontrar contenido por un género especifico")
    print("5 - Encontrar contenido producido en un país")
    print("6 - Encontrar contenido con un director involucrado")
    print("7 - Listar el TOP (N) de los géneros con más contenido")
    print("8 - Listar el TOP (N) de los actores con más participaciones en contenido")

catalog = None

# Se crea el controlador asociado a la vista
control = newController()


def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    netflix, amazon, disney, hulu, titles, features = controller.loadData(control)
    return netflix, amazon, disney, hulu, titles, features

def printLoadedDatas(data, headers):
    """
    Organiza las plataformas de acuerdo a la cantidad de titulos cargados de mayor a menor
    """
    lista = lt.newList()
    for key, value in data.items():
        lt.addLast(lista, {'platform': key, 'amount': value})
    controller.sortDataAmounts(lista)
    table = []
    for element in lt.iterator(lista):
        platform = element['platform']
        amount = element['amount']
        table.append([platform, amount])
    print(tabulate(table, headers, tablefmt="grid"))

def imprimirReq7(data):
    tabular = []
    headers = ['rank', 'listed_in', 'count', 'type', 'stream_service']
    for title in lt.iterator(data):
        cadaTab = []
        cadaTab.append(title['rank'])
        cadaTab.append(title['listed_in'])
        cadaTab.append(title['count'])
        valorA = []
        for key, value in title['type'].items():
            valorInterno = [key, value]
            valorA.append(valorInterno)
        cadaTab.append(tabulate(valorA, ['count type'], tablefmt="plain"))
        valorB = []
        for key, value in title['stream_service'].items():
            valorInterno = [key, value]
            valorB.append(valorInterno)
        cadaTab.append(tabulate(valorB, ['count stream_service'], tablefmt="plain"))
        tabular.append(cadaTab)
    print(tabulate(tabular, headers, tablefmt="grid"))

def imprimirReq8(data):
    tabular = []
    headers = ['rank', 'actor', 'type', 'stream_service']
    for title in lt.iterator(data):
        cadaTab = []
        cadaTab.append(title['rank'])
        cadaTab.append(title['actor'])
        valorA = []
        for key, value in title['type'].items():
            valorInterno = [key, value]
            valorA.append(valorInterno)
        cadaTab.append(tabulate(valorA, ['count type'], tablefmt="plain"))
        valorB = []
        for key, value in title['stream_service'].items():
            valorInterno = [key, value]
            valorB.append(valorInterno)
        cadaTab.append(tabulate(valorB, ['count stream_service'], tablefmt="plain"))
        tabular.append(cadaTab)
    print(tabulate(tabular, headers, tablefmt="grid"))
    
def printTabulatedData(filteredTitles, headers):
    size = lt.size(filteredTitles)
    table = []
    width = 22
    if len(headers) >= 10:
        width = 15
    if size:
        for filteredTitle in lt.iterator(filteredTitles):
            fields = []
            for header in headers:
                fields.append(filteredTitle[header])
            table.append(fields)
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=width))
    else:
        print('\nNo se encontró contenido con este criterio de busqueda')

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("\n\nCargando información de los archivos ....")
        netflix, amazon, disney, hulu, titles, features = loadData(control)
        print('-'*52)
        print('Total loaded streaming service info:')
        print('Total loaded titles: ' + str(titles))
        print('Total loaded features: ' + str(features))
        print('-'*52)
        headers = ["service_name", "count"]
        printLoadedDatas({'netflix': netflix, 'amazon': amazon, 'disney': disney, 'hulu': hulu}, headers)

    elif int(inputs[0]) == 1:
        initialYear = int(input("Ingrese el año inicial: "))
        finalYear = int(input("Ingrese el año final: "))
        startTime = controller.getTime()
        filtered = controller.filteredMoviesByYears(control, initialYear, finalYear)
        size = lt.size(filtered)
        filtered = controller.firstAndLastThreeTitles(filtered)
        print('\n\n' + '='*15 + 'Req No. 1 Inputs' + '='*15)
        print('Movies released between ' + str(initialYear) + ' and ' + str(finalYear))
        print('\n' + '='*15 + 'Req No. 1 Answer' + '='*15)
        print('There are ' + str(size) + " IPs (Intelectual Properties) in 'Movie' type released between " + str(initialYear) + ' and ' + str(finalYear) + '.')
        print('The first 3 and last 3 IPs in range are:')
        headers = ['type', 'release_year', 'title', 'duration', 'stream_service', 'director', 'cast']
        printTabulatedData(filtered, headers)
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"
        print("Tiempo de ejecución: ", deltaTime)

    elif int(inputs[0]) == 2:
        initialDate = str(input("Ingrese la fecha inicial: "))
        finalDate = str(input("Ingrese la fecha final: "))
        startTime = controller.getTime()
        filtered = controller.filteredTVShowsByDates(control, initialDate, finalDate)
        size = lt.size(filtered)
        filtered = controller.firstAndLastThreeTitles(filtered)
        print('\n\n' + '='*15 + 'Req No. 2 Inputs' + '='*15)
        print("'TV Shows' released between " + str(initialDate) + ' and ' + str(finalDate))
        print('\n' + '='*15 + 'Req No. 2 Answer' + '='*15)
        print('There are ' + str(size) + " IPs (Intelectual Properties) in 'TV Show' type released between " + str(initialDate) + ' and ' + str(finalDate) + '.')
        print('The first 3 and last 3 IPs in range are:')
        headers = ['type', 'date_added', 'title', 'duration', 'release_year', 'stream_service', 'director', 'cast']
        printTabulatedData(filtered, headers)
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"
        print("Tiempo de ejecución: ", deltaTime)

    elif int(inputs[0]) == 3:
        actor = input('Ingrese el actor: ')
        startTime = controller.getTime()
        filtered, movies, TVShows = controller.findContentByActor(control, actor)
        size = lt.size(filtered)
        filtered = controller.firstAndLastThreeTitles(filtered)
        print('\n\n' + '='*15 + 'Req No. 3 Inputs' + '='*15)
        print("Content with " + str(actor) + " in the 'cast'")
        print('\n' + '='*15 + 'Req No. 3 Answer' + '='*15)
        print('='*6 + " '" + str(actor) + " cast participation count " + '='*6)
        filtered = controller.firstAndLastThreeTitles(filtered)
        print('-'*6 + "Participation details" + '-'*6)
        if size < 6: 
            print("There are less than 6 participations of '" + actor + "' on record")
        else:
            print("There are " + str(size) + " participations of " + actor + " on record")
            print('The first 3 and last 3 IPs in range are:')
        print(tabulate([['Movie', movies], ['TV Show', TVShows]], ['Type', 'Count'], tablefmt="grid"))
        headers = ['type', 'title', 'release_year', 'director', 'stream_service', 'duration', 'cast', 'country', 'listed_in', 'description']
        printTabulatedData(filtered, headers)
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"
        print("Tiempo de ejecución: ", deltaTime)

    elif int(inputs[0]) == 4:
        genero = input('Ingrese el género: ')
        startTime = controller.getTime()
        filtered = controller.findContentByGenero(control, genero)
        size = lt.size(filtered)
        filtered = controller.firstAndLastThreeTitles(filtered)
        print('\n\n' + '='*15 + 'Req No. 4 Inputs' + '='*15)
        print("The content is listed_in'" + str(genero) + "'")
        print('\n' + '='*15 + 'Req No. 4 Answer' + '='*15)
        print('There are only ' + str(size) + " IPs (Intelectual Properties) produced with the '" + str(genero) + "' label.")
        print('The first 3 and last 3 IPs in range are:')
        headers = ['title', 'release_year', 'director', 'stream_service', 'type', 'duration', 'cast', 'country', 'rating', 'listed_in', 'description']
        printTabulatedData(filtered, headers)
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"
        print("Tiempo de ejecución: ", deltaTime)

    elif int(inputs[0]) == 5:
        country = input('Ingrese el país: ')
        startTime = controller.getTime()
        filtered, movies, TVShows = controller.findContentByCountry(control, country)
        size = lt.size(filtered)
        print('\n\n' + '='*15 + 'Req No. 5 Inputs' + '='*15)
        print("The content produced in '" + str(country) + "'")
        print('\n' + '='*15 + 'Req No. 5 Answer' + '='*15)
        print('-'*6 + "'" + str(country) + "' content type production count" + '-'*6)
        print(tabulate([['Movie', movies], ['TV Show', TVShows]], ['Type', 'Count'], tablefmt="grid"))
        print('\n' + '-'*6 + ' Content details ' + '-'*6)
        print('There are only ' + str(size) + " IPs (Intelectual Properties) produced in '" + str(country) + "'.")
        filtered = controller.firstAndLastThreeTitles(filtered)
        headers = ['release_year', 'title', 'director', 'stream_service', 'duration', 'type', 'cast', 'country', 'listed_in', 'description']
        printTabulatedData(filtered, headers)
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"
        print("Tiempo de ejecución: ", deltaTime)
    
    elif int(inputs[0]) == 6:
        director = input('Ingrese el director: ')
        startTime = controller.getTime()
        filtered, types, platforms, generos = controller.findContentByDirector(control, director)
        print('\n\n' + '='*15 + 'Req No. 6 Inputs' + '='*15)
        print("Find the content with '" + str(director) + "' as 'director'")
        print('\n' + '='*15 + 'Req No. 6 Answer' + '='*15)
        print('-'*6 + " '" + str(director) + "' Content type count " + '-'*6)
        printLoadedDatas(types, ['type', 'count'])
        print('\n' + '-'*6 + " '" + str(director) + "' Streaming content type count " + '-'*6)
        printLoadedDatas(platforms, ['service_name', 'Count'])
        print('\n' + '-'*6 + " '" + str(director) + "' Listed in count " + '-'*6)
        print("There are only " + str(len(generos)) + " tags in 'listed_in'")
        print('The first 3 and 3 last tags in range are:')
        size = lt.size(filtered)
        generos = controller.firstAndLastThreeTitles(generos)
        printTabulatedData(generos, ['listed_in', 'count'])        
        print('\n' + '-'*6 + " '" + str(director) + "' content details " + '-'*6)
        print('There are only ' + str(size) + " IPs (Intelectual Properties) with '" + str(director) + "' as 'director'")
        print('The first 3 and 3 last tags in range are:')
        headers = ['title', 'release_year', 'director', 'stream_service', 'type', 'duration', 'cast', 'country', 'listed_in', 'description']
        filtered = controller.firstAndLastThreeTitles(filtered)
        printTabulatedData(filtered, headers)
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"
        print("Tiempo de ejecución: ", deltaTime)

    elif int(inputs[0]) == 7:
        N = int(input('Número del Ranking de categorias ("Top N") a consultar: '))
        startTime = controller.getTime()
        filtered, size = controller.topNByCategory(control, N)
        print('\n\n' + '='*15 + 'Req No. 7 Inputs' + '='*15)
        print('The TOP ' + str(N) + " in 'listed_in' are:")
        print('\n' + '='*15 + 'Req No. 7 Answer' + '='*15)
        print("There are '" + str(size) + "' tags participating in TOP '" + str(N) + "' generes for 'listed_in'")
        print('\n' + '-'*6 + " The TOP '" + str(N) + "' Listed in tags are " + '-'*6)
        print('There are only ' + str(N) + ' tags in the TOP ranking')
        printTabulatedData(filtered, ['listed_in', 'count'])
        print('\n' + '-'*6 + " TOP listed in tags details " + '-'*6)
        print('There are only ' + str(N) + ' tags in the TOP ranking')
        imprimirReq7(filtered)
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"
        print("Tiempo de ejecución: ", deltaTime)

    elif int(inputs[0]) == 8:
        N = int(input('Número del Ranking de actores ("Top N") a consultar: '))
        startTime = controller.getTime()
        filtered, size = controller.topNByActor(control, N)
        print('\n\n' + '='*15 + 'Req No. 8 (BONUS) Inputs' + '='*15)
        print('The TOP ' + str(N) + " actors in 'cast")
        print('\n' + '='*15 + 'Req No. 8 (BONUS) Answer ' + '='*15)
        print("There are '" + str(size) + "' actors participating in TOP '" + str(N) + "' actors in 'cast'")
        print('\n' + '-'*6 + " The TOP '" + str(N) + "' actors participations are: " + '-'*6)
        print('There are only ' + str(N) + ' in the TOP ranking')
        printTabulatedData(filtered, ['actor', 'count'])
        print('\n' + '-'*6 + " TOP listed in tags details " + '-'*6)
        print('There are only ' + str(N) + ' tags in the TOP ranking')
        imprimirReq8(filtered)
        print('\n' + '-'*6 + " TOP actors colaborations details " + '-'*6)
        print('There are only ' + str(N) + ' in the TOP ranking')
        printTabulatedData(filtered, ['rank', 'actor', 'colaborations'])
        endTime = controller.getTime()
        deltaTime = str(round(controller.deltaTime(startTime, endTime), 2)) + " ms"

    else:
        sys.exit(0)
    
    #Añadido por Wilmer, para mejor experiencia de usuario
    input('\n\nPulse cualquier tecla para continuar...\n\n')

sys.exit(0)