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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as sin
from DISClib.Algorithms.Sorting import selectionsort as ssel
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
import time
assert cf
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# ---------------- Construccion de modelos ---------------------

def newCatalog(inputList):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'movies': None}
    
    if (inputList == 1):
        catalog['movies'] = lt.newList('SINGLE_LINKED')
        print("Catálogo cargado en SINGLE_LINKED")
    elif (inputList == 2):
        catalog['movies'] = lt.newList('ARRAY_LIST')
        print("Catálogo cargado en ARRAY_LIST")
    else:
        print("No entré")
    return catalog


# ----- Funciones para agregar informacion al catalogo -----

def addMovie(catalog, movie, platform):
    # Se adiciona el libro a la lista de contenido
    if platform==0:
        movie['platform']="Amazon Prime"
    if platform==1:
        movie['platform']="Disney Plus"
    if platform==2:
        movie['platform']="Hulu"
    if platform==3:
        movie['platform']="Netflix"
        
    lt.addLast(catalog['movies'], movie)
    
    return catalog

def movieSize(catalog):
    return lt.size(catalog['movies'])



# ---------------- Funciones de ordenamiento -----------------
    
#Funcion que ordena el contenido en base al tipo de ordenamiento y 
#tamaño de la muestra recibidos.
def sortMovies(catalog, size, sortType):
    sub_list = lt.subList(catalog['movies'], 1, size)
    start_time = getTime()
    if(sortType == 1):
        print("Ordenando con Shell Sort")
        sorted_list = sa.sort(sub_list, cmpMoviesByReleaseYear)
    elif(sortType == 2):
        print("Ordenando con Insertion Sort")
        sorted_list = sin.sort(sub_list, cmpMoviesByReleaseYear)
    elif(sortType == 3):
        print("Ordenando con Selection Sort")
        sorted_list = ssel.sort(sub_list, cmpMoviesByReleaseYear)
    elif(sortType == 4):
        print("Ordenando con Quick Sort")
        sorted_list = quick.sort(sub_list, cmpMoviesByReleaseYear)
    elif(sortType == 5):
        print("Ordenando con Merge Sort")
        sorted_list = merge.sort(sub_list, cmpMoviesByReleaseYear)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

# Tipo de ordenamiento elegido para las demas funciones: Merge Sort

# Funcion que ordena el contenido en base a su año de lanzamiento
def sortMoviesByReleaseYear(catalog):
    sub_list = lt.subList(catalog['movies'], 1, lt.size(catalog['movies']))
    start_time = getTime()
    print("Ordenando con Merge Sort")
    sorted_list = merge.sort(sub_list, cmpMoviesByReleaseYear)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time
  
# Funcion que ordena el contenido en base a su fecha de incorporación
def sortMoviesByDateAdded(catalog):
    sub_list = lt.subList(catalog['movies'], 1, lt.size(catalog['movies']))
    start_time = getTime()
    print("Ordenando con Merge Sort")
    sorted_list = merge.sort(sub_list, cmpMoviesByDateAdded)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

# Funcion que ordena el contenido en base a su nombre y duracion
def sortMoviesByName(catalog):
    sub_list = lt.subList(catalog['movies'], 1, lt.size(catalog['movies']))
    start_time = getTime()
    print("Ordenando con Merge Sort")
    sorted_list = merge.sort(sub_list, cmpMoviesByName)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

# Funcion que ordena el contenido en base a su nombre y director
def sortMoviesByName2(catalog):
    sub_list = lt.subList(catalog['movies'], 1, lt.size(catalog['movies']))
    start_time = getTime()
    print("Ordenando con Merge Sort")
    sorted_list = merge.sort(sub_list, cmpMoviesByName2)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def sortMoviesByName2(catalog):
    sub_list = lt.subList(catalog['movies'], 1, lt.size(catalog['movies']))
    start_time = getTime()
    print("Ordenando con Merge Sort")
    sorted_list = merge.sort(sub_list, cmpMoviesByName2)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def sortTop(lstTop):
    sub_list = lt.subList(lstTop, 1, lt.size(lstTop))
    print("Ordenando con Merge Sort")
    sorted_list = merge.sort(sub_list, cmpElemByCant)
    
    return sorted_list

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


