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

def get_env_vars():
    import os
    
    from core_archi_websocket_kube_conceplog.constants import WEB_SOCKET_URL_KEY
    
    from core_archi_websocket_kube_conceplog.constants import LOG_LEVEL_ENV_KEY
    websocket_url = os.getenv(WEB_SOCKET_URL_KEY)
    log_level = os.getenv(LOG_LEVEL_ENV_KEY, "info").upper()
    return websocket_url,log_level
@router.get("/config")
async def queue():
    websocket_url, log_level = get_env_vars()

    return {"web_socket_url":websocket_url,"loglevel":log_level} 

