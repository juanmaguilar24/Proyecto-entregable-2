Autor: Juan Manuel Aguilar González
UVUS: MQR0892

El programa realizado tiene la funcion de leer los datos del dataset, es decri, en este caso clasificar los difernetes tipos de peliculas, series u programas de televisión incluyendo una descripcion de diferentes aspectos de cada uno que se encuentran en el mismo.


**/src**: 
    **\<lecturadatos.py\>**: Módulo principal donde se expone el grueso del programa, es decir, las diferentes variables que van a salir resultantes.
    **\<parsers.py\>**: Módulo secundario en el cual han sido añadidas las direntes funciones ocultas de la clasificación de las variables en el módulo principal.
    **\<test.py\>**: El módulo de pruebas en cual solo se expone la función que imprime todo el programa vinculado con los otros dos por los "import".

**/data**: 
    **\<plataforma_streaming_copy.csv\>**: Expone la información básica de las diferentes peliculas, series y programas que va a leer el programa.


El dataset está compuesto por \<N\> columnas, con la siguiente descripción:

* **\<Type>**: de tipo \<Str\>, representa si es película, serio, programa de televisión.
* **\<Title>**: de tipo \<Str\>, representa el título.
* **\<Director>**: de tipo \<Str\>, representa quien es el director.
* **\<Country>**: de tipo \<Str\>, representa el lugar donde se realizó.
* **\<Co_production>**: de tipo \<Bool\>, representa si tiene coproductor.
* **\<Date_added>**: de tipo \<Datetime\>, representa la fecha de cuando se estrenó.
* **\<Release_year>**: de tipo \<Int\>, representa el año de realización.
* **\<Duration>**: de tipo \<Int\>, representa la duración del mismo/a.
* **\<Description>**: de tipo \<Str\>, representa una pequeña sinopsis. 

**/Namedtuple**
Lector: Función para lectura del texto.
Tupla: Computo de todas las variables.
Fecha: Funcón creada para la lectura de la fecha de realiación.
Lista: Función creada para la lectura de la descripción

**/Funciones** 
**<Parse_fecha>**: Función para la lectura de la fecha.
**<Parse_lista>**: Función para la lectura de la descripción en forma de cadena.
**<Parse_bool>**: Función para reconocer si tiene o no coproductor.
* **<Filtro_country> Aqui hemos realizado un filtro para ordenar por paisesen los cuales se han realizado algunas de las entregas. Para ser mas exactos hemos usado a "United States" en un rango de los 20 primeros que aparecen.
* **<peliculas_mas_frecuente_segun_el_año_de_estreno_por_duracion> En este caso hemos extraido las peliculas mas frecuentes segun el año en el que se extrenaron y para ser mas exactos por su duración.
* **<release_year_mayor_frecuencia_segun_country> Segun los paises en que se han realizado, hemos expuesto el pais en el cual hubo mas estrenos.
* **<frecuencia_media_paises_for_release_year> Esta función esta desactivada ya que no he sido capz de solucionar el error que expone al correrla.

\<modulo 1\>
* **<Lee_fichero>**: Creación del computo y clasificación de cada variable en su tipo de texto.
* **<Lector>**: Formato y de que forma queremos que el program lea el texto.

\<modulo 2\>
* **<Parse_fecha>**: Función lectura en formato de fecha.
* **<Parse_lista>**: Función de cadena para la lectura de la descripción.
* **<Parse_bool>**: Reconocimiento de existencia o no de coproductor.

\<test\>
* **<Test>: Todas las funciones de test se basan en recorrer todas las funciones de filtro realizadas en la pagina de lectura de datos.
* **<Main>**: Función final para el inicio de la lectura del texto, con dos indices para marcar inico y final de la lectura.




