# Trabajo Final de Bioinformática - 1° Cuatrimestre 2020

_Se desarrolló un Software que permite  la visualización de estudios filogenéticos y filodinámicos de secuencias con su posterior geolocalización. Este Software corre en Web de manera local, y soporta la carga de archivos FASTA con secuencias de Ácidos Nucleicos (ADN y ARN)._

***

## Autores ✒️

* **Lucio Francioni** - [franciolucio](https://github.com/franciolucio)
* **Nahuel Pereyra** - [nahuelmpereyra](https://github.com/nahuelmpereyra)
* **Leonardo Di Carlo** - [leonardodicarlo](https://github.com/leonardodicarlo)

***

## Construido con 🛠️

_El trabajo está basado sobre lenguaje Python y bajo el framework de Django, pero se utilizaron distintas bibliotecas y programas dedicados a la biología:_

* [Python 3](https://www.python.org/doc/) - El lenguaje utilizado para resolver la lógica de nuestro Software.
* [Django](https://docs.djangoproject.com/en/3.0/) - El framework web escrito en Python con el que armamos los componentes del Software.
* [Biopython](https://biopython.org/wiki/Documentation) - Biblioteca de Python para manejar archivos de secuencias biológicas.
* [ClustalW](http://www.clustal.org/clustal2/) - Programa instalado en local para realizar el alineamiento de secuencias biológicas.
* [IQ-Tree](http://www.iqtree.org/doc/) - Biblioteca de Python para generar estructuras de árboles filogenéticos.
* [ETE Toolkit](http://etetoolkit.org/cookbook/) - Framework de Python para el análisis y visualización de árboles.
* [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/) - Biblioteca de Python utilizada para realizar el Binding del entorno gráfico.

***

### Instalación (Linux) 🔧

_Para correr el software localmente debemos tener instalado tanto Python 3.6 o superior, como las respectivas librerías que listamos anteriormente._

***

***_Nota: En caso de estar corriendo este software en un IDE propio o por consola, el repositorio incluye un archivo "requirements.txt" con el que automáticamente se solicita la instalación de todas las bibliotecas necesarias para ejecutar el programa. Para ello, se debe ejecutar el siguiente comando:_***

```
$ python3 pip3 install -r requirements.txt
  o bien:
$ python3 pip install -r requirements.txt
```
***



* Primero, nos asegurarnos que tenemos Python 3.6 o superior correctamente instalado (chequeo a través del Terminal):

```
$ python3 -V
```
   _En caso de no tener la versión 3.6 o superior de Python, correr los siguientes comandos:_

```
   $ sudo apt-get update
   $ sudo apt-get -y upgrade
```
   _Además, es recomendado tener instalado *pip* para manejar los paquetes:_

```
   $ sudo apt-get install -y python3-pip
```
* Segundo, instalar la biblioteca de Biopython, a través de la cual manejaremos los archivos de secuencias .FASTA:

```
$ sudo apt-get install python-biopython
```
	
* Tercero, se debe instalar ClustalW ya que el Software lo utiliza para alinear secuencias:

```
$ sudo apt-get update
$ sudo apt-get install clustalw
```

* Cuarto, debemos instalar IQ-Tree para que nuestro programa genere los diagramas de árbol filogenéticos:

```
$ sudo apt-get update
$ sudo apt-get install iqtree
```
* Por último, debe ingresarse a la ruta local donde se descargó este proyecto, y abrir el archivo que se encuentra en la siguiente ruta TpFinalBio -> Settings -> .env.example .

 _En esta misma ruta debemos crear un archivo que se llame ".env" que sea igual al "env.example", pero especificarle los Paths en los que está instalado Clustal e IQTree en la máquina de quien lo corre:_

```
  CLUSTAL_PATH='Donde esta instalado Clustal en tu maquina'
  IQTREE_PATH='Donde esta instalado IQTREE en tu maquina'
  GOOGLE_MAPS_API_KEY='Dejar lo mismo que está en el archivo .env.example'
```
**Con esto deberías estar listo para poder correr el Software.**

---

### Instalación (Windows) 🔧

_Para correr el software localmente debemos tener instalado previamente tanto Python 3.6 o superior, como las respectivas librerías que listamos anteriormente._

***
***_Nota: En caso de estar corriendo este software en un IDE propio o por consola, el repositorio incluye un archivo "requirements.txt" con el que automáticamente se solicita la instalación de todas las bibliotecas necesarias para ejecutar el programa. Para ello, se debe ejecutar el siguiente comando:_***

```
$ python3 pip3 install -r requirements.txt
  o bien:
$ python3 pip install -r requirements.txt
```
***


* Primero, nos asegurarnos que tenemos Python 3.6 o superior correctamente instalado. Puede descargarse desde el siguiente [link](https://www.python.org/downloads/windows/).


* Segundo, instalar la biblioteca de Biopython, a través de la cual manejaremos los archivos de secuencias .FASTA:

   _Para esto, puede instalarse por la web mediante el siguiente [link](https://biopython.org/wiki/Download), o bien mediante *PIP* desde cmd/powershell:_
	
```
   pip install biopython
```
	
* Tercero, instalar ClustalW mediante el siguiente [link](http://www.clustal.org/download/current/). Con esto podremos realizar los alineamientos de secuencias.


* Cuarto, debemos instalar IQ-Tree desde el siguiente [link](http://www.iqtree.org/#download). Con esto dibujaremos los árboles filogenéticos.

* Por último, debe ingresarse a la ruta local donde se descargó este proyecto, y abrir el archivo que se encuentra en la siguiente ruta TpFinalBio -> Settings -> .env.example .

_En esta misma ruta debemos crear un archivo que se llame ".env" que sea igual al "env.example", pero especificarle los Paths en los que está instalado Clustal e IQTree en la máquina de quien lo corre:_

```
  CLUSTAL_PATH='Donde esta instalado Clustal en tu maquina'
  IQTREE_PATH='Donde esta instalado IQTREE en tu maquina'
  GOOGLE_MAPS_API_KEY='Dejar lo mismo que está en el archivo .env.example'
```
**Con esto deberías estar listo para poder correr el Software.**


***

## Ejecución - Paso a Paso 📋

_Una vez realizados los pasos de instalación, debemos pararnos sobre el directorio donde tenemos los archivos y ejecutar los siguientes comandos a través de consola (también puede realizarse el proceso a través de un IDE):_
	
```
$ python manage.py makemigrations
$ python manage.py migrate	
$ python manage.py runserver
```
_Con esto, ya debiera correr localmente nuestro programa en una nueva ventana de nuestro navegador (por defecto es el puerto localhost:8000)._

_Seguidamente, podemos cargar un archivo .FASTA o .fst que sólo contenga secuencias de Ácidos Nucléicos (ADN y ARN, secuencias con A-T-G-C-U)._

***

_El programa validara este archivo con las siguientes pautas:_

1. Que el archivo y su contenido coincidan con el formato de un FASTA: cabecera **(>|gi|12345|gb|accessionCode) - secuencia (ATGCU)**. Es importante que cada secuencia posea su  accesion number de GenBank, ya que el Software va a buscar toda la información a esta Base de Datos.

2. Que el archivo posea además en cada cabecera una locación, unificada por pipes (|) con el siguiente formato ejemplo: **|loc| Universidad Nacional de Quilmes, Bernal**. En    caso de que la secuencia imputada posea una locación cargada en Genbank, el programa tomará esta como principal. Caso contrario, toma la locación cargada por el usuario 	en la cabecera (por esto es que es obligatoria la carga de la locación).

3. Que cada cabecera presente en el archivo tenga su correspondiente secuencia asociada (no pueden quedar cabeceras sin secuencias).

4. Que lo imputado en cada secuencia sean efectivamente secuencias de ADN/ARN.

***
_Una vez superada efectivamente esta validación, se cargará el archivo y el programa nos redireccionará automáticamente a un nuevo link donde tendremos cargado:_

- Una tabla de tipo acordeón que contiene: Accession de GenBank - Descripción de la Secuencia - Fecha de Carga en Genbank.
- Otro desplegable con los diferentes inputs realizados, disponibilizados para su descarga (secuencias alineadas, árbol filogenético).
- Un mapa con la locación de cada una de las respectivas secuencias cargadas junto con su accession code.
- Un diagrama de árbol filogenético que agrupa las secuencias cargadas de acuerdo a su similitud.

_Por último, se puede descargar la información obtenida y volver a correr el programa con un nuevo archivo de secuencias._


***

## Muchas gracias!
