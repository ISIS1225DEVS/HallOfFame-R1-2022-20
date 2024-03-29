﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 #

from calendar import c
import config as cf
import sys
import os
from datetime import datetime
import controller
from DISClib.ADT import list as lt
from tabulate import tabulate
assert cf

def printMovies(movies):
    size = lt.size(movies)
    if size:
        headers = [list(movies['first']['info'].keys())]
        table=[]
        for movie in lt.iterator(movies):
            table.append([movie['show_id'],movie['type'],movie['title'],movie['director'],movie['cast'],movie['country'],movie['date_added'],movie['release_year'],movie['rating'],movie['duration'],movie['listed_in'],movie['description'],movie['stream_service']])
        print(tabulate(table,headers[0],tablefmt="grid",maxcolwidths=14))    
        print('\n')    
    else:
        print('No se encontraron peliculas')
    
def printMoviesCant(movies,cant,head):
    size = lt.size(movies)
    if size:
        
        table=[]
        i=1
        for movie in lt.iterator(movies):
            headers = []
            for j in range(len(head)):
                headers.append(movie[head[j]])
            table.append(headers)
            if i==cant:
                break
            else:
                i+=1
        if size>=cant*2:
            i=0
            for movie in lt.iterator(movies):
                headers = []
                if size-i<=cant:
                    for j in range(len(head)):
                        headers.append(movie[head[j]])
                    table.append(headers)
                if size-i==0:
                    break
                else:
                    i+=1
        print(tabulate(table,head,tablefmt="grid",maxcolwidths=14))    
        print('\n')

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar películas estrenadas en un periodo de tiempo")
    print("3- Consultar programas de TV agregados en un periodo de tiempo")
    print("4- Cosultar contenido por actor")
    print("5- Cosultar contenido por género")
    print("6- Cosultar contenido por país")
    print("7- Cosultar contenido por director involucrado")
    print("8- Cosultar el Top x de los géneros con más contenido")
    print("9- Cosultar el Top x de los actores con más participación")
    print("10- Ordenar los datos")
    print("0- Salir")


def newController(struc):
    control = controller.newController(struc)
    return control

def loadData(control,archiv):
    movies= controller.loadData(control,archiv)
    return movies


def playLoadData():
    print('\nCuántos datos desea cargar?')
    print('1: 0.5% de los datos')
    print('2: 5% de los datos')
    print('3: 10% de los datos')
    print('4: 20% de los datos')
    print('5: 30% de los datos')
    print('6: 50% de los datos')
    print('7: 80% de los datos')
    print('8: 100% de los datos')
    resp=int(input())
    if resp==1:
        archiv='small.csv'
    elif resp==2:
        archiv='5pct.csv'
    elif resp==3:
        archiv='10pct.csv'
    elif resp==4:
        archiv='20pct.csv'
    elif resp==5:
        archiv='30pct.csv'
    elif resp==6:
        archiv='50pct.csv'
    elif resp==7:
        archiv='80pct.csv'
    elif resp==8:
        archiv='large.csv'
    nf,am,hl,dy,features= loadData(catalog,archiv)
    os.system('cls')
    print('----------------------------------')
    print('Loaded straming service info: ')
    print('Total loaded titles: '+str(nf+am+hl+dy))
    print('Total features loaded: '+str(features))
    print('----------------------------------')
    table = [["Netflix",nf],["Amazon",am],["Disney",dy],['Hulu',hl]]
    headers = ["Stream Service", "Count"]
    print(tabulate(table, headers, tablefmt="grid"))
    print('\n------ Content per stream service sorted by title ------')
    plats=['nf','am','dy','hl']
    plats_nombres=['Netflix','Amazon Prime','Disney Plus','Hulu']
    for i in range(4):
        print(f'\n{plats_nombres[i]}')
        print('First 3:')
        firstmovies = controller.getBestBooks(catalog, 3,plats[i])
        printMovies(firstmovies)
        print('Last 3:')
        lastmovies = controller.getLastMovies(catalog, 3,plats[i])
        printMovies(lastmovies)

