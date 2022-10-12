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


from re import A
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as sa
from datetime import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(structure):
    catalog = lt.newList(structure)
    catalog['netflix'] = 0
    catalog['amazon_prime'] = 0
    catalog['disney_plus'] = 0
    catalog['hulu'] = 0
    catalog['features'] = 0
    return catalog

# Funciones para agregar informacion al catalogo
def addTitle(catalog, platform, title):
    lt.addLast(catalog, title)
    catalog[platform] += 1
    if catalog['features'] == 0:
        catalog['features'] = len(title)
    return catalog

# Funciones para creacion de datos
def convertToAdmitedData(data, title1, title2):
    converted = lt.newList()
    for key, value in data.items():
        lt.addLast(converted, {title1: key, title2: value, 'amount': value})
        sortDataAmounts(converted)
    return converted
# Funciones de consulta
def platformSize(catalog, platform):
    return catalog[platform]

def numberFeatures(catalog):
    return catalog['features']

def numberTitles(catalog):
    return lt.size(catalog)

def firstAndLastThreeTitles(lista):
    filteredTitles = lt.newList()
    size = lt.size(lista)
    if size >= 1:
        if size <= 5:
            filteredTitles = lista
        else:
            for pos in range(1, 4):
                title = lt.getElement(lista, pos)
                lt.addLast(filteredTitles, title)
            for pos in range(size-2, size+1):
                title = lt.getElement(lista, pos)
                lt.addLast(filteredTitles, title)
    return filteredTitles

def filteredMoviesByYears(catalog, initialYear ,finalYear):
    filtered = lt.newList()
    for title in lt.iterator(catalog):
        releaseYear = int(title['release_year'])
        if title['type'] == 'Movie':
            if releaseYear >= initialYear and releaseYear <= finalYear:
                lt.addLast(filtered, title)
    sortTitles(filtered, compareReq1)
    return filtered

def filteredTVShowsByDates(catalog, initialDate, finalDate):
    filtered = lt.newList()
    for title in lt.iterator(catalog):
        if title['type'] == 'TV Show' and title['date_added'] != '':
            dateAdded = datetime.strptime(title['date_added'], '%Y-%m-%d')
            if dateAdded >= initialDate and dateAdded <= finalDate:
                lt.addLast(filtered, title)
    sortTitles(filtered, compareReq2)
    return filtered

def findContentByActor(catalog, actor):
    filtered = lt.newList()
    movies = 0
    TVShows = 0
    for title in lt.iterator(catalog):
        if actor in title['cast']:
            if title['type'] == 'Movie':
                movies += 1
            else:
                TVShows += 1
            lt.addLast(filtered, title)
    sortTitles(filtered, compareReq3)
    return filtered, movies, TVShows

def findContentByGenero(catalog, genero):
    filtered = lt.newList()
    for title in lt.iterator(catalog):
        if genero in title['listed_in']:
            lt.addLast(filtered, title)
    sortTitles(filtered, compareReq4)
    return filtered

def findContentByCountry(catalog, country):
    filtered = lt.newList()
    movies = 0
    TVShows = 0   
    for title in lt.iterator(catalog):
        if country in title['country']:
            if title['type'] == 'Movie':
                movies += 1
            else:
                TVShows += 1
            lt.addLast(filtered, title)
    sortTitles(filtered, compareReq5)
    return filtered, movies, TVShows

def findContentByDirector(catalog, director):
    filtered = lt.newList()
    foundTypes = {}
    foundPlatforms = {}
    foundGeneros = {}
    for title in lt.iterator(catalog):
        if director in title['director']:
            platform = title['stream_service']
            platformNumber = foundPlatforms.get(platform, 0)
            foundPlatforms[platform] = platformNumber + 1
            Type = title['type']
            typeNumber = foundTypes.get(Type, 0)
            foundTypes[Type] = typeNumber + 1
            generos = title['listed_in'].split(', ')
            for genero in generos:
                generoNumber = foundGeneros.get(genero, 0)
                foundGeneros[genero] = generoNumber + 1
            lt.addLast(filtered, title)
    sortTitles(filtered, compareReq6)
    foundGeneros = convertToAdmitedData(foundGeneros, 'listed_in', 'count')
    return filtered, foundTypes, foundPlatforms, foundGeneros

def topNByCategory(catalog, N):
    infoData = lt.newList()
    topN = lt.newList()
    filtered = {}
    listGeneros = []
    for title in lt.iterator(catalog):
        platform = title['stream_service']
        Type = title['type']
        generos = title['listed_in'].split(', ')
        for genero in generos:
            if genero not in listGeneros:
                listGeneros.append(genero)
                filtered[genero] = {'listed_in': genero, 'type': {}, 'stream_service': {}}
            generoNumber = filtered[genero].get('count', 0)
            filtered[genero]['count'] = generoNumber + 1
            platformNumber = filtered[genero]['stream_service'].get(platform, 0)
            filtered[genero]['stream_service'][platform] = platformNumber + 1
            typeNumber = filtered[genero]['type'].get(Type, 0)
            filtered[genero]['type'][Type] = typeNumber + 1
    for info in filtered.values():
        lt.addLast(infoData, info)
    infoData = sortDataCounts(infoData)
    for pos in range(1, N+1):
        title = lt.getElement(infoData, pos)
        title['rank'] = pos
        lt.addLast(topN, title)
    return topN, lt.size(infoData)