# ----------------- Funciones de consulta -------------------

def getSampleMovies(catalog,cant):

    Movies = catalog['movies']
    SampleMovies = lt.newList()
    for cont in range(1,cant):
        movie = lt.getElement(Movies, cont)
        lt.addLast(SampleMovies, movie)
        
    return SampleMovies

def getMoviesByReleaseYear(lista,anoinicial,anofinal):
    nueva = lt.newList()
    for elem in range(0,lt.size(lista)):
        movie=lt.getElement(lista,elem)
        year=movie['release_year']
        if movie['type']=='Movie':
         if int(year)>=int(anoinicial) and int(year)<=int(anofinal):
          lt.addLast(nueva,movie)
    total=lt.size(nueva)

    return(total,nueva)

def getShowsByPeriod(lista,fechainicial,fechafinal):
     nueva = lt.newList()
     for elem in range(0,lt.size(lista)):
        movie=lt.getElement(lista,elem)
        fecha=movie['date_added']
        if fecha=='':
            fecha='1800-01-01'
        d1 = datetime.strptime(fecha, "%Y-%m-%d").date()
        d2 = datetime.strptime(fechainicial, "%Y-%m-%d").date()
        d3 = datetime.strptime(fechafinal, "%Y-%m-%d").date()
        if movie['type']=='TV Show':
            if (d1)>=(d2) and (d1)<=(d3):
                lt.addLast(nueva,movie)
     total=lt.size(nueva)

     return(total,nueva)

def getContentByCast(lista,actor):
    nueva = lt.newList()
    cant_movies=0
    cant_tvshow=0
    for elem in range(0,lt.size(lista)):
        movie=lt.getElement(lista,elem)
        actores=movie['cast']
        actor_temp=""
        index=0
        while (index < len(actores)):
            actor_temp=actor_temp+actores[index]
            if actores[index]==",":
                actor_temp=actor_temp[:-1]
                if actor_temp==actor:
                    lt.addLast(nueva,movie)
                    if movie['type']=='Movie':
                        cant_movies=cant_movies+1
                    else: cant_tvshow=cant_tvshow+1
                    break
                actor_temp=""
                index=index+1
            if index==len(actores)-1:
                if actor_temp==actor:
                    lt.addLast(nueva,movie)
                    if movie['type']=='Movie':
                        cant_movies=cant_movies+1
                    else: cant_tvshow=cant_tvshow+1
            index=index+1
    return(nueva,cant_movies,cant_tvshow)


def getShowsByCountry(lista,country):
     nueva = lt.newList()
     moviesCount=0
     showsCount=0
     for elem in range(0,lt.size(lista)):
        movie=lt.getElement(lista,elem)
        pais=movie['country']
        if country==pais:
          lt.addLast(nueva,movie)
          if movie['type']== 'Movie':
              moviesCount+=1
          if movie['type']== 'TV Show':
             showsCount+=1

     return(nueva, moviesCount, showsCount)

def getContentByDirector(lista,director):
    nueva = lt.newList()
    cant_movies=0
    cant_tvshow=0
    for elem in range(0,lt.size(lista)):
        movie=lt.getElement(lista,elem)
        directors=movie['director']
        director_temp=""
        index=0
        while (index < len(directors)):
            director_temp=director_temp+directors[index]
            if directors[index]==",":
                director_temp=director_temp[:-1]
                if director_temp==director:
                    lt.addLast(nueva,movie)
                    if movie['type']=='Movie':
                        cant_movies=cant_movies+1
                    else: cant_tvshow=cant_tvshow+1
                    break
                director_temp=""
                index=index+1
            if index==len(directors)-1:
                if director_temp==director:
                    lt.addLast(nueva,movie)
                    if movie['type']=='Movie':
                        cant_movies=cant_movies+1
                    else: cant_tvshow=cant_tvshow+1
            index=index+1
    return(nueva,cant_movies,cant_tvshow)

