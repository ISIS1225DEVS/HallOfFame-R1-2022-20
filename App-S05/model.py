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

from itertools import count
from platform import platform
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import queue as qe
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
import time
import datetime
from tabulate import tabulate
from prettytable import PrettyTable as ptbl


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""



#! Construccion de modelos: Crean el catalogo con el que se va a trabajar, donde se tienen todas las listas de información


def newCatalog(listType):
    """
    
    Crea un catalogo de plataformas de Contenido 

    Args:
        listType (_type_): _description_

    Returns:
        _type_: _description_
    """    
    
    catalog = {"titles": None,
               "TV Show": None,
               "Movie": None, 
               "actors": None,
               "netflix": None,
               "hulu": None,
               "disney": None, 
               "amazon": None,
               "directors" : None,
               "genres" : None
               }
    
    catalog["titles"] = lt.newList(datastructure=listType, cmpfunction=cmpById)
    catalog["TV Show"] = lt.newList(datastructure=listType, cmpfunction=cmpById)
    catalog["Movie"] = lt.newList(datastructure=listType, cmpfunction=cmpById)
    catalog["netflix"] = lt.newList(datastructure=listType)
    catalog["hulu"] = lt.newList(datastructure=listType)
    catalog["disney_plus"] = lt.newList(datastructure=listType)
    catalog["amazon_prime"] = lt.newList(datastructure=listType)
    catalog["actors"] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpbyName)
    catalog["genres"] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpbyName)
    return catalog

# Funciones para agregar informacion al catalogo

def addContent(catalog, title, content):
    
    lt.addLast(catalog[content], title)
    
    return catalog
    
def addTitle(catalog, title, platform):
    
    lt.addLast(catalog["titles"], title)
    lt.addLast(catalog[platform], title)
        
    return catalog

def addActor(catalog, title):
    
    actors = title['cast']
    
    if actors != "Unknow":
        for person in actors:
            associated_cast = actors.copy()
            associated_cast.remove(person) 
            new_actor = newPerson(person, title['show_id'], title['type'], title["platform"], title['listed_in'], associated_cast, title['director'])
            lt.addLast(catalog['actors'], new_actor)
    else:
        new_actor = newPerson('Unknow', title['show_id'], title['type'], title["platform"], title['listed_in'], ['Unknow'], title['director'])
        lt.addLast(catalog['actors'], new_actor)
        
    return catalog


def loadContent(catalog, content):
    for title in lt.iterator(catalog["titles"]):
        if title["type"] == content:
            lt.addLast(catalog[content],title)
    return catalog

def organize_actor(actor_data):
    name = lt.getElement(actor_data, 1)['Name']
    
    actor = newActor(name)
    
    for element in lt.iterator(actor_data):
        lt.addLast(actor['content'], element['show_id'])
        
        for category in element['listed_in']:
            if lt.isEmpty(actor['categories']) == False:
                pos_category = lt.isPresent(actor['categories'], category)
            else:
                pos_category = 0
            if pos_category == 0:
                lt.addLast(actor['categories'], {'Name': category, 'count' : 1})
            else:
                category_count = lt.getElement(actor['categories'], pos_category)
                category_count['count'] += 1

        if element['platform'] == 'netflix':
            if element['type'] == 'Movie':
                actor['Movie'] +=1
                actor['netflix']['Movie'] += 1
            else:
                actor['netflix']['TV Show'] += 1
                actor['TV Show'] +=1
        elif element['platform'] == 'amazon_prime':
            if element['type'] == 'Movie':
                actor['Movie'] +=1
                actor['amazon_prime']['Movie'] += 1
            else:
                actor['amazon_prime']['TV Show'] += 1
                actor['TV Show'] +=1
        elif element['platform'] == 'disney_plus':
            if element['type'] == 'Movie':
                actor['Movie'] +=1
                actor['disney_plus']['Movie'] += 1
            else:
                actor['disney_plus']['TV Show'] += 1
                actor['TV Show'] +=1
        elif element['platform'] == 'hulu':
            if element['type'] == 'Movie':
                actor['Movie'] +=1
                actor['hulu']['Movie'] += 1
            else:
                actor['hulu']['TV Show'] += 1
                actor['TV Show'] +=1
        
        associated_cast = element['cast']
        if associated_cast != 'Unknow':
            actor['associated_cast'].extend(associated_cast)
        else:
            actor['associated_cast'].append(associated_cast)
            
        directors = element['directors']
        if directors != 'Unknow':
            actor['directors'].extend(directors)
        else:
            actor['directors'].append(directors)
        
    associated_cast = actor['associated_cast']
    directors = actor['directors']
    
    unique_cast = list(set(associated_cast))
    unique_directors = list(set(directors))
    
    actor['associated_cast'] = unique_cast
    actor['directors'] = unique_directors
        
    return actor    
        
