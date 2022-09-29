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
import time
import controller
from DISClib.ADT import list as lt
assert cf
from tabulate import tabulate

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def newController(inputList):
    """
    Se crea una instancia del controlador
    """
    control = controller.newController(inputList)
    return control

def printMenu():
    print("\n\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar películas estrenadas en un periodo de tiempo")
    print("3- Listar programas de televisión agregados en un período de tiempo")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un género específico")
    print("6- Encontrar contenido producido en un país")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el top n de los género con más contenido")
    print("9- Listar el top n de los actores con más participaciones en contenido")
    print("10- Ordenar contenido por release_year")
    print("0- Salir")
    
def loadData(control,filename, platform):
    """
    Solicita al controlador que cargue los datos en el modelo creado
    """
    cant = controller.loadData(control,filename,platform)
    return cant

# ------- Funciones de impresion de resultados --------

def printMovies(movies,amazon, disney, hulu, netflix, cant):
    size = lt.size(movies)
    tabla=[]
    tablaPlataformas = []
    
    if size:
        print("Total de titulos cargados: " + str(cant))
        tablaPlataformas.append(["Amazon Prime", amazon])
        tablaPlataformas.append(["Disney Plus", disney])
        tablaPlataformas.append(["Hulu", hulu])
        tablaPlataformas.append(["Netflix", netflix])
        print(tabulate(tablaPlataformas, headers=["Plataforma", "Contenido"], tablefmt="grid")) 
        print("\n")
        
        print("Las 3 primeras y 3 ultimas peliculas ordenadas son: \n", )
        i = 1
        tabla=[]
        while i <= 3:
            movie = lt.getElement(movies, i)
            i += 1
            tabla.append([movie['release_year'], movie['title'],movie['type'], movie['duration'],movie['platform'], movie['director'], movie['listed_in'] ])
        
        j = size + 1 - 3
        while j <= size:
            movie = lt.getElement(movies, j)
            j += 1
            tabla.append([movie['release_year'], movie['title'], movie['type'], movie['duration'],movie['platform'], movie['director'], movie['listed_in'] ])
        
        print(tabulate(tabla, headers=["Release Year", "Title", "Type" "Duration","Platform", "Director", "Listed In"], tablefmt="grid", maxcolwidths=[8,20,10,10,20,10,15]))
    else:
        print('No se encontraron peliculas')
        
        
def printSortResults(sort_movies, sample=3):
    size = lt.size(sort_movies)
    if size <= sample*2:
        print("Las", size, "peliculas ordenadas son:")
        for movie in lt.iterator(sort_movies):
            print('Titulo: ' + movie['title'] + ' Release Year: ' +
            movie['release_year'] + ' Rating: ' + movie['rating'] + ' Duration: ' + movie['duration'])
    else:
        print("Las", sample, "primeras peliculas ordenadas son:")
        i = 1
        while i <= sample:
            movie = lt.getElement(sort_movies, i)
            print('Titulo: ' + movie['title'] + ' Release Year: ' +
            movie['release_year'] + ' Rating: ' + movie['rating'] + ' Duration: ' + movie['duration'])
            i += 1
        
        print("Las", sample, "ultimas peliculas ordenadas son:")
        i = size - sample
        while i <= size:
            movie = lt.getElement(sort_movies, i)
            print('Titulo: ' + movie['title'] + ' Release Year: ' +
            movie['release_year'] + ' Rating: ' + movie['rating'] + ' Duration: ' + movie['duration'])
            i += 1

def printReq1(sort_movies, sample=3):
    size = lt.size(sort_movies)
    if size <= sample*2:
        print("Las", size, "peliculas ordenadas son:")
        tabla=[]
        for movie in lt.iterator(sort_movies):
            tabla.append([movie['release_year'], movie['title'], movie['duration'], movie['platform'], movie['director'], movie['cast'] ])
        print(tabulate(tabla, headers=["Release Year", "Title", "Duration","Platform", "Director", "Cast"], tablefmt="grid", maxcolwidths=[8,20,10,20,10,15]))
    
    else:
        print("Las", sample, "primeras y ", sample, " ultimas peliculas ordenadas son: \n", )
        i = 1
        tabla=[]
        while i <= sample:
            movie = lt.getElement(sort_movies, i)
            i += 1
            tabla.append([movie['release_year'], movie['title'], movie['duration'],movie['platform'], movie['director'], movie['cast'] ])
        
        j = size + 1 - sample
        while j <= size:
            movie = lt.getElement(sort_movies, j)
            j += 1
            tabla.append([movie['release_year'], movie['title'], movie['duration'],movie['platform'], movie['director'], movie['cast'] ])
        
        print(tabulate(tabla, headers=["Release Year", "Title", "Duration","Platform", "Director", "Cast"], tablefmt="grid", maxcolwidths=[8,20,10,20,10,15]))

