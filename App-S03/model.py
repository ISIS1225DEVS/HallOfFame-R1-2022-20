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


from App.controller import mergesortc
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as m
import datetime as dt

assert cf


def newCatalog():
    """
    Inicializa el catálogo general que guarda todos los elementos en todas las plataformas. 
    Una lista que contenga todas las películas, otra que contenga todos los tv shows, y una por cada plataforma.
    """
    catalog = {'general': None,
               'Movies': None,
               'TV-shows': None,
               'Netflix': None,
               'Hulu': None,
               'Amazon-prime': None,
               'Disney-plus': None}

    catalog["general"]=lt.newList("ARRAY_LIST")
    catalog["Movies"]=lt.newList("ARRAY_LIST")
    catalog["TV-shows"]=lt.newList("ARRAY_LIST")
    catalog["Netflix"]=lt.newList("ARRAY_LIST")
    catalog["Hulu"]=lt.newList("ARRAY_LIST")
    catalog["Amazon-prime"]=lt.newList("ARRAY_LIST")
    catalog["Disney-plus"]=lt.newList("ARRAY_LIST")

    return catalog

def addElement(catalog,element):
    """
    Agrega un elemento a la lista de catálogo general y 
    a su lista correspondiente dependiendo de si es película o show.
    """
    lt.addLast(catalog["general"],element)
    if element["type"]=="Movie":
        lt.addLast(catalog["Movies"],element)
    else:
        lt.addLast(catalog["TV-shows"],element)
    return catalog

def addElement_Platform(catalog,element,platform):
    """
    Agrega un elemento a la lista de su plataforma correspondiente.
    """
    lt.addLast(catalog[platform],element) 
    return catalog

def cmpByReleaseYear(title1, title2):
    """
    Devuelve verdadero (True) si el release_year de title1 es menor que el
    de title2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que
    ambos criterios sean iguales tenga en cuenta la duración, de lo contrario devuelva
    falso (False).
    Args:
    title1: informacion de la primera pelicula que incluye sus valores 'release_year',
    'title' y 'duration'
    title2: informacion de la segunda pelicula que incluye su valor 'release_year',
    'title' y 'duration'
    """
    if int(title1["release_year"])!=int(title2["release_year"]):
        return int(title1["release_year"])<int(title2["release_year"])
    elif title1["title"]!=title2["title"]:
        return title1["title"].lower()<title2["title"].lower()
    else: 
        title1["duration"] = title1["duration"][:len(title1["duration"])-4]
        title2["duration"] = title2["duration"][:len(title2["duration"])-4]
        return title1["duration"]<title2["duration"]

def cmpByTRD(title1, title2):
    """
    Devuelve verdadero (True) si el title de title1 es menor que el
    de title2, en caso de que sean iguales tenga en cuenta el release_year y en caso de que
    ambos criterios sean iguales tenga en cuenta el director, de lo contrario devuelva
    falso (False).
    Args:
    title1: informacion de la primera pelicula que incluye sus valores 'release_year',
    'title' y 'director'
    title2: informacion de la segunda pelicula que incluye su valor 'release_year',
    'title' y 'director'
    """
    if title1["title"]!=title2["title"]:
        return title1["title"].lower()<title2["title"].lower()   
    elif int(title1["release_year"])!=int(title2["release_year"]):
        return int(title1["release_year"])<int(title2["release_year"])
    else: 
        return title1["director"].lower()<title2["director"].lower()

def cmpBydateadded(title1, title2):
    """
    Devuelve verdadero (True) si el date_added de title1 es menor que el
    de title2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que
    ambos criterios sean iguales tenga en cuenta la duración, de lo contrario devuelva
    falso (False). Usa datetime para poder comparar las fechas que vengan de la forma AAAA-MM-DD.
    Args:
    title1: informacion del primer titulo que incluye sus valores 'date_added',
    'title' y 'duration'
    title2: informacion del segundo titulo que incluye su valor 'date_added',
    'title' y 'duration'
    """

    if title1["date_added"]!="" and title2["date_added"]!="":
        date1 = dt.datetime.strptime(title1["date_added"],"%Y-%m-%d")
        date2 = dt.datetime.strptime(title2["date_added"],"%Y-%m-%d")
        if date1!=date2:
            return date1<date2
        elif title1["title"]!=title2["title"]:
            return title1["title"].lower()<title2["title"].lower()
        else:
            title1["duration"] = title1["duration"][:len(title1["duration"])-7]
            title2["duration"] = title2["duration"][:len(title2["duration"])-7] 
            return int(title1["duration"])<int(title2["duration"])

def cmpGenres(genre1, genre2):
    """
    Devuelve verdadero (True) si el 
    """
    if genre1[1]["genre"]!=genre2[1]["genre"]:
        return genre1[1]["genre"]>genre2[1]["genre"] 

def cmpActors(actor1, actor2):
    """
    Devuelve verdadero (True) si el 
    """
    if actor1[1]["Total"]!=actor2[1]["Total"]:
        return actor1[1]["Total"]>=actor2[1]["Total"] 
   

def mergesort(list,cmpfunction):
    """
    Ordena una lista de datos con base en la fecha de lanzamiento 
    por medio del método recursivo de ordenamiento mergesort.
    """
    return m.sort(list,cmpfunction)

## Requerimiento 1
def elements_in_range(list,top,bottom,criteria):
    """
    Selecciona los elementos de una lista que se encuentran en un rango dado de números.
    """
    list_in_range=lt.newList("ARRAY_LIST")
    for i in range(0,list["size"]): 
        element=list["elements"][i]
        if int(element[criteria])>=bottom and int(element[criteria])<=top:
            lt.addLast(list_in_range,element)
    return list_in_range, lt.size(list_in_range)