def addGenre(catalog, title):

    for genre in title['listed_in']:
        new_Genre = newGenre(genre, title['type'], title['platform'], title['show_id'])
        lt.addLast(catalog['genres'], new_Genre)
    
    return catalog

# Funciones para creacion de datos


def newPerson(name, show_id, type, platform, listed_in, cast, directors):
    
    person = {"Name": name,
              'show_id': show_id,
              'type': type,
              'platform': platform,
              'listed_in': listed_in,
              'cast' : cast,
              'directors': directors}
    
    return person

def newActor(name):
    
    actor = {'Name': name,
             'content': None,
             'netflix' : None,
             'amazon_prime' : None,
             'disney_plus' : None,
             'hulu': None,
             'categories' : None,
             'associated_cast' : [],
             'directors' : [], 
             'Movie' : 0,
             'TV Show': 0
             }
    
    actor["content"] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpById)
    actor["categories"] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpbyName)
    actor['netflix'] = {'TV Show' : 0, 'Movie': 0}
    actor['amazon_prime'] = {'TV Show' : 0, 'Movie': 0}
    actor['disney_plus'] = {'TV Show' : 0, 'Movie': 0}
    actor['hulu'] = {'TV Show' : 0, 'Movie': 0}
    
    return actor

def strlstdivider(str):
    strlist = str
    if str != "Unknow":
        strlist = str.replace('Ph.D.,', 'Ph.D.')
        strlist = str.replace(", ", ",")
        strlist = strlist.split(",")
        strlist.sort()
        for name in strlist:
            if name == '':
                strlist.remove('')
        
    return strlist

def reform_title(title, platform):
    if title["country"] == "":
        
        title["country"] = "Unknow"
    
    if title["director"] == "":
        
        title["director"] = "Unknow"

    if title["cast"] == "":
        
        title["cast"] = "Unknow"
        
    id = title["show_id"][1::]
    id = int(id) 
    
    if platform == "netflix":
        title["show_id"] = int(10000 + id)
    elif platform == "amazon_prime":
        title["show_id"] = int(20000 + id)
    elif platform == "hulu":
        title["show_id"] = int(30000 + id)
    elif platform == "disney_plus":
        title["show_id"] = int(40000 + id)
        
    title["release_year"] = int(title["release_year"])
    
    if title['date_added'] == "":
        title['date_added'] =  '2021-01-01'
        
    title['date_added'] = datetime.datetime.strptime(title['date_added'], "%Y-%m-%d")
    return title

def newGenre(genre, kind, platform, id):

    genre = {"Name": genre,
             "type" : kind,
             "platform" : platform,
             "show_id" : id}
    
    return genre
    
#? Funciones de Busqueda


def linealSearch(sort_list, element, parameter):
    found = False
    pos = 1
    max_limit = lt.size(sort_list)
    while found == False and pos <= max_limit:
        if lt.getElement(sort_list, pos)[parameter] == element:
            found = True
        elif lt.getElement(sort_list, pos)[parameter] < element:
            if pos > 1:
                found = True
            else:
                pos = 1
                found = True
    
        else:
            pos += 1
    return pos
        