def printReq2(sort_movies, sample=3):
    size = lt.size(sort_movies)
    if size <= sample*2:
        print("Los", size, "programas de TV ordenados son:")
        tabla=[]
        for movie in lt.iterator(sort_movies):
            tabla.append([movie['title'], movie['date_added'],  movie['duration'], movie['release_year'],movie['platform'], movie['director'], movie['cast'] ])
        print(tabulate(tabla, headers=[ "Title","Date Added", "Duration", "Release Year","Platform", "Director", "Cast"], tablefmt="grid", maxcolwidths=[10,8,8,5,8,10,15]))
    
    else:
        print("Los", sample, "primeros y ", sample, " ultimos programas de TV ordenados son: \n", )
        i = 1
        tabla=[]
        while i <= sample:
            movie = lt.getElement(sort_movies, i)
            i += 1
            tabla.append([movie['title'], movie['date_added'],  movie['duration'], movie['release_year'],movie['platform'], movie['director'], movie['cast'] ])
        
        j = size + 1 - sample
        while j <= size:
            movie = lt.getElement(sort_movies, j)
            j += 1
            tabla.append([movie['title'], movie['date_added'],  movie['duration'], movie['release_year'], movie['platform'], movie['director'], movie['cast'] ])
        
        print(tabulate(tabla, headers=[ "Title","Date Added", "Duration", "Release Year","Platform", "Director", "Cast"], tablefmt="grid", maxcolwidths=[10,8,8,5,8,10,15]))
       
