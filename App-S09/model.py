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


from gettext import Catalog
from datetime import datetime
from re import A
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import insertionsort as inss

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def newCatalog(structure="ARRAY_LIST", sortAlgorithm="SHELL", sufixFile="small"):
    catalog = {
        'videos' : None,
        'videosByReleaseYear': None,
        'videosByDateAdded': None,
        'videosByTitle': None,
        'videosByTitleAndDirector': None,
        'videosByDateAddedAndReleaseYear': None,
        "actores": None,
        'categorias': None,
        'sort': "",
        'sampleSize': ""
    }
    catalog["videos"] = lt.newList(structure)
    catalog['videosByReleaseYear'] = lt.newList(structure)
    catalog['videosByDateAdded'] = lt.newList(structure)
    catalog['videosByTitle'] = lt.newList(structure)
    catalog['videosByTitleAndDirector'] = lt.newList(structure)
    catalog['videosByDateAddedAndReleaseYear'] = lt.newList(structure)
    catalog["actores"] = lt.newList(structure, compareNames)
    catalog["categorias"] = lt.newList(structure, compareCategorias)
    catalog["sort"] = choiseSortFunction(sortAlgorithm)
    catalog["sampleSize"] = sufixFile

    return catalog

"""Variables que se usan para llamar o acceder a una plataforma en particular 
(Y evitar que una misma plataforma aparezca varias veces con mayúsculas o mínusculas diferentes)"""

NETFLIX = "Netflix"
HULU = "Hulu"
DISNEY_PLUS = "Disney_Plus"
AMAZON_PRIME = "Amazon_Prime"


# Funciones para agregar informacion al catalogo

def addVideo (catalog, video, platform):
    showId = video["show_id"] 
    type = video["type"]
    title = video["title"]
    director = video["director"]
    cast = video["cast"]
    country = video["country"]
    dateAdded = video["date_added"]
    releaseYear = video["release_year"]
    rating = video["rating"]
    duration = video["duration"]
    listedIn = video["listed_in"]
    description = video["description"]
    nuevoVideo = newVideo(showId, type, title, director, cast, country, dateAdded, releaseYear, rating, duration, listedIn, description, platform)
    lt.addLast(catalog['videos'], nuevoVideo)
    lt.addLast(catalog['videosByReleaseYear'], nuevoVideo)
    lt.addLast(catalog['videosByDateAdded'], nuevoVideo)
    lt.addLast(catalog['videosByTitle'], nuevoVideo)
    lt.addLast(catalog['videosByTitleAndDirector'], nuevoVideo)
    lt.addLast(catalog['videosByDateAddedAndReleaseYear'], nuevoVideo)
    return nuevoVideo
    
def loadActores(catalog):
    auxCast = {}
    for video in lt.iterator(catalog["videosByReleaseYear"]):
        for actor in lt.iterator(video["cast"]):

            # Validacion existencial
            if auxCast.get(actor, None) == None:
                auxCast[actor] = newActor(actor)
            ac = auxCast[actor]

            # Validacion type Video
            if video["type"] == "Movie":
                ac["movies"] += 1
            else:
                ac["tv_shows"] += 1

            # Validacion platform Video
            if video["platform"] == AMAZON_PRIME:
                ac[AMAZON_PRIME] += 1
            elif video["platform"] == DISNEY_PLUS:
                ac[DISNEY_PLUS] += 1
            elif video["platform"] == HULU:
                ac[HULU] += 1
            elif video["platform"] == NETFLIX:
                ac[NETFLIX] += 1

            ac["total"] += 1
            lt.addLast(ac["videos"], video)

    # Carga de directores y compañeros por actor
    for actor in auxCast:
        for video in lt.iterator(auxCast[actor]["videos"]):
            ac = auxCast[actor]
            loadActorDirectores(ac, video["director"])
            loadActorMates(ac, video["cast"])
            ms.sort(ac["directores"], compareActorDirectoresTop)
            ms.sort(ac["mates"], compareActorMatesTop)
                
    # Conversion de dict a lst
    for actor in auxCast:
        lt.addLast(catalog["actores"], auxCast[actor])

    ms.sort(catalog["actores"], compareActoresTop)

