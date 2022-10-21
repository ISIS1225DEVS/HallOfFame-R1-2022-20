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

from App.model import deltaTime
import config as cf
import model
import csv
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos
def inicializarCatalogo(tipo):
    return model.inicializarCatalogo(tipo)

def loadNetflix(catalogo,tamanio_datos):
    booksfile = cf.data_dir + 'Streaming/netflix_titles-utf8'+ tamanio_datos+ '.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for title in input_file:
        model.addTitle(catalogo, title)
        model.addTitleNetflix(catalogo, title)
    return None

def loadHulu(catalogo,tamanio_datos):
    booksfile = cf.data_dir + 'Streaming/hulu_titles-utf8'+ tamanio_datos+ '.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for title in input_file:
        model.addTitle(catalogo, title)
        model.addTitleHulu(catalogo, title)
    return None

def loadPrime(catalogo,tamanio_datos):
    booksfile = cf.data_dir + 'Streaming/amazon_prime_titles-utf8'+ tamanio_datos+ '.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for title in input_file:
        model.addTitle(catalogo, title)
        model.addTitlePrime(catalogo, title)
    return None

def loadDisney(catalogo,tamanio_datos):
    booksfile = cf.data_dir + 'Streaming/disney_plus_titles-utf8'+ tamanio_datos+ '.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for title in input_file:
        model.addTitle(catalogo, title)
        model.addTitleDisney(catalogo, title)
    return None
# Funciones de ordenamiento
def sortTitles(control, lista, size):
    """
    Ordena los libros por average_rating
    """
    return model.sortTitles(control, lista, size)

def sortDateAdded(catalog,  size):
    return model.sortDateAdded(catalog,  size)

def sortActores(catalog,  lista, size):
    return model.sortActores(catalog, lista,  size)
    
def sortReleaseYear(catalog,  size):
    return model.sortDateAdded(catalog,  size)

def sortSeries(control, lista, size):
    """
    Ordena los libros por date_added
    """
    return model.sortSeries(control, lista, size)

def sortDirector(catalog, lista,  size):
    return model.sortDirector(catalog, lista,  size)

def ordenamiento(catalogo,tipo_alg):
    return model.ordenamiento(catalogo,tipo_alg)

# Funciones de consulta sobre el catálogo
def loadData(catalogo,tamanio_datos):
    loadNetflix(catalogo,tamanio_datos)
    loadHulu(catalogo,tamanio_datos)
    loadDisney(catalogo,tamanio_datos)
    loadPrime(catalogo,tamanio_datos)

def primeros3(lista,opcion):
    return model.primeros3(lista,opcion)

def ultimos3(lista,opcion):
    return model.ultimos3(lista,opcion)

def contenido_por_genero(genero,sorted_listT):
    return model.contenido_por_genero(genero,sorted_listT)

def periodo_tiempo_peliculas(inicial, final,sorted_listT):
    return model.periodo_tiempo_peliculas(inicial,final,sorted_listT)

def periodo_tiempo_series(inicial, final,sorted_listSeries):
    return model.periodo_tiempo_series(inicial,final,sorted_listSeries)

def contenido_director(director,sorted_listT):
    return model.contenido_director(director,sorted_listT)

def top_generos(top,sorted_listT):
    return model.top_generos(top,sorted_listT)

def contenido_por_actor(actor, sorted_listT):
    return model.contenido_por_actor(actor, sorted_listT)

def contenido_por_pais(pais, sorted_listT):
    return model.contenido_por_pais(pais, sorted_listT)

def listar (lista):
    return model.listar(lista)

def top_actores(top,sorted_listT):
    return model.top_actores(top,sorted_listT)
