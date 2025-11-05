import openseespy.opensees as ops
import opsvis as opsv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
from Functions import *

warnings.filterwarnings("ignore")

# Unidades Base mks
m = 1
kg = 1
s = 1

# Otras Unidades
cm = 0.01*m
#kgf = 9.80665*kg*m/s**2
kgf = 9.81*kg*m/s**2
tonf = 1000*kgf

# Constantes Físicas
#g = 9.80665*m/s**2
g = 9.81*m/s**2

ops.wipe()
ops.model('basic','-ndm',3,'-ndf',6)

data1 = pd.read_excel("data.xlsx", sheet_name="nodos")
nodos = data1.to_numpy(dtype=np.float64)

for idx, nodoi in enumerate (nodos):
    ops.node(idx+1, *nodoi)

opsv.plot_model(fig_wi_he = (25,20))
plt.show()

ops.fixZ(0.0, *[1,1,1,1,1,1])

fc = 280*kgf/cm**2
E = 150*fc**0.5*kgf/cm**2   # Modulo de elasticidad
G = 0.5*E/(1+0.2)           # Modulo de corte

# Viga
b, h = 30*cm, 60*cm
Av = b*h
Izv = b*h**3/12
Iyv = b**3*h/12
aa, bb = max(b,h), min(b,h)
B = 1/3-0.21*bb/aa*(1-(bb/aa)**4/12)
Jxxv = B*bb**3*aa

# Columna
a, a = 45*cm, 45*cm
Ac = a*a
Izc = a*a**3/12
Iyc = a**3*a/12
aa, bb = max(a,a), min(a,a)
B = 1/3-0.21*1*(1-(1)**4/12)
Jxxc = B*bb**3*aa

# Densidad del concreto
p = 2400*kg/m**3

CTransform = 1      # Etiqueta de la Transformación para columnas
BTransform = 2      # Etiqueta de la Transformación para vigas

ops.geomTransf("PDelta",CTransform,*[1,0,0])
ops.geomTransf("Linear",BTransform,*[0,0,1])

# Columnas
for i in range(1, 37):
    ops.element('elasticBeamColumn', i, i, i+12, Ac, E, G, Jxxv, Iyc, Izc, CTransform, '-mass', p*Ac*10**-8)

data2 = pd.read_excel("data.xlsx", sheet_name="elementos")
vigas = data2.to_numpy(dtype=np.float64)

# Vigas
for idx, vigai in enumerate(vigas):
    ops.element('elasticBeamColumn', idx+37, *vigai, Av, E, G, Jxxv, Iyv, Izv, BTransform, '-mass', p*Av*10**-8)

opsv.plot_model(fig_wi_he = (25,20))
plt.show()