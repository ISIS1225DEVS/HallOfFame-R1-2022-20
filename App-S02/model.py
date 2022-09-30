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

import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(ListType):
    catalog = {'amazon_prime': None,
               'netflix': None,
               'disney_plus': None,
               'hulu': None}

    catalog['amazon_prime'] = lt.newList(ListType)
    catalog['netflix'] = lt.newList(ListType)
    catalog['disney_plus'] = lt.newList(ListType)
    catalog['hulu'] = lt.newList(ListType)

    return catalog

# Funciones para agregar informacion al catalogo
def addContent(catalog, content,streaming_platform):
    for key in content:
        if content[key] == "":
            content[key] = "unknown"
    platform = catalog[streaming_platform]
    lt.addLast(platform, content)
    return catalog

def StreamingSize(catalog,streaming_platform):
    return lt.size(catalog[streaming_platform])

def firstThree(catalog,streamingService):
    streaming_list = catalog[streamingService] 
    sublist = lt.subList(streaming_list,1,3)
    return sublist
def lastThree(catalog,streamingService):
    streaming_list = catalog[streamingService]
    sublist = lt.subList(streaming_list,(lt.size(streaming_list)-2),3)
    return sublist
def firstandlast3(catalog,streamingService):
    list = lt.newList()
    first = firstThree(catalog,streamingService)
    last = lastThree(catalog,streamingService)
    for i in lt.iterator(first):
        lt.addLast(list,i)
    for i in lt.iterator(last):
        lt.addLast(list,i)
    return list
def sortbydate(catalog,algorithm,ListType):
    start_time = getTime()
    movie_list = lt.newList(ListType)
    for i in (catalog):
        for e in lt.iterator(catalog[i]):
            if e["type"] == "Movie":
                lt.addLast(movie_list,e)
    start_time = getTime()
    if algorithm == 0:
        sorted_catalog = {"amazon_prime":se.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear),
            "netflix":se.sort(catalog["netflix"],cmpMoviesByReleaseYear),
            "disney_plus":se.sort(catalog["disney_plus"],cmpMoviesByReleaseYear),
            "hulu":se.sort(catalog["hulu"],cmpMoviesByReleaseYear)}
        end_time = getTime()
    elif algorithm == 1:
        sorted_catalog = {"amazon_prime":ins.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear),
            "netflix":ins.sort(catalog["netflix"],cmpMoviesByReleaseYear),
            "disney_plus":ins.sort(catalog["disney_plus"],cmpMoviesByReleaseYear),
            "hulu":ins.sort(catalog["hulu"],cmpMoviesByReleaseYear)}
        end_time = getTime()
    elif algorithm == 2:
        sorted_catalog = {"amazon_prime":sa.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear),
            "netflix":sa.sort(catalog["netflix"],cmpMoviesByReleaseYear),
            "disney_plus":sa.sort(catalog["disney_plus"],cmpMoviesByReleaseYear),
            "hulu":sa.sort(catalog["hulu"],cmpMoviesByReleaseYear)}
        end_time = getTime()
    elif algorithm == 3:
        sorted_catalog  = merg.sort(movie_list,cmpMoviesByReleaseYear)
        end_time = getTime()
    elif algorithm == 4:
        sorted_catalog = quk.sort(movie_list,cmpMoviesByReleaseYear)
        end_time = getTime()
    return sorted_catalog,deltaTime(start_time,end_time)
