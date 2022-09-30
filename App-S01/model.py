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
import time
from datetime import datetime
import operator
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ist
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as quick 
assert cf


def newCatalog(struc):
    catalog = {'nf': None, 'am': None, 'dy': None, 'hl': None, 'mix':None}
    catalog['mix'] = lt.newList(struc,cmpfunction=cmpMoviesByReleaseYear)
    catalog['nf'] = lt.newList(struc,cmpfunction=cmpMoviesByReleaseYear)
    catalog['am'] = lt.newList(struc,cmpfunction=cmpMoviesByReleaseYear)
    catalog['dy'] = lt.newList(struc,cmpfunction=cmpMoviesByReleaseYear)
    catalog['hl'] = lt.newList(struc,cmpfunction=cmpMoviesByReleaseYear)
    return catalog

def addMovie(catalog, book,plat,plat2=''):
    book['stream_service']=plat2
    lt.addLast(catalog[plat], book)
    return catalog

def titleSize(catalog,plat):
    return lt.size(catalog[plat])


def cmpMoviesByReleaseYear(movie1, movie2):
    if movie1['release_year']==movie2['release_year']:
        if movie1['title'].lower() == movie2['title'].lower():
            if movie1['duration']<movie2['duration']:
                return 1
        elif movie1['title'].lower() < movie2['title'].lower():
            return 1
        else:
            return 0
    elif movie1['release_year']<movie2['release_year']:
        return 1
    else:
        return 0

def cmpMoviesByTitle(movie1, movie2):
    if movie1['title'].lower()==movie2['title'].lower():
        if movie1['release_year'] == movie2['release_year']:
            if movie1['director'] < movie2['director']:
                return 1
        elif movie1['release_year'] < movie2['release_year']:
            return 1
        else:
            return 0
    elif movie1['title'].lower()<movie2['title'].lower():
        return 1
    else:
        return 0

def cmpMoviesByDateAdded(movie1, movie2):
    try:
        if datetime.strptime(movie1['date_added'],"%Y-%m-%d")==datetime.strptime(movie2['date_added'],"%Y-%m-%d"):
            if movie1['title'].lower() == movie2['title'].lower():
                if movie1['duration']<movie2['duration']:
                    return 0
                else:
                    return 1
            elif movie1['title'].lower() < movie2['title'].lower():
                return 0
            else:
                return 0
        elif datetime.strptime(movie1['date_added'],"%Y-%m-%d")<datetime.strptime(movie2['date_added'],"%Y-%m-%d"):
            return 0
        else:
            return 1
    except:
        if movie1['date_added']=='':
            return 1
        elif movie2['date_added']=='':
            return 0
        else: 
            return 1        

def cmpByCantidad(actor1,actor2):
    #print(actor1[1])
    if actor1[1]>actor2[1]:
        return 1
    else:
        return 0



def getPrimeros(catalog, number,plat):
    movies = catalog[plat]
    bestmovies = lt.newList()
    for cont in range(1, number+1):
        movie = lt.getElement(movies, cont)
        lt.addLast(bestmovies, movie)
    return bestmovies

def getUltimos(catalog, number,plat):
    movies = catalog[plat]
    bestmovies = lt.newList()
    for cont in range(lt.size(catalog[plat]), lt.size(catalog[plat])-number,-1):
        movie = lt.getElement(movies, cont)
        lt.addLast(bestmovies, movie)
    return bestmovies

def getMoviesPais(catalog, pais):
    start_time=getTime()
    movies = catalog['mix']
    movies_pais_TV=lt.newList('ARRAY_LIST')
    movies_pais_Peli=lt.newList('ARRAY_LIST')
    for i in range(lt.size(catalog['mix'])): 
        movie = lt.getElement(movies, i)
        if movie['country']==pais and movie['type']=='TV Show':
            lt.addLast(movies_pais_TV, movie)
        elif movie['country']==pais and movie['type']=='Movie':
            lt.addLast(movies_pais_Peli, movie)
    mer.sort(movies_pais_TV, cmpMoviesByTitle)
    mer.sort(movies_pais_Peli, cmpMoviesByTitle)
    end_time=getTime()
    times=deltaTime(start_time,end_time)
    return movies_pais_TV, movies_pais_Peli,round(times,3)

