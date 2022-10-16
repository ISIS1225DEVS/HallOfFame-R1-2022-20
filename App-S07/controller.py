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
 """

from gettext import Catalog
import config as cf
import model
from datetime import datetime
import time as tm
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros
def newController():
    """
    Crea una instancia del modelo
    """
    control = model.newCatalog('ARRAY_LIST')
    return control

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    netflix = loadPlatform(catalog, 'netflix')
    amazon = loadPlatform(catalog, 'amazon_prime')
    disney = loadPlatform(catalog, 'disney_plus')
    hulu = loadPlatform(catalog, 'hulu')
    titles = model.numberTitles(catalog)
    features = model.numberFeatures(catalog)
    return netflix, amazon, disney, hulu, titles, features

def loadPlatform(catalog, platform):
    contentFile = cf.data_dir + 'Streaming/' + str(platform) + '_titles-utf8-large.csv'
    input_file = csv.DictReader(open(contentFile, encoding='utf-8'))
    features = 0
    for title in input_file:
        title['stream_service'] = platform
        model.addTitle(catalog, platform, title)
    return model.platformSize(catalog, platform)

# Funciones de ordenamiento

def sortDataAmounts(lista):
    model.sortDataAmounts(lista)

def sortDataCounts(lista):
    return model.sortDataCounts(lista)

# Funciones de consulta sobre el catálog, 
def filteredMoviesByYears(catalog, initialYear, finalYear):
    return model.filteredMoviesByYears(catalog, initialYear, finalYear)

def filteredTVShowsByDates(catalog, initialDate, finalDate):
    initialDate = datetime.strptime(initialDate, '%B %d, %Y')
    finalDate = datetime.strptime(finalDate, '%B %d, %Y')
    return model.filteredTVShowsByDates(catalog, initialDate, finalDate)

def findContentByActor(catalog, actor):
    actor = actor.title()
    return model.findContentByActor(catalog, actor)

def findContentByGenero(catalog, genero):
    genero = genero.title()
    return model.findContentByGenero(catalog, genero)

def findContentByCountry(catalog, country):
    country = country.title()
    return model.findContentByCountry(catalog, country)

def findContentByDirector(catalog, director):
    director = director.title()
    return model.findContentByDirector(catalog, director)

def topNByCategory(catalog, N):
    return model.topNByCategory(catalog, N)

def topNByActor(catalog, N):
    return model.topNByActor(catalog, N)

def firstAndLastThreeTitles(lista):
    return model.firstAndLastThreeTitles(lista)

def getTime():
    return float(tm.perf_counter()*1000)

def deltaTime(start, end):
    elapsed = float(end - start)
    return elapsed