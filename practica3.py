import pandas as pd
import matplotlib.pyplot as plt

"""
Importamos las siguientes librerías:
	pandas: para importar el csv con el que trabajaremos y analizar y trabajar con los diferentes métodos que nos proporciona esta librería para realizar operaciones y trabajar con los datos.
	matplotlib: para la creación de gráficos con los diferentes datos que extraemos del documento csv que importamos con pandas para una mejor visualización de los datos.
"""
d = pd.read_csv('finanzas2020[1].csv', header=0, sep= '\t')
d.head()

# En este caso no suma las columnas correctamente por que tiene valores erroneos en algunas columnas, vamos a solucionarlo
d.sum()

"""
Métodos:
	apply: cambia los valores de las columnas a numéricos para que convierta los valores de tipo string a numérico(esto se hace con el método de pandas, to_numeric(se le pasa como parámetro al
	       método apply, el parámetro 'coerce' es para que cuando se encuentre un valor que no pueda convertir a numérico lo convierta en NaN.
	fillna: este método convierte todos los valores de NaN a 0(0 por que es el parámetro que se le pasa, se le pueden pasar otros como la media de la columna u otros valores).
"""
d = d.apply(pd.to_numeric, errors='coerce')
d = d.fillna(0)

"""
Después de cambiar los valores a numéricos y todos los valores de Nan a 0, usamos varios métodos para visualizar datos.
	-describe: devuelve una serie de parámetros de las columnas del csv con el que estamos trabajando como es la media, el mínimo de cada columna, el máximo, el número de valores de cada fila y 
	           algunos valores más. 
	-sum: devuelve la suma de todos los valores de cada columna.
	-min : devuelve el valor más pequeño
	-max : devuelve el valor más grande
	
En este caso tanto el mínimo como el máximo se usan en esta práctica para que nos devuelva los meses en los que menos se ha gastado y en los que más se ha gastado y también los meses en los que más se ha ingresado y en los que menos se ha ingresado.
"""
d.describe()
d.sum()
suma = d.sum()
"""
Variables:
	-suma : creamos la variable suma que está definida con el método sum, por lo que ésta variable suma devuelve la suma de los valores de cada columna
	-gastos : la variable gastos nos devolverá la suma de todas las columnas de la variable g, por lo que nos devolverá la suma de los valores negativos de las columnas.
	-ingresos : la variable ingresos nos devolverá la suma de todas las columnas de la variable i, por lo que nos devolverá la suma de los valores positivos de las columnas.
	-meses : la variable meses nos devuelve el nombre de las columnas, que son los 12 meses del año, desde Enero hasta Diciembre.
	-i : la variable i nos devuelve el csv en los que solo aparecen valores positivos, es decir, que sean mayores que 0, los valores que no sean mayores que 0 aparecerán con un NaN.
	-g : la variable g nos devuelve el csv en los que solo aparecen valores negativos, es decir, que sean menores de 0, los valores que no sean mayores que 0 aparecerán con un NaN.
"""
# Mes en el que más se ha gastado (Abril)
suma.min()
# Mes en el que mas se ha ahorrado (Enero)
suma.max()

g = (d[d<0])
print(g)

g.sum()
gastos = g.sum()

# Suma de los gastos de todo el año 
gastos.sum()

# Media de los gastos de todo el año
gastos.mean()

i = (d[d>0])
print(i)

i.sum()
ingresos = i.sum()

# Media de los ingresos de todo el año
ingresos.mean()

# Suma de los ingresos de todo el año
ingresos.sum()

meses = d.columns
"""
Métodos usados de la librería Matplotlib:
					-figure: con este método creamos la figura en la que vamos a visualizar el gráfico y le pasamos como parámetro las medidas que queremos.
					-bar: con este método le estamos diciendo que queremos que nos muestre los datos del gráfico en barras.
					-title: este método crea el título que aparecerá en el gráfico, se le pasa un texto como parámetro que será el nombre del título
					-xlabel: se le pasa un string como parámetro que será el nombre(etiqueta) de nuestro eje x.
					-ylabel: se le pasa un string como parámetro que será el nombre de nuestro eje y.
					-show: con este método mostramos el gráfico.
					
"""
plt.figure(figsize=(13,5))
plt.bar(meses, ingresos)
plt.title("Ingresos a lo largo del año")
plt.xlabel('Meses')
plt.ylabel('Ingresos')
plt.show()

try:
    file = open('finanzas2020[1].csv')
    lines = file.readlines()
except IOError as err:
    print("No encuentro el fichero o no puedo leerlo. Error: ", err)
else:
    print("He leido el fichero sin problemas. Lo cierro y termino")
    file.close()


len_column = len(d.columns)
class Error(Exception):
    pass

class ValorIncorrecto(Error):
    pass
    
try:
    if len_column < 12 or len_column > 12:
        raise ValorIncorrecto
    else:
        print("El número de columnas es: ", len_column)
        print('Coincide el número de columnas con los meses del año')
except ValorIncorrecto:
    print('No coincide el número de columnas con el de meses del año')
