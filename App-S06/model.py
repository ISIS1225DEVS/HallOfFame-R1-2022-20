"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as selection
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
import csv
csv.field_size_limit(2147483647)

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo
def inicializarCatalogo(tipo):
    catalogo={}
    catalogo['listaNetflix']=lt.newList(tipo)
    catalogo['listaHulu']=lt.newList(tipo)
    catalogo['listaDisney']=lt.newList(tipo)
    catalogo['listaPrime']=lt.newList(tipo)
    catalogo['listaTotal']=lt.newList(tipo)
    return catalogo


def addTitleNetflix(catalogo, title):
    listaTitles=catalogo['listaNetflix']
    title["Streaming_service"]="Netflix"
    lt.addLast(listaTitles, title)


def addTitleHulu(catalogo, title):
    listaTitles=catalogo['listaHulu']
    title["Streaming_service"]="Hulu"
    lt.addLast(listaTitles, title)
    
def addTitleDisney(catalogo, title):
    listaTitles=catalogo['listaDisney']
    title["Streaming_service"]="Disney"
    lt.addLast(listaTitles, title)

def addTitlePrime(catalogo, title):
    listaTitles=catalogo['listaPrime']
    title["Streaming_service"]="Prime"
    lt.addLast(listaTitles, title)

def addTitle(catalogo,title):
    listaTitles=catalogo['listaTotal']
    lt.addLast(listaTitles, title)