def getMoviesAno(catalog,f_ini,f_fin):
    start_time=getTime()
    movies = catalog['mix']
    movies_fecha_Peli=lt.newList('ARRAY_LIST')
    for i in range(lt.size(catalog['mix'])): 
        movie = lt.getElement(movies, i)
        if int(movie['release_year']) >=f_ini and int(movie['release_year'])<=f_fin and movie['type']=='Movie':
            lt.addLast(movies_fecha_Peli, movie)
    mer.sort(movies_fecha_Peli, cmpMoviesByReleaseYear)
    end_time=getTime()
    times=deltaTime(start_time,end_time)
    return movies_fecha_Peli,round(times,3)

def getMoviesFecha(catalog,f_ini,f_fin):
    start_time=getTime()
    movies = catalog['mix']
    movies_fecha_Peli=lt.newList('ARRAY_LIST')
    for i in range(lt.size(catalog['mix'])): 
        movie = lt.getElement(movies, i)
        if movie['date_added']!='':
            if datetime.strptime(movie['date_added'],"%Y-%m-%d") >=f_ini and datetime.strptime(movie['date_added'],"%Y-%m-%d")<=f_fin and movie['type']=='TV Show':
                lt.addLast(movies_fecha_Peli, movie)
    mer.sort(movies_fecha_Peli, cmpMoviesByDateAdded)
    end_time=getTime()
    times=deltaTime(start_time,end_time)
    return movies_fecha_Peli,round(times,3)

def getTopActores(catalog,top):
    start_time=getTime()
    movies=catalog['mix']
    mer.sort(movies, cmpMoviesByDateAdded)
    cuenta={}
    for i in lt.iterator(movies):
        actor=i['cast']
        if actor=='':
            if 'Unknown' in cuenta.keys():
                cuenta['Unknown']+=1
            else:
                cuenta['Unknown']=1
        elif ',' in actor:
            lista_actores=actor.split(', ')
            for i in lista_actores:
                if i in cuenta.keys():
                    cuenta[i]+=1
                else:
                    cuenta[i]=1
        else:
            if actor in cuenta.keys():
                cuenta[actor]+=1
            else:
                cuenta[actor]=1
    lista_cuenta=lt.newList('ARRAY_LIST')
    for i in cuenta:
        lt.addLast(lista_cuenta,[i,cuenta[i]])
    
    mer.sort(lista_cuenta,cmpByCantidad)
    top_n=lt.subList(lista_cuenta,1,top)
    info_actores={}
    
    for i in lt.iterator(top_n):
        listica_colab=[]
        for j in lt.iterator(movies):
            if i[0] in j['cast'] or (i[0]=='Unknown' and j['cast']==''):

                if i[0] in info_actores.keys():
                
                    if ',' in j['listed_in']:
                        lista_genero=j['listed_in'].split(', ')
                        for k in lista_genero:
                            if k in info_actores[i[0]]['genero']:
                                info_actores[i[0]]['genero'][k]+=1
                            else:
                                info_actores[i[0]]['genero'][k]=1
                    else:
                        if j['listed_in'] in info_actores[i[0]]['genero']:
                            info_actores[i[0]]['genero'][j['listed_in']]+=1
                        else:
                            info_actores[i[0]]['genero'][j['listed_in']]=1 

                    info_actores[i[0]][j['stream_service']][j['type']]+=1

                    if ',' in j['cast']:
                        lista_colab=j['cast'].split(', ')
                        for k in lista_colab:
                            if k not in info_actores[i[0]]['colaborations']:
                                if j['cast']=='':
                                    info_actores[i[0]]['colaborations']='Unknown'
                                listica_colab.append(k)  
                    else:
                        if j['cast']!='':
                            info_actores[i[0]]['colaborations']=info_actores[i[0]]['colaborations']+', '+j['cast']
                
                else:
                    info_actores[i[0]]={'genero':{},'netflix':{'TV Show':0,'Movie':0},'amazon prime':{'TV Show':0,'Movie':0},'hulu':{'TV Show':0,'Movie':0},'disney plus':{'TV Show':0,'Movie':0},'colaborations':''}
                    info_actores[i[0]][j['stream_service']][j['type']]+=1
                    if ',' in j['cast']:
                        lista_colab=j['cast'].split(', ')
                        for k in lista_colab:
                            if k not in info_actores[i[0]]['colaborations']:
                                
                                listica_colab.append(k)
                    else:
                        if j['cast']=='':
                            info_actores[i[0]]['colaborations']='Unknown'
        esta=True
        while esta:
            if i[0] in listica_colab:
                listica_colab.remove(i[0])
            else:
                esta=False
        listica_colab.sort()
        
        for colab in listica_colab:
            if info_actores[i[0]]['colaborations']=='':
                info_actores[i[0]]['colaborations']=colab
            else:
                info_actores[i[0]]['colaborations']=info_actores[i[0]]['colaborations']+', '+colab
    end_time=getTime()
    times=deltaTime(start_time,end_time)
    return lista_cuenta, info_actores, round(times,3)

