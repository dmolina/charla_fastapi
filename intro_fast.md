---
pagetitle: "Servicios REST con FastAPI"
theme: sky
author: "Daniel Molina Cabrera"
---

## Servicios REST con
<img src="slides/FastAPI.jpg" width="30%"></img><br>

<center>Daniel Molina Cabrera<br>
(http://dmolina.github.io)
</center>

---

## ¿Quién soy yo?

<ul style="margin=300px">
<li>Profesor Titular de Informática de la Universidad de Granada</li>
<li>Experto en Inteligencia Artificial.</li>
<li>Desarrollador/Usuario de Python durante más de 10 años.</li></ul>
<img src="yo_serio.png" width="20%" style="float: center"/>

---

## ¿Quién soy yo?

<ul style="margin=300px">
<li> Partidario convencido del Software Libre</li>
<li> <i>Linuxero</i> convencido.</li>
<li> Gran fan de Python.</li>
</ul>
<img src="yo_indiana.jpg" width="30%" style="float: center"></img>

# Servicios REST

## ¿Qué son servicios REST?

<img src="rest.png" alt="Servicio REST"/>

---

## ¿Qué son servicios REST?

<img src="rest_imagen.png" alt="Esquema REST"/>

---


## Ventajas de los servicios REST

- Distinto lenguaje de <i>frontend</i> y de <i>backend</i>.

- Fácil y cómodo.

- Modelo multi-servicios.

- Cada vez más usados con frameworks JS.

# FastAPI

## ¿Qué es FastAPI?

<img src="slides/FastAPI.jpg" width="30%"></img><br>

- Librería en <strong>Python</strong> para servicios <strong>REST</strong>.

- Fácil de usar, y centrada en lo usado.

---

## ¿Qué es Python?

Lenguaje de programación

de <span class="fragment visible highlight-blue">propósito general</span> y
<span class="fragment visible highlight-red">fácil de aprender</span>.

---

## ¿Por qué es popular?

Es muy sencillo y legible

```python
msg = "Hola a todos"
print(msg)
print(msg.replace("os", "as"))

for name in ["Amalia", "Arturo"]:
    print(f"a {name} también")
```
---

## Es muy potente

- Repositorio centralizado de librerías. 
- Librerías para casi todo.

<img src="slides/box_python.png" class="plain" width="50%">

# demo de FastAPI

---

### Muy Sencillo

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hola a todo el  mundo"}
```

---

## Ejecutándolo

```sh
unicorn test:app --reload
ó
hypercorn test:app --reload
```

---

## Documentación

<img src="docs.png" width="60%"></img>

---

### Lectura de parámetros

```python
@app.get("/hello/{name}")
def  hello(name):
    return {"msg": f"Hola, {name}"}
```

---

### Parámetros

```python
@app.get("/list/{category}")
def list(category, page=0):
    return {"series": f"series from category {category}, from page {page}"}
```

---

### Validación automática

```python
@app.get("/vota/{puntuacion}")
def  hello(puntuacion: int):
    return {"resultado": f"Sumo {puntuacion}"}
```

---

### Opciones de Validación

```python
@app.get("/hola/{name}")
def  hello(name: str = Path("desconocido", min_length=5)):
    return {"msg": f"Hola, {name}"}
```

```python
@app.get("/vota/{puntuacion}")
# gt implies greater than
# le implies less or equals to
def hello(puntuacion: int,  Path(0, gt=0, le=10)):
   return {"resultado": f"Sumo {puntuacion}"}
```

# Servicio REST de Series

---

## Servicio REST de Series

- Acceso a Base de Datos de datos sobre series de streaming.

- Servicio REST sobre dichos datos.

- Validación de datos.

---

## Página web

- Usaremos Bootstrap v5 como framework CSS.

- Usaremos Vue como frontend.

- Se ejecuta JS en el cliente.

- Compondremos la web a partir de los servicios REST.

---

## Caso 1: Consulta de Categorías

### Servicio REST (demo

```python
@app.get("/categories")
def hello():
    return {"categories": [{'id': 0, 'text': "Comedy"}, {'id': 1, 'text': "Drama"}, {'id': 2, 'text': 'Musical'}]}
```

---

### HTML

```html
            <div id="app">
                <h1>Listado de las Categorías:</h1>
                <ul>
             <li v-for="category in categories" :key="category.id">
                 <strong>{{category.text}}</strong>
             </li>
                </ul>
            </div>
```

---

### Javascript

```javascript
app = new Vue({
    el: '#app',
    created() {
        this.fetchData();
    },
    data: {
        categories: []
    },
    methods: {
        fetchData() {
            axios.get('http://localhost:8000/categories').then(response => {
                this.categories = response.data.categories;
            });
        }
    }
});
```

--

## Resultado

<img src="categorias.png" width="80%"></img>
