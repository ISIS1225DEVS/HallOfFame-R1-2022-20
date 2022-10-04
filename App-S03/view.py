"""
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
import datetime as dt
assert cf
from tabulate import tabulate

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

# Se crea el controlador asociado a la vista

def printMenu():
    """
    Menu de usuario
    """
    print("\nBienvenido, por favor seleccione alguna de las siguientes opciones para continuar:\n")
    print("0- Cargar información en el catálogo")
    print("1- Películas estrenadas en un periodo de tiempo")
    print("2- Programas de televisión agregados en un periodo de tiempo")
    print("3- Contenido por actor")
    print("4- Contenido por género")
    print("5- Contenido por país")
    print("6- Contenido por director")
    print("7- Top (n) géneros con más contenido")
    print("8- Top (n) actores con más contenido")
    print("9- Salir")

catalog = None

def loadData(control,size):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    nt, hl, dp, ap = controller.loadData(control,size)
    return nt, hl, dp, ap

"""
Menu principal 
"""
while True:
    printMenu()
    inputs = input('\nOpción: ')
    if int(inputs) == 0:
        size = input("\nIngrese el tamaño de la muestra que desea cargar:")
        control = newController()
        print("Cargando información de los archivos ....\n")
        nt, hl, dp, ap = loadData(control,size)
        print("Se ha realizado la carga de los datos\nReporte de carga de servicios de Streaming:\n")
        Headers = ['Servicio de Streaming','Títulos cargados']
        Report = [
            ['Netflix',lt.size(nt)],
            ['Amazon Prime',lt.size(ap)],
            ['Disney+',lt.size(dp)],
            ['Hulu',lt.size(hl)],
            ['Total',lt.size(nt)+lt.size(hl)+lt.size(dp)+lt.size(ap)]]
        print(tabulate(Report,headers=Headers,tablefmt='fancy_grid'))
        
    elif int(inputs) == 1:
        inferior = int(input("Indique el año inferior para realizar la busqueda (AAAA): "))
        superior = int(input("Indique el año superior para realizar la busqueda (AAAA): "))
        print(f"Cargando información de las películas estrenadas entre {inferior} y {superior}")
        t0=dt.datetime.now()
        movies,size = controller.Movies_in_range(control["model"]["Movies"],superior,inferior)
        print(dt.datetime.now()-t0)
        print(f'\nSe estrenaron {size} películas entre {inferior} y {superior}')
        print("Las primeras y últimas 3 películas estrenadas en este rango son: ")
        titles = movies["elements"]
        Headers = ['Título','Director','Fecha de estreno','Duración','Plataforma','Reparto']
        table = [[titles[0]['title'],titles[0]['director'],titles[0]['release_year'],titles[0]['duration'],titles[0]['platform'],titles[0]['cast']],
                 [titles[1]['title'],titles[1]['director'],titles[1]['release_year'],titles[1]['duration'],titles[1]['platform'],titles[1]['cast']],
                 [titles[2]['title'],titles[2]['director'],titles[2]['release_year'],titles[2]['duration'],titles[2]['platform'],titles[2]['cast']],
                 ['...','...','...','...','...','...'],
                 [titles[-3]['title'],titles[-3]['director'],titles[-3]['release_year'],titles[-3]['duration'],titles[-3]['platform'],titles[-3]['cast']],
                 [titles[-2]['title'],titles[-2]['director'],titles[-2]['release_year'],titles[-2]['duration'],titles[-2]['platform'],titles[-2]['cast']],
                 [titles[-1]['title'],titles[-1]['director'],titles[-1]['release_year'],titles[-1]['duration'],titles[-1]['platform'],titles[-1]['cast']]]
        print(tabulate(table,headers=Headers,tablefmt='fancy_grid'))

    elif int(inputs) == 2:
        inferior = (input("Indique la fecha inferior para realizar la busqueda (Month %B day %d, year %Y): "))
        superior = (input("Indique la fecha superior para realizar la busqueda (Month %B day %d, year %Y): "))
        inferiorf = dt.datetime.strptime(inferior,"%B %d, %Y")
        superiorf = dt.datetime.strptime(superior,"%B %d, %Y")
        print("Cargando información de los shows agregados entre "+inferior+" y "+superior)
        t0=dt.datetime.now()
        shows,size = controller.Shows_in_range(control["model"]["TV-shows"],superiorf,inferiorf)
        print(dt.datetime.now()-t0)
        print(f'\nSe agregaron {size} shows entre {inferiorf} y {superiorf}')       
        print("\nLos primeros y últimos 3 shows agregados en este rango son: ")
        titles = shows["elements"]
        Headers = ['Título','Director','Fecha de carga a plataforma','Fecha de estreno','Duración','Plataforma','Reparto']
        table = [[titles[0]['title'],titles[0]['director'],titles[0]['date_added'],titles[0]['release_year'],titles[0]['duration'],titles[0]['platform'],titles[0]['cast']],
                 [titles[1]['title'],titles[1]['director'],titles[1]['date_added'],titles[1]['release_year'],titles[1]['duration'],titles[1]['platform'],titles[1]['cast']],
                 [titles[2]['title'],titles[2]['director'],titles[2]['date_added'],titles[2]['release_year'],titles[2]['duration'],titles[2]['platform'],titles[2]['cast']],
                 ['...','...','...','...','...','...','...'],
                 [titles[-3]['title'],titles[-3]['director'],titles[-3]['date_added'],titles[-3]['release_year'],titles[-3]['duration'],titles[-3]['platform'],titles[-3]['cast']],
                 [titles[-2]['title'],titles[-2]['director'],titles[-2]['date_added'],titles[-2]['release_year'],titles[-2]['duration'],titles[-2]['platform'],titles[-2]['cast']],
                 [titles[-1]['title'],titles[-1]['director'],titles[-1]['date_added'],titles[-1]['release_year'],titles[-1]['duration'],titles[-1]['platform'],titles[-1]['cast']]]
        print(tabulate(table,headers=Headers,tablefmt='fancy_grid'))

    elif int(inputs) == 3:
        actor = input("Indique el actor que quiere consultar: ")
        t0=dt.datetime.now()
        titles , mov , shw = controller.actor_in_film(control["model"]["general"],actor)
        print(dt.datetime.now()-t0)
        titles = titles["elements"]
        Headers_1 = [f'Títulos del actor: {actor}']
        General_report = [['Shows',shw],
                        ['Películas',mov],
                        ['total',mov+shw]]
        if 6 >= int(mov) + int(shw):
            print("Hay menos de 6 participaciones de " + actor + " en peliculas o series registradas.")
        Headers_2 = ['Título','Fecha de estreno','Director','Plataforma',"Duración",'Actores','País','Género','Descripción']
        if int(mov) + int(shw) >= 6:
            Specific_report = [[titles[0]['title'],titles[0]['release_year'],titles[0]['director'],titles[0]['platform'],titles[0]['duration'],titles[0]['cast'],titles[0]['country'],titles[0]['listed_in'],titles[0]['description']],
                           [titles[1]['title'],titles[1]['release_year'],titles[1]['director'],titles[1]['platform'],titles[1]['duration'],titles[1]['cast'],titles[1]['country'],titles[1]['listed_in'],titles[1]['description']],
                           [titles[2]['title'],titles[2]['release_year'],titles[2]['director'],titles[2]['platform'],titles[2]['duration'],titles[2]['cast'],titles[2]['country'],titles[2]['listed_in'],titles[2]['description']],
                           ['...','...','...','...','...','...','...','...','...'],
                           [titles[-3]['title'],titles[-3]['release_year'],titles[-3]['director'],titles[-3]['platform'],titles[-3]['duration'],titles[-3]['cast'],titles[-3]['country'],titles[-3]['listed_in'],titles[-3]['description']],
                           [titles[-2]['title'],titles[-2]['release_year'],titles[-2]['director'],titles[-2]['platform'],titles[-2]['duration'],titles[-2]['cast'],titles[-2]['country'],titles[-2]['listed_in'],titles[-2]['description']],
                           [titles[-1]['title'],titles[-1]['release_year'],titles[-1]['director'],titles[-1]['platform'],titles[-1]['duration'],titles[-1]['cast'],titles[-1]['country'],titles[-1]['listed_in'],titles[-1]['description']]]
        else:
            Specific_report = []
            for i in range(int(mov) + int(shw)):
                Specific_report.append([titles[i]['title'],titles[i]['release_year'],titles[i]['director'],titles[i]['platform'],titles[i]['duration'],titles[i]['cast'],titles[i]['country'],titles[i]['listed_in'],titles[i]['description']])
                
        print(tabulate(General_report,headers=Headers_1,tablefmt='fancy_grid'))
        print(tabulate(Specific_report,headers=Headers_2,tablefmt='fancy_grid'))
    
    elif int(inputs) == 4:
        genre = input("\nIndique el género que quiere consultar: ")
        t0=dt.datetime.now()
        titles , mov , shw = controller.titles_by_genre(control["model"]["general"],genre)
        print(dt.datetime.now()-t0)
        titles = titles['elements']
        Headers_1 = [f'Títulos del género: {genre}']
        General_report = [['Shows',shw],
                        ['Películas',mov],
                        ['total',mov+shw]]
        Headers_2 = ['Título','Director','País','Fecha de carga a plataforma','Fecha de estreno','Rating','Duración']
        Specific_report = [[titles[0]['title'],titles[0]['director'],titles[0]['country'],titles[0]['date_added'],titles[0]['release_year'],titles[0]['rating'],titles[0]['duration']],
                           [titles[1]['title'],titles[1]['director'],titles[1]['country'],titles[1]['date_added'],titles[1]['release_year'],titles[1]['rating'],titles[1]['duration']],
                           [titles[2]['title'],titles[2]['director'],titles[2]['country'],titles[2]['date_added'],titles[2]['release_year'],titles[2]['rating'],titles[2]['duration']],
                           ['...','...','...','...','...','...','...'],
                           [titles[-3]['title'],titles[-3]['director'],titles[-3]['country'],titles[-3]['date_added'],titles[-3]['release_year'],titles[-3]['rating'],titles[-3]['duration']],
                           [titles[-2]['title'],titles[-2]['director'],titles[-2]['country'],titles[-2]['date_added'],titles[-2]['release_year'],titles[-2]['rating'],titles[-2]['duration']],
                           [titles[-1]['title'],titles[-1]['director'],titles[-1]['country'],titles[-1]['date_added'],titles[-1]['release_year'],titles[-1]['rating'],titles[-1]['duration']]]
                           
        print(tabulate(General_report,headers=Headers_1,tablefmt='fancy_grid'))
        print(tabulate(Specific_report,headers=Headers_2,tablefmt='fancy_grid'))

    elif int(inputs) == 5:
        country = input("Indique el país que quiere consultar: ")
        t0=dt.datetime.now()
        titles , mov , shw = controller.titles_by_country(control["model"]["general"],country)
        print(dt.datetime.now()-t0)
        print(titles)
        print("Movies: "+str(mov))
        print("Shows: "+str(shw))

    elif int(inputs) == 6:
        director = input("Indique el director que quiere consultar: ")
        t0=dt.datetime.now()
        titles , mov , shw , gnr , plt= controller.titles_by_director(control["model"]["general"],director)
        print(dt.datetime.now()-t0)
        print(titles)
        print("Movies: "+str(mov))
        print("Shows: "+str(shw))
        for i in range(0,gnr["size"]): 
            print(str(gnr["elements"][i][0])+": "+str(gnr["elements"][i][1]["genre"]))
        for p in plt: 
            if p[1]>0:
                print(str(p[0])+": "+str(p[1]))
        
    elif int(inputs) == 7:
        top = int(input("Indique la cantidad de elementos que quiere en el top de resultados:"))
        t0=dt.datetime.now()
        genres = controller.count_per_genre(control["model"]["general"])
        print(dt.datetime.now()-t0)
        
        print(f'------Los {top} géneros con más contenido------')
        headers_1 = ['Género','Títulos']
        table_1 = []

        for i in range(0,top):
            table_1.append([ genres["elements"][i][0] , genres["elements"][i][1]["genre"] ])
        print(tabulate(table_1,headers=headers_1,tablefmt='fancy_grid'))
        print(f"------ Detalles de los TOP {top} géneros ------")

        table_2 = []
        headers_2 = ['Top','Género','Títulos','Tipo','Conteo por plataformas']
        
        for i in range(0,top):
            aux = []
            for plt in ["Netflix","Hulu","Disney Plus","Amazon Prime"]:
                aux.append(plt + ": "+str(genres["elements"][i][1][plt])+'\n')
            auxs = ' '.join(map(str,aux))
            table_2.append([i+1, genres["elements"][i][0] , genres["elements"][i][1]["genre"] , 
            'Movies: '+ str(genres["elements"][i][1]["Movie"])+'\nTV Shows: '+ str(genres["elements"][i][1]["TV Show"]) ,
            auxs])
                
            
        print(tabulate(table_2,headers=headers_2,tablefmt='fancy_grid'))

    elif int(inputs) == 8:
        top = int(input("Indique la cantidad de elmentos que quiere en el top de resultados: "))
        t0=dt.datetime.now()
        actors = controller.count_per_actor(control["model"]["general"])
        print(dt.datetime.now()-t0)
        print("Top "+str(top)+" actors with more content:")
        for i in range(0,top):
            print(str(actors["elements"][i][0]) + ": "+str(actors["elements"][i][1]["Total"]) )
        print("----------------------------------")
        for i in range(0,top):
            print(str(actors["elements"][i][0])+"\n"+"Count: "+str(actors["elements"][i][1]["Total"])
            +"\n"+"Movies: "+str(actors["elements"][i][1]["Movie"])
            +"\n"+"TV Shows: "+str(actors["elements"][i][1]["TV Show"]) )
            for plt in ["Netflix","Hulu","Disney Plus","Amazon Prime"]:
                print(plt + ": "+"Movies: "+str(actors["elements"][i][1][plt]["Movie"])+
                        "\nTV Shows: "+str(actors["elements"][i][1][plt]["TV Show"]))
            print("Ha colaborado con: "+str(actors["elements"][i][1]["Collaborations"]))
            print("\n")
    elif int(inputs) == 9:
        sys.exit(0)

    else:
        continue
    
sys.exit(0)