def topNByActor(catalog, N):
    infoData = lt.newList()
    topN = lt.newList()
    filtered = {}
    listActors = []
    for title in lt.iterator(catalog):
        platform = title['stream_service']
        Type = title['type']
        actores = title['cast'].split(', ')
        for actor in actores:
            if actor not in listActors:
                listActors.append(actor)
                filtered[actor] = {'actor': actor, 'type': {}, 'stream_service': {}}
            actorNumber = filtered[actor].get('count', 0)
            filtered[actor]['count'] = actorNumber + 1
            platformNumber = filtered[actor]['stream_service'].get(platform, 0)
            filtered[actor]['stream_service'][platform] = platformNumber + 1
            typeNumber = filtered[actor]['type'].get(Type, 0)
            filtered[actor]['type'][Type] = typeNumber + 1
            colaborations = filtered[actor].get('colaborations', title['cast'])
            for colaborate in colaborations.split(', '):
                if colaborate not in colaborations:
                    colaborations += ', ' + colaborate
                filtered[actor]['colaborations'] = colaborations
    for info in filtered.values():
        lt.addLast(infoData, info)
    infoData = sortDataCounts(infoData)
    for pos in range(1, N+1):
        title = lt.getElement(infoData, pos)
        title['rank'] = pos
        lt.addLast(topN, title)
    return topN, lt.size(infoData)

# Funciones utilizadas para comparar elementos dentro de una lista
def compareReq1(title1, title2):
    if (int(title1['release_year']) == int(title2['release_year'])):
        if (str(title1['title']) == str(title2['title'])):
            return compareDurationMovies(title1, title2)
        else:
            return compareTitle(title1, title2)
    else:
        return compareReleaseYear(title1, title2)

def compareReq2(title1, title2):
    if str(title1['date_added']) == str(title2['date_added']):
        if (str(title1['title']) == str(title2['title'])):
            return compareDurationTVShows(title1, title2)
        else:
            return compareTitle(title1, title2)
    else:
        return compareDateAdded(title1, title2)

def compareReq3(title1, title2):
    if (str(title1['title']) == str(title2['title'])):
        if (int(title1['release_year']) == int(title2['release_year'])):
            return compareDirector(title1, title2)
        else:
            return compareReleaseYear(title1, title2)
    else:
        return compareTitle(title1, title2)

def compareReq4(title1, title2):
    if (str(title1['title']) == str(title2['title'])):
        if (int(title1['release_year']) == int(title2['release_year'])):
            return compareDirector(title1, title2)
        else:
            return compareReleaseYear(title1, title2)
    else:
        return compareTitle(title1, title2)


def compareReq5(title1, title2):
    if (str(title1['title']) == str(title2['title'])):
        if (int(title1['release_year']) == int(title2['release_year'])):
            return compareDirector(title1, title2)
        else:
            return compareReleaseYear(title1, title2)
    else:
        return compareTitle(title1, title2)

def compareReq6(title1, title2):
    if (int(title1['release_year']) == int(title2['release_year'])):
        if (str(title1['title']) == str(title2['title'])):
            return compareDurationMovies(title1, title2)
        else:
            return compareTitle(title1, title2)
    else:
        return compareReleaseYear(title1, title2)

def compareReleaseYear(title1, title2):
    return (int(title1['release_year']) < int(title2['release_year']))

def compareTitle(title1, title2):
    return (str(title1['title']) < str(title2['title']))

def compareDurationMovies(title1, title2):
    return (int(title1['duration'][:-4]) < int(title2['duration'][:-4]))

def compareDurationTVShows(title1, title2):
    return (int(title1['duration'][:-7]) < int(title2['duration'][:-7]))

def compareDataAmounts(amount1, amount2):
    return (int(amount1['amount']) > int(amount2['amount']))

def compareCounts(amount1, amount2):
    return (int(amount1['count']) > int(amount2['count']))

def compareDateAdded(title1, title2):
    return datetime.strptime(title1['date_added'], '%Y-%m-%d') > datetime.strptime(title2['date_added'], '%Y-%m-%d')

def compareDirector(title1, title2):
    return (str(title1['director']) < str(title2['director']))

# Funciones de ordenamiento
def sortTitles(lista, compareReq):
    return sa.sort(lista, compareReq)

def sortDataAmounts(lista):
    return sa.sort(lista, compareDataAmounts)

def sortDataCounts(lista):
    return sa.sort(lista, compareCounts)