def binarySearch(sort_list, element, parameter):
    """
    Busqueda Binaria de un elemento en una lista ordenada ascendentemente
    Resultado: Indice en la lista donde se encuentra el elemento. -1 si no se encuentra.
    """
    i = 0
    f = lt.size(sort_list)
    pos = -1
    found = False
    while i <= f and not found:
        # calcular la posicion de la mitad entre i y f
        m = (i + f) // 2
        if lt.getElement(sort_list, m)[parameter] == element:
            pos = m
            found = True
        elif lt.getElement(sort_list, m)[parameter] > element:
            f = m - 1
        else:
            i = m + 1
    return pos

def binarySearchMin(sort_list, element, parameter):
    m = 0
    i = 0
    f = lt.size(sort_list)
    pos = -1
    found = False
    while i <= f and not found:
        m = (i + f) // 2
        if lt.getElement(sort_list, m)[parameter] == element:
            pos = m
            found = True
        elif lt.getElement(sort_list, m)[parameter] > element:
            f = m - 1
        else:
            i = m + 1
    if found == True:
        while lt.getElement(sort_list, pos - 1)[parameter] == element:
            pos -= 1
            if pos == 1:
                break
    elif lt.getElement(sort_list, m)[parameter] > element:
        pos = m
        if pos != 1 and pos != 0:
            while lt.getElement(sort_list, pos - 1)[parameter] > element:
                pos -= 1
                if pos == 1:
                    break 
    return pos

def binarySearchMax(sort_list, element, parameter):
    m = 0
    i = 0
    
    f = lt.size(sort_list)
    max_index = lt.size(sort_list)
    pos = -1
    found = False
    while i <= f and not found:
        m = (i + f) // 2
        if lt.getElement(sort_list, m)[parameter] == element:
            pos = m
            found = True
        elif lt.getElement(sort_list, m)[parameter] > element:
            f = m - 1
        else:
            i = m + 1
    if found == True and pos < max_index:
        if pos < max_index:
            while lt.getElement(sort_list, pos + 1)[parameter] == element:
                pos += 1
                if pos == max_index:
                    break
    elif lt.getElement(sort_list, m)[parameter] < element and pos < max_index:
        pos = m
        if pos < max_index:
            while lt.getElement(sort_list, pos + 1)[parameter] > element:
                pos += 1
                if pos == max_index:
                    break
    return pos + 1

#! Funciones de Consulta

def getMoviesbyYear(catalog, init_year, final_year):
    sort_movies, time = sortTitles_by_release_year(catalog, 'merge', 'Movie')
    init_pos = binarySearchMin(sort_movies, init_year, 'release_year')
    final_pos = binarySearchMax(sort_movies, final_year, 'release_year')
    if init_pos == 0:
        init_pos = 1
    cantidad = final_pos - init_pos
    answer_list = lt.subList(sort_movies, init_pos, cantidad)
    return answer_list

def getTvSHowsbydate(catalog, init_date, final_date):
    init_date = datetime.datetime.strptime(init_date, '%B %d, %Y')
    final_date = datetime.datetime.strptime(final_date, '%B %d, %Y')
    sort_TVShows = sortTV_ShowbyDate(catalog)
    init_pos = linealSearch(sort_TVShows, final_date, 'date_added')
    final_pos = linealSearch(sort_TVShows, init_date, 'date_added')
    cantidad = final_pos - init_pos 
    answer_list = lt.subList(sort_TVShows, init_pos, cantidad)
    return answer_list
    


def get_titles_by_country(catalog, countryname):

    sublist = lt.newList("SINGLE_LINKED", cmpMoviesbyTitle)
    origin_copy = lt.subList(catalog['titles'], 0, lt.size(catalog['titles']))

    tv_show_count = 0
    movie_count = 0
    for title in lt.iterator(origin_copy):
        if (countryname in title['country']) or (countryname.lower() in title['country'].lower()):
            lt.addLast(sublist, title)
            if title['type'] == "TV Show":
                tv_show_count += 1
            else:
                movie_count += 1
    
    sublist = sa.sort(sublist, cmpMoviesbyTitle)

    return sublist, movie_count, tv_show_count

