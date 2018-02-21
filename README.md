# ProyectoBIAnalisisConsultaPopular2018
Diseño e Implementación de un modelo de consecha,clasificación de sentimientos expresados mediante Twiter,
utilizando machine learning para la consulta popular del 4 de febrero del 2018.
# Integrantes
	* Jefferson Paredes
	* Daniela Ramos
# Prerequisitos
- Instalar la base de datos CouchDB en su ultima versión: http://couchdb.apache.org/
- Instalar Interprete de Python V 2.7.14 https://www.python.org/downloads/ con las siguientes librerias:
	* CouchDb V 1.1 --> para conexión con la base de datos
	* pandas V 0.22.0 ---> para la presentación de datos con gráficas
	* urllib3 V 1.22 --> para consumir servicios Rest de las vistas de la base de datos
	* tweepy V 3.5.0 --> para consumir el API de twitter
	* TextBlob V 0.15.1 --> para crear un clasificador bayesiano

# Cosecha de twwets
El script de python /harvester_ecu.py es el encargado de conectarse
al api de tweeter, y guardar los tweets recolectados en la base datos couchdb

	** importante especificar las credenciales de desarrollador de tweeter en el script.
# Procesamiento
# Limpieza de datos
- En la base de datos procedemos a generar cada una de las vistas por ciudad y limpieza de los datos
con el script adjunto /FuncioneslimpiartextoCouchDB.txt

# Consumo
- Con los script de python ubicados en la ruta /proyectoFinal/consumirVistas/* , procedemos a consumir
cada una de las vistas generadas procesando cada tweet, con lo cual verificamos si contienen alguna
de las palabras mas comunes relacionadas a la consulta popular, almacenamos los resultados en un archivo
con formato json, los cuales se pueden observar en la ruta /proyectoFinal/tweetsConsulta/*

# Entrenamiento
- Con los archivos en formato json de la ruta /proyectoFinal/tweetsConsulta/, procedemos a generar dos archivos
uno de entrenamiento y otro de test, los cuales están ubicados en la ruta /proyectoFinal/clasificador/, para 
el clasificador bayesiano que se encuentra en la misma ruta, obteniendo una certeza(accuracy) del 0.

# Análisis
- El análisis de los datos se realiza en base a cada uno de los archivos json generados, contando el número
de registros a favor del SI, y a favor del NO, generamos un gráfico de tipo pastel con los resultados.
- Las gráficas generadas y los archivos que las generan se pueden observar en la ruta /proyectoFinal/graficas/