## Requerimiento 2
def elements_in_range_date(list,top,bottom,criteria):
    """
    Selecciona los elementos de una lista que se encuentran en un rango dado de fechas.
    """
    list_in_range = lt.newList("ARRAY_LIST")
    for i in range(0,list["size"]):
        element=list["elements"][i]
        if element[criteria]!="":
            fecha=dt.datetime.strptime(element[criteria],"%Y-%m-%d")
            if fecha>=bottom and fecha<=top:
                lt.addLast(list_in_range,element)
    return list_in_range, lt.size(list_in_range)

## Requerimiento 3
def find_actor(list,name):
    list_with = lt.newList("ARRAY_LIST")
    for i in range(0,list["size"]):
        element=list["elements"][i]
        if element["cast"]!="":
            c = element["cast"].split(",")
            for i in range(0,len(c)):
                act_i = c[i].strip()
                if act_i == name:
                    lt.addLast(list_with,element)
    return list_with

## Requerimiento 4
def find_genre(list,name):
    list_with = lt.newList("ARRAY_LIST")
    for i in range(0,list["size"]):
        element=list["elements"][i]
        if element["listed_in"]!="":
            c = element["listed_in"].split(",")
            for i in range(0,len(c)):
                genre_i = c[i].strip()
                if genre_i == name:
                    lt.addLast(list_with,element)
    return list_with

## Requerimientos 5 y 6
def find_by(list,criteria,name):
    list_with = lt.newList("ARRAY_LIST")
    for i in range(0,list["size"]):
        element=list["elements"][i]
        if element[criteria]!="":
            if element[criteria] == name:
                lt.addLast(list_with,element)
    return list_with

def count_by(list,type,criteria):
    count=0
    for i in range(0,list["size"]):
        element=list["elements"][i]
        if element[criteria]!="":
            if element[criteria] == type:
                count+=1
    return count

## Requerimiento 6 y 7
def listed_in(list):
    genres = {}
    for i in range(0,list["size"]):
        element = list["elements"][i]
        if element["listed_in"] != "" :
            g = element["listed_in"].split(",")
            for i in range(0,len(g)):
                genre = g[i].strip()
                if genre not in genres.keys():
                    genres[genre]={"genre":1,"Movie":0,
                                    "TV Show":0,"Netflix":0,
                                    "Hulu":0,"Disney Plus":0,
                                    "Amazon Prime": 0 }
                    genres[genre][element["type"]]+=1
                    genres[genre][element["platform"]] +=1
                else:
                    genres[genre]["genre"]+=1
                    genres[genre][element["type"]] +=1
                    genres[genre][element["platform"]] +=1
                    
    listed = lt.newList("ARRAY_LIST")
    for key in genres.keys():
        lt.addLast(listed,(key,genres[key]))
    return listed 

## Requerimiento 8
def collabs(list,dicc,actor):
    pos=lt.isPresent(list,actor)
    if pos != 0:
        for i in range(list["size"]):
            if list["elements"][i] != actor :
                if dicc["Collaborations"] == None:
                    dicc["Collaborations"] = list["elements"][i]
                elif list["elements"][i] not in dicc["Collaborations"] :
                    dicc["Collaborations"] += list["elements"][i]+","       
    return dicc

def cast_count(list):
    lista = mergesortc(list,cmpByReleaseYear)
    actors = {}
    for i in range(0,lista["size"]):
        element = lista["elements"][i]
        if element["cast"] != "" :
            a = element["cast"].split(",")
            a_array =lt.newList("ARRAY_LIST")
            for elem in a :
                lt.addLast(a_array,elem)
            for i in range(0,len(a)):
                actor = a[i].strip()
                if actor not in actors.keys():
                    actors[actor]={"Total":1,"Movie":0,"TV Show":0,
                                    "Netflix":{"Total":0,"Movie":0,"TV Show":0},
                                    "Hulu":{"Total":0,"Movie":0,"TV Show":0},
                                    "Disney Plus":{"Total":0,"Movie":0,"TV Show":0},
                                    "Amazon Prime":{"Total":0,"Movie":0,"TV Show":0},
                                    "Collaborations":None}
                    actors[actor][element["type"]]+=1
                    actors[actor][element["platform"]][element["type"]] +=1
                    actors[actor][element["platform"]]["Total"] +=1
                else:
                    actors[actor]["Total"]+=1
                    actors[actor][element["type"]] +=1
                    actors[actor][element["platform"]][element["type"]] +=1
                    actors[actor][element["platform"]]["Total"] +=1
                collabs(a_array,actors[actor],a[i])
        else: 
            actor = "Unknown"
            if actor not in actors.keys():
                actors[actor]={"Total":1,"Movie":0,"TV Show":0,
                                "Netflix":{"Total":0,"Movie":0,"TV Show":0},
                                "Hulu":{"Total":0,"Movie":0,"TV Show":0},
                                "Disney Plus":{"Total":0,"Movie":0,"TV Show":0},
                                "Amazon Prime":{"Total":0,"Movie":0,"TV Show":0},
                                "Collaborations":"Unknown"}
                actors[actor][element["type"]]+=1
                actors[actor][element["platform"]][element["type"]] +=1
                actors[actor][element["platform"]]["Total"] +=1
            else:
                actors[actor]["Total"]+=1
                actors[actor][element["type"]] +=1
                actors[actor][element["platform"]][element["type"]] +=1
                actors[actor][element["platform"]]["Total"] +=1


    for actor in actors.keys():
        if actors[actor]["Collaborations"] != None:
            actors[actor]["Collaborations"][-1].replace(",","")
                
    cast = lt.newList("ARRAY_LIST")
    for key in actors.keys():
        lt.addLast(cast,(key,actors[key]))
    return cast