def get_titles_by_director(catalog, directorname):

    sublist = lt.newList("SINGLE_LINKED", cmpMoviesByReleaseYear)
    origin_copy = lt.subList(catalog['titles'], 0, lt.size(catalog['titles']))

    tv_show_count = 0
    movie_count = 0
    netflix_count_movie= 0
    amazon_count_movie= 0
    hulu_count_movie= 0
    disney_count_movie= 0
    netflix_count_tv= 0
    amazon_count_tv= 0
    hulu_count_tv= 0
    disney_count_tv= 0
    for title in lt.iterator(origin_copy):
        for director_str in title["director"]:
            if (directorname in director_str):
                lt.addLast(sublist, title)
                if title['type'] == "TV Show":
                    tv_show_count += 1
                    if title["platform"]=="netflix":
                        netflix_count_tv +=1
                    elif title["platform"]=="hulu":
                        hulu_count_tv +=1
                    elif title["platform"]=="amazon_prime":
                        amazon_count_tv +=1
                    elif title["platform"]=="disney_plus":
                        disney_count_tv +=1
                else:
                    movie_count += 1
                    if title["platform"]=="netflix":
                        netflix_count_movie +=1
                    elif title["platform"]=="hulu":
                        hulu_count_movie +=1
                    elif title["platform"]=="amazon_prime":
                        amazon_count_movie +=1
                    elif title["platform"]=="disney_plus":
                        disney_count_movie +=1
    
    sublist = sa.sort(sublist, cmpMoviesByReleaseYear)
    #ACÁ SE CREA LA LISTA CON CADA PLATAFORMA Y SUS CONTADAS
    platforms_count = lt.newList("SINGLE_LINKED", cmpMoviesByReleaseYear)
    lt.addLast(platforms_count,{"platform":"Netflix","Movie":netflix_count_movie,"TV Shows":netflix_count_tv})
    lt.addLast(platforms_count,{"platform":"Hulu","Movie":hulu_count_movie,"TV Shows":hulu_count_tv})
    lt.addLast(platforms_count,{"platform":"Amazon Prime","Movie":amazon_count_movie,"TV Shows":amazon_count_tv})
    lt.addLast(platforms_count,{"platform":"Disney Plus","Movie":disney_count_movie,"TV Shows":disney_count_tv})
    
    #creación de LINKEDLIST de diccionarios con el listed in y veces que se reitera
    listedin_count = lt.newList("SINGLE_LINKED", cmpMoviesByReleaseYear)
    for title in lt.iterator(sublist):
        for genero in title["listed_in"]:
            if lt.isEmpty(listedin_count):
                lt.addLast(listedin_count,{"listed in":genero,"count":1})
            else:
                for dict_genero_listadito in lt.iterator(listedin_count):
                    existe=False
                    if genero == dict_genero_listadito["listed in"]:
                        existe=True
                        cuenta_nueva = dict_genero_listadito["count"] + 1
                        dict_genero_listadito["count"] = cuenta_nueva
                if not(existe):
                    lt.addLast(listedin_count,{"listed in":genero,"count":1})
    return sublist, movie_count,tv_show_count, platforms_count,listedin_count

def get_titles_by_genre(catalog, genrename):

    sublist = lt.newList("SINGLE_LINKED", cmpGenres)
    origin = lt.subList(catalog['titles'], 0, lt.size(catalog['titles']))

    tv_show_count = 0
    movie_count = 0

    for title in lt.iterator(origin):
        if genrename in title['listed_in']:           
            lt.addLast(sublist, title)
            if title['type'] == "TV Show":
                tv_show_count += 1
            else:
                movie_count += 1

    sublist = sa.sort(sublist, cmpGenres)

    return sublist, movie_count, tv_show_count