def cmpMoviesByReleaseYear(movie1, movie2):
    """
    Devuelve verdadero (True) si el release_year de movie1 son menores que los
    de movie2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que
    ambos criterios sean iguales tenga en cuenta la duración, de lo contrario devuelva
    falso (False).
    Args:
    movie1: informacion de la primera pelicula que incluye sus valores 'release_year',
    ‘title’ y ‘duration’
    movie2: informacion de la segunda pelicula que incluye su valor 'release_year', 
    ‘title’ y ‘duration’
    """
    if movie1["release_year"] < movie2["release_year"]:
        return True
    if movie1["release_year"] == movie2["release_year"]:
        if movie1["title"] < movie2["title"]:
            return True
        elif movie1["title"] == movie2["title"]:
            if movie1["duration"] < movie2["duration"]:
                return True
    else:
        return False

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
def ReqsTimeCounts(catalog):
    times = lt.newList()
    time1 = getTime()
    TitlesByYear(catalog,"1920","1999")#req1
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    time1 = getTime()
    TitleByTime(catalog,"2018-01-07","2020-12-31")#req2
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    time1 = getTime()
    TitlesByActor("Sissy Spacek",catalog)#req3
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    time1 = getTime()
    genero("Fantasy",catalog)
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    time1 = getTime()
    producedAt(catalog,"Colombia")#req5
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    time1 = getTime()
    TitlesByDirector(catalog,"John Hughes")#req6
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    time1 = getTime()
    topGenres(catalog,"7")#req7
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    time1 = getTime()
    ActorTop(catalog,"7")#req8
    time2 = getTime()
    lt.addLast(times,round(deltaTime(time1,time2),5))
    return times
def TitlesByYear(catalog,first_year,last_year): #Función Principal Requerimiento 1
    titlesList = lt.newList()
    for stream in catalog:
        for title in lt.iterator(catalog[stream]):
            if (title["release_year"] != "unknown") and (title["type"] == "Movie"):
                if int(title["release_year"]) >= int(first_year) and int(title["release_year"]) <= int(last_year):
                    title["streaming_service"] = stream
                    lt.addLast(titlesList,title)
    merg.sort(titlesList,cmpyear)
    return titlesList
def cmpyear(title1,title2): #Función Auxiliar Requerimiento 1
    if title1["release_year"] < title2["release_year"]:
        return True
    elif title1["release_year"] == title2["release_year"]:
        if title1["title"] < title2["title"]:
            return True
    else:
        return False
def TitleByTime(catalog,firstDate,LastDate):#Función Principal Requerimiento 2
    returnlist = lt.newList()
    for streaming_platform in catalog:
        for title in lt.iterator(catalog[streaming_platform]):
            if (title["date_added"] != "unknown") and (title["type"] == "TV Show"):
                if DateCompare(title["date_added"],firstDate,LastDate) == True:
                    title["streaming_service"] = streaming_platform
                    lt.addLast(returnlist,title)
    merg.sort(returnlist, comparedate)
    return lt.size(returnlist),returnlist
def DateCompare(date,firstDate,LastDate): #Función Auxiliar Requerimiento 2
    date__ = time.strptime(date, "%Y-%m-%d")
    firstDate_ = time.strptime(firstDate, "%Y-%m-%d")
    LastDate_ = time.strptime(LastDate, "%Y-%m-%d")

    if date__ <= LastDate_ and date__ >= firstDate_:
        return True
    else:
        return False
def comparedate(pelicula1, pelicula2): #CMP Function para requerimiento 2

    fecha1 = str(pelicula1["date_added"])
    fecha2 = str(pelicula2["date_added"])

    fechadatetime1 = time.strptime(fecha1, "%Y-%m-%d")
    fechadatetime2 = time.strptime(fecha2, "%Y-%m-%d")

    if fechadatetime1 > fechadatetime2:
        return True
    if fechadatetime1 == fechadatetime2:
        return False
def TitlesByActor(actor,catalog): #Función Principal Requerimiento 3
    TV_count = 0
    Movie_count = 0
    titles = lt.newList()
    for streaming_service in catalog:
        for title in lt.iterator(catalog[streaming_service]):
            if (title["cast"] != "") and (actor in title["cast"]):
                if title["type"] == "Movie":
                    Movie_count += 1
                else:
                    TV_count += 1
                title["streaming_platform"] = streaming_service
                title["cast"] = title["cast"].strip()
                lt.addLast(titles,title)
    merg.sort(titles,ActorCompare)
    return titles,TV_count,Movie_count
def ActorCompare(title1,title2): #Función Auxiliar Requerimiento 3
    if title1["title"] < title2["title"]:
        return True
    elif title1["title"] == title2["title"]:
        if title1["release_year"] < title2["release_year"]:
            return True
        elif title1["release_year"] == title2["release_year"]:
            if title1["director"] < title2["director"]:
                return True
    else:
        return False
