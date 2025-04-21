import json
import os
from api.utilities.models import Notebook


# Clase que nos permite trabajar con los datos de laptops
class NotebookData:

    #Propiedades que almacenarán todos los datos
    notebooks = []
    file_notebooks = None
    work_dic = None

    def __init__(self):
        self.work_dic = os.getcwd()
        self.work_dic = self.work_dic + "\\api\\data\\"
        #Carga de los ficheros de datos de prueba
        self.file_notebooks = open(self.work_dic + 'notebooks.json')
        self.notebooks = json.load(self.file_notebooks)
        self.file_notebooks.close()


    # Devolucion asincrona de un portatil
    async def get_notebook(self, notebook_id: int):
        # si no se encuentra el alimento se devolverá el nulo en vez de un objeto JSON
        notebook = None
        #Recorremos todos los datos JSON
        for item in self.notebooks['notebooks']:
            #Comparamos el id que es int
            if item['id'] == notebook_id:
                notebook = item
                break
        return notebook

    # Devolucion asincrona todos los portátiles
    async def get_all_notebooks(self):
        return self.notebooks

    #Devolucion asincrona de datos de portatiles de un modelo
    async def get_notebook_model(self, skip:int, total: int, name_filter = None):
        notebooks = []
        #si existe name_filter nos quedamos con aquellos que contengan ese filtro
        if name_filter:
            for item in self.notebooks['notebooks'][skip:(total+skip)]:
                # Vemos que el name_filter este incluido en el nombre
                if name_filter in item['modelo']:
                    notebooks.append(item)
        else:
            notebooks = self.notebooks['notebooks'][skip:(total+skip)]
        return {'notebooks': notebooks}

    # Devolucion asincrona de datos de portatiles con un precio menor al marcado
    async def get_notebooks_max_price(self, max_price: int):
        notebooks = []
        #si existe filtronombre nos quedamos con aquellos que contengan ese filtro
        for item in self.notebooks['notebooks']:
            # Comparamos el id que es int
            if item['precio'] <= max_price:
                notebooks.append(item)
        return {'notebooks': notebooks}

    # Devolucion asincrona de datos de portatiles por sistema operativo
    async def get_notebooks_os(self, os: str):
        notebooks = []
        #si existe filtronombre nos quedamos con aquellos que contengan ese filtro
        for item in self.notebooks['notebooks']:
            # Comparamos el id que es int
            if item['OS'] == os:
                notebooks.append(item)
        return {'notebooks': notebooks}

    # Recibimos y guardamos un nuevo portatil
    async def write_notebook(self, notebook: Notebook):
        self.file_notebooks = open(self.work_dic + 'notebooks.json', 'w')
        #Conseguimos el último id de la lista
        last_id_notebook = self.notebooks['notebooks'][-1]['id']
        #Añadimos un nuevo id al ingrediente nuevo
        notebook_dict = notebook.model_dump()
        new_notebook_dict = {
            "id": last_id_notebook + 1,
            **notebook_dict
        }
        # notebook_dict['id'] = last_id_notebook + 1
        self.notebooks['notebooks'].append(new_notebook_dict)
        json.dump(self.notebooks, self.file_notebooks, indent=2)
        self.file_notebooks.close()
        return new_notebook_dict

    # Recibimos y actualizamos un nuevo portatil
    async def update_notebook(self, notebook_id: int, notebook: Notebook):
        self.file_notebooks = open(self.work_dic + 'notebooks.json', 'w')
        #Buscamos el portatil
        notebook_found = None
        notebook_pos = 0
        #Recorremos todos los datos JSON
        for item in self.notebooks['notebooks']:
            #Comparamos el id que es int
            if item['id'] == notebook_id:
                notebook_found = item
                break
            notebook_pos = notebook_pos + 1
        #Si se ha encontrado
        if notebook_found:
            #Realizamos la actualization
            notebook_dict = notebook.model_dump()
            for elem in notebook_dict:
                if notebook_dict[elem]:
                #cambiamos el valor
                    self.notebooks['notebooks'][notebook_dict][elem]=notebook_dict[elem]
            json.dump(self.notebooks, self.file_notebooks, indent=2)
            self.file_notebooks.close()
            return self.notebooks['notebooks'][notebook_dict]
        else:
            return None

    # Borramos un portatil
    async def delete_notebook(self, notebook_id: int):
        self.file_notebooks = open(self.work_dic + 'notebooks.json', 'w')
        #Buscamos el portatil
        notebook_found = None
        notebook_pos = 0
        #Recorremos todos los datos JSON
        for item in self.notebooks['notebooks']:
            #Comparamos el id que es int
            if item['id'] == notebook_id:
                portatil_encontrado = item
                break
            portatil_pos = notebook_pos + 1
        #Si se ha encontrado
        if notebook_found:
            self.notebooks['notebooks'].pop(notebook_pos)
            json.dump(self.notebooks, self.file_notebooks, indent=2)
            self.file_notebooks.close()
            return {"info": "borrado notebook " + str(notebook_id)}
        else:
            return None
