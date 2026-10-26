import pytest
from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_health_devuelve_200_y_estado_ok():
    respuesta = cliente.get("/health")

    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}


""" def test_pedido_valido_devuelve_201():
    respuesta = cliente.post(
        "/pedidos",
        json={"producto": "Teclado mecánico", "cantidad": 2},
    )

    assert respuesta.status_code == 201
    assert respuesta.json() == {
        "mensaje": "Pedido registrado correctamente.",
        "producto": "Teclado mecánico",
        "cantidad": 2,
    } """


def test_pedido_valido_recorta_espacios_del_producto():
    respuesta = cliente.post(
        "/pedidos",
        json={"producto": "  Monitor  ", "cantidad": 1},
    )

    assert respuesta.status_code == 201
    assert respuesta.json()["producto"] == "Monitor"


def test_cantidad_cero_devuelve_400():
    respuesta = cliente.post(
        "/pedidos",
        json={"producto": "Mouse", "cantidad": 0},
    )

    assert respuesta.status_code == 400
    assert respuesta.json()["detail"] == "La cantidad debe ser mayor que cero."


def test_cantidad_negativa_devuelve_400():
    respuesta = cliente.post(
        "/pedidos",
        json={"producto": "Mouse", "cantidad": -5},
    )

    assert respuesta.status_code == 400
    assert respuesta.json()["detail"] == "La cantidad debe ser mayor que cero."


def test_producto_vacio_devuelve_400():
    respuesta = cliente.post(
        "/pedidos",
        json={"producto": "   ", "cantidad": 1},
    )

    assert respuesta.status_code == 400
    assert (
        respuesta.json()["detail"]
        == "El nombre del producto no puede estar vacío."
    )


@pytest.mark.parametrize(
    "datos",
    [
        {"cantidad": 1},
        {"producto": "Teclado"},
    ],
)
def test_campo_obligatorio_ausente_devuelve_422(datos):
    respuesta = cliente.post("/pedidos", json=datos)

    assert respuesta.status_code == 422
    assert "detail" in respuesta.json()


def test_tipo_invalido_en_cantidad_devuelve_422():
    respuesta = cliente.post(
        "/pedidos",
        json={"producto": "Teclado", "cantidad": "muchas"},
    )

    assert respuesta.status_code == 422
    assert respuesta.json()["detail"][0]["loc"] == ["body", "cantidad"]