def playReq1():
    ano_ini=int(input('\nIngrese el año de inicio: '))
    ano_fin=int(input('Ingrese el año de fin: '))
    Peli,time = controller.getMoviesAno(catalog, ano_ini,ano_fin)
    os.system('cls')
    print('============ Req No. 1 Inputs ============')
    print(f'Movie released between {ano_ini} and {ano_fin}')

    print('\n============ Req No. 1 Answer ============')
    print(f'There are {lt.size(Peli)} IPs (Intelectual Properties) in "Movie" type released between {ano_ini} and {ano_fin}')
    print('The first 3 and last 3 IPs in range are:')
    head=['type','release_year','title','duration','stream_service','director','cast']
    printMoviesCant(Peli,3,head) if lt.size(Peli)>0 else print(f'No hay peliculas entre los años {ano_ini} y {ano_fin}')
    print('Tiempo de ejecución:',time,'ms\n')

def playReq2():
    ano_ini=datetime.strptime(input('\nIngrese la fecha de inicio: '), "%B %d, %Y")
    ano_fin=datetime.strptime(input('Ingrese la fecha de fin: '), "%B %d, %Y")
    Tv, time = controller.getMoviesFecha(catalog, ano_ini,ano_fin)
    os.system('cls')
    print('============ Req No. 2 Inputs ============')
    print(f'"TV Show" released between {str(ano_ini)[:10]} and {str(ano_fin)[:10]}')

    print('\n============ Req No. 2 Answer ============')
    print(f'There are {lt.size(Tv)} IPs (Intelectual Properties) between {str(ano_ini)[:10]} and {str(ano_fin)[:10]}')
    print('The first 3 and last 3 IPs in range are:')
    head=['type','date_added','title','duration','release_year','stream_service','director','cast']
    printMoviesCant(Tv,3,head) if lt.size(Tv)>0 else print(f'No hay peliculas entre los años {datetime.strftime(ano_ini, "%Y-%m-%d")} y {datetime.strftime(ano_fin, "%Y-%m-%d")}')
    print('Tiempo de ejecución:',time,'ms\n')

def playReq3():
    casting = input("\nIngrese el nombre del actor que desea buscar: ")
    info_actor,a,b,timesito = controller.getActor(catalog, casting)
    os.system('cls')
    print('============ Req No. 3 Inputs ============')
    print(f'Content with {casting} in the "cast"')
    
    print('\n============ Req No. 3 Answer ============')
    print(f'------ "{casting}" cast participation count ------')
    numero_peliculas_y_shows = [["Movie",a],["TV Show",b]]
    print(tabulate(numero_peliculas_y_shows,['type','count'],tablefmt='grid'))
    
    print(f'\n------ Participation Detalis ------')
    print(f'There are less than 6 participation of "{casting}" on record') if lt.size(info_actor)<6 else print(f'The first 3 and last 3 IPs of "{casting}" are:')
    headers = ['type','title','release_year','director','stream_service','duration','cast','country','listed_in','description']
    printMoviesCant(info_actor,3,headers) if lt.size(info_actor)>0 else print(f'No hay peliculas del actor {casting}')
    print(f'\nEl tiempo de ejecución es: {timesito} ms\n')

def playReq4():
    generodeseado = input("\nDigita el género: ")
    num_movies, num_shows,todas,timesito= controller.generos_contr(catalog, generodeseado)
    os.system('cls')
    print('============ Req No. 4 Inputs ============')
    print(f'The content is "listed_in" {generodeseado}')
    
    print('\n============ Req No. 4 Answer ============')
    print(f'There are {lt.size(todas)} IPs (Intelectual Properties) with the {generodeseado} label')
    print("El numero de películas del género",generodeseado, "es: ", num_movies)
    print("El numero de shows del género",generodeseado, "es: ", num_shows)
    print(f'There are less than 6 "listed_in" {generodeseado} on record') if lt.size(todas)<6 else print(f'The first 3 and last 3 IPs in range are:')
    head=['title','release_year','director','stream_service','duration','cast','country','listed_in','description']
    printMoviesCant(todas,3,head) if lt.size(todas)>0 else print(f'No hay peliculas del genero {generodeseado}')
    print(f'\nEl tiempo de ejecución es: {timesito} ms\n')

