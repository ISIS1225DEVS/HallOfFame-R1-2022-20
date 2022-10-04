from gettext import Catalog
import controller
import matplotlib.pyplot as plt
import sys
from DISClib.ADT import list as lt
from prettytable import PrettyTable as ptbl
print('---------------Análisis de Requerimientos-----------')
print('Escoja el requerimiento que quiera analizar:')

for i in range(1, 9):
    print('{0}- Requerimiento {1}'.format(str(i), str(i)))

opcion = int(input('Digite su opcion: '))
large_file = ['small', '5pct', '10pct', '20pct', '30pct', '50pct', '80pct', 'large']
n_data = []
rq_data = []
plt.figure(figsize=(15,10))
plt.xlim([0,25000])
table = ptbl()
table.field_names = ['Representacion de Datos','Tiempo de Ejecucion Promedio']
promedios = []
for file in large_file:

    control = controller.newController('ARRAY_LIST', ('-'+file +'.csv'))

    netflix, hulu, disney, amazon = controller.loadData(control, ('-'+file +'.csv'))

    n_data.append(lt.size(control['model']['titles']))
    
    
    if opcion == 1:
        times = []
        datos_prueba = [(2014,2020), (1990, 2005), (1000, 1990)]
        
        for dato in datos_prueba:
            init_time = controller.getTime()
            controller.getMoviesbyYear(control, dato[0], dato[1])
            final_time = controller.getTime()
            delta = controller.deltaTime(init_time, final_time)
            times.append(delta)
        plt.xlabel('Tamaño del Archivo')
        plt.ylabel('Tiempos de Ejecucion')
        plt.title('Requerimiento 1\nListar las películas estrenadas en un periodo de tiempo')
        rq_data.append(times)
        suma = 0
        for x in times:
            suma += x
        promedio = suma/len(times)
        table.add_row([file,promedio])
        promedios.append(promedio)

    elif opcion == 2:
        times = []
        datos_prueba = [('2007-01-03','2007-12-04'), ('2003-01-05', '2008-05-04'), ('2009-03-05','2019-07-03')]
        for dato in datos_prueba:
            init_time = controller.getTime()
            controller.getTvShowsbyDate(control, dato[0], dato[1])
            final_time = controller.getTime()
            delta = controller.deltaTime(init_time, final_time)
            times.append(delta)
        plt.xlabel('Tamaño del Archivo')
        plt.ylabel('Tiempos de Ejecucion\n(milisegundos)')
        plt.title('Requerimiento 2\nListar programas de televisión agregados en un periodo de tiempo')
        rq_data.append(times)
        suma = 0
        for x in times:
            suma += x
        promedio = suma/len(times)
        table.add_row([file,promedio])
        promedios.append(promedio)
        
        
    elif opcion == 3:
        times = []
        datos_prueba = ['Sissy Spacek', 'Arnold Schwarzenegger', 'Peyton List']
        for dato in datos_prueba:
            init_time = controller.getTime()
            controller.get_content_by_actor(control, dato)
            final_time = controller.getTime()
            delta = controller.deltaTime(init_time, final_time)
            times.append(delta)
        plt.xlabel('Tamaño del Archivo')
        plt.ylabel('Tiempos de Ejecucion\n(milisegundos)')
        plt.title('Requerimiento 3\nEncontrar contenido donde participa un actor')
        rq_data.append(times)
        suma = 0
        for x in times:
            suma += x
        promedio = suma/len(times)
        table.add_row([file,promedio])
        promedios.append(promedio)

    elif opcion == 4:
        times = []
        datos_prueba = ['Comedy', 'Drama', 'Action']
        for dato in datos_prueba:
            init_time = controller.getTime()
            controller.get_titles_by_genre(control, dato)
            final_time = controller.getTime()
            delta = controller.deltaTime(init_time, final_time)
            times.append(delta)
        plt.xlabel('Tamaño del Archivo')
        plt.ylabel('Tiempos de Ejecucion\n(milisegundos)')
        plt.title('Requerimiento 4\nEncontrar contenido por un género especifico')
        rq_data.append(times)
        suma = 0
        for x in times:
            suma += x
        promedio = suma/len(times)
        table.add_row([file,promedio])
        promedios.append(promedio)
    elif opcion == 5:
        times = []
        datos_prueba = ['Colombia', 'Canada','United Kingdom']
        for dato in datos_prueba:
            init_time = controller.getTime()
            controller.get_titles_by_country(control, dato)
            final_time = controller.getTime()
            delta = controller.deltaTime(init_time, final_time)
            times.append(delta)
        plt.xlabel('Tamaño del Archivo')
        plt.ylabel('Tiempos de Ejecucion\n(milisegundos)')
        plt.title('Requerimiento 5\nEncontrar contenido por país')
        rq_data.append(times)
        suma = 0
        for x in times:
            suma += x
        promedio = suma/len(times)
        table.add_row([file,promedio])
        promedios.append(promedio)
    elif opcion == 8:
        times = []
        datos_prueba = [10, 20, 50]
        for dato in datos_prueba:
            init_time = controller.getTime()
            controller.get_top_actors(control, dato)
            final_time = controller.getTime()
            delta = controller.deltaTime(init_time, final_time)
            times.append(delta)
        plt.xlabel('Tamaño del Archivo')
        plt.ylabel('Tiempos de Ejecucion\n(milisegundos)')
        plt.title('Requerimiento 8 (Bono)\nListar el TOP (N) de los actores con más participaciones en contenido')
        rq_data.append(times)
        suma = 0
        for x in times:
            suma += x
        promedio = suma/len(times)
        table.add_row([file,promedio])
        promedios.append(promedio)
        

coordenadas = ptbl()
coordenadas.add_column(fieldname= 'X', column = n_data)
coordenadas.add_column(fieldname=  'Y',column=promedios)
print(coordenadas)

print(table)
plt.plot(n_data, rq_data)
plt.show()

    
#%%
    