def getTopActors(catalog, topSize):

    sort_Actors = catalog['actors']   
    actor_data = lt.getElement(sort_Actors, 1)
    actor_name = actor_data['Name']
    
    actor_info = {"Name": actor_name,
                  "count": 0}
    
    top_actors = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpbyName)
    
    for actor in lt.iterator(sort_Actors): #! -> O(n)
        if actor_name == actor["Name"]:
            actor_info['count'] += 1
        else:
            lt.addLast(top_actors,actor_info)
            actor_name = actor["Name"]
            actor_info = {"Name" : actor_name, "count": 1}
            
    
    top_actors, time = merge_sort(top_actors, cmp_function=cmpActorsbyCount) #! -> O(nlogn)
    size = lt.size(top_actors) + 1
    top_actors = lt.subList(top_actors, 1, topSize)
    datatop = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=cmpbyName)
    for actor in lt.iterator(top_actors): #! -> O(n)
        actor_name = actor['Name']
        data_actor = getActorData(catalog, actor_name) #-> O(logn)
        top_listed_in, time = shell_sort(data_actor['categories'], cmpActorsbyCount)
        top_listed_in = lt.getElement(top_listed_in, 1)
        data_actor['top_listed_in'] = top_listed_in
        data_actor['count'] = actor['count']
        lt.addLast(datatop, data_actor)
    return datatop, size

    

def getActorData(catalog, actor_name):
    
    actors = catalog['actors']
    
    pos_inicial = binarySearchMin(actors, actor_name, 'Name') #!-> O(logn)
    pos_final = binarySearchMax(actors, actor_name, 'Name') #! -> O(logn)
    
    count = pos_final - pos_inicial
    actor_data = lt.subList(actors, pos_inicial, count)
    
    actor = organize_actor(actor_data) 
    
    return actor


def getMoviesInfo(ids, catalog):
    sort_titles, time = merge_sort(catalog['titles'], cmp_function=cmpTitlesbyId) 
    shows = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpById)
    
    for id in lt.iterator(ids):
        
        pos = binarySearch(sort_titles, id, 'show_id')
        
        show = lt.getElement(sort_titles, pos)

        lt.addLast(shows, show)
    
    sorted_shows, time = quick_sort(shows, cmpMoviesbyTitle) 

    return sorted_shows      
    

def getTopGenres(catalog, topSize):

    sortedGenres, time = merge_sort(catalog["genres"], cmpPersonbyName)
    genreData = lt.getElement(sortedGenres, 1)
    genreName = genreData['Name']

    genreInfo = {"Name" : genreData['Name'],
                 "count" : 0,
                 "Movie" : 0,
                 "TV Show" : 0,
                 "amazon_prime" : 0,
                 "netflix" : 0,
                 "hulu" : 0,
                 "disney_plus" : 0}

    topGenres = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=cmpbyName)

    for genre in lt.iterator(sortedGenres):
        if genreName == genre['Name']:
            genreInfo['count'] += 1
            genreInfo[genre['type']] += 1
            genreInfo[genre['platform']] += 1
        else:
            lt.addLast(topGenres, genreInfo)
            genreName = genre['Name']
            genreInfo = {"Name" : genre['Name'],
                         "count" : 1,
                         "Movie" : 0,
                         "TV Show" : 0,
                         "amazon_prime" : 0,
                         "netflix" : 0,
                         "hulu" : 0,
                         "disney_plus" : 0}
            genreInfo[genre['type']] += 1
            genreInfo[genre['platform']] += 1
    
    topGenres, time = merge_sort(topGenres, cmp_function=cmpActorsbyCount)

    return lt.subList(topGenres, 1, topSize)
     
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpById(title1, title2):
    """

    Args:
        release_year1 (_type_): _description_
        title (_type_): _description_

    Returns:
        _type_: _description_
    """
    if int(title1["show_id"]) == int(title2["show_id"]):
        return 0 
    elif int(title1["show_id"]) > int(title2["show_id"]):
        return 1
    else: 
        return -1

def cmpbyName(actor1, actor2):
    
    if actor1 == actor2['Name']:
        return 0
    elif actor1 > actor2["Name"]:
        return 1
    else:
        return -1
    
