
from collections import namedtuple
from parsers import *
from test import *
import csv


Registro = namedtuple('Registro', 'type,title,director,country,co_production,date_added,release_year,duration,description')


def lee_fichero(plataforma_streaming):
    Dato = []
    with open(plataforma_streaming, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        res = [Registro(str(type), str(title), str(director), str(country), parse_bool(co_production), parse_fecha(date_added), str(release_year), duration, description) for type, title, director,country, co_production, date_added,release_year, duration, description in lector]
        return res 


def filtrar_por_co_production(plataforma_streaming):
    registros = []
    with open(plataforma_streaming, 'r') as f: 
        lector = csv.reader(f)
        next(lector)
        for type, title, director, country, co_production, date_added, release_year, duration, description in lector:
            tupla = Registro(int(type), int(title), int(director), int(country), parse_bool(co_production), parse_fecha(date_added), str(release_year), duration, description) 
            registros.append(tupla)
    return tupla  
#Definión total del programa y agrupación de cada variable en el tipo de lectura debido para que el programa lo represente tal y como queremos, y poder evitar todos los problemas de lectura que puedan aparecer en la descodificación.


def filtro_country(registros, country):     
    res = [t for t in registros if t.country == country]   
    return res
    #Filtra segun los paises que hayamos seleccionado

def frecuencia_country(registros, country):
    return sum ([tupla.duration for tupla in registros if tupla.duration == 220])
    #Nos extrae una tupla con los paises que tengan una duración de 220 minutos


def peliculas_mas_frecuente_segun_el_año_de_estreno_por_duracion(registros, type, release_year, n=3):
    lista_aux = [tupla for tupla in registros 
                        if tupla.type == type and tupla.release_year == release_year]
    # 2 Ordeno
    lista_aux.sort(key = lambda tupla:tupla.duration, reverse=True)
    # 3 Me quedo solo con los n primeras peliculas
    return lista_aux[:n]

def release_year_mayor_frecuencia_segun_country(registros, country):
    #filtramos por pais
    lista_aux = [tupla for tupla in registros if tupla.country == country]
    #Calcular la tupla cuya frecuencia fuese máxima
    tupla_maxima= max(lista_aux, key = lambda tupla:tupla.release_year)
    return tupla_maxima.release_year


#def frecuencia_media_paises_for_release_year(registros, country, a1, a2):
  #  lista_auxiliar = [tupla.release_year for tupla in registros               
   #                     if(tupla.country == country and tupla.parse_lista(release_year) >= a1 and tupla.parse_lista(release_year) >= a2)]
    #suma = sum(lista_auxiliar)
    #total_elem = len(lista_auxiliar)
    #return suma/total_elem
