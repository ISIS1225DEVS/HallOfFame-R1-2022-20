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


from email import header
from genericpath import getatime
from operator import truediv
from os import remove
from platform import platform
import config as cf
import textwrap
from tabulate import tabulate
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se 
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qs
from prettytable import PrettyTable
from prettytable import ALL
assert cf
import datetime 
import time 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(estructura="ARRAY_LIST"):
   
    catalog = {'Amazon Prime':None,
               'Disney+':None,
               'Hulu': None,
               'Netflix': None, 
               'total': None,
               'movies':None,
               'tvShows':None}
        
    for servicio in catalog:
        catalog[servicio]=lt.newList(estructura)
        
    return catalog


# Funciones para agregar informacion al catalogo
def addService(catalog, elem,service):
    for llave in elem:
        if elem[llave]=="":
            elem[llave]="Unknown"
    elem["Platform"]=service
    lt.addLast(catalog[service],elem)
    lt.addLast(catalog["total"],elem)
    if elem["type"]=="Movie":
        lt.addLast(catalog["movies"],elem)
    else:
        lt.addLast(catalog["tvShows"],elem)

    return catalog
   
def catalogZize(catalog,Service):
    return lt.size(catalog[Service])

def catalogGet(catalog,pos,platform):
    return lt.subList(catalog[platform],pos,3)

def sorting(new_list,type_sort):

    if type_sort=="selection":
        start_time=getTime()
        sort=se.sort(new_list, cmpMoviesByReleaseYear)
        end_time= getTime()
        delta_time = deltaTime(start_time, end_time)

    elif type_sort=="insertion":
        start_time=getTime()
        sort= ins.sort(new_list, cmpfunction=cmpMoviesByReleaseYear)
        end_time= getTime()
        delta_time = deltaTime(start_time, end_time)

    elif type_sort=="shell":
        start_time=getTime()
        sort= sa.sort(new_list, cmpfunction=cmpMoviesByReleaseYear)
        end_time= getTime()
        delta_time = deltaTime(start_time, end_time)

    elif type_sort=="merge":
        start_time=getTime()
        sort= me.sort(new_list, cmpfunction=cmpMoviesByReleaseYear)
        end_time= getTime()
        delta_time = deltaTime(start_time, end_time)

    else: 
        start_time=getTime()
        sort= qs.sort(new_list, cmpfunction=cmpMoviesByReleaseYear)
        end_time= getTime()
        delta_time = deltaTime(start_time, end_time)

    return round(delta_time,2)

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
def cmpString(str1,str2):
    var=False
    if str1<str2:
        var=True
    return var
def cmpMoviesByReleaseYear1(movie1, movie2):
    var=False
    if int(movie1["release_year"]) > int(movie2["release_year"]):
        var=True
    elif int(movie1["release_year"]) == int(movie2["release_year"]):
        if movie1["title"].lower() > movie2["title"].lower():
            var= True
        else:
            var=False
    else: 
        var=False 
    return var

def cmpMoviesByReleaseYear(movie1, movie2):
    var=False
    if int(movie1["release_year"]) < int(movie2["release_year"]):
        var=True
    elif int(movie1["release_year"]) == int(movie2["release_year"]):
        if movie1["title"] < movie2["title"]:
            var= True
        elif movie1["title"].lower() == movie2["title"].lower():
            movie1["duration"] < movie2["duration"]
        else:
            var=False 
    else: 
        var=False 
    return var

def cmpalphabetically(dict1, dict2):
    var=False
    if dict1["title"].lower() < dict2["title"].lower():
        var= True
    elif dict1["title"].lower() == dict2["title"].lower():
        if dict1["release_year"] < dict2["release_year"]:
            var= True
        elif dict1["release_year"] == dict2["release_year"]:
            if dict1["duration"] < dict2["duration"]:
                var= True 
    return var
    
