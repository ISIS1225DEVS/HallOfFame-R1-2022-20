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
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import tabulate as tblt
import model
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""




#Configurar el entorno de desarrollo

default_limit = 1000
sys.setrecursionlimit(default_limit*10)



#!
#!Creación del Controlador: Crea el controlador de los datos 

def newController(listType, large_file):
    """
    Se crea una nueva instancia del Controlador
    """
    
    control = controller.newController(listType, large_file)
    return control


#! Load_data : Función Encargada de Cargar los datos en el catalogo

def loadData(control, suffix):
    """
    
    Carga los datos del CSV en la estructura de Datos

    Args:
        suffix (_type_): Sufijo de la representación de los datos escogida

    Returns:
        _type_: Tamaños de las listas de las plataformas
    """    
    
    
    netflix, hulu, disney, amazon = controller.loadData(control, suffix)
    
    return netflix, hulu, disney, amazon
        

#? Funciones Print: Se usan principalmente para ahorrar la escritura de prints

def printchooseList():
    print("\nEscoja una representación del ADT")
    print("1- Arreglo")
    print("2- Lista Enlazada")
    
def printchooseCSV():
    print('\nIngrese la representación de los datos que quiere usar: ')
    print(' 1. -small')
    print(' 2. -5pct')
    print(' 3. -10pct')
    print(' 4. -20pct')
    print(' 5. -30pct')
    print(' 6. -50pct')
    print(' 7. -80pct')
    print(' 8. -large')

def printchooseSort():
    print('\nIngrese el algoritmo de ordenamiento que desea usar: ')
    print(' 1. Insertion')
    print(' 2. Selection')
    print(' 3. Shell')
    print(' 4. Quick')
    print(' 5. Merge')    
    
def printHeader(rqn, msg_rq, msg_answer):
    """
    Imprime en consola los encabezados de cada requerimiento

    Args:
        rqn (_type_):   Numero del requerimiento 
        msg_rq (_type_): Mensaje del requerimiento (Inputs)
        msg_answer (_type_): Mensaje de Respuesta
    """    
    print("\n============= Req No. " + str(rqn) + " Inputs =============")
    print(msg_rq)
    print("\n============= Req No. " + str(rqn) + " Answer =============" )
    print(msg_answer)
    print("------------------------------------------------------------------------")
    
#? Funciones Choose: Se usan principalmente para que el usuario escoja un tipo de representacion

def fileChoose():
    """
    
    Da opciones al usuario para que escoja la representación de los datos de su preferencia

    Returns:
        
        El sufijo de la representación de los datos escogida
    """    
    fileChoose = False
    while fileChoose == False:
    
        suffixFileChoose = input('Opción seleccionada: ')
        if int(suffixFileChoose[0]) == 1:
            suffix = '-small'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 2:
            suffix = '-5pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 3:
            suffix = '-10pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 4:
            suffix = '-20pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 5:
            suffix = '-30pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 6:
            suffix = '-50pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 7:
            suffix = '-80pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 8:
            suffix = '-large'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True    
            
    return suffix

def listChoose():
    listChoose = False
    while listChoose == False:
        listTypeChoose = input('Opción seleccionada: ')
        if int(listTypeChoose[0]) == 1:
            listType = 'ARRAY_LIST'
            print('\nSeleciono ARRAY_LIST')
            listChoose = True
        elif int(listTypeChoose[0]) == 2:
            listType = 'SINGLE_LINKED'
            print('\nSeleciono LINKED_LIST')
            listChoose = True
        else:
            input('\nSeleccion Erronea! Oprima ENTER para continuar...')
    
    return listType

def sortChoose():
    sortChoose = False
    while sortChoose == False:
        sortTypeChoose = input("Opción Seleccionada: ")
        if int(sortTypeChoose[0]) == 1:
            sortType = "insertion"
            print("\nSelecciono Insertion Sort")
            sortChoose = True
        elif int(sortTypeChoose[0]) == 2:
            sortType = "selection"
            print("\nSelecciono Selection Sort")
            sortChoose = True
        elif int(sortTypeChoose[0]) == 3:
            sortType = "shell"
            print("\nSelecciono Shell Sort")
            sortChoose = True
        elif int(sortTypeChoose[0]) == 4:
            sortType = "quick"
            print("\nSelecciono Quick Sort")
            sortChoose = True
        elif int(sortTypeChoose[0]) == 5:
            sortType = "merge"
            print("\nSelecciono Merge Sort")
            sortChoose = True
    return sortType