def playReq5():
    pais=input('Ingrese el país a consultar Ej. "United States": ')
    TV, Peli,time = controller.getMoviesPais(catalog, pais)
    os.system('cls')
    print('============ Req No. 5 Inputs ============')
    print(f'The content produced in the "{pais}"')
    
    print('\n============ Req No. 5 Answer ============')
    print(f'------ "{pais}" content type production count ------')
    table = [["TV Show",lt.size(TV)],["Movies",lt.size(Peli)]]
    headers = ["Type", "Count"]
    print(tabulate(table, headers, tablefmt="grid"))

    print('\n------ Content details ------')
    print(f'There are less than 6 produced in "{pais}" on record') if (lt.size(TV)+lt.size(Peli))<6 else print(f'The first 3 and last 3 IPs in produced in "{pais}" are:')

    head=['release_year','title','director','stream_service','duration','type','cast','country','listed_in','description']
    printMoviesCant(TV,3,head) if lt.size(TV)>0 else print(f'There are not "TV Shows" in {pais}')
    printMoviesCant(Peli,3,head) if lt.size(Peli)>0 else print(f'\nThere are not "Movies" in {pais}\n')
    print('Tiempo de ejecución:',time,'ms')

def playReq6():
    director = input("Digita el director: ")
    num_todo_director,num_movies_director, num_shows_director, numero_generos_autor, plataformas, filtro_director,timesito= controller.req6(catalog, director)
    os.system('cls')
    print('============ Req No. 6 Inputs ============')
    print(f'Find the content with "{director}" as ""director" ')
    
    print('\n============ Req No. 6 Answer ============')
    print(f'------ "{director}" Content type count ------')
    headers=["Type", "Count"]
    table1=[["Movies",num_movies_director],["Shows",num_shows_director]]
    print(tabulate(table1, headers, tablefmt="grid"))

    print(f'\n------ "{director}" Streaming content type count ------')
    headers2=["Service_name", "movie"]
    print(tabulate(plataformas,headers2,tablefmt="grid",maxcolwidths=18))

    print(f'\n------ "{director}" Listed in count ------')
    print("There are only", len(numero_generos_autor),"tags ib 'listed_in'")
    print('The first 3 and last 3 tags in range are:')
    headers3=['listed_in','count']
    print(tabulate(numero_generos_autor,headers3,tablefmt='grid'))
    
    print(f'\n------ "{director}" content details ------')
    print("There are only", num_todo_director, "IPs (Intelectual Properties) with", director, "as director")
    print('The first 3 and last 3 tags in range are:')
    printMoviesCant(filtro_director,3,['title','release_year','director','stream_service','type','duration','cast','country', 'rating','listed_in','description'])
    print(f'\nEl tiempo de ejecución es: {timesito} ms\n')

def playReq7():
    top_n=int(input('Que top desea consultar: '))
    cuenta_actores,info_actores,timesito=controller.getTopGeneros(catalog,top_n)
    
    #os.system('cls')
    print('============ Req No. 7 Inputs ============')
    print(f'the TOP "{top_n}" genres in "listed_in" ')
    
    print('\n============ Req No. 7 Answer ============')
    print(f'There are "{lt.size(cuenta_actores)}" tags participating for the TOP {top_n} genres for "listed_in"')

    print(f'\n------ The TOP "{top_n}" listed_in tags are: ------')
    print(f'The TOP "{top_n}" actors are:')
    table = []
    for i in range(top_n):
        table.append([cuenta_actores['elements'][i][0],cuenta_actores['elements'][i][1]])
    headers = ["Listed_in", "Count"]
    print(tabulate(table, headers, tablefmt="grid"))

    print(f'\n------ Top actors participations details: ------')
    print(f'The TOP "{top_n}" actors are:')
    headers2 = ["type", 'count']
    headerspro=['rank','listed_in','count','type','stream_service']
    headers3=['stream_service','count']
    
    tablepro=[]
    k=1
    for i in info_actores.keys():
        table2=[]
        table3=[]
        table2.append(['Movie',info_actores[i]['Movie']])
        table2.append(['TV Show',info_actores[i]['TV Show']])
        table3.append(['netflix',info_actores[i]['netflix']])
        table3.append(['amazon',info_actores[i]['amazon prime']])
        table3.append(['hulu',info_actores[i]['hulu']])
        table3.append(['disney',info_actores[i]['disney plus']])
        tablepro.append([k,i,cuenta_actores['elements'][k-1][1],tabulate(table2,headers2,tablefmt='plain'),tabulate(table3,headers3,tablefmt='plain')])
        k+=1
    print(tabulate(tablepro,headerspro,tablefmt='grid'))
    print(f'\nEl tiempo de ejecución es: {timesito} ms\n')

