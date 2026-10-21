from pydantic import BaseModel, Field


class PedidoRequest(BaseModel):
    producto: str = Field(description="Nombre del producto solicitado")
    cantidad: int = Field(description="Cantidad de unidades del producto")


class PedidoResponse(BaseModel):
    mensaje: str
    producto: str
    cantidad: int


class HealthResponse(BaseModel):
    status: str
