# Markdown en Jupyter Notebooks para Ingeniería

## Markdown

---
Texto de enfasis
---

*Cursiva* o _texto en cursiva_

**Negrita**

texto en formato normal

***Negrita y Cursiva***

~~Tachado~~

# Seccion 1
## Seccion 1.1
# Seccion 2
## Sub-seccion debajo de la seccion 2
### Sub seccion debajo de la sub-seccion 2 2
# Seccion 3

---

Listas:

* Forma 1

- Forma 2

- Lista
  - Sub-lista debajo de la lista
    - Sub-lista debajo de una sub-lista

1. Lista ordenada
1. Lista ordenada
   1. Sub-lista ordenada debajo de la lista ordenada

---

### BLOQUE DE CODIGO

```python
def nombre_funcion(input1, input2, ..., inputn):
    cuerpo de la funcion
    return output
```

```java
script type="text/javascript">
    function fancyAlert(arg) {
        if(arg) {
            $.facebox({div:'#foo'})
        }
    }
```

```python
Li = object.define(corri,   # Coordenada i
                    coork,  # Coordenada i
                    A,      # Area de la seccion
                    E,      # Modulo de elasticidad
                    I,      # Inercia de la seccion
                    J,      # Torsion
                    mass)   # Masa modal
```

---

### LINKS DE ENLACES

```markdown
[nombre de tu referencia] (http:www.tuenlace.com)
```

---

### IMAGENES

```markdown
![Texto alternativo](/ruta/a/la/imagen.jpg)
```

```html
<p align="center">
    <img src="enlace-o-ruta" alt="drawing" width="100" />
</p>
```

---

### TABLAS

| How | To | Make | a table
| --- | --- | --- | ---
| in  | Jupyter | Notebook| Markdown
| It  | is | really| cool

---

### INDENTACION

```markdown
> Un nivel de Indentacion
```

```markdown
>> Dos niveles de indentacion
```

> 1 Blockquotes
>> 2 Blockquotes
>>> 3 Blockquotes
>>>> 4 Blockquotes
>>>>>>>> 8 Blockquotes

---

$$x^{2}+3x_{b} = \sum f_{{x}}$$

[Calculadora Latex](https://latex.codecogs.com/eqneditor/editor.php?lang=es-es)