#Función que cuenta la cantidad de trabajos de un actor con un director.

def loadActorDirectores(actor, directorName):
    pos = lt.isPresent(actor["directores"], directorName)
    
    #Si no existe lo crea
    if pos == 0:
        acd = newActorDirector(directorName)
        lt.addLast(actor["directores"], acd)

    #Si existe le suma un trabajo
    else:
        acd = lt.getElement(actor["directores"], pos)
    acd["cant_works"] += 1

#Función que cuenta la cantidad de trabajos de un actor y llena la lista de sus compañeros de rojade

def loadActorMates(actor, matesList):
    for mateName in lt.iterator(matesList):
        pos = lt.isPresent(actor["mates"], mateName)

        #Si no existe lo crea y añade a compañeros
        if pos == 0:
            acm = newActorMate(mateName)
            lt.addLast(actor["mates"], acm)

        #Si existe lo consigue
        else:
            acm = lt.getElement(actor["mates"], pos)
        
        #Y le añade 1 trabajo
        acm["cant_works"] += 1

#Función que cuenta la cantidad veces que una categoría pertenece a una película, show y/o plataforma

def loadCategorias(catalog):
    for video in lt.iterator(catalog["videos"]):
        #Recorre todas las categorías de todos los videos
        for categoria in lt.iterator(video["listed_in"]):
            c = newCategoria(categoria)
            pos = lt.isPresent(catalog["categorias"], categoria)
            #Si la categoría no existe, la crea
            if pos == 0:
                c = newCategoria(categoria)
                lt.addLast(catalog["categorias"], c)
            #Si existe la trae
            else:
                c = lt.getElement(catalog["categorias"], pos)
            #Se suma 1 a movie o show, y a una plataforma, según corresponda
            if video["type"] == "Movie":
                c["movies"] += 1
            else:
                c["tv_shows"] += 1
            if video["platform"] == AMAZON_PRIME:
                c[AMAZON_PRIME] += 1
            elif video["platform"] == DISNEY_PLUS:
                c[DISNEY_PLUS] += 1
            elif video["platform"] == HULU:
                c[HULU] += 1
            elif video["platform"] == NETFLIX:
                c[NETFLIX] += 1
            #Se suma 1 al total de videos de esa categoría
            c["total"] += 1

    #Se ordenan las categorías
    ms.sort(catalog["categorias"], compareCategoriasTop)

# Funciones para creacion de datos

def newVideo(showId, type, title, director, cast, country, dateAdded, releaseYear, rating, duration, listedIn, description, platform):
    video = {
        "show_id": "",
        "type": "",
        "title": "",
        "director": "",
        "cast": lt.newList("ARRAY_LIST"),
        "country": "",
        "date_added": "",
        "release_year": "",
        "rating": "",
        "duration": "",
        "listed_in": lt.newList("ARRAY_LIST"),
        "description": "",
        "platform": ""
    }
    video["show_id"] = showId + "_" + platform
    video["type"] = type
    video["title"] = title
    video["director"] = director if len(director) > 2 else "Unknown"
    video["country"] = country
    video["release_year"] = int(releaseYear)
    video["rating"] = rating
    video["description"] = description
    video["platform"] = platform

    # Conversion de string a duration
    try:
        video["duration"] = int(duration.split(" ")[0])
        video["type_duration"] = duration.split(" ")[1]
    except:
        video["duration"] = 0
        video["type_duration"] = ""

    # Conversion de string a datetime
    try:
        video["date_added"] = datetime.strptime(dateAdded, "%Y-%m-%d")
    except:
        video["date_added"] = None

    # Conversion de string en list de actores
    for c in cast.split(","):
        c = c if len(c) > 2 else "Unknown"
        lt.addLast(video["cast"], c.strip())

    # Conversion de string en list de generos
    for genre in listedIn.split(","):
        lt.addLast(video["listed_in"], genre.strip())

    return video

