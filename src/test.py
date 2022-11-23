from parsers import *
from lecturadatos import * 
import csv 



def test_filtro_country(lista):     
    print('---------------------------------------------------FILTRO---------------------------------------------------')    
    lista_h = filtro_country(lista, 'United States')     
    print(lista_h[:20])


def test_frecuencia_country(lista):
    duration = 220
    total = frecuencia_country(lista, duration)
    print('----------------------------------------------------SUMA-----------------------------------------------------')
    print(f'El total de veces que se ha puesto el nombre {duration} es {total}')


def test_peliculas_mas_frecuente_segun_el_año_de_estreno_por_duracion(datos):
    nombres = peliculas_mas_frecuente_segun_el_año_de_estreno_por_duracion(datos, 'Movie', 2019, 3)
    print('--------------------------------------------Peliculas mas frecuentes---------------------------------------------')
    print(f'Las PELICULAS mas populares son: {nombres}')


def test_release_year_mayor_frecuencia_segun_country(datos):
    country = 'United States'
    release_year = release_year_mayor_frecuencia_segun_country(datos, country)
    print('--------------------------------------------El año que mas se uso---------------------------------------------')
    print (f'El año en el que mas veces se uso {country} para hacer alguna entrega fue el {release_year}')

#def test_frecuencia_media_paises_for_release_year(datos):
    #country= 'United States'
    #a1 = 114
    #a2 = 205
    #media = frecuencia_media_paises_for_release_year(datos, country, a1, a2)
   # print('--------------------------------------------Media de Estados Unidos-------------------------------------------')
   # print ( f'La frecuencia media de {country} es de {media}')

if __name__=='__main__':
    print('Inicio de la lectura')
    lectura = lee_fichero('./data/plataforma_streaming_copy.csv')
    print(lectura)
    print('------------------------------------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------------------------------------')
    test_filtro_country(lectura)
    test_frecuencia_country(lectura)
    test_peliculas_mas_frecuente_segun_el_año_de_estreno_por_duracion(lectura)
    test_release_year_mayor_frecuencia_segun_country(lectura)
    #test_frecuencia_media_paises_for_release_year(lectura)
    print('Fin')
#Función final para la lectura del texto, incluyendo dos comandos (Inicio y Fin) para que sea mas facil reconocer el principio y el final del texto.
#Todas las funciones de test se basan en recorrer todos los filtro que le hemos aplicado al csv para recorrer sus datos para diferentes valores, en cantidades distintas.