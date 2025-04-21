from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

# Tests para endopints de tipo get

# Primer test
def test_get_notebook_filter():

    response = client.get("/notebooks/filter?total=3")
    assert response.status_code == 200
    assert response.json() == {
        "notebooks": [
            {
                "id": 1,
                "marca": "tecno",
                "modelo": "Tecno Megabook T1 Laptop (11th Gen Core i3/ 8GB/ 512GB SSD/ Win11 Home)",
                "precio": 264,
                "rating": 63,
                "marcaprocesador": "intel",
                "modeloprocesador": "core i3",
                "numcores": 2,
                "numthreads": 4,
                "memoriaram": 8,
                "tipomemoriaprimaria": "SSD",
                "capacidadmemoriaprimaria": 512,
                "tipomemoriasecundaria": "No secondary storage",
                "capacidadmemoriasecundaria": 0,
                "marcagpu": "intel",
                "tipogpu": "integrated",
                "pantallatactil": "FALSO",
                "tamanyopantalla": 156,
                "resolucionpantalla1": 1920,
                "resolucionpantalla2": 1080,
                "OS": "windows",
                "anyosgarantia": 1
            },
            {
                "id": 2,
                "marca": "tecno",
                "modelo": "Tecno Megabook T1 Laptop (11th Gen Core i7/ 16GB/ 1TB SSD/ Win11 Home)",
                "precio": 396,
                "rating": 67,
                "marcaprocesador": "intel",
                "modeloprocesador": "core i7",
                "numcores": 4,
                "numthreads": 8,
                "memoriaram": 16,
                "tipomemoriaprimaria": "SSD",
                "capacidadmemoriaprimaria": 1024,
                "tipomemoriasecundaria": "No secondary storage",
                "capacidadmemoriasecundaria": 0,
                "marcagpu": "intel",
                "tipogpu": "integrated",
                "pantallatactil": "FALSO",
                "tamanyopantalla": 156,
                "resolucionpantalla1": 1920,
                "resolucionpantalla2": 1080,
                "OS": "windows",
                "anyosgarantia": 1
            },
            {
                "id": 3,
                "marca": "hp",
                "modelo": "HP Victus 15-fb0157AX Gaming Laptop (AMD Ryzen 5 5600H/ 8GB/ 512GB SSD/ Win11/ 4GB Graph)",
                "precio": 562,
                "rating": 73,
                "marcaprocesador": "amd",
                "modeloprocesador": "ryzen 5",
                "numcores": 6,
                "numthreads": 12,
                "memoriaram": 8,
                "tipomemoriaprimaria": "SSD",
                "capacidadmemoriaprimaria": 512,
                "tipomemoriasecundaria": "No secondary storage",
                "capacidadmemoriasecundaria": 0,
                "marcagpu": "amd",
                "tipogpu": "dedicated",
                "pantallatactil": "FALSO",
                "tamanyopantalla": 156,
                "resolucionpantalla1": 1920,
                "resolucionpantalla2": 1080,
                "OS": "windows",
                "anyosgarantia": 1
            }
        ]
    }

# Segundo test
def test_get_notebooks_max_price():
    response = client.get("/notebooks/price?max_price=120")

    assert response.status_code == 200
    assert response.json() == {
        "notebooks": [
            {
                "id": 83,
                "marca": "iball",
                "modelo": "iBall Excelance CompBook Laptop (AQC/ 2GB/ 32GB/Win10)",
                "precio": 108,
                "rating": 41,
                "marcaprocesador": "intel",
                "modeloprocesador": "other",
                "numcores": 4,
                "numthreads": 0,
                "memoriaram": 2,
                "tipomemoriaprimaria": "HDD",
                "capacidadmemoriaprimaria": 32,
                "tipomemoriasecundaria": "No secondary storage",
                "capacidadmemoriasecundaria": 0,
                "marcagpu": "intel",
                "tipogpu": "integrated",
                "pantallatactil": "FALSO",
                "tamanyopantalla": 116,
                "resolucionpantalla1": 1366,
                "resolucionpantalla2": 768,
                "OS": "windows",
                "anyosgarantia": 1
            }
        ]
    }

# Tercer test
def test_get_notebooks_os_not_found():
    response = client.get("notebooks/operating_systeam?os=ubuntuu")

    assert response.status_code == 404
    assert response.json() == {
        "error": "Input should be 'other', 'windows', 'ubuntu', 'mac' or 'dos'",
        "dato_enviado": "ubuntuu"
    }

# Tests para endopints de tipo post

# Primer test
def test_write_notebook():
    response = client.post(
        url="/notebooks",
        headers={"Content-Type": "application/json"},
        json={
            "marca": "Dell",
            "modelo": "XPS 13",
            "precio": 1500,
            "rating": 5,
            "marcaprocesador": "Intel",
            "modeloprocesador": "i7-1165G7",
            "numcores": 4,
            "numthreads": 8,
            "memoriaram": 16,
            "tipomemoriaprimaria": "SSD",
            "capacidadmemoriaprimaria": 512,
            "tipomemoriasecundaria": "Ninguna",
            "capacidadmemoriasecundaria": 0,
            "marcagpu": "Intel",
            "tipogpu": "Iris Xe",
            "pantallatactil": "Sí",
            "tamanyopantalla": 13,
            "resolucionpantalla1": 1920,
            "resolucionpantalla2": 1080,
            "OS": "windows",
            "anyosgarantia": 2
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "marca": "Dell",
        "modelo": "XPS 13",
        "precio": 1500,
        "rating": 5,
        "marcaprocesador": "Intel",
        "modeloprocesador": "i7-1165G7",
        "numcores": 4,
        "numthreads": 8,
        "memoriaram": 16,
        "tipomemoriaprimaria": "SSD",
        "capacidadmemoriaprimaria": 512,
        "tipomemoriasecundaria": "Ninguna",
        "capacidadmemoriasecundaria": 0,
        "marcagpu": "Intel",
        "tipogpu": "Iris Xe",
        "pantallatactil": "Sí",
        "tamanyopantalla": 13,
        "resolucionpantalla1": 1920,
        "resolucionpantalla2": 1080,
        "OS": "windows",
        "anyosgarantia": 2
    }

# Tests para endopints de tipo delete

# Primer test
def test_delete_notebook_bad_input():
    response = client.delete("/notebooks/-1")

    assert response.status_code == 404
    assert response.json() == {
        "error": "Input should be greater than 0",
        "dato_enviado": "-1"
    }

# Segundo test
def test_delete_notebook():
    response = client.delete("/notebooks/1")

    assert response.status_code == 200
    assert response.json() == {
        "info": "borrado notebook 1"
    }