def playReq8():
    top_n=int(input('Que top desea consultar: '))
    cuenta_actores,info_actores,timesito=controller.getTopActores(catalog,top_n)
    
    os.system('cls')
    print('============ Req No. 8 (BONUS) Inputs ============')
    print(f'Ranking the TOP "{top_n}" actors in "cast" ')
    
    print('\n============ Req No. 8 (BONUS) Answer ============')
    print(f'There are "{lt.size(cuenta_actores)}" actors participating for the TOP {top_n} actors in "cast"')

    print(f'\n------ The TOP "{top_n}" participations are: ------')
    print(f'The TOP "{top_n}" actors are:')
    table = []
    j=0
    for i in info_actores.keys():
        max_key = max(info_actores[i]['genero'], key = info_actores[i]['genero'].get)
        table.append([cuenta_actores['elements'][j][0],cuenta_actores['elements'][j][1],max_key])
        j+=1
    headers = ["Actor", "Count", 'Top_listed_in']
    print(tabulate(table, headers, tablefmt="grid"))

    print(f'\n------ Top actors participations details: ------')
    print(f'The TOP "{top_n}" actors are:')
    headers2 = ["stream_service", "type", 'count']
    headers3=['','actor','content_type']
    plats=['netflix','amazon prime','hulu','disney plus']
    table3=[]
    table4=[['TV Show'],['Movie']]
    k=1
    for j in info_actores.keys():
        table2 = []
        for i in plats:
            table5=[[info_actores[j][i]['TV Show']],[info_actores[j][i]['Movie']]]
            table2.append([i,tabulate(table4,tablefmt='plain'),tabulate(table5, tablefmt='plain')])
        table3.append([k,j,tabulate(table2,headers2,tablefmt='plain')])
        k+=1
    print(tabulate(table3, headers3, tablefmt="grid"))

    print(f'\n------ Top actors colaborations details: ------')
    print(f'The TOP "{top_n}" actors are:') 
    headers_colab=['','actor','colaborations']
    table_colab=[]
    i=1
    for j in info_actores:
        table_colab.append([i,j,info_actores[j]['colaborations']])
        i+=1
    print(tabulate(table_colab,headers_colab,tablefmt='grid',maxcolwidths=60))

    print(f'\nEl tiempo de ejecución es: {timesito} ms\n')

def playSortFunc():
    print('\nComo desea organizar los datos?')
    print('1: Selection Sort')
    print('2: Insertion Sort')
    print('3: Shell Sort')
    print("4: Merge Sort")
    print("5: Quick Sort")
    sorts = input()
    if sorts=='1':
        result = controller.sortList(catalog,'1')
    elif sorts=='2':
        result = controller.sortList(catalog,'2')
    elif sorts=='3':
        result = controller.sortList(catalog,'3')
    elif sorts =="4":
        result = controller.sortList(catalog, "4")
    elif sorts=="5":
        result = controller.sortList(catalog, "5")
    else:
        sys.exit(0)    
    delta_time = f"{result:.3f}"
    print("Tiempo de ejecución:", str(delta_time))


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:
        label = input("\nDigita 1 para cargar en ARRAY_LIST o 2 para SINGLED_LISTED: ")
        if label =='1':
            struc='ARRAY_LIST'
        elif label =='2':
            struc='SINGLE_LINKED'
        catalog = newController(struc)
        playLoadData() 
    elif int (inputs[0])==2:
        playReq1()
    elif int (inputs[0])==3:
        playReq2()
    elif int (inputs[0])==4:
        playReq3()
    elif int(inputs[0])==5:
        playReq4() 
    elif int(inputs[0])==6:
        playReq5()
    elif int (inputs[0])==7:
        playReq6()
    elif int (inputs[0])==8:
        playReq7()
    elif int(inputs[0])==9:
        playReq8()
    elif int(inputs[0]) == 10:
        playSortFunc()
    else:
        sys.exit(0)

