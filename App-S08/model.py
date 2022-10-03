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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sc
from DISClib.Algorithms.Sorting import insertionsort as inter
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
from operator import itemgetter
from prettytable import PrettyTable as pretty
import datetime
assert cf
import time
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def crearCatalogo(ordenamiento):
    catalogo={"Amazon Prime":0,
            "Hulu":0,
            "Disney":0,
            "Netflix":0}
    for plataforma in catalogo:
        catalogo[plataforma]=lt.newList(datastructure=ordenamiento)
    return catalogo

# Funciones para agregar informacion al catalogo
def addContent(platform, content):
    lt.addLast(platform, content)

# Funciones para creacion de datos
def escoger_atributos(lista, atributos):
    listanueva=lt.newList(datastructure="ARRAY_LIST")
    for show in lt.iterator(lista):
        temp={}
        for atributo in atributos:
            temp[atributo]=show[atributo]
        lt.addLast(listanueva, temp)
    return listanueva

def formatoFecha(fecha):
    fecha=fecha.lower().strip(",")
    fecha=fecha.split(" ")
    if fecha[0][0]=="0":
        fecha[0]=fecha[0].strip("0")
    if fecha[0]=="january":
        fecha[0]=1
    if fecha[0]=="february":
        fecha[0]=2
    if fecha[0]=="march":
        fecha[0]=3
    if fecha[0]=="april":
        fecha[0]=4
    if fecha[0]=="may":
        fecha[0]=5
    if fecha[0]=="june":
        fecha[0]=6
    if fecha[0]=="july":
        fecha[0]=7
    if fecha[0]=="august":
        fecha[0]=8
    if fecha[0]=="september":
        fecha[0]=9
    if fecha[0]=="october":
        fecha[0]=10
    if fecha[0]=="november":
        fecha[0]=11
    if fecha[0]=="december":
        fecha[0]=12
    return fecha

# Funciones de consulta
def platformSize(list):
    return lt.size(list)


# Funciones utilizadas para comparar elementos dentro de una lista
def requerimiento1(desde, hasta, catalog):
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    sortcatalog(catalog, comparerequerimiento168)
    for plataforma in catalog:
        for show in lt.iterator(catalog[plataforma]):
            if show["release_year"]>=desde and show["release_year"]<=hasta and show["type"]=="Movie":
                temp={}
                temp["type"]=show["type"]
                temp["release_year"]=show["release_year"]
                temp["title"]=show["title"]
                temp["duration"]=show["duration"]
                temp["stream_service"]=show["stream_service"]
                temp["director"]=show["director"]
                temp["cast"]=show["cast"]
                lt.addLast(respuesta, temp)
    return respuesta
                
def requerimiento2(desde, hasta, catalog):
    sortcatalog(catalog, comparerequerimiento2)
    desde=datetime.date.fromisoformat(desde)
    hasta=datetime.date.fromisoformat(hasta)
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    for plataforma in catalog:
        for show in lt.iterator(catalog[plataforma]):
            if show["date_added"]!= "unknown":
                if datetime.date.fromisoformat(show["date_added"])>=desde and datetime.date.fromisoformat(show["date_added"])<=hasta and show["type"]=="TV Show":
                    temp={}
                    for atribute in show:
                        temp[atribute]=show[atribute]
                    lt.addLast(respuesta, temp)
    return respuesta

def requerimiento3(actorbuscar,catalog):
    sortcatalog(catalog, comparerequerimiento345)
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    tabla=lt.newList(datastructure="ARRAY_LIST")
    temp={"type":"count", "Movies":0, "TV Shows":0}
    actorbuscar=actorbuscar.lower().replace(" ", "")
    for plataforma in catalog:
        for show in lt.iterator(catalog[plataforma]):
            cast=show["cast"].lower().replace(" ", "")
            cast=cast.split(",")
            for actor in cast:
                if actorbuscar in actor:
                    lt.addLast(respuesta,show)
                    if show["type"]=="Movie":
                        temp["Movies"]+=1
                    elif show["type"]=="TV Show":
                        temp["TV Shows"]+=1
    lt.addLast(tabla,temp)
    return (respuesta, tabla)

