
import sqlalchemy as sa

from typing import List
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from core import deps, security
from models import home_model, user_model
from core.auth import autenticar, criar_token_acesso
from schemas import cliente_schema, base_schema, usuario_schema
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi import WebSocket, WebSocketDisconnect, FastAPI, APIRouter, status, Depends, HTTPException, Response

from celery import Celery


# Bypass warning SQLmodel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True # type: ignore
Select.inherit_cache = True # type: ignore
# Fim Bypass

router = APIRouter()

# POST Login
@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(deps.get_session_sistemas)):
    usuario = await autenticar(cliente_id=form_data.username, senha=form_data.password, db=db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Dados de acesso incorretos.')

    return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)

#GET test User
@router.get('/user/{cliente_id}', response_model=usuario_schema.AuthUserSchema, status_code=status.HTTP_200_OK)
async def get_user(cliente_id: int, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_sistemas)):
    async with db as session:
        query = select(user_model.AuthUser).filter(user_model.AuthUser.is_active == 1, user_model.AuthUser.id == current_user.id)
        result = await session.execute(query)
        user: List[user_model.AuthUser] = result.scalar_one_or_none()
        print('acessoLiberado')        
        return user    


#GET only CLients
@router.get('/only_clients/{cliente_id}', response_model=List[cliente_schema.OnlyClienteSchema])
async def get_only_clients(current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        query = select(home_model.TbClientes).filter(home_model.TbClientes.ativo == 1)        
        result = await session.execute(query)
        clientes: List[home_model.TbClientes] = result.scalars().unique().all()
        return clientes    

# GET Clientes
@router.get('/', response_model=List[cliente_schema.ClienteSchema])
async def get_clientes(db: AsyncSession = Depends(deps.get_session_gerencial)):
    
    async with db as session:
        query = select(home_model.TbClientes)
        result = await session.execute(query)
        clientes: List[home_model.TbClientes] = result.scalars().unique().all()

        return clientes

# GET DwIcmsIpiEntradas
@router.get('/dw/', response_model=List[base_schema.DwIcmsIpiEntradasSchema])
async def get_DwIcmsIpiEntradas(db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        query = '''
        SELECT
            ID_ITEM, CHV_PK, DATA_INI
        FROM
            DB_00820120.dw_icms_ipi_entradas
        WHERE
            DB_00820120.dw_icms_ipi_entradas.ID_ITEM IS NOT NULL
        '''
        result = await session.execute(sa.text(query))
        clientes = result.fetchall()
        
        return clientes


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/api/v1/clientes/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@router.get("/html/")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)


# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}


# GET Cliente
# @router.get('/{cliente_id}', response_model=TbClientes, status_code=status.HTTP_200_OK)
# async def get_cliente(cliente_id: int, db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         query = select(TbClientes).filter(TbClientes.id_cliente == cliente_id)
#         result = await session.execute(query)
#         cliente = TbClientes = result.scalar_one_or_none()

#         if cliente:
#             return cliente
#         else:
#             raise HTTPException(detail='Cliente não encontrado', status_code=status.HTTP_404_NOT_FOUND)