def printReq3(sort_movies, sample=3):
    size = lt.size(sort_movies)
    if size <= sample*2:
        print("Los", size, "contenidos ordenados son:")
        tabla=[]
        for movie in lt.iterator(sort_movies):
            tabla.append([movie['title'], movie['release_year'], movie['director'], movie['platform'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        print(tabulate(tabla, headers=[ "Title",  "Release Year", "Director", "Platform", "Duration", "Cast", "Country", "Listed In", "Description"], tablefmt="grid", maxcolwidths=[20,8,8,8,8,15,8,8,10]))
    
    else:
        print("Los", sample, "primeros y ", sample, " ultimos contenidos ordenados son: \n", )
        i = 1
        tabla=[]
        while i <= sample:
            movie = lt.getElement(sort_movies, i)
            i += 1
            tabla.append([movie['title'], movie['release_year'], movie['director'], movie['platform'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        
        j = size + 1 - sample
        while j <= size:
            movie = lt.getElement(sort_movies, j)
            j += 1
            tabla.append([movie['title'], movie['release_year'], movie['director'], movie['platform'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        
        print(tabulate(tabla, headers=[ "Title",  "Release Year", "Director", "Platform", "Duration", "Cast", "Country", "Listed In", "Description"], tablefmt="grid", maxcolwidths=[20,8,8,8,8,15,8,8,10]))
            
def printReq4(sort_movies, sample=3):
    size = lt.size(sort_movies)
    tabla=[]
    if size <= sample*2:
        print("Los", size, "contenidos ordenados son:")
        for movie in lt.iterator(sort_movies):
            tabla.append([ movie['title'], movie['release_year'], movie['platform'], movie['director'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        print(tabulate(tabla, headers=["Titulo","Release Year", 'Platform',"Director","Duration",'Cast','Country','Listed In', 'Description'], tablefmt="grid", maxcolwidths=[10,8,8,10,8,15,10,10,15]))
    
    else:
        print("Los", sample, "primeros y ", sample, " ultimos contenidos ordenados son: \n", )
        i = 1
        tabla=[]
        while i <= sample:
            movie = lt.getElement(sort_movies, i)
            i += 1
            tabla.append([ movie['title'], movie['release_year'],movie['platform'], movie['director'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])

        j = size + 1 - sample
        while j <= size:
            movie = lt.getElement(sort_movies, j)
            j += 1
            tabla.append([ movie['title'], movie['release_year'],movie['platform'], movie['director'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        print(tabulate(tabla, headers=["Titulo","Release Year", 'Platform',"Director","Duration",'Cast','Country','Listed In', 'Description'], tablefmt="grid", maxcolwidths=[10,8,8,10,8,15,10,10,15]))

def printReq5(sort_movies, sample=3):
    size = lt.size(sort_movies)
    tabla=[]
    if size <= sample*2:
        print("Los", size, "contenidos ordenados son:")
        for movie in lt.iterator(sort_movies):
            tabla.append([ movie['title'], movie['release_year'], movie['director'],movie['platform'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        print(tabulate(tabla, headers=["Titulo","Release Year", "Director", 'Platform',"Duration",'Cast','Country','Listed In', 'Description'], tablefmt="grid", maxcolwidths=[10,10,10,8,10,15,8,10,15]))
    
    else:
        print("Los", sample, "primeros y ", sample, " ultimos contenidos ordenados son: \n", )
        i = 1
        tabla=[]
        while i <= sample:
            movie = lt.getElement(sort_movies, i)
            i += 1
            tabla.append([ movie['title'], movie['release_year'], movie['director'],movie['platform'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])

        j = size + 1 - sample
        while j <= size:
            movie = lt.getElement(sort_movies, j)
            j += 1
            tabla.append([ movie['title'], movie['release_year'], movie['director'],movie['platform'], movie['duration'], movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        print(tabulate(tabla, headers=["Title","Release Year", "Director",'Platform',"Duration",'Cast','Country','Listed In', 'Description'], tablefmt="grid", maxcolwidths=[10,10,10,8,10,15,8,10,15]))

def printReq6(sort_movies, sample=3):
    size = lt.size(sort_movies)
    tabla=[]
    tab_gen=[]
    service=[0,0,0,0,0,0,0,0]

    for movie in lt.iterator(sort_movies):
        if movie['platform']=="Amazon Prime" and movie['type']=="Movie":
            service[0]=service[0]+1
        elif movie['platform']=="Disney Plus" and movie['type']=="Movie":
            service[1]=service[1]+1
        elif movie['platform']=="Hulu" and movie['type']=="Movie":
            service[2]=service[2]+1
        elif movie['platform']=="Netflix" and movie['type']=="Movie":
            service[3]=service[3]+1
        if movie['platform']=="Amazon Prime" and movie['type']=="TV Show":
            service[4]=service[4]+1
        elif movie['platform']=="Disney Plus" and movie['type']=="TV Show":
            service[5]=service[5]+1
        elif movie['platform']=="Hulu" and movie['type']=="TV Show":
            service[6]=service[6]+1
        elif movie['platform']=="Netflix" and movie['type']=="TV Show":
            service[7]=service[7]+1

        generos=movie['listed_in'].split(sep=', ')
        for i in range(0,len(generos)):
            for j in range(0,len(tab_gen)):
                if generos[i]==tab_gen[j][0]:
                    tab_gen[j][1]=tab_gen[j][1]+1
                else: tab_gen.append([generos[i],1])
            if len(tab_gen)==0:
                tab_gen.append([generos[i],1])

    conte=[["Amazon",service[0],service[4]],["Disney",service[1],service[5]],["Hulu",service[2],service[6]],["Netflix",service[3],service[7]]]
    print(tabulate(conte,headers=["Service name","Movie","TV Show"], tablefmt="grid"))
    print("\n----------- Cantidad por Genero ------------")
    print(tabulate(tab_gen,headers=["Generos","Cantidad"],tablefmt="grid"))

    if size <= sample*2:
        for movie in lt.iterator(sort_movies):
            tabla.append([movie['release_year'], movie['title'], movie['duration'],movie['platform'], movie['director'],  movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        print("\n-----------Los", size, "contenidos ordenados son:")
        print(tabulate(tabla, headers=["Release Year", "Title", "Duration","Platform","Director",'Cast','Country','Listed In', 'Description'], tablefmt="grid", maxcolwidths=[8,10,8,10,10,15,8,10,15]))

    else:
        print("Los", sample, "primeros y ", sample, " ultimos contenidos ordenados son: \n", )
        i = 1
        tabla=[]
        while i <= sample:
            movie = lt.getElement(sort_movies, i)
            i += 1
            tabla.append([movie['release_year'], movie['title'], movie['duration'], movie['director'],  movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])

        j = size + 1 - sample
        while j <= size:
            movie = lt.getElement(sort_movies, j)
            j += 1
            tabla.append([movie['release_year'], movie['title'], movie['duration'], movie['director'],  movie['cast'], movie['country'], movie['listed_in'], movie['description'] ])
        print(tabulate(tabla, headers=["Release Year", "Title", "Duration", "Director",'Cast','Country','Listed In', 'Description'], tablefmt="grid", maxcolwidths=[8,10,8,10,10,15,8,10,15]))

def printReq7(top, n):
    tabla=[]
    i = 1
    while i <= n:
        genero = lt.getElement(top, i)
        typeCount = "Movies: " + str(genero['movies']) + "\n\nTV Shows: " + str(genero['shows'])
        platformCount = "Disney: " + str(genero['disney']) + "\nAmazon Prime: " + str(genero['amazon']) + "\nNetflix: " + str(genero['netflix']) + "\nHulu: " + str(genero['hulu'])
        i+=1
        tabla.append([i-1, genero['genero'], genero['cantidad'], typeCount, platformCount])
    print(tabulate(tabla, headers=["Rank","Género", "Cantidad", "Type", "Stream Service"], tablefmt="grid", maxcolwidths=[8,10,8,15,15]))


def printReq8(top, n):
    tabla=[]
    i = 1
    while i <= n:
        actor = lt.getElement(top, i)
        actoresT= list(set(actor['actores']))
        directoresT= list(set(actor['directores']))
        typeCount = "Movies: " + str(actor['movies']) + "\nTV Shows: " + str(actor['shows'])
        platformCount = "Disney: " + str(actor['disney']) + "\nAmazon Prime: " + str(actor['amazon']) + "\nNetflix: " + str(actor['netflix']) + "\nHulu: " + str(actor['hulu'])
        i+=1
        tabla.append([i-1, actor['actor'], actor['cantidad'], typeCount, platformCount, str(actoresT), str(directoresT)])
    print(tabulate(tabla, headers=["Rank","Actor", "Cantidad", "Type", "Stream Service", "Actores", "Directores"], tablefmt="grid",  maxcolwidths=[8,10,8,10,10,15,15]))


# ------- Funciones de medicion de tiempo --------
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

catalog = None
cant_ant=0

"""
Menu principal
"""

#Conjunto de nombres de archivo para la carga de diferentes tamaños de datos.
filenames =[['amazon_prime_titles-utf8-small.csv','disney_plus_titles-utf8-small.csv','hulu_titles-utf8-small.csv','netflix_titles-utf8-small.csv'],
            ['amazon_prime_titles-utf8-5pct.csv','disney_plus_titles-utf8-5pct.csv','hulu_titles-utf8-5pct.csv','netflix_titles-utf8-5pct.csv'],
            ['amazon_prime_titles-utf8-10pct.csv','disney_plus_titles-utf8-10pct.csv','hulu_titles-utf8-10pct.csv','netflix_titles-utf8-10pct.csv'],
            ['amazon_prime_titles-utf8-20pct.csv','disney_plus_titles-utf8-20pct.csv','hulu_titles-utf8-20pct.csv','netflix_titles-utf8-20pct.csv'],
            ['amazon_prime_titles-utf8-30pct.csv','disney_plus_titles-utf8-30pct.csv','hulu_titles-utf8-30pct.csv','netflix_titles-utf8-30pct.csv'],
            ['amazon_prime_titles-utf8-50pct.csv','disney_plus_titles-utf8-50pct.csv','hulu_titles-utf8-50pct.csv','netflix_titles-utf8-50pct.csv'],
            ['amazon_prime_titles-utf8-80pct.csv','disney_plus_titles-utf8-80pct.csv','hulu_titles-utf8-80pct.csv','netflix_titles-utf8-80pct.csv'],
            ['amazon_prime_titles-utf8-large.csv','disney_plus_titles-utf8-large.csv','hulu_titles-utf8-large.csv','netflix_titles-utf8-large.csv']]

while True:
    printMenu()
    inputs = int(input('Seleccione una opción para continuar\n'))
    
    if inputs == 1:
        control = newController(2) #Se crea una lista de tipo Array List (2)
        print("Seleccione el tamaño del archivo a cargar")
        filesize = input('1. Small\n2. 5pct\n3. 10pct\n4. 20pct\n5. 30pct\n6. 50pct\n7. 80pct\n8. Large\n')
        print("Cargando información de los archivos ....")
        amazon=0
        netflix=0
        hulu=0
        disney=0
        for i in range(4):
            cant = loadData(control,filenames[int(filesize)-1][i],i)
            cant_tem=cant-cant_ant
            if i==0:
                amazon=cant_tem
            if i==1:
                disney=cant_tem
            if i==2:
                hulu=cant_tem
            if i==3:
                netflix=cant_tem
            cant_ant=cant
            
        SampleMovies = controller.getSampleMovies(control, cant)
        printMovies(SampleMovies, amazon, disney, hulu, netflix, cant)

    elif inputs == 2:
        print("Digite el rango de años que desea consultar")
        fecha1=input("Digite el año inicial: ")
        fecha2=input("Digite el año final: ")
        start_time = getTime()
        result = controller.sortMoviesByReleaseYear(control)
        sorted_list = result[0]
        respuesta=controller.getMoviesByReleaseYear(sorted_list,fecha1,fecha2)
        lista=respuesta[1]
        print("======= REQUERIMIENTO 1 ======")
        print("La cantidad de peliculas presentes en el periodo es de: "+str(respuesta[0])+'\n')
        print(printReq1(lista,3))
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")

    elif inputs == 3:
        print("Digite el rango de fechas que desea consultar")
        fecha1=input("Digite la fecha inicial en formato AAAA-MM-DD: ")
        fecha2=input("Digite la fecha final en formato AAAA-MM-DD: ")
        start_time = getTime()
        result = controller.sortMoviesByDateAdded(control)
        sorted_list = result[0]
        respuesta=controller.getShowsByPeriod(sorted_list,fecha1,fecha2)
        lista=respuesta[1]
        print("======= REQUERIMIENTO 2 ======")
        print("La cantidad de títulos registrados durante estas fechas es: "+str(respuesta[0])+'\n')
        print(printReq2(lista,3))
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")

    elif inputs == 4:
        actor=input("Indique el nombre del actor: ")
        start_time = getTime()
        result = controller.sortMoviesByName(control)
        sorted_list = result[0]
        respuesta=controller.getContentByCast(sorted_list,actor)
        lista=respuesta[0]
        print("======= REQUERIMIENTO 3 ======")
        print("El actor ha participado en: "+str(respuesta[1])+" peliculas")
        print("El actor ha participado en: "+str(respuesta[2])+" tv shows")
        print(printReq3(lista,3))
        print("\n-------- Para esta cantidad de elementos ")
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")

    elif inputs == 5:
        genero= input('Ingrese el género que desee buscar: ')
        start_time = getTime()
        result = controller.sortMoviesByName2(control)
        sorted_list = result[0]
        respuesta=controller.getContentByGenero(sorted_list,genero)
        print("======= REQUERIMIENTO 4 ======")
        print("El total de películas del género seleccionado es de : "+str(respuesta[0])+" peliculas")
        print("El total de TV Shows del género seleccionado es de : "+str(respuesta[1])+" shows")
        print(printReq4(respuesta[2],3))
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")

    elif inputs == 6:
        pais = input("Ingrese el nombre del país: ")
        start_time = getTime()
        result = controller.sortMoviesByName2(control)
        sorted_list = result[0]
        respuesta=controller.getShowsByCountry(sorted_list,pais)
        lista=respuesta[0]
        print("======= REQUERIMIENTO 5 ======")
        print("El número total de películas producidos en " + pais + " es: "+str(respuesta[1]))
        print("El número total de programas producidos en " + pais + " es: "+str(respuesta[2]))
        print(printReq5(lista,3))
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")
         
    elif inputs == 7:
        director=input("Indique el nombre del director: ")
        start_time = getTime()
        result = controller.sortMoviesByReleaseYear(control)
        sorted_list = result[0]
        respuesta=controller.getContentByDirector(sorted_list,director)
        lista=respuesta[0]
        print("======= REQUERIMIENTO 6 ======")
        print("El director ha participado en: "+str(respuesta[1])+" peliculas")
        print("El director ha participado en: "+str(respuesta[2])+" tv shows")
        print(printReq6(lista,3))
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")
    
    elif inputs == 8:
        n=input("Indique el numero de elementos del top: ")
        start_time = getTime()
        respuesta=controller.getTopByGenero(control)
        print("======= REQUERIMIENTO 7 ======")
        printReq7(respuesta, int(n))
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")

    elif inputs == 9:
        n=input("Indique el numero de elementos del top: ")
        start_time = getTime()
        respuesta=controller.getTopByActor(control)
        print("======= REQUERIMIENTO 8 ======")
        printReq8(respuesta, int(n))
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
        print("\n-----> El tiempo ejecutado del proceso de este requerimiento es de: ", f"{delta_time:.3f}")
    
    else:
        sys.exit(0)
        
        
        
        
        
    # Utilizada en los laboratorios 4 y 5  
    '''elif inputs == 10:
            size = input("Indique tamaño de la muestra: ")
            print("Seleccione el tipo de ordenamiento")
            sortType = input("1.Shell Sort\n2.Insertion Sort\n3.SelectionSort\n4.QuickSort\n5.MergeSort\n")
            result = controller.sortMovies(control, int(size), int(sortType))
            delta_time = f"{result[1]:.3f}"
            sorted_list = result[0]
            print("Para", size, "elementos, delta tiempo:", str(delta_time))
            printSortResults(sorted_list)'''
            
    

