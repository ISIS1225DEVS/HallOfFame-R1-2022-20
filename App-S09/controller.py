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

from platform import platform
import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def newCatalog(structure="DEFAULT", sortAlgorithm="DEFAULT", sampleSize="DEFAULT"):
    structure = structure if structure != "DEFAULT" else "ARRAY_LIST"
    sortAlgorithm = sortAlgorithm if sortAlgorithm != "DEFAULT" else "SHELL"
    sampleSize = "small" if sampleSize == "DEFAULT" else sampleSize
    catalog = model.newCatalog(structure, sortAlgorithm, sampleSize)
    return catalog


# Función para la carga de datos

def loadData(catalog):
    amazon = loadDataPlatform(catalog, model.AMAZON_PRIME)
    disney = loadDataPlatform(catalog, model.DISNEY_PLUS)
    hulu = loadDataPlatform(catalog, model.HULU)
    netflix = loadDataPlatform(catalog, model.NETFLIX)
    backLoad(catalog)
    return amazon, disney, hulu, netflix

# Función para la carga de cada plataforma

def loadDataPlatform(catalog, platform):
    archivo = cf.data_dir + f"{platform.lower()}_titles-utf8-{catalog['sampleSize']}.csv"
    datos= csv.DictReader(open(archivo, encoding="utf-8"))
    for video in datos:
        model.addVideo(catalog, video, platform)
    return model.videosByPlatform(catalog, platform)
    
# Funciones de ordenamiento

def backLoad(catalog):
    model.loadActores(catalog)
    model.loadCategorias(catalog)
    sortVideos(catalog)

def sortVideos(catalog):
    data = model.sortVideos(catalog)
    return data

# Funciones de consulta sobre el catálogo

def getElements(lst, subkeys=[]):
    return model.getElements(lst, subkeys)

def findTopActores(catalog, top=5):
    data = model.topActores(catalog, top)
    return data

def findTopCategorias(catalog, top):
    data = model.topCategorias(catalog, top)
    return data
    
def filterByPais(catalog, paisName):
    data = model.videosByPais(catalog, paisName)
    return data

def filterByDirector(catalog, director):
    data = model.videosByDirector(catalog, director)
    return data
    
def filterByCategoria(catalog, categoriaName):
    data = model.videosByCategoria(catalog, categoriaName)
    return data
    
def filterByActor(catalog, actorName):
    data = model.videosByActor(catalog, actorName)
    return data
    
def filterProgramas(catalog, aInicial, aFinal):
    data = model.filterProgramas(catalog, aInicial, aFinal)
    return data
     
def filterPeliculas(catalog, aInicial, aFinal):
    data = model.filterPeliculas(catalog, aInicial, aFinal)
    return data