def getContentByGenero(lista,genero):
    movies = 0
    shows= 0
    todas = lt.newList()
    for elem in range(0,lt.size(lista)):
        movie=lt.getElement(lista,elem)
        tipo=movie['listed_in']
        tipos=tipo.split(', ')
        for elem in tipos:
            if elem==genero:
                lt.addLast(todas,movie)
                if movie['type']=='Movie':
                    movies+=1
                else:
                    shows+=1

    return (movies,shows,todas)

def getTopByGenero(catalog):
    top = lt.newList()
    for elem in range(0, lt.size(catalog['movies'])):
        movie=lt.getElement(catalog['movies'],elem)
        listedIn=movie['listed_in']
        tipos=listedIn.split(', ')
        for tipo in tipos:
            if(lt.size(top)>0):
                found = False
                for i in range(0, lt.size(top)):
                    gen=lt.getElement(top, i)
                    if(gen['genero']==tipo):
                        gen['cantidad']+=1
                        found = True
                        if movie['type']=='Movie':
                            gen['movies']+=1
                        elif movie['type']=='TV Show':
                            gen['shows']+=1
                        if movie['platform']=='Disney Plus':
                            gen['disney']+=1
                        elif movie['platform']=='Netflix':
                            gen['netflix']+=1
                        elif movie['platform']=='Hulu':
                            gen['hulu']+=1
                        elif movie['platform']=='Amazon Prime':
                            gen['amazon']+=1
                if(not found):
                    gen={'genero': tipo, 'cantidad': 1, 'movies':0,'shows':0,'amazon':0,'disney':0,'hulu':0,'netflix':0}
                    lt.addLast(top, gen)
                    if movie['type']=='Movie':
                        gen['movies']+=1
                    elif movie['type']=='TV Show':
                        gen['shows']+=1
                    if movie['platform']=='Disney Plus':
                        gen['disney']+=1
                    elif movie['platform']=='Netflix':
                        gen['netflix']+=1
                    elif movie['platform']=='Hulu':
                        gen['hulu']+=1
                    elif movie['platform']=='Amazon Prime':
                        gen['amazon']+=1
            else:
                gen = {'genero': tipo, 'cantidad': 1, 'movies':0,'shows':0,'amazon':0,'disney':0,'hulu':0,'netflix':0}
                lt.addLast(top, gen)
                if movie['type']=='Movie':
                    gen['movies']+=1
                elif movie['type']=='TV Show':
                    gen['shows']+=1
                if movie['platform']=='Disney Plus':
                    gen['disney']+=1
                elif movie['platform']=='Netflix':
                    gen['netflix']+=1
                elif movie['platform']=='Hulu':
                    gen['hulu']+=1
                elif movie['platform']=='Amazon Prime':
                    gen['amazon']+=1    
                    
    topOrd = sortTop(top)
   
    return (topOrd)

