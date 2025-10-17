# APLICACIONES WEB EN INGENIERÍA ESTRUCTURAL
## Desarrollo de Aplicaciones Web en la Ingeniería Estructural

### ¿Cuáles son las **ventajas** de **programar** frente a otras herramientas?

Con **excel** se puede hacer muchas cosas interesantes **pero** es muy engorroso.

#### Accesibilidad y Portabilidad

Solo necesitamos una conexión a internet para poder acceder a estas herramientas.

#### Automatización y optimización

Los lenguajes de programación nos permiten automatizar nuestros flujos de trabajo.

#### Interactividad y Experiencia de Usuario

Personalización del UX/UI.

#### Escalabilidad y Mantenimiento

Ir añadiendo más módulos con el tiempo.

#### Integración con Herramientas Externas

Conectarnos mediante APIs con herramientas como Revit, SAP2000, Etabs, AutoCAD.

### ¿Qué **implica** desarrollar una **aplicación web**?

* Frontend
* Backend
* Despliegue, seguridad, etc

### Hoy usaremso **python**

Con el framework **Streamlit**.

---

## Uso de Streamlit

### Instalar Streamlit

Crear entorno virtual:

```bash
python -m venv <nombre-venv>
```

Instalar **Streamlit**:

```bash
pip install streamlit
```

Instalar todas las dependencias:

```bash
pip install -r requirements.txt
```

### Primer programa

```python
import streamlit as st

st.write("Esta es nuestra primera aplicación con streamlit para ingenieria estructural")
```

Ejecutar el programa:

```bash
streamlit run app.py
```

Por defecto corre en el puerto:

```plaintext
http://localhost:8501/
```

## Aplicación vista en clase

* Enlace a GitHub: [Repositorio del Taller](https://github.com/efradev/TallerAppWeb)

---

## Versión de Python usada

* Python **3.13.1**