def requerimiento4(generobuscar,catalog):
    sortcatalog(catalog, comparerequerimiento345)
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    tabla=lt.newList(datastructure="ARRAY_LIST")
    temp={"type":"count", "Movies":0, "TV Shows":0}
    generobuscar=generobuscar.lower().replace(" ", "")
    for plataforma in catalog:
        for show in lt.iterator(catalog[plataforma]):
            generos=show["listed_in"].lower().replace(" ", "")
            generos=generos.split(",")
            for g in generos:
                if generobuscar in g:
                    lt.addLast(respuesta,show)
                    if show["type"]=="Movie":
                        temp["Movies"]+=1
                    elif show["type"]=="TV Show":
                        temp["TV Shows"]+=1
    lt.addLast(tabla,temp)
    return (respuesta, tabla)

def requerimiento5(paisbuscar,catalog):
    sortcatalog(catalog, comparerequerimiento345)
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    tabla=lt.newList(datastructure="ARRAY_LIST")
    temp={"type":"count", "Movies":0, "TV Shows":0}
    paisbuscar=paisbuscar.lower().replace(" ", "")
    for plataforma in catalog:
        for show in lt.iterator(catalog[plataforma]):
            paises=show["country"].lower().replace(" ", "")
            paises=paises.split(",")
            for p in paises:
                if paisbuscar in p:
                    lt.addLast(respuesta,show)
                    if show["type"]=="Movie":
                        temp["Movies"]+=1
                    elif show["type"]=="TV Show":
                        temp["TV Shows"]+=1
    lt.addLast(tabla,temp)
    return (respuesta, tabla)
    
def requerimiento6(nombre, catalog):
    sortcatalog(catalog, comparerequerimiento168)
    tabla1=lt.newList(datastructure="ARRAY_LIST")
    tabla2=lt.newList(datastructure="ARRAY_LIST")
    tabla3=lt.newList(datastructure="ARRAY_LIST")
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    t1={"type":"count"}
    t2={"stream_service":"count"}
    t3={"listed_in":"count"}
    nombre=nombre.lower().replace(" ", "")
    for plataforma in catalog:
        for show in lt.iterator(catalog[plataforma]):
            generos=show["listed_in"].lower().split(", ")
            directores= show["director"].lower().replace(" ", "").split(",")
            for director in directores:
                if director==nombre:
                    lt.addLast(respuesta, show)
                    if show["type"] not in t1.keys():
                        tipo=show["type"]
                        t1[tipo]=1
                    else:
                        tipo=show["type"]
                        t1[tipo]+=1
                    if show["stream_service"] not in t2.keys():
                        tipo=show["stream_service"]
                        t2[tipo]=1
                    else:
                        tipo=show["stream_service"]
                        t2[tipo]+=1
                    for genero in generos:
                        if genero not in t3.keys():
                            t3[genero]=1
                        else:
                            t3[genero]+=1
    lt.addLast(tabla1,t1)
    lt.addLast(tabla2,t2)
    lt.addLast(tabla3,t3)

    return tabla1,tabla2,tabla3,respuesta

def requerimiento7(catalog, num):
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    tabla1=lt.newList(datastructure="ARRAY_LIST")
    atributos=["rank", "listed_in", "count", "Movie", "TV Show", "Amazon Prime","Hulu","Disney", "Netflix"]
    contadorestabla2={}
    generoscontadores={}
    for plataforma in catalog:
        for show in lt.iterator(catalog[plataforma]):
            generos=show["listed_in"].lower().split(", ")
            for genero in generos:
                if genero not in generoscontadores.keys():
                    generoscontadores[genero]=1
                else:
                    generoscontadores[genero]+=1
                if genero not in contadorestabla2:
                    contadorestabla2[genero]={}
                    for atributo in atributos:
                        contadorestabla2[genero][atributo]=0
                if show["type"]=="Movie":
                        contadorestabla2[genero]["Movie"]+=1
                elif show["type"]=="TV Show":
                        contadorestabla2[genero]["TV Show"]+=1
                contadorestabla2[genero][show["stream_service"]]+=1            
    contadorord=organizarcontador(generoscontadores)
    top=sacartop(contadorord, num)
    temp={"listed_in":"count"}
    for genero in top.values():
        temp[genero]=generoscontadores[genero]
    lt.addLast(tabla1, temp)
    i=1
    tabla2={}
    for genero in temp:
        if genero !="listed_in":
            contadorestabla2[genero]["rank"]=i
            contadorestabla2[genero]["count"]=temp[genero]
            contadorestabla2[genero]["listed_in"]=genero
            i+=1
            tabla2[genero]=contadorestabla2[genero]
    for genero in tabla2:
        lt.addLast(respuesta, tabla2[genero])
    return (tabla1,respuesta)

