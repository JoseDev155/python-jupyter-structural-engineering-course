# Introducción a Matplotlib para Ingeniería Civil

## matplotlib

### Representación gráfica en Python
### INTRODUCCION A MATPLOTLIB

La visualización de datos es la respresentación gráfica de los datos. Implica producir imágenes que comuniquen las relaciones entre los datos
representados. La visualizaciín de datos es una parte esencial del análisi de datos y el aprendizaje automática. Usaremos la biblioteca de
Python Matplotlib para aprender y aplicar algunas técnicas populares de visualización de datos.

#### Librerías necesarias

Para este tema vamos a necesitar las siguientes librerías

```python
import matplotlib.pyplot as plt
import numpy as np
```

```python
import warnings
warnings.filterwarnings("ignore")
```

#### General

Al modulo Matplotlib.plyplot lo renombramos como `plt`:

```python
import matplotlib.pyplot as plt
```

#### Colores
##### Colores por defecto

Python trae los siguientes colores por defecto:

| nombre    | abreviatura | color    |
| --------- | ----------- | -------- |
| `blue`    | b           | azul     |
| `green`   | g           | verde    |
| `red`     | r           | rojo     |
| `cyan`    | c           | cian     |
| `magenta` | m           | magenta  |
| `yellow`  | y           | amarillo |
| `black`   | k           | negro    |
| `white`   | w           | blanco   |

#### Scatter Plot

Para hacer un gráfico de nube de puntos, usamos el método `.scatter()` del módulo `plt`.

Algunos de los parámetros de este método son:

* `x`: scalar, array o lista que indica la primera coordenada de las observaciones
* `y`: scalar, array o lista que indica la segunda coordenada de las observaciones
* `c`: para cambiar el color de relleno
* `edgecolors`: para cambiar el color del contorno
* `alpha`: para cambiar la transparencia
* `marker`: para cambiar la forma del punto
* `s`: para cambiar el tamaño de los puntos (se mide en puntos)
* `linewidths`: para cambiar el grosor del contorno

```python
height = [174.3, 180.3, 183.4, 173.2, 186.4, 188.7, 175.8, 178.2, 177.2, 189.1]
weight = [65.7, 71.8, 76.4, 69.7, 78.5, 80.9, 71.2, 73.1, 74.9 84.3]

plt.figure()
plt.scatter(height,
            weight,
            color = "blue",
            edgecolors = "black",
            alpha = 0.8,
            marker = "o",
            s = 200,
            linewidths = 0.5)
plt.title("Altura vs pesos")
plt.xlabel("Alturas $(cm)$")
plt.ylabel("Pesos $(Kg)$")
plt.show()
```

**Observción**. Podríamos mostrar 2 conjuntos diferentes de datos en un gráfico de nube de puntos:

```python
height_boys = [174.3, 180.3, 183.4, 173.2, 186.4, 188.7, 175.8, 178.2, 177.2, 189.1]
weight_boys = [65.7, 71.8, 76.4, 69.7, 78.5, 80.9, 71.2, 73.1, 74.9, 84.3]

height_girls = [154.2, 156.1, 160.3, 157.9, 162.6, 153.9, 170.1, 165.2, 157.6, 163.5]
weight_girls = [55.3, 54.2, 47.3, 62.4, 77.5, 60.3, 52.4, 58.1, 50.2, 80.1]

plt.figure()
plt.scatter(height_boys, weight_boys, c = "red", marker = "^", s = 100)
plt.scatter(height_girls, weight_girls, c = "blue", marker = "^", s = 300, alpha = 0.4)

plt.title("Altura vs pesos")
plt.xlabel("Alturas $(cm)$")
plt.ylabel("Pesos $(Kg)$")
plt.show()
```

**Observción**. Podemos dibujar cada punto de un tamaño, pasando una lista al parámetro `s`:

```python
x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 6, 4, 8, 10, 9, 7]
sizes = [100, 250, 300, 450, 500, 550, 600]
```

```python
plt.figure()
plt.scatter(x, y, s = sizes, c = "r")
plt.title("Diferentes tamaños")
plt.show()
```

## Crear y activar entorno virtual

## Instalar librerías

Ejecutamos:

```bash
pip install -r requirements.txt
```