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

from filecmp import cmp
from gettext import Catalog
from re import S
from tkinter.tix import COLUMN
import config as cf
import model
import csv
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

#Configurar el entorno de desarrollo

csv.field_size_limit(2147483647)


# Inicialización del Catálogo de Plataformas Digitales

def newController(listType, large_file):
    """
    Llama la función para iniciar el Catalogo de Plataformas Digitales
    """
    
    control = {"model" : None}
    control["model"] = model.newCatalog(listType)
    
    return control   
    
    

# Funciones para la carga de datos

def loadData(control, suffix):
    
    start_time = model.getTime()
    catalog = control["model"]
    netflix = loadNetflix(catalog, suffix)
    amazon_prime = loadAmazon_prime(catalog, suffix)
    disney_plus = loadDisney_plus(catalog, suffix)
    hulu = loadHulu(catalog, suffix)
    loadContent(catalog, "Movie")
    loadContent(catalog, "TV Show")
    model.sortActors(catalog)
    return netflix, amazon_prime, disney_plus, hulu

def loadNetflix(catalog, suffix):
    netflix_file = cf.data_dir + "netflix_titles-utf8" + suffix
    input_file = csv.DictReader(open(netflix_file, encoding = 'utf-8'))
    count = 1
    for title in input_file:
        title = model.reform_title(title, "netflix")
        title["cast"] = model.strlstdivider(title["cast"])
        title["listed_in"] = model.strlstdivider(title["listed_in"])
        title['director'] = model.strlstdivider(title['director'])
        title["platform"] = "netflix"
        model.addActor(catalog, title)
        model.addTitle(catalog, title, "netflix")
        model.addGenre(catalog, title)
    
    return lt.size(catalog["netflix"])

def loadAmazon_prime(catalog, suffix):
    amazon_prime_file = cf.data_dir + "amazon_prime_titles-utf8" + suffix
    input_file = csv.DictReader(open(amazon_prime_file, encoding = 'utf-8'))
    for title in input_file:

        title = model.reform_title(title, "amazon_prime")
        title["cast"] = model.strlstdivider(title["cast"])
        title["listed_in"] = model.strlstdivider(title["listed_in"])
        title["platform"] = "amazon_prime"
        title['director'] = model.strlstdivider(title['director'])
        model.addActor(catalog, title)
        model.addTitle(catalog, title, "amazon_prime")
        model.addGenre(catalog, title)
    return lt.size(catalog["amazon_prime"])

def loadHulu(catalog, suffix):
    hulu_file = cf.data_dir + "hulu_titles-utf8" + suffix
    input_file = csv.DictReader(open(hulu_file, encoding = 'utf-8'))
    for title in input_file:
        title = model.reform_title(title, "hulu")
        title["cast"] = model.strlstdivider(title["cast"])
        title["listed_in"] = model.strlstdivider(title["listed_in"])
        title["platform"] = "hulu"
        title['director'] = model.strlstdivider(title['director'])
        model.addActor(catalog, title)
        model.addTitle(catalog, title, "hulu")
        model.addGenre(catalog, title)
    return lt.size(catalog["hulu"])    

def loadDisney_plus(catalog, suffix):
    disney_plus_file = cf.data_dir + "disney_plus_titles-utf8" + suffix
    input_file = csv.DictReader(open(disney_plus_file, encoding = 'utf-8'))
    for title in input_file:
        title = model.reform_title(title, "disney_plus")
        title["cast"] = model.strlstdivider(title["cast"])
        title["listed_in"] = model.strlstdivider(title["listed_in"])
        title["platform"]= "disney_plus"
        title['director'] = model.strlstdivider(title['director'])
        model.addActor(catalog, title)
        model.addTitle(catalog, title, "disney_plus")
        model.addGenre(catalog, title)
    return lt.size(catalog["disney_plus"]) 

def loadContent(catalog, content):
    model.loadContent(catalog, content)
    return catalog    

        
        
#Requerimientos    
    
def get_titles_by_country(control, countryname):
    countrydata = model.get_titles_by_country(control["model"], countryname)

    return countrydata
    
def get_titles_by_genre(control, genrename):
    genredata = model.get_titles_by_genre(control["model"], genrename)

    return genredata

def get_top_actors(control, topSize):
    topActors, count_actors = model.getTopActors(control['model'], topSize)

    return topActors, count_actors

def get_titles_by_director(control, directorname):
    directordata = model.get_titles_by_director(control["model"], directorname)

    return directordata