def cmpdate(dict1, dict2):
    var=False
    if dict1["date_added"]!="" and dict2["date_added"]!="":
        date1=time.strptime(dict1["date_added"], "%Y-%m-%d")
        date2=time.strptime(dict2["date_added"], "%Y-%m-%d")
        if date1 > date2:
            var=True
        elif date1==date2:
            if dict1["title"].lower() > dict2["title"].lower():
                var= True
            elif dict1["title"].lower() == dict2["title"].lower():
                if dict1["duration"] > dict2["duration"]:
                    var= True
    return var

def cmpByTitle(dict1,dict2):
    var=False
    if dict1["title"].lower() < dict2["title"].lower():
        var= True
    elif dict1["title"].lower() == dict2["title"].lower():
        if dict1["release_year"] < dict2["release_year"]:
            var= True
        elif dict1["release_year"] == dict2["release_year"]:
            if dict1["director"] < dict2["director"]:
                var= True 
    return var
def cmpByCOunt(elem1,elem2):
    var=False
    if elem1[1]>elem2[1]:
        var=True
    return var
def cmpByCount_Name(elem1,elem2):
    var=False
    if elem1[1]>elem2[1]:
        var=True
    elif elem1[1]==elem2[1]:
        if elem1[0].lower()>elem2[0].lower():
            var=True
    return var

def primeros_ultimos(list, no_titles, cmp):
    list=me.sort(list, cmp)
    if lt.size(list)>=6:
        primeros=lt.subList(list,1,3)
        ultimos=lt.subList(list,-2,3)
        list=lt.newList("ARRAY_LIST")
        for elem in lt.iterator(primeros):
            lt.addLast(list,elem)
        for elem in lt.iterator(ultimos):
            lt.addLast(list,elem)
    titulos=[]
    filas=[]
    for elem in lt.iterator(list):
        temp=[]
        for titulo in elem:
            if titulo not in no_titles:
                if titulo not in titulos:
                    titulos.append(titulo)
                if titulo=="description":
                    temp.append(textwrap.fill(elem[titulo],width=10))
                else:
                   temp.append(elem[titulo]) 
                   
        filas.append(temp)
    return filas, titulos

def req1_movies_in_date(catalog, start_year, end_year, no_titles, cmp):
    start_year=time.strptime(start_year, "%Y")
    end_year=time.strptime(end_year, "%Y")
    final=lt.newList("ARRAY_LIST")
    for var in lt.iterator(catalog["movies"]):
        year=time.strptime(var["release_year"][:4], "%Y")
        if (year>=start_year) and (year<=end_year):
            lt.addLast(final, var)
    final=me.sort(final, cmp)
    filas, titulos=primeros_ultimos(final, no_titles, cmp)
    return filas,titulos, lt.size(final)

def req2_tv_in_date(catalog, start_date, end_date, no_titles, cmp):
    start_date=time.strptime(start_date, "%Y-%m-%d")
    end_date=time.strptime(end_date, "%Y-%m-%d")
    final=lt.newList("ARRAY_LIST")
    for var in lt.iterator(catalog["tvShows"]):
        if var["date_added"]!="Unknown":
            date=time.strptime(var["date_added"], "%Y-%m-%d")
            if (date>start_date) and (date<end_date):
                lt.addLast(final, var)
    final=me.sort(final, cmp)
    filas,titulos=primeros_ultimos(final, no_titles, cmp)
    return filas,titulos, lt.size(final)
    

def req3_search_actor(catalog, actor, no_titles, cmp):
    n_movies=0
    n_tv_shows=0
    final=lt.newList("ARRAY_LIST")
    for var in lt.iterator(catalog["total"]):
        if var["type"] == "Movie":
            if actor in var["cast"]:
                lt.addLast(final, var)
                n_movies+=1
        if var["type"] == "Tv Show":
            if actor in var["cast"]:
                lt.addLast(final, var)
                n_tv_shows+=1
    final=me.sort(final, cmp)
    x=primeros_ultimos(final, no_titles, cmp)
    return x, {"Type":["Movies", "Tv Shows"],"Count": [n_movies, n_tv_shows]}

