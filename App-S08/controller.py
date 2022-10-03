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

from xml.dom.minidom import Element
import config as cf
import model
import csv
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sc
from DISClib.Algorithms.Sorting import insertionsort as inter
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
from prettytable import PrettyTable as pretty
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def newCatalog(ordenamiento):
    control={"model":None}
    control["model"]= model.crearCatalogo(ordenamiento)
    return control['model']

# Funciones para la carga de datos
def loadContentCatalog(catalog):
    files={"Amazon Prime": "Streaming/amazon_prime_titles-utf8-small.csv",
                "Disney":"Streaming/disney_plus_titles-utf8-small.csv", 
                "Hulu":"Streaming/hulu_titles-utf8-small.csv", 
                "Netflix":"Streaming/netflix_titles-utf8-small.csv"}
    ret=lt.newList(datastructure="ARRAY_LIST")
    ids=0
    for plataforma in files:
        temp= {plataforma:0}
        contentfile= cf.data_dir + files[plataforma]
        platform= csv.DictReader(open(contentfile, encoding='utf-8'))
        for content in platform:
            for key in content:
                if content[key]=="":
                    content[key]="unknown"
            content["stream_service"]=plataforma
            content["show_id"]=ids
            content["description"]=content["description"]
            model.addContent((catalog[plataforma]),content)
            ids+=1
        temp[plataforma]=model.platformSize(catalog[plataforma])
        lt.addLast(ret, (temp))       
    return ret

def escogeratributos(lista, atributos):
    return model.escoger_atributos(lista,atributos)
# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo
def requerimiento1(desde,hasta,catalog):
    return model.requerimiento1(desde,hasta,catalog)

def requerimiento2(desde,hasta,catalog):
    return model.requerimiento2(desde,hasta,catalog)

def requerimiento3(actorbuscar,catalog):
    return model.requerimiento3(actorbuscar,catalog)

def requerimiento4(generobuscar,catalog):
    return model.requerimiento4(generobuscar,catalog)

def requerimiento5(paisbuscar,catalog):
    return model.requerimiento5(paisbuscar,catalog)

def requerimiento6(nombre, catalogo):
    return model.requerimiento6(nombre,catalogo)

def requerimiento7(catalog, num):
    return model.requerimiento7(catalog, num)

def first3last3(lista):
    ret=model.First3Last3(lista)
    return ret
    
def tabla_carga_datos(control):
    columna=["service_name","count"]
    return model.crear_tabla1(control,columna)

def creartablas(adtStructure):
    return model.crear_tablas(adtStructure)

def getTime():
    return model.getTime()
