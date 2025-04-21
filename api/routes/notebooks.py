from fastapi import APIRouter, status, Path, HTTPException, Query
from typing_extensions import Annotated
from watchfiles import awatch

from api import NotebookData

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
            summary="Devuelve notebooks",
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





