def req4_ist_genre(catalog,genero,cmp,no_titles):
    n_movies=0
    n_tv_shows=0
    services={"Amazon Prime":0,"Netflix":0,"Hulu":0,"Disney+":0}
    final=lt.newList("ARRAY_LIST")
    for var in lt.iterator(catalog["total"]):
        if genero in var["listed_in"]:
            if var["type"]=="Movie":
                n_movies+=1
            else:
                n_tv_shows+=1
            services[var["Platform"]]+=1
            
            lt.addLast(final,var)
    count={"stream_service":[],"count":[]}
    for service in list(services):
        if services[service]==0:
            services.pop(service)
    for service in services:
        count["stream_service"].append(service)
        count["count"].append(services[service])
    
    final=me.sort(final, cmp)
    filas,columnas=primeros_ultimos(final,no_titles,cmp)
    return n_movies,n_tv_shows,filas,columnas,count

def req5_search_pais(catalog,pais,no_titles,cmp):
    num_movies=0
    num_tvshows=0
    lista_total=lt.newList("ARRAY_LIST")
    for bpais in lt.iterator(catalog["total"]):
        if pais in bpais["country"]:
            if bpais["type"] == "Movie":
                num_movies+=1
            else:
                num_tvshows+=1
            lt.addLast(lista_total, bpais)

    lista_total=me.sort(lista_total, cmp)
    prim_ult=primeros_ultimos(lista_total,no_titles, cmp)

    return prim_ult, {"Type":["Movies", "Tv Shows"],"Count": [num_movies, num_tvshows]}

def req6_search_c_with_director(catalog, director, no_titles, cmp):
    movies_tvshows_genre={}
    n_movies_tv_shows_plataform={}
    final=lt.newList("ARRAY_LIST")
    for var in lt.iterator(catalog["total"]):
        if director in var["director"]:
            lt.addLast(final, var)
    for var in lt.iterator(final):
        for genre in var["listed_in"].split(sep=","):
            if genre not in movies_tvshows_genre:
                movies_tvshows_genre[genre]=0
            if genre in movies_tvshows_genre:
                movies_tvshows_genre[genre]+=1

        if var["Platform"] not in n_movies_tv_shows_plataform:
            n_movies_tv_shows_plataform[var["Platform"]]=0
        if var["Platform"] in n_movies_tv_shows_plataform:
            n_movies_tv_shows_plataform[var["Platform"]]+=1
    
    platforms=[]
    count=[]
    for plt in n_movies_tv_shows_plataform:
        platforms.append(plt)
        count.append(n_movies_tv_shows_plataform[plt])
    
    if len(movies_tvshows_genre)>6:
        primeros=dict(list(movies_tvshows_genre.items())[:3])
        ultimos=dict(list(movies_tvshows_genre.items())[-3:])
        movies_tvshows_genre=primeros.update(ultimos)
    genero=[]
    countg=[]
    for gen in movies_tvshows_genre:
        genero.append(gen)
        countg.append(movies_tvshows_genre[gen])
    final=me.sort(final, cmp)
    filas,columnas=primeros_ultimos(final,no_titles,cmp)
    x={"Type": ["Movies and Tv Shows"], "Count": [lt.size(final)]}
    y={"Service name": platforms, "Count": count}
    z={"Listed_in" : genero, "Count": countg}

    return x , y, filas, columnas, z

def req7_top_list(catalog,top):
    generos={}
    lista_generos=lt.newList("ARRAY_LIST")
    
    for elem in lt.iterator(catalog["total"]):
        for genero in elem["listed_in"].split(", "):
    
                if genero in generos:
                    generos[genero]+=1

                else:
                    generos[genero]=1

    tabla_generos={"listed_in":[],"count":[]}
    tabla_type={"type":["Movies","Tv_shows"],"count":[]}
    tabla_f={"Rank":[],"listed_in":[],"count":[],"type":[],"stream_service":[]}
    for genero in generos:
        lt.addLast(lista_generos,(genero,generos[genero]))
    me.sort(lista_generos,cmpByCOunt)
    top_generos=lt.subList(lista_generos,1,top)
    i=1
    for elem in lt.iterator(top_generos):
        total=req4_ist_genre(catalog,elem[0],cmpByTitle,"typedurationshow_idPlatform")
        tabla_generos["listed_in"].append(elem[0])
        tabla_f["count"].append(elem[1])
        tabla_f["listed_in"].append(elem[0])
        tabla_generos["count"].append(elem[1])
        tabla_type["count"].append(total[0])
        tabla_type["count"].append(total[1])
        tabla_f["type"].append(tabulate(tabla_type,headers="keys"))
        tabla_f["stream_service"].append(tabulate(total[-1],headers="keys"))
        tabla_f["Rank"].append(i)
        i+=1
    
    return tabla_generos,tabla_f