def genero(generos, catalog): #principal req 4 
    contadortv = 0
    contadorpelicula = 0
    generoscu = lt.newList()
    for streaming_service in catalog:
        for title in lt.iterator(catalog[streaming_service]):
            if (title["listed_in"] != "" ) and (generos in title["listed_in"]):
                if title["type"] == "Movie":
                    contadorpelicula += 1
                else:
                    contadortv += 1
                title["streaming_platform"] = streaming_service
                title["listed_in"] = title["listed_in"].strip()
                lt.addLast(generoscu,title)
    merg.sort(generoscu,cmpgen)
    return generoscu, contadortv, contadorpelicula
    
def cmpgen(title1,title2): #aux req 4 
    if title1["title"] < title2["title"]:
        return True
    elif title1["title"] == title2["title"]:
        if title1["release_year"] < title2["release_year"]:
            return True
        elif title1["release_year"] == title2["release_year"]:
            if title1["director"] < title2["director"]:
                return True
    else:
        return False



#Req 5
def producedAt(catalog,country): #Principal req 5
    movies = 0
    TV_Shows = 0

    country_catalog = lt.newList()
    for streaming in catalog:
        for title in lt.iterator(catalog[streaming]):
            title["streaming_platform"] = streaming
            for on_country in title["country"].split(","):
                on_country = on_country.strip()
                if country in on_country:
                    lt.addLast(country_catalog, title)
                    if title['type'] == 'Movie':
                        movies += 1
                    else:
                        TV_Shows += 1
    merg.sort(country_catalog,cmpCountry)

    return movies,TV_Shows,country_catalog

def cmpCountry(title1,title2): # Auxiliar req 5
    if title1["release_year"] < title2["release_year"]:
        return True
    elif title1["release_year"] == title2["release_year"]:
        if title1["title"] < title2["title"]:
            return True
        elif title1["title"] == title2["title"]:
            title1["director"] < title2["director"]
    else:
        return False
    
def TitlesByDirector(catalog,director): #Función Principal Requerimiento 6
    type_count = {}
    streaming_count = {}
    listed_in_count = {}
    directorTitles = lt.newList()
    for streaming in catalog:
        for title in lt.iterator(catalog[streaming]):
            for i_dic in title["director"].split(","):
                i_dic = i_dic.strip()
                if i_dic == director:
                    if title["type"] not in type_count:
                        type_count[title["type"]] = 1
                    else:
                        type_count[title["type"]] += 1
                    title["streaming_platform"] = streaming
                    if title["streaming_platform"] not in streaming_count:
                        streaming_count[title["streaming_platform"]] = {"Movie":0,"TV Show":0}
                        streaming_count[title["streaming_platform"]][title["type"]] += 1
                    else:
                        streaming_count[title["streaming_platform"]][title["type"]] += 1
                    for genre in title["listed_in"].split(","):
                        genre = genre.strip()
                        if genre not in listed_in_count:
                            listed_in_count[genre] = 1
                        else:
                            listed_in_count[genre] += 1
                    lt.addLast(directorTitles,title)
    merg.sort(directorTitles,cmpTitlesByDirector)
    return directorTitles,type_count,streaming_count,listed_in_count
def cmpTitlesByDirector(title1,title2): #CMP function requerimiento 6
    if title1["release_year"] < title2["release_year"]:
        return True
    elif title1["release_year"] == title2["release_year"]:
        if title1["title"] < title2["title"]:
            return True
        elif title1["title"] == title2["title"]:
            title1["duration"] < title2["duration"]
    else:
        return False
#Req 7

