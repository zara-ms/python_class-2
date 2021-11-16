### SCIPY Y MATPLOTLIB
import numpy as np
#from scipy.special import jn
# ejemplo con funcion Bessel (foto de Rosalind Franklin)
#x = np.linspace(xmin, xmax, npts)
#layers = np.array([jn(i, x)**2 for i in range(nlayers)])
#maxi = [(np.diff(np.sign(np.diff(layers[i,:]))) < 0).nonzero()[0] + 1
#                                                   for i in range(nlayers)]
### EJEMPLO DEL MODELO EPIDEMIOLOGICO DE SIR
#from scipy.integrate import odeint
#import matplotlib.pyplot as plt
#SI: Enfermedades víricas que causan infección vitalicia, como el VIH.
#SIS: Enfermedades que no confieren inmunidad tras la infección
#SIR: Enfermedades víricas en las que una vez infectado, se obtiene inmunidad vitalicia
#def deriv(y, t, N, beta, gamma):
    #S, I, R = y
    #dSdt = -beta * S * I / N
    #dIdt = beta * S * I / N - gamma * I
    #dRdt = gamma * I
    #return dSdt, dIdt, dRdt
# Initial conditions vector
#y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
#ret = odeint(deriv, y0, t, args=(N, beta, gamma))
#S, I, R = ret.T

### Grafica interactiva
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons  # Interactivo

def dySIS(y, t, lamda, mu):  # SI/SIS model
    dy_dt = lamda*y*(1-y)-mu*y
    return dy_dt
def dySIR(y, t, lamda, mu):  # SIR model,
    i, s = y
    di_dt = lamda*s*i-mu*i
    ds_dt = -lamda*s*i
    return np.array([di_dt,ds_dt])

# valores de parametros
number = 1e5 # total number of people
lamda = 0.2 # Daily contact rate, the average number of susceptible persons who are effectively in contact with the sick each day
sigma = 2.5 # Number of contacts during infectious period
mu = lamda/sigma # Daily cure rate, the ratio of the number of patients cured each day to the total number of patients
tEnd = 200 # Forecast date length
t = np.arange(0.0,tEnd,1) # (start,stop,step)
i0 = 1e-4 # Initial value of the proportion of patients
s0 = 1-i0 # Initial value of the proportion of susceptible persons
Y0 = (i0, s0) # Initial value of the differential equation system

ySI = odeint(dySIS, i0, t, args=(lamda,0)) # SI model
ySIS = odeint(dySIS, i0, t, args=(lamda,mu)) # SIS model
ySIR = odeint(dySIR, Y0, t, args=(lamda,mu)) # SIR model

#Graficar
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.4)

plt.title("Comparison among SI, SIS and SIR models")
plt.xlabel('time')
plt.axis([0, tEnd, -0.1, 1.1])

si_plt, = plt.plot(t, ySI,':g', label='i(t)-SI')

sis_plt, = plt.plot(t, ySIS,'--g', label='i(t)-SIS')

sir_i_plt, = plt.plot(t, ySIR[:,0],'-r', label='i(t)-SIR')
sir_s_plt, = plt.plot(t, ySIR[:,1],'-b', label='s(t)-SIR')
sir_r_plt, = plt.plot(t, 1-ySIR[:,0]-ySIR[:,1],'-m', label='r(t)-SIR')

plt.legend(loc='best')  # buscar la mejor localizacion

#Agregar barras interactivas
axcolor = 'lightgoldenrodyellow'
# Generamos el área de las barras
axlambda = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axsigma = plt.axes([0.25, 0.18, 0.65, 0.03], facecolor=axcolor)
axi0 = plt.axes([0.25, 0.26, 0.65, 0.03], facecolor=axcolor)
# Agregamos la información
slambda = Slider(axlambda, 'Daily contact rate', 0.1, 1,
               valinit=lamda, color="green")
ssigma = Slider(axsigma, 'Contacts during\ninfectious period', 0.1, 10,
                valinit=sigma)
si0 = Slider(axi0, 'Initial proportion\nof patients', 1e-4, 5e-1,
                valinit=i0, color="orange")
plt.show()
### actualizacion
def update(val, ):
    lamda = slambda.val
    sigma = ssigma.val
    i0 = si0.val
    mu = lamda / sigma
    s0 = 1 - i0
    Y0 = (i0, s0)
    ySI = odeint(dySIS, i0, t, args=(lamda, 0))  # SI model
    ySIS = odeint(dySIS, i0, t, args=(lamda, mu))  # SIS model
    ySIR = odeint(dySIR, Y0, t, args=(lamda, mu))  # SIR model
    si_plt.set_ydata(ySI)
    sis_plt.set_ydata(ySIS)
    sir_i_plt.set_ydata(ySIR[:, 0])
    sir_s_plt.set_ydata(ySIR[:, 1])
    sir_r_plt.set_ydata(1 - ySIR[:, 0] - ySIR[:, 1])
    fig.canvas.draw_idle()
    plt.show()

### se aplica la funcion
slambda.on_changed(update)
ssigma.on_changed(update)
si0.on_changed(update)

### botones para ver un solo tipo de modelo
rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('SI', 'SIS', 'SIR'), active=0)
lines = {'SI':[si_plt], 'SIS':[sis_plt],
             'SIR':[sir_i_plt, sir_s_plt, sir_r_plt]}
def select_model(label):
    # la linea seleccionada no es transparente
    for line_m in lines[label]:
        line_m.set_alpha(1)
    # las demas lineas seran transparentes
    for others in set(lines.keys()) - set([label]):
        for line_m in lines[others]:
            line_m.set_alpha(0)
    fig.canvas.draw_idle()
# donde de click, va a mostrar
radio.on_clicked(select_model)
plt.show()