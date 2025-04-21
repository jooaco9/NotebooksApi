from fastapi import APIRouter, status, Path, HTTPException, Query, Body
from typing_extensions import Annotated

from api import NotebookData
from api import OSType, Notebook

# Instancia de NotebookData
notebooks = NotebookData()

# Router
router = APIRouter()

# GETS

# Endopoint para obtener notebooks con distintos filtrados
@router.get("/filter", status_code=status.HTTP_200_OK,
            summary="Devuleve notebooks con filtrados",
            description="""
                Devuelve notebooks salteando "skip" notebooks, la cantidad van a ser "total" y con un opcional de filtrar segun el modelo con "filter_name"
            """
            )
async def get_notebook_filter(skip: Annotated[int,
                                    Query(
                                        description="Cantidad de notebooks a saltear"
                                    )] = 0,
                              total: Annotated[int,
                                    Query(
                                        description="Cantidad total de notebooks a mostrar"
                                    )] = 15,
                              name_filter: Annotated[str | None,
                                            Query(
                                                description="Filtro de busqueda, por modelo de notebook",
                                                min_length=2,
                                                max_length=12
                                            )] = None
                              ):

    return await notebooks.get_notebook_model(skip, total, name_filter)

# Endpoint para obtener notebooks con precio menor a max_price
@router.get("/price", status_code=status.HTTP_200_OK,
            summary="Devuelve notebooks segun un precio",
            description="""
                Devuelve las notebooks con precio menor a "max_price"
            """
            )
async def get_notebooks_max_price(max_price: Annotated[int,
                                            Query(
                                                description="Precio maximo que pueden tener las notebooks",
                                                gt=0
                                            )] = 1):
    return await notebooks.get_notebooks_max_price(max_price)

# Endopoint para obtener notebooks por sistema operativo "os"
@router.get("/operating_systeam", status_code=status.HTTP_200_OK,
            summary="Devuelve las notebooks de un sistema operativo en concreto",
            description="""
                Devuelve las notebooks con el sistema operativo "os" 
            """
            )
async def get_notebooks_os(os: Annotated[OSType,
                                Query(
                                    description="Nombre del sisetma operativo"
                                )] = OSType.other):
    return await notebooks.get_notebooks_os(os)

# Endopoint para obtener notebook mediante id
@router.get("/{notebook_id}", status_code=status.HTTP_200_OK,
            summary= "Buscar notebook",
            description="Buscar notebook a traves del notebook_id"
            )
async def get_notebook(notebook_id: Annotated[int,
                                    Path(
                                        description="Id del notebook",
                                        gt=0
                                    )]):
    # Obtener notebook
    notebook = await notebooks.get_notebook(notebook_id)

    # Si no esta la notebook con ese id, excepcion
    if not notebook:
        raise HTTPException(status_code=404, detail=f"Notebook con id: {notebook_id} no encontrada")

    return notebook

# Endpoint para obtener todas las notebooks
@router.get("", status_code=status.HTTP_200_OK,
            summary="Devolver notebooks",
            description="Devuelve todas las notebooks del sistema"
            )
async def get_all_notebooks():
    return await notebooks.get_all_notebooks()


# POSTS

# Endpoint para agregar una notebook
@router.post("", status_code=status.HTTP_200_OK,
             summary="Agregar notebook",
             description="Agregar una nueva notebook al catalogo de notebooks"
             )
async def write_notebook(notebook: Annotated[Notebook,
                                    Body(
                                        description="Modelo para representar cada notebook"
                                    )]) -> Notebook:
    return await notebooks.write_notebook(notebook)


# PUTS

# Endpoint para actualizar una notebook
@router.put("/{notebook_id}", status_code=status.HTTP_200_OK,
            summary="Actualizar notebook",
            description="Actualizart una notebook del catalogo mediante un notebook_id"
            )
async def update_notebook(notebook_id: Annotated[int,
                                        Path(
                                            gt=0,
                                            description="Id de la notebook a actualizar"
                                        )],
                          notebook: Annotated[Notebook,
                                    Body(
                                        description="Notebook con los datos actualizados"
                                    )]) -> Notebook:

    notebook_found = await notebooks.update_notebook(notebook_id, notebook)

    if not notebook_found:
        raise HTTPException(status_code=404, detail=f"Notebook con id: {notebook_id} no encontrada")

    return notebook_found

