def getTopByActor(catalog):
    top = lt.newList()
    for elem in range(0, lt.size(catalog['movies'])):
        movie=lt.getElement(catalog['movies'],elem)
        cast=movie['cast']
        actores=cast.split(', ')
        for actor in actores:
            if(lt.size(top)>0):
                found = False
                for i in range(0, lt.size(top)):
                    act=lt.getElement(top, i)
                    if(act['actor']==actor):
                        act['cantidad']+=1
                        found = True
                        if movie['type']=='Movie':
                            act['movies']+=1
                        elif movie['type']=='TV Show':
                            act['shows']+=1
                        if movie['platform']=='Disney Plus':
                            act['disney']+=1
                        elif movie['platform']=='Netflix':
                            act['netflix']+=1
                        elif movie['platform']=='Hulu':
                            act['hulu']+=1
                        elif movie['platform']=='Amazon Prime':
                            act['amazon']+=1
                        if(movie['cast']!=''):
                            act['actores'].append(movie['cast'])
                        if(movie['director']!=''):
                            act['directores'].append(movie['director'])
                if(not found):
                    act={'actor': actor, 'cantidad': 1, 'movies':0,'shows':0,'amazon':0,'disney':0,'hulu':0,'netflix':0, 'actores': [], 'directores': []}
                    lt.addLast(top, act)
                    if movie['type']=='Movie':
                        act['movies']+=1
                    elif movie['type']=='TV Show':
                        act['shows']+=1
                    if movie['platform']=='Disney Plus':
                        act['disney']+=1
                    elif movie['platform']=='Netflix':
                        act['netflix']+=1
                    elif movie['platform']=='Hulu':
                        act['hulu']+=1
                    elif movie['platform']=='Amazon Prime':
                        act['amazon']+=1
                    if(movie['cast']!=''):
                        act['actores'].append(movie['cast'])
                    if(movie['director']!=''):
                        act['directores'].append(movie['director'])
            else:
                act = {'actor': actor, 'cantidad': 1, 'movies':0,'shows':0,'amazon':0,'disney':0,'hulu':0,'netflix':0, 'actores': [], 'directores': []}
                lt.addLast(top, act)
                if movie['type']=='Movie':
                    act['movies']+=1
                elif movie['type']=='TV Show':
                    act['shows']+=1
                if movie['platform']=='Disney Plus':
                    act['disney']+=1
                elif movie['platform']=='Netflix':
                    act['netflix']+=1
                elif movie['platform']=='Hulu':
                    act['hulu']+=1
                elif movie['platform']=='Amazon Prime':
                    act['amazon']+=1
                if(movie['cast']!=''):   
                    act['actores'].append(movie['cast'])
                if(movie['director']!=''):
                    act['directores'].append(movie['director']) 
                    
    topOrd = sortTop(top)
   
    return (topOrd)


# ------------- Funciones de comparacion -----------

def cmpMoviesByReleaseYear(movie1, movie2):
    if (float(movie1['release_year']) < float(movie2['release_year'])):
        return True
    elif(float(movie1['release_year']) == float(movie2['release_year'])):
        if ((movie1['title']) < (movie2['title'])):
            return True
        elif((movie1['title']) == (movie2['title'])):
            if((movie1['duration']) < (movie2['duration'])):
                return True
            else: 
                return False
        else:
            return False
    else:
        return False

def cmpMoviesByName(movie1, movie2):
    if ((movie1['title']) < (movie2['title'])):
        return True
    elif((movie1['title']) == (movie2['title'])):
        if (float(movie1['release_year']) < float(movie2['release_year'])):
            return True
        elif(float(movie1['release_year']) == float(movie2['release_year'])):
            if((movie1['duration']) < (movie2['duration'])):
                return True
            else: 
                return False
        else:
            return False
    else:
        return False
    
def cmpElemByCant(elem1, elem2):
    if ((elem1['cantidad']) > (elem2['cantidad'])):
        return True
    else:
        return False
    
def cmpMoviesByName2(movie1, movie2):
    if ((movie1['title']) < (movie2['title'])):
            return True
    elif((movie1['title']) == (movie2['title'])):
        if (float(movie1['release_year']) < float(movie2['release_year'])):
            return True
        elif(float(movie1['release_year']) == float(movie2['release_year'])):
            if((movie1['director']) < (movie2['director'])):
                return True
            else: 
                return False
        else:
            return False
    else:
        return False
    
def cmpMoviesByDateAdded(movie1, movie2):
    fecha1=movie1['date_added']
    fecha2=movie2['date_added']
    
    if fecha1== '':
        fecha1='1800-01-01'
    if fecha2=='':
        fecha2='1800-01-01'
    d1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
    d2 = datetime.strptime(fecha2, "%Y-%m-%d").date() 
       
    if d1<d2:
        return True
    elif d1 == d2:
        if ((movie1['title']) < (movie2['title'])):
            return True
        elif((movie1['title']) == (movie2['title'])):
            if((movie1['duration']) < (movie2['duration'])):
                return True
            else: 
                return False
        else:
            return False
    else:
        return False

