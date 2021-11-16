### SCATTER PLOT
### import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# plt.scatter(x, y, marker="o") # para scatter
# datos de iris de sklearn.database
iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.title("scatter plot exploratorio")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()

### DATAFRAMES
import pandas as pd
air_quality = pd.read_csv("files/clase_8_pt1/air_data.csv",
                            index_col=0, parse_dates=True)
print(air_quality.head())
# NO2 de Londres a Paris
print(air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5))
#boxplot (DataFrame.plot.box())
print(air_quality.plot.box())

### Graficas separadas
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
### Personalizacion
# fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
# fig.savefig("no2_concentrations.png")
### matplot.widgets
### slider > variar cosas en la grafica
import numpy as np
from math import pi
a = 5
b = 5
t = np.linspace(0, 2*pi, 100)
x = a * np.cos(t)
y = b * np.sin(t)
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
# importante ajustar espacio donde queremos el slider
plt.subplots_adjust(bottom = 0.3)
#usamos la coma para poder quedarnos con el valor y
plot, = ax.plot(x,y)
recuadro = plt.axes([0.25, 0.1, 0.65, 0.03])
recuadro2 = plt.axes([0.25, 0.2, 0.65, 0.03])
#                   x     y    ancho  altura
factor = Slider(recuadro, 'factor a cambiar', valmin = 0.1,
                  valmax = 10, valinit = 1, valstep = 1)
#crear slider
factor2 = Slider(recuadro, 'factor a cambiar', valmin = 0.1,
                  valmax = 10, valinit = 1, valstep = 1)
factor3 = Slider(recuadro, '2do factor a cambiar', valmin = 0.1,
                  valmax = 10, valinit = 8, valstep = 1)

### funcion para actualizar datos y plotear linea

def update(val):
    #1. tomamos valor de slider
    nuevo_valor = factor2.val
    nuevo_valor2 = factor3.val
    #2. actualizamos operaciones que son afectadas por el factor
    x = nuevo_valor*np.sin(t)
    y = nuevo_valor2*np.cos(t)
    #3. Modificamos datos que están en plot (p.)
    #p.set_xdata(x)
    #p.set_ydata(y)
    #4. dibujar linea con actualizaciones
    plt.draw()
# llamado
factor2.on_changed(update)

plt.show()

ax.set_ylim([-25, 25])
plt.title("elipse")

### RADIO BUTTONS
from matplotlib.widgets import RadioButtons
f_seno = np.sin(t)
f_coseno = np.cos(t)
f_tan = np.tan(t)
fig, ax = plt.subplots()
plot, = ax.plot(x,y)
plt.subplots_adjust(left=0.3)
#color del recuadro
axcolor = 'lightgoldenrodyellow'
# x, y, ancho, alto y color
rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor = axcolor)
# especificamos opciones que tendra el botón
radio = RadioButtons(rax, ('f_seno', 'f_coseno', 'f_tan'))
plt.show()
#actualizacion
#def estilo(label):
    #l.set_linestyle(label)
    #plt.draw()
def tipo_funcion(label):
    fun_dict = {"seno": f_seno, "coseno": f_coseno, "tangente": f_tan}
    nueva_funcion = fun_dict[label]
    #cambiar datos de y
    plot.set_(nueva_funcion)
    #plotear nueva funcion
    plt.draw()
#cada cambio de radio hay una actualizacion
radio.on_clicked(tipo_funcion)
plt.show()
