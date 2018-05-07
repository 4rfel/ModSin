def test(Tdentro,t):
    Qsaida = (Tdentro-Tfora)/(espessura/(kar*Areainterna) + 1/(har*Areainterna))
    Qentrada = o * emissividade * Areainterna * (Tpessoa**4-Tdentro**4)
    dTdt = (Qentrada-Qsaida)/m0*cneve
    print(Qsaida)
    return dTdt

from math import pi

kar = 500
raio = 2
Areainterna = 4*pi*raio**2/2
espessura = 0.3
har = 10
Tfora = -45 + 273.15
o = 5.6703e-8
emissividade = 0.95
Tpessoa = 37 + 273.15
volume_ar =  4/3*pi*raio**3
densidade_ar = 1.2922
m0 = densidade_ar * volume_ar
cneve = 2090


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

Tdentro = [Tfora]

Tmax = 24
listaTempo = np.arange(0,Tmax,1)

solucao = odeint(test,Tdentro,listaTempo)
#TempC = [temp-273.15 for temp in solucao[:,0]]
#TempoH = [t/3600 for t in listaTempo]
plt.plot(listaTempo,solucao)
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura K')
plt.show()