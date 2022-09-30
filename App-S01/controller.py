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

csv.field_size_limit(2147483647)

def newController(struc):
    control = {
        'model': None
    }
    control['model'] = model.newCatalog(struc)
    return control

def loadData(control,archiv):
    catalog = control['model']
    nf,features= loadMovieNetflix(catalog,archiv)
    am= loadMovieAmazon(catalog,archiv)
    hl= loadMovieHulu(catalog,archiv)
    dy= loadMovieDisney(catalog,archiv)
    return nf, am,hl,dy,features

def loadMovieNetflix(catalog,archiv):
    booksfile = cf.data_dir + 'netflix_titles-utf8-'+archiv
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    plat='nf'
    for book in input_file:
        model.addMovie(catalog, book, plat)
        model.addMovie(catalog,book,'mix', 'netflix')
        features=len(book.keys())
    sortMovies(catalog,plat)
    return model.titleSize(catalog,plat),features

def loadMovieAmazon(catalog,archiv):
    booksfile = cf.data_dir + 'amazon_prime_titles-utf8-'+archiv
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    plat='am'
    for book in input_file:
        model.addMovie(catalog, book,plat)
        model.addMovie(catalog,book,'mix','amazon prime')
    sortMovies(catalog,plat)
    return model.titleSize(catalog,plat)

def loadMovieHulu(catalog,archiv):
    booksfile = cf.data_dir + 'hulu_titles-utf8-'+archiv
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    plat='hl'
    for book in input_file:
        model.addMovie(catalog, book,plat)
        model.addMovie(catalog,book,'mix','hulu')
    sortMovies(catalog,plat)
    return model.titleSize(catalog,plat)

def loadMovieDisney(catalog,archiv):
    booksfile = cf.data_dir + 'disney_plus_titles-utf8-'+archiv
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    plat='dy'
    for book in input_file:
        model.addMovie(catalog, book,plat)
        model.addMovie(catalog,book,'mix','disney plus')
    sortMovies(catalog,plat)
    return model.titleSize(catalog,plat)

# Funciones de ordenamiento
def sortMovies(catalog,plat):
    model.sortMovies(catalog,plat)

def sortList(control,sort):
    return model.sortList(control['model'],sort)

# Funciones de consulta sobre el catálogo
def getBestBooks(control, number,plat):
    bestbooks = model.getPrimeros(control['model'], number,plat)
    return bestbooks

def getLastMovies(control, number,plat):
    bestbooks = model.getUltimos(control['model'], number,plat)
    return bestbooks

def getMoviesPais(control,pais):
    movies_pais=model.getMoviesPais(control['model'],pais)
    return movies_pais

def getMoviesAno(control,ini,fin):
    movies_pais,time=model.getMoviesAno(control['model'],ini,fin)
    return movies_pais,time

def getMoviesFecha(control,ini,fin):
    movies_pais,time=model.getMoviesFecha(control['model'],ini,fin)
    return movies_pais,time

def getTopActores(control,top):
    actor=model.getTopActores(control['model'],top)
    return actor

def getTopGeneros(control,top):
    actor=model.getTopGeneros(control['model'],top)
    return actor

def generos_contr(control,genero):
    generos=model.getGeneros(control['model'],genero)
    return generos

def getActor(control,actor):
    casting = model.buscar_por_actor(control['model'], actor)
    return casting

def req6(control, director):
    return model.req6(control['model'], director)

#