#Crea una categoría con su nombre

def newCategoria(name):
    categoria = {
        "name": "",
        "tv_shows": 0,
        "movies": 0,
        "total": 0,
        "videos": None,
        AMAZON_PRIME : 0,
        DISNEY_PLUS : 0,
        HULU : 0,
        NETFLIX : 0
    }
    
    categoria["name"] = name
    categoria["videos"] = lt.newList("ARRAY_LIST")

    return categoria

#Crea un actor con su nombre

def newActor(name):
    actor = {
        "name": "",
        "tv_shows": 0,
        "movies": 0,
        "total": 0,
        "directores": None,
        "mates": None,
        "videos": None,
        "genero_actuado": "",
        AMAZON_PRIME : 0,
        DISNEY_PLUS : 0,
        HULU : 0,
        NETFLIX : 0
    }

    actor["name"] = name
    actor["directores"] = lt.newList("ARRAY_LIST", compareNames)
    actor["mates"] = lt.newList("ARRAY_LIST", compareNames)
    actor["videos"] = lt.newList("ARRAY_LIST")

    return actor

#Función que crea un actor para contar sus trabajos con un director.

def newActorDirector(directorName):
    actorDirector = {
        "name": "",
        "cant_works": 0
    }

    actorDirector["name"] = directorName

    return actorDirector

#Crea un director con su nombre

def newDirector(directorName):
    Director = {
        "name": "",
        "movies":0,
        "tv_shows":0,
        NETFLIX: 0, 
        HULU: 0, 
        AMAZON_PRIME: 0, 
        DISNEY_PLUS: 0, 
        "generos": lt.newList("ARRAY_LIST"),
        "videos": lt.newList("ARRAY_LIST")
    }

    Director["name"] = directorName

    return Director

#Función que crea un compañero para contar sus trabajos con un actor.

def newActorMate(mateName):
    actorMate = {
        "name": "",
        "cant_works": 0
    }

    actorMate["name"] = mateName

    return actorMate

#Función que crea un país

def newPais(name):
    pais = {
        "name": "",
        "movies": 0,
        "tv_shows": 0,
        "videos": lt.newList("ARRAY_LIST")
    }

    pais["name"] = name

    return pais

# Funciones de consulta

#Función que consulta cuántos videos hay en una plataforma

def videosByPlatform(catalog, platform):
    videosInPlatform = lt.newList("ARRAY_LIST")
    videos = lt.iterator(catalog["videos"])
    for video in videos:
        if video["platform"] == platform:
            lt.addLast(videosInPlatform, video)
    return videosInPlatform

#Función que consulta cuántas categorías hay en el catálogo

def categoriasSize(catalog):
    return lt.size(catalog["categorias"])

#Función que extrae el top N de actores la lista ya ordenada del catálogo

def topActores(catalog, top=5):
    if top > lt.size(catalog["actores"]):
        return catalog["actores"]
    return lt.subList(catalog["actores"], 1, top)

#Función que extrae el top N de categorías la lista ya ordenada del catálogo

def topCategorias(catalog, top):
    if top > lt.size(catalog["categorias"]):
        return catalog["categorias"]
    return lt.subList(catalog["categorias"], 1, top)

#Función obtiene todos o una parte de los elementos de un TAD lista (sin importar si es Array List o Single Linked List)

def getElements(lst, subkeys=[]):
    elements = []
    data = []
    if lst['type'] == "ARRAY_LIST":
        data = lst["elements"]
    else:
        for e in lt.iterator(lst):
            data.append(e)
    if len(subkeys) > 0:
        for d in data:
            value = d[subkeys[0]]
            for sk in subkeys[1:]:
                value = value[sk]
            elements.append(value)
    return data if len(elements) == 0 else elements

#Función que filtra y cuenta la cantidad de videos producidos en un país particular

