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
from App.model import cmpMoviesByReleaseYear, cmpMoviesByReleaseYear1, cmpalphabetically, cmpdate
from App.model import cmpByTitle, cmpMoviesByReleaseYear, cmpalphabetically, cmpdate
from DISClib.ADT.list import firstElement
import config as cf
import model
import csv


csv.field_size_limit(2147483647)
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def newController(estructura="ARRAY_LIST"):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.newCatalog(estructura)
    return control


# Inicialización del Catálogo de libros

# Funciones para la carga de datos

def loadData(control,tamaño):
    
    catalog = control['model']
    services,total = loadServices(catalog,tamaño)

    return services,total


def loadServices(catalog, tamaño="small"):
 
    ServicesfileAmazon = cf.data_dir + 'Challenge-1/Streaming/amazon_prime_titles-utf8-{0}.csv'.format(tamaño)
    input_file = csv.DictReader(open(ServicesfileAmazon, encoding='utf-8'))
    for elem in input_file:
        model.addService(catalog, elem, 'Amazon Prime')
    amz= model.catalogZize(catalog,"Amazon Prime")
    
    ServicesfileDisney = cf.data_dir + 'Challenge-1/Streaming/disney_plus_titles-utf8-{0}.csv'.format(tamaño)
    input_file = csv.DictReader(open(ServicesfileDisney, encoding='utf-8'))
    for elem in input_file:
        model.addService(catalog, elem, 'Disney+')
    dsn= model.catalogZize(catalog,"Disney+")
    ServicesfileHulu = cf.data_dir + 'Challenge-1/Streaming/hulu_titles-utf8-{0}.csv'.format(tamaño)
    input_file = csv.DictReader(open(ServicesfileHulu, encoding='utf-8'))
    for elem in input_file:
        model.addService(catalog, elem, 'Hulu')
    hul= model.catalogZize(catalog,"Hulu")

    
    ServicesfileNetflix = cf.data_dir + 'Challenge-1/Streaming/netflix_titles-utf8-{0}.csv'.format(tamaño)
    input_file = csv.DictReader(open(ServicesfileNetflix, encoding='utf-8'))
    for elem in input_file:
        model.addService(catalog, elem, 'Netflix')
    net=model.catalogZize(catalog,"Netflix")
    total=amz+dsn+hul+net
    return {"service_name":["Amazon","Disney+","Hulu","Netflix"],"count":[amz,dsn,hul,net]},total



def load_data_req1(catalog):
    return model.primeros_ultimos(catalog, "", cmpMoviesByReleaseYear1)

def req1(catalog, start_year, end_year):
    return model.req1_movies_in_date(catalog, start_year, end_year, "show_idtypedateaddedrating", cmpMoviesByReleaseYear)

def req2(catalog, start_date, end_date):
    return model.req2_tv_in_date(catalog, start_date, end_date, "show_idratingdescriptionlisted_incountry", cmpdate)

def req3(catalog , actor):
    return model.req3_search_actor(catalog, actor, "show_iddate_addedrating", cmpalphabetically)

def req4(catalog,genero):
    return model.req4_ist_genre(catalog,genero,cmpByTitle,"typedurationshow_idPlatform")

def req5(catalog, pais):
    return model.req5_search_pais(catalog, pais, "show_iddate_addedrating", cmpByTitle)

def req6(catalog , director):
    return model.req6_search_c_with_director(catalog, director, "show_idtypedateaddedrating", cmpMoviesByReleaseYear)
def req7(catalog,top):
    return model.req7_top_list(catalog,top)
def req8(catalog,top):
    return model.req8_topActroes(catalog,top)

def imprimirTabla(columnas,filas):
    model.imprimir_tabla(columnas,filas)