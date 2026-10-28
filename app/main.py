from fastapi import FastAPI, HTTPException, status

from app.models import HealthResponse, PedidoRequest, PedidoResponse

app = FastAPI(
    title="MiniAPI de Pedidos",
    description="API didáctica para validar pedidos. No utiliza base de datos.",
    version="1.0.0",
)


@app.get("/health", response_model=HealthResponse, tags=["Sistema"])
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post(
    "/pedidos",
    response_model=PedidoResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Pedidos"],
)
def crear_pedido(pedido: PedidoRequest) -> PedidoResponse:
    producto = pedido.producto.strip()

    if not producto:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre del producto no puede estar vacío.",
        )

    if pedido.cantidad < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La cantidad debe ser mayor que cero.",
        )

    return PedidoResponse(
        mensaje="Pedido registrado correctamente.",
        producto=producto,
        cantidad=pedido.cantidad,
    )
