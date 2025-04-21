from enum import Enum
from pydantic import BaseModel, Field

class OSType(str, Enum):
    other = "other"
    windows = "windows"
    ubuntu = "ubuntu"
    mac = "mac"
    dos = "dos"

# Modelo para un Laptop
class Notebook(BaseModel):
    marca: str = Field(description="Nombre de la marca de la notebook")
    modelo: str = Field(description="Nombre del modelo de la notebook")
    precio: int = Field(gt=0, description="Precio de la notebook. Mayor a 0")
    rating: int = Field(gt=0, description="Rating de la notebook. Mayor a 0")
    marcaprocesador: str = Field(description="Marca del procesador de la notebook")
    modeloprocesador: str = Field(description="Modelo del procesador de la notebook")
    numcores: int = Field(gt=0, description="Cantidad de nucleos del procesador. Mayor a 0")
    numthreads: int = Field(gt=0, description="Cantidad de hilos del procesador. Mayor a 0")
    memoriaram: int = Field(gt=0, description="Memoria RAM de la notebook. Mayor a 0")
    tipomemoriaprimaria: str = Field(description="Tipo de memoria de la notebook(HDD, SSD, etc)")
    capacidadmemoriaprimaria: int = Field(gt=0, description="Cantidad de almacenamiento. Mayor a 0")
    tipomemoriasecundaria: str = Field(description="Tipo de almacenamiento secundario")
    capacidadmemoriasecundaria: int = Field(ge=0, description="Cantidad del almacenamiento secundario. Mayor o igual a 0")
    marcagpu: str = Field(description="Marca de la GPU de la notebook")
    tipogpu: str = Field(description="Tipo de GPU")
    pantallatactil: str = Field(description="Si tiene pantalla tactil o no")
    tamanyopantalla: int = Field(gt=0, description="Tamaño de la pantalla. Mayor a 0")
    resolucionpantalla1: int = Field(gt=0, description="Resolucion en el largo de la pantalla. Mayor a 0")
    resolucionpantalla2: int = Field(gt=0, description="Resolucion en el ancho de la pantalla. Mayor a 0")
    OS : OSType = Field(default=OSType.other, description="Sistema operativo que tiene la notebook")
    anyosgarantia: int = Field(gt=0, description="Cantidad de años de garantia de la notebook. Mayor a 0")