def get_content_by_actor(control, actor_name):
    
    catalog = control['model']
    
    actor_data = model.getActorData(catalog, actor_name) #O(logn)
    actor_movies = model.getMoviesInfo(actor_data['content'], catalog)  #O(n)  
    
    if lt.size(actor_movies) > 10000:
        return 'El actor no esta en la lista de Actores', False
    
    return actor_data, actor_movies

def get_top_genres(control, topSize):
    return model.getTopGenres(control['model'], topSize)

# Funciones de ordenamiento


def sort_titles_by_release(control, algorithm, type):
    
    catalog = control["model"]
    
    return model.sortTitles_by_release_year(catalog, algorithm, type)

def sort_titles_by_title(control, list):
    
    catalog = control['model']

    return model.sortTitles_by_title(catalog, list)


# Funciones de consulta sobre el catálogo

def getMoviesbyYear(control, init_year, final_year):
    
    catalog = control["model"]
    
    return model.getMoviesbyYear(catalog, init_year, final_year)

def getTvShowsbyDate(control, init_date, final_date):
    
    catalog = control['model']
    
    return model.getTvSHowsbydate(catalog, init_date, final_date)


def getTime():
    
    return model.getTime()

def deltaTime(start, end):
    
    return model.deltaTime(start, end)


#? Funciones Visualización

def visual_charge_data(list, control):
    
    columns = ['show_id', 
               'platform', 
               'type', 
               'release_year', 
               'title',
               'director', 
               'cast',
               'country', 
               'date_added', 
               'rating',
               'duration', 
               'listed_in', 
               'description'
               ]
    
    catalog = control["model"]
    
    
    return model.FirstandLast(list, 3, columns), model.platforms_size(catalog)
    

def visualreq_5fal(list):
    
    columns = ['title',
               'platform', 
               'director', 
               'cast',
               'duration', 
               'listed_in',
               'description',
               'country']
    
    return model.FirstandLast(list, 3, columns)

def visualreq_6fal(list):
    
    columns = ['title',
               'release_year', 
               'director', 
               'platform',
               'type',
               'duration',
               'cast', 
               'country', 
               'rating',
               'listed_in',
               'description']
    
    return model.FirstandLast(list, 3, columns)

def visualreq_6_0fal(list):
    
    columns = ['listed in',
               'count']
    
    return model.FirstandLast(list, 3, columns)

def visual_charge_data_without_id(list):
    
    columns = ['title',
               'release_year', 
               'director',
               'platform', 
               'type', 
               'duration', 
               'cast', 
               'country', 
               'rating',
               'listed_in',  
               'description']
    
    return model.FirstandLast(list, 3, columns)

def visual_req_6(list):
    
    columns = ['platform',
               'Movie', 
               'TV Shows']
    
    return model.simplePrettyTable(list, columns)
    

def visualSort(list):
    
    columns = ["title",
               "type",
               "release_year",
               "duration",
               "platform", 
               "director"]
    
    return model.FirstandLast(list, 3, columns)

def visualRq1y2(list):
    
    columns = ['type',
               "release_year", 
               'date_added',
               "title", 
               "duration",
               "platform",
               "director",
               "cast",
               ]
    
    return model.FirstandLast(list, 3, columns)

def visualreq3st(list):
    
    columns = ['type',
               'title',
               'release_year',
               'director',
               'platform',
               'duration',
               'cast',
               'country',
               'listed_in',
               'description']
    
    return model.simplePrettyTable(list, columns)

def visualreq5st(list):
    
    columns = ["release_year",
               'title',
               "director",
               "platform",
               "duration",
               "type",
               'cast',
               'listed_in',
               'description']
    
    return model.simplePrettyTable(list, columns)

def visualreq6st(list):
    
    columns = ['title',
               'release_year', 
               'director', 
               'platform',
               'type',
               'duration',
               'cast', 
               'country', 
               'rating',
               'listed_in',
               'description']
    
    return model.simplePrettyTable(list, columns)

def visualR8(list):
    
    return model.visalRq8(list)

def visualreq6_0st(list):
    
    columns = ['listed in',
               'count']
    
    return model.simplePrettyTable(list, columns)

def visualCountTable(columns, titles, counts):
    
    return model.countTable(columns, counts, titles)

def visualActorsCatalog(list):
    
    columns = ['Name',
               'title_id', 
               'type', 
               'platform',
               'listed_in',
               ]
    
    return model.FirstandLast(list, 3, columns)

def visualReq7 (list):
    columns = ['rank',
               'listed_in',
               'count',
               'type',
               'stream_service']
    
    return model.topGenresTable(list, columns)

def visualReq7Extra (list):
    columns = ["listed_in",
               "count"]

    return model.topGenresLittleTable(list, columns)