def organizarcontador(contador):
    contadorord=sorted(contador.items(), key=itemgetter(1), reverse=True)
    return contadorord

def sacartop(contadores, num):
    top={}
    for i in range(0,num):
        genero=contadores[i][1]
        numero=contadores[i][0]
        top[genero]=numero
    return top
   

# Funciones de ordenamiento
def sortcatalog(catalog, cmpfunction):
    start=getTime()
    for plataforma in catalog:
        plataforma=merge.sort(catalog[plataforma], cmpfunction)
    end=getTime()
    return (end-start)

def comparerequerimiento168(content1,content2):
    rta=False
    if int(content1["release_year"]) < int(content2["release_year"]):
        rta=True
    elif int(content1["release_year"]) == int(content2["release_year"]):
        if content1["title"] > content2["title"]:
            rta=True
        elif content1["title"] == content2["title"]:
            if int(content1["duration"].replace(" min", "").replace(" Season", ""))< int(content2["duration"].replace(" min", "").replace(" Season", "")):
                rta=True
    return rta

def comparerequerimiento2(content1,content2):
    rta=False
    if content1["date_added"]!="unknown" and content2["date_added"]!="unknown":
        fecha1=datetime.date.fromisoformat(content1["date_added"])
        fecha2=datetime.date.fromisoformat(content2["date_added"])
        if fecha1 < fecha2:
            rta=True
        elif fecha1 == fecha2:
            if content1["title"] > content2["title"]:
                rta=True
            elif content1["title"] == content2["title"]:
                if int(content1["duration"].replace(" min", "").replace(" Season", ""))< int(content2["duration"].replace(" min", "").replace(" Season", "")):
                    rta=True
    return rta

def comparerequerimiento345(content1,content2):
    rta=False
    if content1["title"] > content2["title"]:
        rta=True
    elif content1["title"] == content2["title"]:
        if int(content1["release_year"]) < int(content2["release_year"]):
            rta=True
        elif int(content1["release_year"]) == int(content2["release_year"]):
            if int(content1["duration"].replace(" min", "").replace(" Season", ""))< int(content2["duration"].replace(" min", "").replace(" Season", "")):
                rta=True
    return rta


def First3Last3(lista):
    tamaño=platformSize(lista)
    respuesta=lt.newList(datastructure="ARRAY_LIST")
    i=1
    if tamaño>=6:
        antepenultimo=tamaño-3
        penultimo=tamaño-2
        ultimo=tamaño-1
        util={"primero":1, "segundo":2, "tercero":3,"antepenultimo":antepenultimo,"penultimo":penultimo,"ultimo":ultimo}
        for posicion in util.values():
            elemento=lt.getElement(lista, posicion)
            lt.addLast(respuesta, elemento)
    elif tamaño<6:
        while i <= tamaño:
            elemento=lt.getElement(lista, i)
            lt.addLast(respuesta, elemento)
            i+=1
    
    return respuesta


def crear_tabla1(catalog,columna):
    tabla=pretty()
    tabla.field_names=columna
    tabla.add_rows([['netflix',lt.size(catalog['Netflix'])],
                    ['Hulu',lt.size(catalog['Hulu'])],['Disney',lt.size(catalog['Disney'])],
                    ['amazon prime',lt.size(catalog['Amazon Prime'])]])
    tabla.max_width=30
    return tabla

def crear_tablas(adtstructure):
    columnas=[]
    dc=lt.getElement(adtstructure, 1)
    valoresTabla=[]
    for key in dc.keys():
        columnas.append(key)
    for shows in lt.iterator(adtstructure):
        showtoadd=[]
        for atribute in shows.values():
            showtoadd.append(atribute)
        valoresTabla.append(showtoadd)
    tabla=pretty()
    tabla.field_names=columnas
    tabla.add_rows(valoresTabla)
    tabla.max_width=15
    return tabla

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