#Opciones

def printMenu():
    print("\nMenu Reto 1")
    print("1- Cargar información en el catálogo")
    print("2- Peliculas Estrenadas en un periodo de Tiempo")
    print('3- Obtener TV shows en un periodo de Tiempo')
    print("4- Encontrar contenido donde participa un actor")
    print("5- Buscar Contenido por País")
    print("6- Encontrar contenido por un género especifico")
    print('7- Encontrar Contenido de un Director')
    print("8- Listar el TOP (N) de los géneros con más contenido")
    print("9- Listar el TOP (N) de los actores con más participaciones en contenido")
    print("10- Pruebas de Rendimiento - Algoritmos de Ordenamiento")

catalog = None



"""
Menu principal
"""
print("========== Reto 1 - Contenido en Plataformas Digitales ==========")
print("\nBienvenido :)")
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        
        printchooseList()
        listType = listChoose()
        printchooseCSV()
        suffix = fileChoose()
        print("\nCargando Información...")
        control = newController(listType, suffix)
        start = controller.getTime()
        netflix, hulu, disney, amazon = loadData(control, suffix)
        end = controller.getTime()
        charge_time = controller.deltaTime(start, end)
        if listType == "ARRAY_LIST":
            list, time = controller.sort_titles_by_release(control,'quick', 'titles')
            init_message = "Datos Cargados con Archivo: " + suffix[1:6] + "\nRepresentacion de la lista: " + listType
            end_message = "Titulos Cargados: " + str(lt.size(list)) + "\nCategorias Cargadas: En construcción\nTiempo de Carga:  " + str(charge_time) + " milisegundos"  
            printHeader("Carga de Datos", init_message, end_message)
            data, platforms =  controller.visual_charge_data(list, control)
            print("\n")
            print(platforms)
            print("\n")
            print("Los primeros 3 y ultimos 3 titulos cargados en el rango de datos son: \nTitulos ordenados por Titulo en un tiempo de: " + str(time) +  " milisegundos")
            print(data)
            netflix, time = controller.sort_titles_by_release(control,'quick', 'netflix')
            amazon, time = controller.sort_titles_by_release(control,'quick', 'amazon_prime')
            disney, time = controller.sort_titles_by_release(control,'quick', 'disney_plus')
            hulu, time = controller.sort_titles_by_release(control,'quick', 'hulu')
            data_netflix, platforms = controller.visual_charge_data(netflix, control)
            data_amazon, platforms = controller.visual_charge_data(amazon, control)
            data_disney, platforms = controller.visual_charge_data(disney, control)
            data_hulu, platforms = controller.visual_charge_data(hulu, control)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Netflix')
            print(data_netflix)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Amazon Prime')
            print(data_amazon)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Disney +')
            print(data_disney)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Hulu')
            print(data_hulu)
            
            
            
        
        else:
            list = control["model"]["titles"]
            init_message = "Datos Cargados con Archivo: " + suffix[1:6] + "\nRepresentacion de la lista: " + listType
            end_message = "Titulos Cargados: " + str(lt.size(list)) + "\nCategorias Cargadas: En construcción" 
        
            printHeader("Carga de Datos", init_message, end_message)
            
            data, platforms =  controller.visual_charge_data(list, control)
            print("\n")
            print(platforms)
            print("\n")
            print("Los primeros 3 y ultimos 3 titulos cargados en el rango de datos son: \nTitulos no Ordenados")
            print(data) 
            data_netflix, platforms = controller.visual_charge_data(control['model']['netflix'], control)
            data_amazon, platforms = controller.visual_charge_data(control['model']['amazon_prime'], control)
            data_disney, platforms = controller.visual_charge_data(control['model']['disney_plus'], control)
            data_hulu, platforms = controller.visual_charge_data(control['model']['hulu'], control)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Netflix')
            print(data_netflix)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Amazon Prime')
            print(data_amazon)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Disney +')
            print(data_disney)
            print('\n Los primeros 3 y ultimos 3 shows cargados en la plataforma de Hulu')
            print(data_hulu)  
        
        
    elif int(inputs[0]) == 2:
        init_year = int(input("Digite el año de inicio: "))
        end_year = int(input("Digite el año final: "))
        start = controller.getTime()
        list = controller.getMoviesbyYear(control, init_year, end_year)
        end = controller.getTime()
        charge_time = str(round(controller.deltaTime(start, end), 2)) + " ms"
        msg1 = "Peliculas Lanzadas entre " + str(init_year) + ' y ' + str(end_year)
        msg2 = "Hay " + str(lt.size(list)) + " IPs (intelectual properties) en Peliculas lanzadas entre " +  str(init_year) + " y " +  str(end_year) + "\nTiempo de ejecución: " + charge_time
        
        printHeader("1", msg1, msg2)
        
        table = controller.visualRq1y2(list)
        
        print(table)
    
    elif int(inputs[0]) == 3:
        init_year = input('Ingrese el año inicial de busqueda: ')
        init_month = input('Ingrese el mes inicial de busqueda: ')
        init_day = input('Ingrese el dia inicial de busqueda: ')
        final_year = input('Ingrese el año final de busqueda: ')
        final_month = input('Ingrese el mes final de busqueda: ')
        final_day = input('Ingrese el dia final de busqueda: ')
        init_date = '{0} {1}, {2}'.format(init_month, init_day, init_year)
        final_date = '{0} {1}, {2}'.format(final_month, final_day, final_year)
        
        list = controller.getTvShowsbyDate(control, init_date, final_date)
        
        msg1 = 'TV Shows released between {0} and {1}'.format(init_date, final_date)
        msg2 = 'There are {0} TV Shows between {1} and {2}'.format(str(lt.size(list)), init_date, final_date)
        
        printHeader(2, msg1, msg2)
        
        table = controller.visualRq1y2(list)
        print(table)  
    
    
    elif int(inputs[0]) == 4:
        actor_name = input("Ingrese el nombre del actor a buscar: ")
        
        actor_data, actor_movies = controller.get_content_by_actor(control, actor_name)
        if actor_movies != False:
            msg1 = 'Contenido con ' + actor_name + ' en el Cast'
            msg2 = '------ ' + actor_name + ' cast participation count ------'
            printHeader(3, msg1, msg2)
            print(controller.visualCountTable(['type', 'count'], ['Movies', 'TV Shows'], [actor_data['Movie'], actor_data['TV Show']]))
            print('\n ------ Participation Details ------')
            if lt.size(actor_movies) > 6:
                print(controller.visualreq_6fal(actor_movies))
            else:
                print(controller.visualreq3st(actor_movies))
        else:
            print(actor_data)
            
    elif int(inputs[0]) == 5:
        country_name = input("Ingrese el país a buscar: ")
        print('\nBuscando contenido por país ' + country_name + '...')
        country_data = controller.get_titles_by_country(control, country_name)
        msg1 = 'El contenido producido en ' + country_name
        msg2 = country_name + ' content type production count'
        printHeader(4, msg1, msg2)
        print(controller.visualCountTable(['type', 'count'], ['Movies', 'TV Shows'], [country_data[1], country_data[2]]))
        print("\n------ Detalles de Contenido ------")
        print('Hay ' + str(country_data[1] + country_data[2]) + ' IPs (Intelectual Properties) producidas en ' + country_name)
        if lt.size(country_data[0]) < 6:
            print(controller.visualreq5st(country_data[0]))
        else:
            print(controller.visualreq_5fal(country_data[0]))

    elif int(inputs[0]) == 6:
        genrename = input("Ingrese el género a buscar: ")
        print('\nBuscando contenido por género ' + genrename + '...')
        start = controller.getTime()
        genredatalist, movie_count, show_count = controller.get_titles_by_genre(control, genrename)
        end = controller.getTime()
        charge_time = str(round(controller.deltaTime(start, end), 2)) + " ms"
        init_message = "Contenido listado como " + genrename
        end_message = "Hay " + str(movie_count + show_count) + " títulos con la etiqueta " + "\"" + genrename + "\""
        printHeader(4, init_message, end_message )
        print("\nHay " + str(movie_count) + " películas etiquetadas como " + "\"" + genrename + "\"")
        print("\nHay " + str(show_count) + " TV shows etiquetados como " + "\"" + genrename + "\"")
        print("\nLos primeros 3 y últimos 3 titulos cargados son:" + "\nTiempo de ejecución: " + charge_time)
        print(controller.visual_charge_data_without_id(genredatalist))

    elif int(inputs[0]) == 7:
        director_name = input("Ingrese el director a buscar: ")
        print('\nBuscando contenido por director ' + director_name + '...')
        director_data = controller.get_titles_by_director(control, director_name)
        #CAMBIAR FORMA DE IMPRIMIR
        msg1 = 'El contenido producido por ' + director_name
        msg2 = director_name + ' content type production count'
        print("\n------ '"+director_name+"' Content type count ------")
        print(controller.visualCountTable(['type', 'count'], ['Movies', 'TV Shows'], [director_data[1], director_data[2]]))
        print("\n------ '"+director_name+"' streaming content count ------")
        print(controller.visual_req_6(director_data[3]))
        #decidir si mostrar 6 o menos
        print("\n------ '"+director_name+"' 'listed in' count ------")
        if lt.size(director_data[4]) < 6:
            print(controller.visualreq6_0st(director_data[4]))
        else:
            print(controller.visualreq_6_0fal(director_data[4]))
        print("\n------ Detalles de Contenido ------")
        print('Hay ' + str(director_data[1] + director_data[2]) + ' IPs (Intelectual Properties) producidas en ' + director_name)
        if lt.size(director_data[0]) < 6:
            print(controller.visualreq6st(director_data[0]))
        else:
            print(controller.visualreq_6fal(director_data[0]))

    elif int(inputs[0]) == 8:
        topSize = int(input("Ingrese el número N de géneros a identificar: "))
        print('\nListando TOP ' + str(topSize) + ' géneros con más contenido...')
        start = controller.getTime()
        topGenres = controller.get_top_genres(control, topSize)
        end = controller.getTime()
        charge_time = str(round(controller.deltaTime(start, end), 2)) + " ms"
        msg1 = 'El TOP {0} de géneros en \'listed_in\' son:'.format(topSize)
        msg2 = 'Hay \'76\' tags participando por el top {0} de géneros en \'listed_in\''.format(topSize)
        printHeader(7, msg1, msg2 )
        print("\nHay {0} tags en el TOP ranking".format(topSize))
        print(controller.visualReq7Extra(topGenres))
        print(controller.visualReq7(topGenres))
        print("\nTiempo de ejecución: " + charge_time)

    elif int(inputs[0]) == 9:
        topSize = int(input("Ingrese el número N de actores a identificar: "))
        topActors, count_actors = controller.get_top_actors(control, topSize)
        table1, table2, table3, table4 = controller.visualR8(topActors)
        msg1 = 'Ranking the TOP ' + str(topSize) + ' actors in cast'
        msg2 = 'There are ' + str(count_actors) + ' actors participating for the TOP ' + str(topSize) + ' actors in cast'
        printHeader('8 (BONUS)', msg1, msg2)
        print('\n------The top ' + str(topSize) + ' actors participations are: ------\n')
        print(table1)
        print('\n------TOP Actors participation details -------\n')
        print(table2)
        print('\n------TOP Actors Colaborations Details -------\n')
        print(table3)
        print('\n------TOP Actors Directos Details ------\n')
        print(table4)
        
        

    elif int(inputs) == 10:
        print("Escoja el tipo de contenido que quiere ordenar: ")
        print("1- Películas")
        print("2- TV Shows")
        print("3- Todo")
        choose = int(input("Digite su opción: "))
        init = False
        
        while init == False:
            if choose == 1:
                type = 'Movie'
                type_msg = "Peliculas"
                init = True
                print("Opción Escogida: Peliculas")
            elif choose == 2:  
                type = "TV Show"
                type_msg = "TV Shows"
                init = True
                print("Opción Escogida: TV Shows")
            elif choose == 3:  
                type = "titles"
                type_msg = "Producciones"
                init = True
                print("Opción Escogida: Todo")
            else:
                print("Opcion no valida :(")
                choose = int(input("Digite de nuevo su opción: "))
                
        printchooseSort()
        sort = sortChoose()
        list, time = controller.sort_titles_by_release(control, sort, type)
        message1 = "Representación de los Datos: " + suffix[1:6] + "\nRepresentación de la lista: " + listType + "\nAlgoritmo Escogido " + sort.title() + " Sort"
        message2 = "Cantidad de datos ordenados: " + str(lt.size(list))
        
        printHeader("Laboratorio 4 y 5", message1, message2)
        
        table = controller.visualSort(list)
        
        print("\nTiempo de Procesamiento: " + str(round(time,3)) +" milisegundos"+ "\nLas primeras 3 y ultimas " + type_msg +  " en la lista ordenada son:")
        print(table)
        
    else:
        sys.exit(0)
sys.exit(0)

#%%
    
#modificaciones tiempos de ejecución – Laboratorio 4


# %%