#Funciones Utilizadas para Comparar elementos en Algoritmos de Ordenamiento

def cmpMoviesByReleaseYear(movie1, movie2):
    """
    Debuelve verdadero (True) si el release_year de movie1 son menores que los
    de movie2, en caso de que sean iguales tenga en cuenta el titulo y en caso
    de que ambos criterios sean iguales tenga en cuenta la duración, de lo contrario
    devuelva falso (False)
    Args:
        movie1 : información de la primera película que incluye sus valores "release year",
        "title", y "duration" 
        movie2 : información de la segunda película que incluye sus valores "release year",
        "title", y "duration"

    Returns:
        _type_: True or False
    """    
    
    #TODO Implementación de laboratorio 4
    
    if movie1["release_year"] == movie2["release_year"]:
        if movie1["title"] == movie2["title"]:
            if movie1["duration"] > movie2["duration"]:
                return False
            else:
                return True
        elif movie1["title"] > movie2["title"]:
            return False
        else:
            return True
        
    elif movie1["release_year"] > movie2["release_year"]:
        return False
    
    else:
        return True
    
def cmpMoviesbyTitle(movie1, movie2):
    
    if movie1['title'] == movie2["title"]:
        if movie1['release_year'] == movie2['release_year']:     
            if movie1["duration"] > movie2["duration"]:
                return False
            else:
                return True
        elif movie1['release_year'] > movie2['release_year']:
            return False
        else:
            return True
    elif movie1["title"] > movie2["title"]:
        return False
    else:
        return True 
    
def cmpPersonbyName(person1, person2):
    if person1["Name"] ==  person2["Name"]:
        if person1["show_id"] > person2["show_id"]:
            return False
        else:
            return True
    elif person1["Name"] > person2["Name"]:
        return False
    else:
        return True

def cmpTitlesbyTitlesReleaseDirector(title1, title2):

    if title1['title'] == title2['title']:
        if title1['release_year'] == title2['release_year']:
            if title1['director'] > title2['director']:
                return False
            else:
                return True
        else:
            return cmpMoviesbyTitle(title1, title2)
    else:
        return cmpMoviesbyTitle(title1, title2)
    
def cmpActorsbyCount(actor1, actor2):
    
    if actor1['count'] == actor2['count']:
        if actor1['Name'] > actor2['Name']:
            return False
        else:
            return True
    elif actor1['count'] > actor2["count"]:
        return True
    else:
        return False
    
def cmpTitlesbyId(title1, title2):
    
    return title1['show_id'] < title2['show_id']

def cmpTV_ShowbyDate(title1, title2):
    
    if title1['date_added'] == title2['date_added']:
        if title1['title'] == title2['title']:
            if title1['duration'] > title2['duration']:
                return True
            else:
                return False
        elif title1['title'] > title2['title']:
            return True
        else:
            return False
    elif title1['date_added'] > title2['date_added']:
        return True
    else:
        return False

def cmpGenres(title1, title2):

    if title1['title'] == title2['title']:
        if title1['release_year'] == title2['release_year']:
            if title1['director'][0] > title2['director'][0]:
                return False
            else:
                return True
        else:
            return cmpMoviesbyTitle(title1, title2)
    else:
        return cmpMoviesbyTitle(title1, title2)

# Funciones de ordenamiento

def sortTitles_by_release_year(catalog, algorithm, type):
    """
    
    Ordena los Shows por Año de lanzamiento

    Args:
        catalog (_type_): Catalogo de Shows
        algorithm (_type_): Algoritmo de Ordenamiento  a utilizar

    """    

    titles = lt.subList(catalog[type], 1, lt.size(catalog[type]))
    
    if algorithm == "shell":
        sort_titles, time= shell_sort(titles, cmp_function=cmpMoviesByReleaseYear)
    elif algorithm == "selection":
        sort_titles, time= selection_sort(titles, cmp_function=cmpMoviesByReleaseYear)
    elif algorithm == "insertion":
        sort_titles, time= insertion_sort(titles, cmpfunction=cmpMoviesByReleaseYear)
    elif algorithm == "quick":
        sort_titles, time= quick_sort(titles, cmp_function=cmpMoviesByReleaseYear)
    elif algorithm == "merge":
        sort_titles, time= merge_sort(titles, cmp_function=cmpMoviesByReleaseYear)
        
    return sort_titles, time
        
