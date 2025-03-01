from fastapi import APIRouter

from service.socket_client import SocketClient
from core_archi_websocket_kube_conceplog.reponse import Reponse


router = APIRouter()

# equivalent d'un router dans un autre module
@router.post("/broadcast")
async def broadcast(reponse:Reponse):
    with SocketClient.from_env() as socket_client_service:
        socket_client_service.broadcast_reponse(reponse=reponse) 
    return {"message": f"Message {str(reponse)} transmis"}

@router.get("/queue")
async def queue():
    return {"message":"Hello world"} 

