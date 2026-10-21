# MiniAPI de Pedidos

Proyecto didáctico para la materia **Fundamentos de Arquitectura de Software y Desarrollo Backend**. La aplicación expone una API pequeña construida con **Python, FastAPI y Pydantic**, y cuenta con pruebas automatizadas con **pytest** y **httpx**.

> **Nota:** esta versión es didáctica y **no utiliza base de datos**. Los pedidos solo se validan y se devuelven en la respuesta; no se almacenan en ningún lado.

## Objetivo

Demostrar, con una aplicación mínima y comprensible, cómo se estructura una API con FastAPI y cómo se validan sus reglas de negocio mediante pruebas automatizadas. Más adelante, estas mismas pruebas se ejecutarán con GitHub Actions.

## Funcionalidad

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/health` | Comprueba que la API responde. Devuelve `{"status": "ok"}`. |
| `POST` | `/pedidos` | Registra un pedido válido y devuelve HTTP 201. |

### Reglas de negocio

- El nombre del producto no puede estar vacío (HTTP 400).
- La cantidad debe ser un número entero mayor que cero (HTTP 400).
- Si la estructura del JSON es incorrecta o los tipos no coinciden, FastAPI responde HTTP 422.

### Ejemplo de solicitud válida

```json
{
  "producto": "Teclado mecánico",
  "cantidad": 2
}
```

Respuesta (`201 Created`):

```json
{
  "mensaje": "Pedido registrado correctamente.",
  "producto": "Teclado mecánico",
  "cantidad": 2
}
```

## Requisitos

- Python 3.12 o superior.
- Windows, Linux o macOS con capacidad para crear entornos virtuales.

Las versiones de las dependencias directas están fijadas en `requirements.txt`.

## Crear el entorno virtual e instalar dependencias

Desde la raíz del repositorio, en **Windows CMD**:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Iniciar la API localmente

Con el entorno virtual activado:

```cmd
uvicorn app.main:app --reload
```

La documentación interactiva queda disponible en:

- <http://127.0.0.1:8000/docs>
- <http://127.0.0.1:8000/redoc>

Para detener el servidor, presiona `Ctrl+C`.

## Ejecutar las pruebas

Con el entorno virtual activado, desde la raíz del repositorio:

```cmd
python -m pytest -v
```

Las pruebas cubren el endpoint de salud, un pedido válido, cantidades cero y negativas, producto vacío, campos obligatorios ausentes y tipos inválidos.

## Estructura del proyecto

```text
.
├── app/
│   ├── __init__.py
│   ├── main.py        # Endpoints de la API
│   └── models.py      # Esquemas Pydantic
├── tests/
│   ├── __init__.py
│   └── test_pedidos.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Material del equipo

El borrador de la exposición se conserva en el archivo `Equipo-GitHub _Actions_borrador.pdf`.