def getGeneros(catalog,genero):
    start_time=getTime()
    peliculas= catalog["mix"]
    
    peliculascongenero=lt.newList("ARRAY_LIST")
    for cont in range(lt.size(peliculas)):
        movie=lt.getElement(peliculas, cont)

        if genero in movie["listed_in"] and movie["type"] =="Movie":
            lt.addLast(peliculascongenero, movie)
    num_peliculas_genero= lt.size(peliculascongenero)
    """ 2 """
    shows=lt.newList("ARRAY_LIST")
    for cont in range(lt.size(peliculas)):
        movie=lt.getElement(peliculas, cont)
        if genero in movie["listed_in"] and movie["type"] =="TV Show":
            lt.addLast(shows, movie)
    num_shows_genero= lt.size(shows)

    todas=lt.newList("ARRAY_LIST")
    for cont in range(lt.size(peliculas)):
        movie=lt.getElement(peliculas, cont)
        if genero in movie["listed_in"] :
            lt.addLast(todas, movie)

    mer.sort(todas, cmpMoviesByTitle)
    end_time=getTime()
    times=deltaTime(start_time,end_time)
    return  num_peliculas_genero, num_shows_genero, todas,round(times,3)

def req6(catalog, director):
    start_time=getTime()
    peliculas= catalog["mix"]
    filtro_director=lt.newList("ARRAY_LIST")
    for cont in lt.iterator(peliculas):
        if director in cont["director"] :
            lt.addLast(filtro_director, cont)

    num_todo_director= lt.size(filtro_director)
    
    mer.sort(filtro_director, cmpMoviesByReleaseYear)

    num_movies_director= 0
    num_shows_director=0
    numero_generos_autordic={} 
    for cont in lt.iterator(filtro_director):
        if cont["type"] =="Movie":
            num_movies_director+=1
        elif cont["type"] =="TV Show":
            num_shows_director=+1
        x=cont["listed_in"]
        if ',' in x:
            genero_x_pelicula=x.split(', ')
            for i in genero_x_pelicula:
                if i in numero_generos_autordic:
                    numero_generos_autordic[i]+=1
                else:
                    numero_generos_autordic[i]=1
    
    numero_generos_autor=[]
    for i in numero_generos_autordic:
        j=[i,numero_generos_autordic[i]]
        numero_generos_autor.append(j)

    plataformasdic={}
    for cont in lt.iterator(filtro_director):
        plat=cont["stream_service"]
        if plat in plataformasdic:
            plataformasdic[plat]+=1
        else:
            plataformasdic[plat]=1
    
    plataformas=[]
    for i in plataformasdic:
        j=[i,plataformasdic[i]]
        plataformas.append(j)
    end_time=getTime()
    times=deltaTime(start_time,end_time)
    return num_todo_director,num_movies_director, num_shows_director, numero_generos_autor, plataformas, filtro_director,round(times,3)

def buscar_por_actor(catalog, actor):
    start_time=getTime()
    movies = catalog["mix"]
    lista_actor = lt.newList("ARRAY_LIST")
    size_lista = lt.size(catalog["mix"])
    numero_peliculas = 0
    numero_shows = 0
    for i in range(size_lista):
        posicion = i
        elemento_lista = lt.getElement(movies,posicion)
        if actor in elemento_lista["cast"]:
                lt.addLast(lista_actor,elemento_lista)
                if elemento_lista["type"] == "Movie":
                    numero_peliculas += 1
                else:
                    numero_shows += 1

    mer.sort(lista_actor, cmpMoviesByTitle)
    end_time=getTime()
    times=deltaTime(start_time,end_time)
    return lista_actor, numero_peliculas, numero_shows, round(times,3)