def videosByPais(catalog, paisName):
    dataPais = newPais(paisName)
    found = False
    for video in lt.iterator(catalog["videosByTitleAndDirector"]):
        if video["country"] == paisName:
            found = True
            if video["type"] == "Movie":
                dataPais["movies"] += 1
            else:
                dataPais["tv_shows"] += 1
            lt.addLast(dataPais["videos"], video)
    return dataPais if found else None

#Función que filtra y cuenta la cantidad de videos producidos por un director particular
    
def videosByDirector(catalog, directorName):
    dataDirector = newDirector(directorName)
    auxGeneros = {}
    found = False
    for video in lt.iterator(catalog["videosByReleaseYear"]):
        if video["director"] == directorName:
            found = True
            if video["type"] == "Movie":
                dataDirector["movies"] += 1
            else:
                dataDirector["tv_shows"] += 1

            if video["platform"] == NETFLIX:
                dataDirector[NETFLIX] +=1
            elif video["platform"] == AMAZON_PRIME:
                dataDirector[AMAZON_PRIME] +=1
            elif video["platform"] == HULU:
                dataDirector[HULU] +=1
            elif video["platform"] == DISNEY_PLUS:
                dataDirector[DISNEY_PLUS] +=1

            #Se cuentan la cantidad de videos de cada género relativos al director
            for gen in lt.iterator(video["listed_in"]):
                if gen in auxGeneros:
                    auxGeneros[gen] +=1
                else:
                    auxGeneros[gen] = 1
            
            lt.addLast(dataDirector["videos"], video)
    
    #Se convierten los datos del diccionario a una lista "generos" en los datos del director
    for g in auxGeneros:
        c = newCategoria(g)
        c["total"] = auxGeneros[g]
        lt.addLast(dataDirector["generos"], c)
        
    return dataDirector if found else None

#Función que filtra y cuenta la cantidad de videos de una categoría particular
    
def videosByCategoria(catalog, categoriaName):
    dataCategoria = newCategoria(categoriaName)
    found = False
    for video in lt.iterator(catalog["videosByTitleAndDirector"]):
        for genero in lt.iterator(video["listed_in"]):
            if genero == categoriaName:
                found = True
                if video["type"] == "Movie":
                    dataCategoria["movies"] += 1
                else:
                    dataCategoria["tv_shows"] += 1
                lt.addLast(dataCategoria["videos"], video)
    return dataCategoria if found else None

#Función que filtra y cuenta la cantidad de videos en los que participa un actor particular

def videosByActor(catalog, actorName):
    dataActor = newActor(actorName)
    found = False
    for video in lt.iterator(catalog["videosByTitle"]):
        for actor in lt.iterator(video["cast"]):
            if actor == actorName:
                found = True
                if video["type"] == "Movie":
                    dataActor["movies"] += 1
                else:
                    dataActor["tv_shows"] += 1
                lt.addLast(dataActor["videos"], video)
    return dataActor if found else None
    
#Función que filtra y cuenta la cantidad de tv shows producidos en un intervalo de fechas particular

def filterProgramas(catalog, aInicial, aFinal):
    data = {
        "periodo": (f'{aInicial} {" - "} {aFinal}'),
        "tv_shows": 0,
        "videos": lt.newList("ARRAY_LIST")
    }
    for video in lt.iterator(catalog["videosByDateAdded"]):
        formatValid=video["date_added"]!=None
        if formatValid and video["type"] == "TV Show" and aInicial <= video["date_added"] and aFinal >= video["date_added"]:
            found = True
            data["tv_shows"] += 1
            lt.addLast(data["videos"], video)
    return data if found else None

#Función que filtra y cuenta la cantidad de películas producidas en un intervalo de fechas particular