def colaborations(catalog,actor):
    colaboraciones=[]
    lista=lt.newList("ARRAY_LIST")
    for elem in lt.iterator(catalog["total"]):
        if actor in elem["cast"]:
            for actore in elem["cast"].split(", "):
                if actore!=actor:
                    if actore not in colaboraciones:
                        
                        lt.addLast(lista,actore)
    me.sort(lista,cmpString)
    for colab in lt.iterator(lista):
        colaboraciones.append(colab)
    a= ",".join(colaboraciones)
    return textwrap.fill(a,width=60)
            
def mayor_listed(catalog,actor):
    lista_final=lt.newList("ARRAY_LIST")
    generos={}
    for elem in lt.iterator(catalog["total"]):
        for genero in elem["listed_in"].split(", "):
            if actor in elem["cast"]:
                if genero in generos:
                    generos[genero]+=1
                else:
                    generos[genero]=1
    for genero in generos:
        lt.addLast(lista_final,(genero,generos[genero]))
    me.sort(lista_final,cmpByCount_Name)
    a=lt.firstElement(lista_final)
    return a[0]

def count_by_actor(catalog,actor):
    tabla={"stream_service":[],"type":[],"count":[]}
    type={"Netflix":{"Movie":0,"TV Show":0},"Amazon Prime":{"Movie":0,"TV Show":0},"Hulu":{"Movie":0,"TV Show":0},"Disney+":{"Movie":0,"TV Show":0}}
    
    for elem in lt.iterator(catalog["total"]):
        if actor in elem["cast"]:
            type[elem["Platform"]][elem["type"]]+=1
    
    for clave,valor in type.items():
        for type in valor:
            if valor[type]>0:
                tabla["stream_service"].append(clave)
                tabla["type"].append(type)
                tabla["count"].append(valor[type])
        
                
    return tabulate(tabla,headers="keys")
def req8_topActroes(catalog,top):
    actores={}
    lista_actores=lt.newList("ARRAY_LIST")
  
    
    for elem in lt.iterator(catalog["total"]):
        for actor in elem["cast"].split(", "):

                if actor in actores:
                    actores[actor]+=1
                else:
                    actores[actor]=1
    tabla2={"actor":[],"content_type":[]}
    tabla={"actor":[],"count":[],"top_listed_in":[]}
    tabla3={"actor":[],"colaborations":[]}
    for actor in actores:
        genero=mayor_listed(catalog,actor)
        lt.addLast(lista_actores,(actor,actores[actor],genero,count_by_actor(catalog,actor),colaborations(catalog,actor)))
        
    me.sort(lista_actores,cmpByCount_Name)
    top=lt.subList(lista_actores,1,top)
    for elem in lt.iterator(top):
        tabla["actor"].append(elem[0])
        tabla2["actor"].append(elem[0])
        tabla["count"].append(elem[1])
        tabla["top_listed_in"].append(elem[2])
        tabla2["content_type"].append(elem[3])
        tabla3["actor"].append(elem[0])
        tabla3["colaborations"].append(elem[4])

    return tabla,tabla2,tabla3




def imprimir_tabla(columnas,filas):
    myTable=PrettyTable(columnas)
    for i in filas:
            myTable.add_row(i)
    myTable.max_width=10
    myTable.hrules=ALL
    print(myTable)
