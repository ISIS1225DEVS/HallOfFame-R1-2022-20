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
import datetime as dt


csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 

def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control

# Funciones para la carga de datos

def loadData(control,size):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    Netflix = loadNetflix(catalog,size)
    Hulu = loadHulu(catalog,size)
    Disney_plus = loaddisneyplus(catalog,size)
    Amazon_prime = loadamazonprime(catalog,size)
    return Netflix, Hulu, Disney_plus, Amazon_prime

def loadNetflix(catalog,size):
    """
    Carga la información de las películas y shows de Netflix.
    """
    netflixfile = cf.data_dir + 'Streaming/netflix_titles-utf8'+size+'.csv'
    input_file = csv.DictReader(open(netflixfile, encoding='utf-8'))
    for element in input_file:
        element["platform"] = "Netflix"
        model.addElement(catalog, element)
        model.addElement_Platform(catalog,element,"Netflix")
    return catalog["Netflix"]

def loadHulu(catalog,size):
    """
    Carga la información de las películas y shows de Hulu.
    """
    hulufile = cf.data_dir + 'Streaming/hulu_titles-utf8'+size+'.csv'
    input_file = csv.DictReader(open(hulufile, encoding='utf-8'))
    for element in input_file:
        element["platform"] = "Hulu"
        model.addElement(catalog, element)
        model.addElement_Platform(catalog,element,"Hulu")
    return catalog["Hulu"]

def loadamazonprime(catalog,size):
    """
    Carga la información de las películas y shows de Amazon Prime.    
    """
    amazonfile =  cf.data_dir + 'Streaming/amazon_prime_titles-utf8'+size+'.csv'
    input_file = csv.DictReader(open(amazonfile, encoding='utf-8'))
    for element in input_file:
        element["platform"] = "Amazon Prime"
        model.addElement(catalog, element)
        model.addElement_Platform(catalog,element,"Amazon-prime")
    return catalog["Amazon-prime"]

def loaddisneyplus(catalog,size):
    """
    Carga la información de las películas y shows de Disney plus.
    """
    disneyfile =  cf.data_dir + 'Streaming/disney_plus_titles-utf8'+size+'.csv'
    input_file = csv.DictReader(open(disneyfile, encoding='utf-8'))
    for element in input_file:
        element["platform"] = "Disney Plus"
        model.addElement(catalog, element)
        model.addElement_Platform(catalog,element,"Disney-plus")
    return catalog["Disney-plus"]

def mergesortc(list,cmpfunction):
    mrg = model.mergesort(list,cmpfunction)
    return mrg

## Requerimiento 1
def Movies_in_range(list,top,bottom,criteria="release_year"):
    Movies, size = model.elements_in_range(list,top,bottom,criteria)
    return mergesortc(Movies , model.cmpByReleaseYear), size
 
## Requerimiento 2
def Shows_in_range(list,top,bottom,criteria="date_added"):
    Shows, size = model.elements_in_range_date(list,top,bottom,criteria)
    return mergesortc(Shows , model.cmpBydateadded), size

## Requerimiento 3
def actor_in_film(list,actor):
    titles = model.find_actor(list,actor)
    ammount_movie= model.count_by(titles,"Movie","type")
    ammount_shows= model.count_by(titles,"TV Show","type")
    return mergesortc(titles,model.cmpByTRD), ammount_movie , ammount_shows

## Requerimiento 4
def titles_by_genre(list,name):
    titles = model.find_genre(list,name)
    ammount_movie= model.count_by(titles,"Movie","type")
    ammount_shows= model.count_by(titles,"TV Show","type")
    return mergesortc(titles , model.cmpByTRD) , ammount_movie , ammount_shows

## Requerimiento 5 
def titles_by_country(list,name,criteria="country"):
    titles = model.find_by(list,criteria,name)
    ammount_movie= model.count_by(titles,"Movie","type")
    ammount_shows= model.count_by(titles,"TV Show","type")
    return mergesortc(titles , model.cmpByTRD) , ammount_movie , ammount_shows

## Requerimiento 6 
def count_by_platform(list,criteria="platform"):
    counted=[]
    for platform in ["Netflix","Hulu","Disney Plus","Amazon Prime"]:
        ammount=model.count_by(list,platform,criteria)
        counted.append((platform,ammount))
    return counted

def titles_by_director(list,name,criteria="director"):
    titles = model.find_by(list,criteria,name)
    ammount_movie = model.count_by(titles,"Movie","type")
    ammount_shows = model.count_by(titles,"TV Show","type")
    ammount_genres = model.listed_in(titles)
    ammount_platforms = count_by_platform(titles)
    return mergesortc(titles , model.cmpByReleaseYear) , ammount_movie , ammount_shows , ammount_genres , ammount_platforms

## Requerimiento 7 
def count_per_genre(list):
    genres = model.listed_in(list)
    return mergesortc(genres,model.cmpGenres)

## Requerimiento 8
def count_per_actor(list):
    actors = model.cast_count(list)
    return mergesortc(actors , model.cmpActors)