def primeros3(lista,opcion):
    i=1
    listaPrimeros3=lt.newList()
    if opcion == 1:
        while i<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(i)+ ") ID: " +elemento['show_id'] + "\nType: " +elemento['type'] +"\nTitle: " +elemento['title'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+"\nDate added: " +elemento['date_added']+ "\nRating: " +elemento['rating']+ "\nListed in: " +elemento['listed_in']+ "\nDescripcion: " +elemento['description'] +"\nStreaming Service: " +elemento['Streaming_service']
            lt.addLast(listaPrimeros3, name)
            i+=1
    if opcion == 2:
        while i<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(i)+ ") Type: " +elemento['type'] +"\nTitle: " +elemento['title'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] +"\nStreaming Service: " +elemento['Streaming_service']
            lt.addLast(listaPrimeros3, name)
            i+=1

    if opcion == 3:
        while i<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(i)+ ") Type: " +elemento['type'] +"\nTitle: " +elemento['title'] + "\nDate added: " +elemento['date_added'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nRelease year: " +elemento['release_year'] + "\nCast: " +elemento['cast'] +"\nStreaming Service: " +elemento['Streaming_service']
            lt.addLast(listaPrimeros3, name)
            i+=1
    
    if opcion ==4 or opcion== 5 or opcion==6:
        z=1
        while z<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(z)+ ") Title: " +elemento['title'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] +"\nStreaming Service: " +elemento['Streaming_service'] + "\nDuration: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+  "\nListed in: " +elemento['listed_in'] +  "\nDescription: " +elemento['description'] 
            lt.addLast(listaPrimeros3, name)
            i+=1
            z+=1
            
    if opcion == 7:
        if lt.size(lista)<=3:
            while i<=lt.size(lista):
                elemento=lt.getElement(lista,i)
                name= "------------------------------------------------------------------------------------------------------\n"
                name+=str(i)+ ") Title: " +elemento['title'] + "\nType: " +elemento['type'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+"\nRating: " +elemento['rating']+ "\nListed in: " +elemento['listed_in']+ "\nDescripcion: " +elemento['description']+"\nStreaming Service: " +elemento['Streaming_service']
                lt.addLast(listaPrimeros3, name)
                i+=1
        else:
            i=1
            while i<=3:
                elemento=lt.getElement(lista,i)
                name= "--------------------------------------------------------------------------------------------------------------------------------\n"
                name+=str(i)+ ") Title: " +elemento['title'] + "\nType: " +elemento['type'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+"\nRating: " +elemento['rating']+ "\nListed in: " +elemento['listed_in']+ "\nDescripcion: " +elemento['description']+"\nStreaming Service: " +elemento['Streaming_service']
                lt.addLast(listaPrimeros3, name)
                i+=1

    return listaPrimeros3

def listar (lista):
    i=1
    z=lt.size(lista)
    listaListar = lt.newList()
    while i<z+1:
        elemento = lt.getElement(lista,i)
        name= "--------------------------------------------------------------------------------------------------------------------------------\n"
        name+=str(z)+ ") Title: " +elemento['title'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] +"\nStreaming Service: " +elemento['Streaming_service'] + "\nDuration: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+  "\nListed in: " +elemento['listed_in'] +  "\nDescription: " +elemento['description'] 
        lt.addLast(listaListar, name)
        i+=1
    return (listaListar)

def ultimos3(lista,opcion):
    
    i = lt.size(lista)-2
    z= 1
    listaUltimos3=lt.newList()
    if opcion == 1:
        while z<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(z)+ ") ID: " +elemento['show_id'] + "\nType: " +elemento['type'] +"\nTitle: " +elemento['title'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+"\nDate added: " +elemento['date_added']+ "\nRating: " +elemento['rating']+ "\nListed in: " +elemento['listed_in']+ "\nDescripcion: " +elemento['description']+"\nStreaming Service: " +elemento['Streaming_service']
            lt.addLast(listaUltimos3, name)
            i+=1
            z+=1
    
    if opcion == 2:
        while z<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(z)+ ") Type: " +elemento['type'] +"\nTitle: " +elemento['title'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] +"\nStreaming Service: " +elemento['Streaming_service']
            lt.addLast(listaUltimos3, name)
            i+=1
            z+=1

    if opcion == 3:
        while z<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(z)+ ") Type: " +elemento['type'] +"\nTitle: " +elemento['title'] + "\nDate added: " +elemento['date_added'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nRelease year: " +elemento['release_year'] + "\nCast: " +elemento['cast'] +"\nStreaming Service: " +elemento['Streaming_service']
            lt.addLast(listaUltimos3, name)
            i+=1
            z+=1

    if opcion ==4 or opcion==5 or opcion==6:
        z=1
        while z<=3:
            elemento=lt.getElement(lista,i)
            name= "--------------------------------------------------------------------------------------------------------------------------------\n"
            name+=str(z)+ ") Title: " +elemento['title'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] +"\nStreaming Service: " +elemento['Streaming_service'] + "\nDuration: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+  "\nListed in: " +elemento['listed_in'] +  "\nDescription: " +elemento['description'] 
            lt.addLast(listaUltimos3, name)
            i+=1
            z+=1

    if opcion == 7:
        if lt.size(lista)<=3:
            while z<=lt.size(lista):
                elemento=lt.getElement(lista,i)
                name= "--------------------------------------------------------------------------------------------------------------------------------\n"
                name+=str(z)+ ") Title: " +elemento['title'] + "\nType: " +elemento['type'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+"\nRating: " +elemento['rating']+ "\nListed in: " +elemento['listed_in']+ "\nDescripcion: " +elemento['description']+"\nStreaming Service: " +elemento['Streaming_service']
                lt.addLast(listaUltimos3, name)
                i+=1
                z+=1
        else:
            z=1
            while z<=3:
                elemento=lt.getElement(lista,i)
                name= "--------------------------------------------------------------------------------------------------------------------------------\n"
                name+=str(z)+ ") Title: " +elemento['title'] + "\nType: " +elemento['type'] + "\nRelease year: " +elemento['release_year'] + "\nDirector: " +elemento['director'] + "\nDuración: " +elemento['duration'] + "\nCast: " +elemento['cast'] + "\nCountry: " +elemento['country']+"\nRating: " +elemento['rating']+ "\nListed in: " +elemento['listed_in']+ "\nDescripcion: " +elemento['description']+"\nStreaming Service: " +elemento['Streaming_service']
                lt.addLast(listaUltimos3, name)
                i+=1
                z+=1
    return listaUltimos3


# Funciones para creacion de datos

# Funciones de consulta
def contenido_por_genero(genero,sorted_listT):
    lista_gen = lt.newList()
    cont = 1
    num = 1
    peliculas = 0
    series = 0
    streaming = ''
    size = lt.size(sorted_listT)
    
    while cont<=size:
        elemento=lt.getElement(sorted_listT,cont)
        if genero in str(elemento['listed_in']):
            lt.addLast(lista_gen,elemento)
            num+=1

            if str(elemento['type']) == 'Movie':
                peliculas+=1
            elif str(elemento['type']) == 'TV Show':
                series+=1

        cont+=1
    
    return lista_gen, peliculas, series

def periodo_tiempo_peliculas(inicial, final,sorted_listT):
    lista_periodo_tiempo = lt.newList()
    cont = 1
    size = lt.size(sorted_listT)
    while cont<=size:
        elemento=lt.getElement(sorted_listT,cont)
        if elemento['type'] == 'Movie' and (elemento['release_year'] >= inicial and elemento['release_year'] <= final):
            lt.addLast(lista_periodo_tiempo,elemento)
        cont +=1

    return lista_periodo_tiempo

def periodo_tiempo_series(inicial,final,sorted_listT):
    lista_periodo_tiempo = lt.newList()
    cont = 1
    size = lt.size(sorted_listT)

    while cont<=size:
        elemento=lt.getElement(sorted_listT,cont)
        fecha_inicial= inicial.split("-")
        fecha_final= final.split("-")
        fecha1 = elemento['date_added'].split("-")

        if elemento['date_added'] != "" and elemento['type'] == 'TV Show': 
            if (fecha1[0] > fecha_inicial[0] and fecha1[0] < fecha_final[0]):
                lt.addLast(lista_periodo_tiempo,elemento)
            elif (fecha1[0] == fecha_inicial[0]):
                if (fecha1[1]> fecha_inicial[1]):
                    lt.addLast(lista_periodo_tiempo,elemento)
                elif ((fecha1[1] == fecha_inicial[1])and (fecha1[2]>=fecha_inicial[2])):
                    lt.addLast(lista_periodo_tiempo,elemento)
            elif (fecha1[0] == fecha_final[0]):
                if (fecha1[1]< fecha_final[1]):
                    lt.addLast(lista_periodo_tiempo,elemento)
                elif ((fecha1[1] == fecha_final[1])and (fecha1[2]<=fecha_final[2])):
                    lt.addLast(lista_periodo_tiempo,elemento)
        cont +=1

    return lista_periodo_tiempo

def contenido_por_actor(actor, sorted_listT):
    lista_actor = lt.newList()
    cont=1
    size = lt.size(sorted_listT)
    while cont <= size:
        elemento=lt.getElement(sorted_listT,cont)
        if actor in elemento['cast']:
            lt.addLast(lista_actor, elemento)
        cont+=1
    
    peliculas = lt.newList()
    series = lt.newList()
    contador = 1
    tamaño = lt.size(lista_actor)
    while contador<= tamaño:
        titulo = lt.getElement(lista_actor, contador)
        if titulo['type']== "Movie":
            lt.addLast(peliculas,titulo)
        else:
            lt.addLast(series, titulo)
        contador+=1
    return peliculas, series, lista_actor

def contenido_por_pais(pais, sorted_listT):
    lista_p= lt.newList()
    peliculas= 0
    series= 0
    i=1
    while i<= lt.size(sorted_listT):
        elemento= lt.getElement(sorted_listT,i)
        if pais == elemento['country']:
            lt.addLast(lista_p,elemento)
            if elemento['type']=="Movie":
                peliculas+=1
            else:
                series+=1
        i+=1
    return lista_p, peliculas, series
        

def contenido_director(director,sorted_listT):
    lista_director = lt.newList()
    peliculas = 0
    programas = 0
    cont = 1
    size = lt.size(sorted_listT)

    while cont<=size:
        elemento=lt.getElement(sorted_listT,cont)
        if str(director) in elemento['director']:
            if elemento['type'] == 'Movie':
                peliculas+=1
            else:
                programas+=1
            lt.addLast(lista_director,elemento)
        cont +=1

    z= 1
    listastreaming= {}
    size1= lt.size(lista_director)
    pel = 0
    ser = 0
    while z <= size1:
        streaming= lt.getElement(lista_director,z)
        if streaming['Streaming_service'] not in listastreaming.keys():
            listastreaming[streaming['Streaming_service']]=1
            if streaming['type'] == 'Movie':
                pel+=1
                listastreaming[streaming['type']]=pel
            else:
                ser+=1
                listastreaming[streaming['type']]=1
        else:
            listastreaming[streaming['Streaming_service']]+=1
            if streaming['type'] == 'Movie':
                pel+=1
                listastreaming[streaming['type']]= pel
            else:
                ser+=1
                listastreaming[streaming['type']]= ser
        z+=1

    i= 1
    listasgenero= {}
    while i<= size1:
        genero= lt.getElement(lista_director,i)
        generos= genero['listed_in'].split(", ")
        z=1
        pos = 0
        size2 = len(generos)
        while z <= size2:
            if generos[pos] not in listasgenero.keys():
                listasgenero[generos[pos]]=1
            else:
                listasgenero[generos[pos]]+=1
            z+=1
            pos+=1
        i+=1
    return lista_director, peliculas, programas, listastreaming, listasgenero

def top_generos(top,sorted_listT):
    listageneros= {}
    i= 1
    while i<= lt.size(sorted_listT):
        genero= lt.getElement(sorted_listT,i)
        generos= genero['listed_in'].split(", ")
        
        z=1
        pos = 0
        while z <= len(generos):
            if (generos[pos]) not in listageneros.keys():
                listageneros[generos[pos]]=1
            else:
                listageneros[generos[pos]]+=1
            z+=1
            pos+=1
        i+=1
    

    listanombres = lt.newList()
    i=0
    inicial = 0
    for ele in listageneros.keys():
        lt.addLast(listanombres,ele)

    listanumeros = lt.newList()
    i=0
    inicial = 0
    for ele in listageneros.values():
        lt.addLast(listanumeros,ele)

    merge.sort(listanumeros,mayor_menor)
    
    listaposiciones =lt.newList()

    i=0
    num = len(listageneros)
    for numero in lt.iterator(listanumeros):
        for nombre in lt.iterator(listanombres):
            i+=1
            size= lt.size(listaposiciones)
            if listageneros[nombre] == numero and size < num:
                lt.addLast(listaposiciones,nombre) 

    listafinaltags= lt.newList()
    listafinalnumeros= lt.newList()
    i=1
    while i<=top:
        elemento1= lt.getElement(listaposiciones,i)
        elemento2= lt.getElement(listanumeros,i)
        lt.addLast(listafinaltags,elemento1)
        lt.addLast(listafinalnumeros,elemento2)
        i+=1
    
    listaMovies = lt.newList()
    listaTV = lt.newList()
    listaN = lt.newList()
    listaA = lt.newList()
    listaH = lt.newList()
    listaD = lt.newList()

    j=1
    while j<= top:
        elemento2= lt.getElement(listafinaltags,j)
        contadorM=0
        contadorTV=0
        contadorN=0
        contadorA=0
        contadorH=0
        contadorD=0
        i=1
        while i<= lt.size(sorted_listT):
            elemento1= lt.getElement(sorted_listT,i)
            if elemento2 in elemento1["listed_in"] :
                if elemento1["type"]== "Movie":
                    contadorM+=1
                else:
                    contadorTV+=1
                if elemento1["Streaming_service"]=="Netflix":
                    contadorN+=1
                elif elemento1["Streaming_service"]=="Hulu":
                    contadorH+=1
                elif elemento1["Streaming_service"]=="Amazon":
                    contadorA+=1
                else:
                    contadorD+=1
            i+=1
        lt.addLast(listaMovies, contadorM)
        lt.addLast(listaTV, contadorTV)
        lt.addLast(listaN, contadorN)
        lt.addLast(listaH, contadorH)
        lt.addLast(listaA, contadorA)
        lt.addLast(listaD, contadorD)

        j+=1

    return listafinaltags, listafinalnumeros, listaMovies, listaTV, listaN, listaH, listaA, listaD

def top_actores(top,sorted_listT):
    listaactores= {}
    i= 1
    while i<= lt.size(sorted_listT):
        actor= lt.getElement(sorted_listT,i)
        actores= actor['cast'].split(", ")
        
        z=1
        pos = 0
        while z <= len(actores):
            if (actores[pos]) not in listaactores.keys():
                listaactores[actores[pos]]=1
            else:
                listaactores[actores[pos]]+=1
            z+=1
            pos+=1
        i+=1
    
    listanombres = lt.newList()
    i=0
    inicial = 0
    for ele in listaactores.keys():
        lt.addLast(listanombres,ele)

    listanumeros = lt.newList()
    i=0
    inicial = 0
    for ele in listaactores.values():
        lt.addLast(listanumeros,ele)

    merge.sort(listanumeros,mayor_menor)
    
    listaposiciones =lt.newList()

    i=0
    num = len(listaactores)
    for numero in lt.iterator(listanumeros):
        for nombre in lt.iterator(listanombres):
            i+=1
            size= lt.size(listaposiciones)
            if listaactores[nombre] == numero and size < num:
                lt.addLast(listaposiciones,nombre) 

    listafinaltags= lt.newList()
    listafinalnumeros= lt.newList()
    i=1
    while i<=top:
        elemento1= lt.getElement(listaposiciones,i)
        elemento2= lt.getElement(listanumeros,i)
        lt.addLast(listafinaltags,elemento1)
        lt.addLast(listafinalnumeros,elemento2)
        i+=1

    listaN_M = lt.newList()
    listaN_TV = lt.newList()
    listaH_M = lt.newList()
    listaH_TV = lt.newList()
    listaD_M = lt.newList()
    listaD_TV = lt.newList()
    listaA_M = lt.newList()
    listaA_TV = lt.newList()

    j=1

    while j<= top:
        elemento2= lt.getElement(listafinaltags,j)
        contadorA_M=0
        contadorA_TV=0
        contadorN_M=0
        contadorN_TV=0
        contadorH_M=0
        contadorH_TV=0
        contadorD_M=0
        contadorD_TV=0
        i=1
        while i<= lt.size(sorted_listT):
            elemento1= lt.getElement(sorted_listT,i)
            if elemento2 in elemento1["cast"]:
                if (elemento1["Streaming_service"]== "Prime" and elemento1["type"]== "Movie"):
                    contadorA_M+=1
                elif elemento1["Streaming_service"]== "Prime" and elemento1["type"]== "TV Show":
                    contadorA_TV+=1
                elif elemento1["Streaming_service"]== "Netflix" and elemento1["type"]== "Movie":
                    contadorN_M+=1
                elif elemento1["Streaming_service"]== "Netflix" and elemento1["type"]== "TV Show":
                    contadorN_TV+=1
                elif elemento1["Streaming_service"]== "Hulu" and elemento1["type"]== "Movie":
                    contadorH_M+=1
                elif elemento1["Streaming_service"]== "Hulu" and elemento1["type"]== "TV Show":
                    contadorH_TV+=1
                elif elemento1["Streaming_service"]== "Disney" and elemento1["type"]== "Movie":
                    contadorD_M+=1
                elif elemento1["Streaming_service"]== "Disney" and elemento1["type"]== "TV Show":
                    contadorD_TV+=1
            i+=1
        lt.addLast(listaN_M, contadorN_M)
        lt.addLast(listaN_TV, contadorN_TV)
        lt.addLast(listaA_M, contadorA_M)
        lt.addLast(listaA_TV, contadorA_TV)
        lt.addLast(listaD_M, contadorD_M)
        lt.addLast(listaD_TV, contadorD_TV)
        lt.addLast(listaH_M, contadorH_M)
        lt.addLast(listaH_TV, contadorH_TV)

        j+=1
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def mayor_menor(uno,dos):
    return (float(uno) > float(dos))

def compareyear(title1, title2):
    return (float(title1['release_year']) < float(title2['release_year']))

def sortTitles(catalog, lista,  size):
    sub_list = lt.subList(catalog[str(lista)], 1, size)
    start_time = getTime()
    sorted_list= sa.sort(sub_list, cmpMoviesByReleaseYear)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def sortReleaseYear(catalog,  size):
    sub_list = lt.subList(catalog, 1, size)
    start_time = getTime()
    sorted_list= sa.sort(sub_list, cmpMoviesByReleaseYear)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time
    

def sortDateAdded(catalog,  size):
    sub_list = lt.subList(catalog, 1, size)
    start_time = getTime()
    sorted_list= sa.sort(sub_list, cmpSeriesByDateAdded)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time
    
def cmpMoviesByReleaseYear(movie1,movie2):
    retorno= False
    if movie1['release_year']< movie2['release_year']:
        retorno= True
    elif movie1['release_year'] == movie2['release_year']:
        if movie1['title']< movie2['title']:
            retorno= True
        elif movie1['title'] == movie2['title']:
            if movie1['duration']< movie2['duration']:
                retorno= True
        else:
            retorno= False
    return retorno
    
def sortActores(catalog, lista,  size):
    sub_list = lt.subList(catalog[str(lista)], 1, size)
    start_time = getTime()
    sorted_list= sa.sort(sub_list, cmpByTitle)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def sortSeries(catalog, lista,  size):
    sub_list = lt.subList(catalog[str(lista)], 1, size)
    start_time = getTime()
    sorted_list= sa.sort(sub_list, cmpSeriesByDateAdded)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def cmpSeriesByDateAdded(movie1,movie2):
    retorno= False
    if movie1['date_added']< movie2['date_added']:
        retorno= True
    elif movie1['date_added'] == movie2['date_added']:
        if movie1['title']< movie2['title']:
            retorno= True
        elif movie1['title'] == movie2['title']:
            if movie1['duration']< movie2['duration']:
                retorno= True
        else:
            retorno= False

    return retorno

def cmpByTitle(movie1,movie2):
    retorno= False
    if movie1['title']< movie2['title']:
        retorno= True
    elif movie1['title'] == movie2['title']:
        if movie1['release_year']< movie2['release_year']:
            retorno= True
        elif movie1['release_year'] == movie2['release_year']:
            if movie1['duration']< movie2['duration']:
                retorno= True
        else:
            retorno= False
    return retorno

def sortDirector(catalog, lista,  size):
    sub_list = lt.subList(catalog[str(lista)], 1, size)
    start_time = getTime()
    sorted_list= sa.sort(sub_list, cmpByReleaseYearAndDirector)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def cmpByReleaseYearAndDirector(movie1,movie2):
    if movie1['title']< movie2['title']:
        return True
    elif movie1['title'] == movie2['title']:
        if movie1['release_year']< movie2['release_year']:
            return True
        elif movie1['release_year'] == movie2['release_year']:
            if movie1['director']< movie2['director']:
                return True
        else:
            return False
    else:
        return False

def ordenamiento(catalogo,tipo_alg):
    start_time = getTime()
    if tipo_alg =='selection':
        selection.sort(catalogo['listaNetflix'],cmpMoviesByReleaseYear)
        selection.sort(catalogo['listaHulu'],cmpMoviesByReleaseYear)
        selection.sort(catalogo['listaDisney'],cmpMoviesByReleaseYear)
        selection.sort(catalogo['listaPrime'],cmpMoviesByReleaseYear)
    
    elif tipo_alg =='insertion':
        insertion.sort(catalogo['listaNetflix'],cmpMoviesByReleaseYear)
        insertion.sort(catalogo['listaHulu'],cmpMoviesByReleaseYear)
        insertion.sort(catalogo['listaDisney'],cmpMoviesByReleaseYear)
        insertion.sort(catalogo['listaPrime'],cmpMoviesByReleaseYear)

    elif tipo_alg =='shell':
        sa.sort(catalogo['listaNetflix'],cmpMoviesByReleaseYear)
        sa.sort(catalogo['listaHulu'],cmpMoviesByReleaseYear)
        sa.sort(catalogo['listaDisney'],cmpMoviesByReleaseYear)
        sa.sort(catalogo['listaPrime'],cmpMoviesByReleaseYear)

    elif tipo_alg =='merge':
        merge.sort(catalogo['listaNetflix'],cmpMoviesByReleaseYear)
        merge.sort(catalogo['listaHulu'],cmpMoviesByReleaseYear)
        merge.sort(catalogo['listaDisney'],cmpMoviesByReleaseYear)
        merge.sort(catalogo['listaPrime'],cmpMoviesByReleaseYear)

    elif tipo_alg =='quick':
        quick.sort(catalogo['listaNetflix'],cmpMoviesByReleaseYear)
        quick.sort(catalogo['listaHulu'],cmpMoviesByReleaseYear)
        quick.sort(catalogo['listaDisney'],cmpMoviesByReleaseYear)
        quick.sort(catalogo['listaPrime'],cmpMoviesByReleaseYear)

    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return delta_time

# Funciones para medir tiempos de ejecucion

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