def filterPeliculas(catalog, aInicial, aFinal):
    try:
        aInicial = int(aInicial)
        aFinal = int(aFinal)
    except:
        aInicial = 0
        aFinal = 0
    found = False
    data = {
        "periodo": (f'{aInicial} {" - "} {aFinal}'),
        "movies": 0,
        "videos": lt.newList("ARRAY_LIST")
    }
    for video in lt.iterator(catalog["videosByReleaseYear"]):
        if video["type"] == "Movie" and int(aInicial) <= video["release_year"] and int(aFinal) >= video["release_year"]:
            found = True
            data["movies"] += 1
            lt.addLast(data["videos"], video)
    return data if found else None

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpMoviesByReleaseYear(movie1,movie2):
    """Devuelve verdadero(True) si el release_year de movie 1 son menores que los 
    de movie 2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que 
    ambos criterios sean iguales tenga en cuenta la duración,de lo contrario devuelva
    falso (False).
    Args:
        movie1: informacion de la primera pelicula que incluye sus valores 'release_year', ‘title’y ‘duration’
        movie2: informaciondela   segunda   pelicula que incluye su valor'release_year', ‘title’ y ‘duration’"""

    result = False  

    if movie1["release_year"] < movie2["release_year"]:
        result = True
    elif movie1["release_year"] == movie2["release_year"]:
        if movie1["title"] < movie2["title"]:
            result = True
        elif movie1["title"] == movie2["title"]:
            if movie1["duration"] < movie2["duration"]:
                result = True
    
    return result

def cmpMoviesByDateAdded(movie1,movie2):
    """Devuelve verdadero(True) si el date_added de movie 1 son menores que los 
    de movie 2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que 
    ambos criterios sean iguales tenga en cuenta la duración,de lo contrario devuelva
    falso (False).
    Args:
        movie1: informacion de la primera pelicula que incluye sus valores 'date_added', ‘title’y ‘duration’
        movie2: informacion de la segunda pelicula que incluye su valor'date_added', ‘title’ y ‘duration’"""

    result = False  
    validDates = movie1["date_added"] != None and movie2["date_added"] != None
    if validDates and movie1["date_added"] < movie2["date_added"]:
        result = True
    elif movie1["date_added"] == movie2["date_added"]:
        if movie1["title"] < movie2["title"]:
            result = True
        elif movie1["title"] == movie2["title"]:
            if movie1["duration"] < movie2["duration"]:
                result = True
    
    return result
    
def cmpMoviesByTitle(movie1,movie2):
    """Devuelve verdadero(True) si el title de movie 1 son menores que los 
    de movie 2, en caso de que sean iguales tenga en cuenta el 'release_year' y en caso de que 
    ambos criterios sean iguales tenga en cuenta la duración,de lo contrario devuelva
    falso (False).
    Args:
        movie1: informacion de la primera pelicula que incluye sus valores ‘title’, 'release_year' y ‘duration’
        movie2: informacion de la segunda   pelicula que incluye su valor‘title’, 'release_year'  y ‘duration’"""

    result = False  

    if movie1["title"] < movie2["title"]:
        result = True
    elif movie1["title"] == movie2["title"]:
        if movie1['release_year'] < movie2['release_year']:
            result = True
        elif movie1['release_year'] == movie2['release_year']:
            if movie1["duration"] < movie2["duration"]:
                result = True
    
    return result

def cmpMoviesByTitleAndDirector(movie1,movie2):
    """Devuelve verdadero(True) si el title de movie 1 son menores que los 
    de movie 2, en caso de que sean iguales tenga en cuenta el 'release_year' y en caso de que 
    ambos criterios sean iguales tenga en cuenta el director, de lo contrario devuelva
    falso (False).
    Args:
        movie1: informacion de la primera pelicula que incluye sus valores ‘title’, 'release_year' y ‘director’
        movie2: informacion de la segunda   pelicula que incluye su valor‘title’, 'release_year'  y director"""

    result = False  

    if movie1["title"] < movie2["title"]:
        result = True
    elif movie1["title"] == movie2["title"]:
        if movie1['release_year'] < movie2['release_year']:
            result = True
        elif movie1['release_year'] == movie2['release_year']:
            if movie1["director"] < movie2["director"]:
                result = True
    
    return result