def sortTitles_by_title(catalog, list):
    
    titles = lt.subList(catalog[list], 1, lt.size(catalog[list]))
    
    sort_list, time = merge_sort(titles, cmpMoviesbyTitle)

    return sort_list, time

def sortTV_ShowbyDate(catalog):
    TV_Show = lt.subList(catalog['TV Show'], 1, lt.size(catalog['TV Show']))
    
    sort_list, time = merge_sort(TV_Show, cmpTV_ShowbyDate)
    
    return sort_list

def sortActors(catalog):
    
    catalog['actors'], time_sort = merge_sort(catalog['actors'], cmp_function= cmpPersonbyName)
    
    return catalog


#?Algoritmos de Ordenamiento

def shell_sort(list, cmp_function):
    """
    Implementa el algoritmo de shell_sort para 

    Args:
        catalog (_type_): _description_

    Returns:
        _type_: _description_
    """ 
    
    start_time = getTime()
    sorted_list = sa.sort(list, cmp_function)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def insertion_sort (list, cmpfunction):
    sub_list = list
    start_time = getTime()
    sorted_list = ins.sort(sub_list, cmpfunction)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sorted_list, delta_time

def selection_sort(list,cmp_function):
    start_time = getTime()
    sorted_list = ss.sort(list,cmp_function)
    end_time = getTime()
    delta_time = deltaTime(start_time,end_time)
    return sorted_list,delta_time

def quick_sort(list, cmp_function):
    start_time = getTime()
    sorted_list = qs.sort(list,cmp_function)
    end_time = getTime()
    delta_time = deltaTime(start_time,end_time)
    return sorted_list,delta_time    

def merge_sort(list, cmp_function):
    start_time = getTime()
    sorted_list = ms.sort(list,cmp_function)
    end_time = getTime()
    delta_time = deltaTime(start_time,end_time)
    return sorted_list,delta_time        


#?Funciones Calculos: Ayudan para la realización de Calculos para los Analisis

def getTime():
    """
    Devuelve el tiempo en el instante que se llama la función
    

    Returns:
        _type_: Instante de Tiempo 
    """    
    
    return float(time.perf_counter()*1000)

def deltaTime(start, end):
    """
    Retorna la difre

    Args:
        start (_type_): _description_
        end (_type_): _description_

    Returns:
        _type_: _description_
    """    
    
    
    return float(end - start)


#? Funciones de Visualización
def FirstandLast(list, count, columns):
    
    table = ptbl()
    size = lt.size(list)
    table.field_names = columns
    table.max_width = 35
    first = lt.subList(list, 1, count)
    last = lt.subList(list, (size-count+1), count)
    
    for i in range(1, count+1):
        
        data = lt.getElement(first, i)
        rows = []
        
        for n in range(0, len(columns)):
            rows.append(data[columns[n]])
        table.add_row(rows)
        
    for i in range(1, count+1):
        
        data = lt.getElement(last, i)
        rows = []
        
        for n in range(0, len(columns)):
            rows.append(data[columns[n]])
        table.add_row(rows)
        table.hrules = True
    
    return table

def platforms_size(catalog):
    
    table = ptbl()
    
    table.field_names = ["Sevice Name", "Count"]
    
    table.add_row(["Netflix", lt.size(catalog["netflix"])])
    table.add_row(["Hulu", lt.size(catalog["hulu"])])
    table.add_row(["Disney +", lt.size(catalog["disney_plus"])])
    table.add_row(["Amazon Prime", lt.size(catalog["amazon_prime"])])

    return table