def getTopGeneros(catalog, top):
    start_time=getTime()
    movies=catalog['mix']
    cuenta={}
    for i in lt.iterator(movies):
        genero=i['listed_in']
        if genero=='':
            if 'Unknown' in cuenta.keys():
                cuenta['Unknown']+=1
            else:
                cuenta['Unknown']=1
        elif ',' in genero:
            lista_actores=genero.split(', ')
            for i in lista_actores:
                if i in cuenta.keys():
                    cuenta[i]+=1
                else:
                    cuenta[i]=1
        else:
            if genero in cuenta.keys():
                cuenta[genero]+=1
            else:
                cuenta[genero]=1
    
    lista_cuenta=lt.newList('ARRAY_LIST')
    for i in cuenta:
        lt.addLast(lista_cuenta,[i,cuenta[i]])
    mer.sort(lista_cuenta,cmpByCantidad)
    print(lista_cuenta)
    top_n=lt.subList(lista_cuenta,1,top)
    info_genero={}
    for i in lt.iterator(top_n):
        listica_colab=[]
        for j in lt.iterator(movies):
            if i[0] in j['listed_in']:
                if i[0] in info_genero.keys():
                    info_genero[i[0]][j['stream_service']]+=1
                    info_genero[i[0]][j['type']]+=1
                else:
                    info_genero[i[0]]={'Movie':0,'TV Show':0,'netflix':0,'amazon prime':0,'hulu':0,'disney plus':0}
                    info_genero[i[0]][j['stream_service']]+=1
                    info_genero[i[0]][j['type']]+=1
                            

    print(info_genero)
    end_time=getTime()
    times=deltaTime(start_time,end_time)            
    return lista_cuenta, info_genero, round(times,3)

def sortMovies(catalog,plat):
    sa.sort(catalog[plat], cmpMoviesByTitle)

def sortList(catalog, sort):
    if sort=='1':
        start_time = getTime()
        #ss.sort(catalog['mix'], cmpMoviesByReleaseYear)
        ss.sort(catalog['nf'], cmpMoviesByReleaseYear)
        ss.sort(catalog['am'], cmpMoviesByReleaseYear)
        ss.sort(catalog['hl'], cmpMoviesByReleaseYear)
        ss.sort(catalog['dy'], cmpMoviesByReleaseYear)
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
    elif sort=='2':
        start_time = getTime()
        #ist.sort(catalog['mix'], cmpMoviesByReleaseYear)
        ist.sort(catalog['nf'], cmpMoviesByReleaseYear)
        ist.sort(catalog['am'], cmpMoviesByReleaseYear)
        ist.sort(catalog['hl'], cmpMoviesByReleaseYear)
        ist.sort(catalog['dy'], cmpMoviesByReleaseYear)
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
    elif sort=='3':
        start_time = getTime()
        #sa.sort(catalog['mix'], cmpMoviesByReleaseYear)
        sa.sort(catalog['nf'], cmpMoviesByReleaseYear)
        sa.sort(catalog['am'], cmpMoviesByReleaseYear)
        sa.sort(catalog['hl'], cmpMoviesByReleaseYear)
        sa.sort(catalog['dy'], cmpMoviesByReleaseYear)
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
    elif sort == "4":
        start_time = getTime()
        #sa.sort(catalog['mix'], cmpMoviesByReleaseYear)
        mer.sort(catalog['nf'], cmpMoviesByReleaseYear)
        mer.sort(catalog['am'], cmpMoviesByReleaseYear)
        mer.sort(catalog['hl'], cmpMoviesByReleaseYear)
        mer.sort(catalog['dy'], cmpMoviesByReleaseYear)
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
    elif sort == "5":
        start_time = getTime()
        #sa.sort(catalog['mix'], cmpMoviesByReleaseYear)
        quick.sort(catalog['nf'], cmpMoviesByReleaseYear)
        quick.sort(catalog['am'], cmpMoviesByReleaseYear)
        quick.sort(catalog['hl'], cmpMoviesByReleaseYear)
        quick.sort(catalog['dy'], cmpMoviesByReleaseYear)
        end_time = getTime()
        delta_time = deltaTime(start_time, end_time)
    else:
        delta_time=0
    return delta_time


def getTime():
    return float(time.perf_counter()*1000)

def deltaTime(start, end):
    elapsed = float(end - start)
    return elapsed

#