def topGenres(catalog,TopN): # Principal Top Generos
    genres_dict = {}
    top_genres = lt.newList()
    top_Num = lt.newList()
    for streaming in catalog:
        for title in lt.iterator(catalog[streaming]):
            title["streaming_platform"] = streaming
            for genre in title["listed_in"].split(","):
                genre = genre.strip()
                if genre not in genres_dict:
                    genres_dict[genre] = lt.newList()
                    lt.addLast(genres_dict[genre],title)
                else:
                    lt.addLast(genres_dict[genre],title)
    i = 0
    while i < int(TopN):
        max_ = None
        genreName = None
        for key in genres_dict:
            if max_ == None:
                genreName = key
                max_ = genres_dict[key]
            elif lt.size(genres_dict[key]) > lt.size(max_):
                genreName = key
                max_ = genres_dict[key]
        genres_dict.pop(genreName)
        lt.addLast(top_genres,{"listed_in": genreName,"titles": max_})
        i += 1
    for elems in lt.iterator(top_genres):
        lt.addLast(top_Num,topGenresInPlatform(elems))
    return top_Num, len(genres_dict)

def topGenresInPlatform(dict_): # Auxiliar Top Generos
    type_counter = {}
    streaming_counter = {}
    for title in lt.iterator(dict_['titles']):
        if title["type"] not in type_counter:
            type_counter[title["type"]] = 1
        else:
            type_counter[title["type"]] += 1
        if title['streaming_platform'] not in streaming_counter:
            streaming_counter[title['streaming_platform']] = 1
        else:
            streaming_counter[title['streaming_platform']] += 1

    
    return dict_['listed_in'],type_counter,streaming_counter,lt.size(dict_['titles'])

def ActorTop(catalog,N): #Función Principal Requerimiento 8
    actor_dict = {}
    top_actors = lt.newList()
    top_N = lt.newList()
    for stream in catalog:
        for title in lt.iterator(catalog[stream]):
            title["streaming_platform"] = stream
            for cast in title["cast"].split(","):
                cast = cast.strip()
                if cast not in actor_dict:
                    actor_dict[cast] = lt.newList()
                    lt.addLast(actor_dict[cast],title)
                else:
                    lt.addLast(actor_dict[cast],title)
    i = 0
    while i < int(N):
        max_ = None
        name = None
        for key in actor_dict:
            if max_ == None:
                name = key
                max_ = actor_dict[key]
            elif lt.size(actor_dict[key]) > lt.size(max_):
                name = key
                max_ = actor_dict[key]
        actor_dict.pop(name)
        lt.addLast(top_actors,{"name":name,"titles":max_})
        i += 1
    for i in lt.iterator(top_actors):
        lt.addLast(top_N,TopActorPropierties(i))
    return top_N,len(actor_dict)
def TopActorPropierties(actor_dict): #Función Auxiliar Requerimiento 8 

    titles = actor_dict["titles"]
    colaborations = lt.newList()
    stream_show_tvCount = {}
    genre_count = {}
    for i in lt.iterator(titles):
        if i["streaming_platform"] not in stream_show_tvCount:
            stream_show_tvCount[i["streaming_platform"]] = {"Movie":0,"TV Show":0}
            stream_show_tvCount[i["streaming_platform"]][i["type"]] += 1
        else:
            stream_show_tvCount[i["streaming_platform"]][i["type"]] += 1
        for genre in i["listed_in"].split(","):
            if genre not in genre_count:
                genre_count[genre] = 1
            else:
                genre_count[genre] += 1
        if actor_dict["name"] != "unknown":
            for colleague in i["cast"].split(","):
                colleague = colleague.strip()
                if (colleague != actor_dict["name"].strip()) and (lt.isPresent(colaborations,colleague) == 0):
                    lt.addLast(colaborations,colleague)
            for colleague in i["director"].split(","):
                colleague = colleague.strip()
                if lt.isPresent(colaborations,colleague) == 0:
                    lt.addLast(colaborations,colleague)
    if actor_dict["name"] == "unknown":
        lt.addLast(colaborations,"Unknown")
    merg.sort(colaborations,sortAlphabet)
    return actor_dict["name"],colaborations,stream_show_tvCount,maxKey(genre_count),lt.size(titles)
def sortAlphabet(item1,item2): #CMP Function Requerimiento 8 
    if item1 < item2:
        return True
    else:
        return False
def maxKey(dict): #Función Auxiliar Requerimiento 8 
    max_ = max(dict, key=dict.get)
    return (max_,dict[max_])