def simplePrettyTable(list, columns):
    table = ptbl()
    table.field_names = columns
    table.max_width = 30
    for element in lt.iterator(list):
        rows = []
        for n in range(0, len(columns)):
            rows.append(element[columns[n]])
        table.add_row(rows)
    table.hrules = True
        
    return table

def countTable(columns, counts, titles):
    table = ptbl()
    
    table.field_names = columns
    
    for i in range(0, len(titles)):
        
        row = [titles[i], counts[i]]
        table.add_row(row)
        
    return table

def visalRq8(list):
    
    table_count = ptbl()
    table_count.field_names = ['actor', 'count', 'top_listed_in']
    table_content = ptbl()
    table_content.field_names = ['Rank', 'Actor', 'Content_Type']
    table_content.align['Content_Type'] = 'l'
    table_cast_info = []
    table_directors_info = []
    count = 1
    
    for actor in lt.iterator(list):
        row = [actor['Name'], lt.size(actor['content']), actor['top_listed_in']['Name']]
        table_count.add_row(row)
        row2 = []
        row2.append(count)
        row2.append(actor['Name'])
        content_type = 'Count\nStream Service Type'
        Netflix = '\nNetflix        TV Show  {0} \n               Movie    {1}'.format(actor['netflix']['TV Show'], actor['netflix']['Movie'])
        Amazon  = '\nAmazon         TV Show  {0} \n               Movie    {1}'.format(actor['amazon_prime']['TV Show'], actor['amazon_prime']['Movie'])
        Disney  = '\nDisney         TV Show  {0} \n               Movie    {1}'.format(actor['disney_plus']['TV Show'], actor['disney_plus']['Movie'])
        Hulu    = '\nHulu           TV Show  {0} \n               Movie    {1}'.format(actor['hulu']['TV Show'], actor['hulu']['Movie'])
        content_type += Netflix + Amazon + Disney + Hulu
        row2.append(content_type)
        table_content.add_row(row2)
        cast_associated = actor['associated_cast']
        cast_associated.sort()
        cast_associated = ', '.join(cast_associated)
        if len(cast_associated) > 900:
            cast_associated = cast_associated[0:900]
        row3 = [count, actor['Name'], cast_associated]
        table_cast_info.append(row3)
        directors = actor['directors']
        directors.sort()
        directors = ', '.join(directors)
        if len(directors) > 900:
            directors = directors[0:900]
        row4 = [count, actor['Name'], directors]
        table_directors_info.append(row4)
        count += 1 
    
    table_cast = tabulate(table_cast_info, headers=['Rank', 'Actor', 'Colaborations'], tablefmt='grid', maxcolwidths=[10,20,180])
    table_directors = tabulate(table_directors_info, headers=['Rank', 'Actor', 'Directors'], tablefmt='grid', maxcolwidths=[10,20,180])
    return table_count, table_content, table_cast, table_directors

        
        
def topGenresTable(list, columns):
    table = ptbl()
    table.title = 'Top {0} géneros con más contenido'.format(lt.size(list))
    table.field_names = columns
    table.align['listed_in'] = 'l'
    table.align['type'] = 'l'
    table.align['stream_service'] = 'l'
    table.align['count'] = 'r'

    rank = 1

    for genre in lt.iterator(list):     
        row = []
        row.append(rank)
        row.append(genre['Name'])
        row.append(genre['count'])
        row.append("count type:\nMovie: {0}\nTV Show: {1}".format(genre['Movie'], genre['TV Show']))
        row.append("count stream service:\namazon: {0}\nnetflix: {1}\nhulu: {2}\ndisney: {3}".format(genre['amazon_prime'], genre['netflix'], genre['hulu'], genre['disney_plus']))
        table.add_row(row)
        table.hrules = True
        rank += 1
    
    return table

def topGenresLittleTable (list, columns):
    table = ptbl()   
    table.field_names = columns
    table.align['listed_in'] = 'l'
    table.align['count'] = 'r'
    for genre in lt.iterator(list):     
        row = []        
        row.append(genre['Name'])
        row.append(genre['count'])
        table.add_row(row)
        table.hrules = True
    return table
    
# %%
