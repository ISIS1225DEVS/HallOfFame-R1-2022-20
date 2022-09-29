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


import config as cf
import model
import csv
from DISClib.ADT import list as lt

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def newController(inputList):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog(inputList)
    return control


# Funciones para la carga de datos


def loadData(control,filename, platform):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    cant= loadMovies(catalog, filename, platform)
    #sortBooks(catalog)
    return cant


def loadMovies(catalog,filename,platform):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    moviesfile = cf.data_dir + 'Streaming/'+filename
    input_file = csv.DictReader(open(moviesfile, encoding='utf-8'))
    for movie in input_file:
        model.addMovie(catalog, movie, platform)
    return model.movieSize(catalog)

def getSampleMovies(control,cant):
    """
    Retorna los mejores libros
    """
    SampleMovies = model.getSampleMovies(control['model'],cant)
    return SampleMovies

def sortMovies(control, size, sortType):
    """
    Ordena los libros por average_rating
    """
    return model.sortMovies(control['model'], size, sortType)

def sortMoviesByReleaseYear(control):
    """
    Ordena el contenido por la fecha de lanzamiento
    """
    return model.sortMoviesByReleaseYear(control['model'])

def sortMoviesByDateAdded(control):
    """
    Ordena el contenido por la fecha e incorporacion
    """
    return model.sortMoviesByDateAdded(control['model'])

def sortMoviesByName(control):
    """
    Ordena el contenido por nombre, año de lanzamiento y duracion
    """
    return model.sortMoviesByName(control['model'])


def sortMoviesByName2(control):
    """
    Ordena el contenido por nombre, año de lanzamiento y director
    """
    return model.sortMoviesByName2(control['model'])

#Requerimiento 1
def getMoviesByReleaseYear(lista,anoinicial,anofinal):
    filteredList = model.getMoviesByReleaseYear(lista,anoinicial,anofinal)
    return filteredList 

#Requerimiento 2
def getShowsByPeriod(lista,fechainicial,fechafinal):
    filteredList = model.getShowsByPeriod(lista,fechainicial,fechafinal)
    return filteredList 

#Requerimiento 3
def getContentByCast(lista,actor):
    filteredList  = model.getContentByCast(lista,actor)
    return filteredList 

#Requerimiento 4 
def getContentByGenero(lista,genero):
    filteredList = model.getContentByGenero(lista,genero)
    return filteredList 

#Requerimiento 5
def getShowsByCountry(lista,country):
    filteredList = model.getShowsByCountry(lista,country)
    return filteredList 

#Requerimiento 6
def getContentByDirector(lista,director):
    filteredList  = model.getContentByDirector(lista,director)
    return filteredList 

#Requerimiento 7
def getTopByGenero(control):
    filteredList  = model.getTopByGenero(control['model'])
    return filteredList 

#Requerimiento 8
def getTopByActor(control):
    filteredList  = model.getTopByActor(control['model'])
    return filteredList 