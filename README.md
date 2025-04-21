NotebooksApi
API RESTful para la gestión de notebooks (portátiles) desarrollada con FastAPI como proyecto final de un curso.
Descripción
NotebooksApi es una API que permite administrar un catálogo de notebooks con operaciones CRUD (Crear, Leer, Actualizar y Eliminar). Este proyecto representa el trabajo final de un curso de FastAPI, aplicando los conocimientos adquiridos durante el mismo.
Características

Arquitectura RESTful: Implementación de endpoints siguiendo principios REST
Documentación automática: Generada por FastAPI (Swagger UI y ReDoc)
Validación de datos: Mediante Pydantic
Manejo de excepciones: Sistema para gestión de errores HTTP
Testing: Pruebas implementadas con pytest

Requisitos
Para ejecutar este proyecto necesitarás:

Python 3.7+
FastAPI
Uvicorn
Otras dependencias especificadas en requirements.txt

Instalación

Clona este repositorio
Crea un entorno virtual (recomendado)
Instala las dependencias:
pip install -r requirements.txt


Ejecución
Para iniciar el servidor de desarrollo:
uvicorn main:app --reload
Esto lanzará la API en http://localhost:8000.
Estructura del proyecto
NotebooksApi/
├── .venv/
├── api/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── notebooks.json
│   ├── routes/
│   │   ├── __init__.py
│   │   └── notebooks.py
│   └── utilities/
│       ├── __init__.py
│       ├── docs.py
│       └── models.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── main.py
├── notebooks_data.py
├── README.md
└── requirements.txt
Documentación de la API
Una vez iniciado el servidor, puedes acceder a la documentación interactiva:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Endpoints principales
Notebooks

GET /notebooks: Obtiene todas las notebooks
GET /notebooks/{notebook_id}: Obtiene una notebook por su ID
GET /notebooks/filter: Filtra notebooks por modelo con opciones de paginación
GET /notebooks/price: Filtra notebooks por precio máximo
GET /notebooks/operating_systeam: Filtra notebooks por sistema operativo
POST /notebooks: Añade una nueva notebook
PUT /notebooks/{notebook_id}: Actualiza información de una notebook existente
DELETE /notebooks/{notebook_id}: Elimina una notebook

Pruebas
El proyecto incluye pruebas con pytest para verificar la funcionalidad de los endpoints.
bashpytest
Este proyecto representa la culminación de un curso de FastAPI, donde se aplicaron conceptos como la creación de rutas, manejo de modelos de datos, documentación automática y testing.