def cmpMoviesByDateAndReleaseYear(movie1,movie2):
    """Devuelve verdadero(True) si el date_added de movie 1 son menores que los 
    de movie 2, en caso de que sean iguales tenga en cuenta el 'release_year' y en caso de que 
    ambos criterios sean iguales tenga en cuenta el title, de lo contrario valida la menor duración,
    sino devuelve False (False).
    Args:
        movie1: informacion de la primera pelicula que incluye sus valores ‘date_added’, 'release_year', ‘title’
        y 'duration' 
        movie2: informacion de la segunda   pelicula que incluye su valor ‘date_added’, 'release_year', ‘title’
        y 'duration'"""

    result = False  
    validDates = movie1["date_added"] != None and movie2["date_added"] != None
    if validDates and movie1["date_added"] < movie2["date_added"]:
        result = True
    elif movie1["date_added"] == movie2["date_added"]:
        if movie1['release_year'] < movie2['release_year']:
            result = True
        elif movie1['release_year'] == movie2['release_year']:
            if movie1["title"] < movie2["title"]:
                result = True
            elif movie1["title"] == movie2["title"]:
                if movie1["duration"] < movie2["duration"]:
                    result = True

    return result

def compareNames(subject1, subject2):
    if (subject1.lower() == subject2["name"].lower()):
        return 0
    elif (subject1.lower() > subject2["name"].lower()):
        return 1
    return -1

def compareActoresTop(actor1, actor2):
    if actor1["total"] > actor2["total"]:
        return True
    elif actor1["total"] == actor2["total"]:
        if actor1["movies"] > actor2["movies"]:
            return True
        elif actor1["movies"] == actor2["movies"]:
            if actor1["tv_shows"] > actor2["tv_shows"]:
                return True
    return False

def compareActorDirectoresTop(director1, director2):
    if director1["name"] < director2["name"]:
        return True
    elif director1["name"] == director2["name"]:
        if director1["cant_works"] < director2["cant_works"]:
            return True
    return False

def compareActorMatesTop(mate1, mate2):
    if mate1["name"] < mate2["name"]:
        return True
    elif mate1["name"] == mate2["name"]:
        if mate1["cant_works"] < mate2["cant_works"]:
            return True
    return False

def compareCategorias(categoria1, categoria2):
    if (categoria1.lower() == categoria2["name"].lower()):
        return 0
    elif (categoria1.lower() > categoria2["name"].lower()):
        return 1
    return -1

def compareCategoriasTop(categoria1, categoria2):
    if categoria1["total"] > categoria2["total"]:
        return True
    elif categoria1["total"] == categoria2["total"]:
        if categoria1["movies"] > categoria2["movies"]:
            return True
        elif categoria1["movies"] == categoria2["movies"]:
            if categoria1["tv_shows"] > categoria2["tv_shows"]:
                return True
    return False

# Funciones de ordenamiento

def sortVideos(catalog):
    catalog["sort"].sort(catalog['videosByReleaseYear'], cmpMoviesByReleaseYear) 
    catalog["sort"].sort(catalog['videosByDateAdded'], cmpMoviesByDateAdded)
    catalog["sort"].sort(catalog['videosByTitle'], cmpMoviesByTitle)
    catalog["sort"].sort(catalog['videosByTitleAndDirector'], cmpMoviesByTitleAndDirector)
    catalog["sort"].sort(catalog['videosByDateAddedAndReleaseYear'],cmpMoviesByDateAndReleaseYear)
    return catalog

#Función del laboratorio 4 que fija el tipo de algortimo que se usará para ordenar el catálogo

def choiseSortFunction(type):
    if type == "SELECTION":
        return ss
    if type == "INSERTION":
        return inss
    if type == "SHELL":
        return sa
    if type == "MERGE":
        return ms
    if type == "QUICK":
        return qs
    else:
        return ss

# Utils

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
