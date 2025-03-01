# Ici on va installer un serveur
# https://python-socketio.readthedocs.io/en/stable/server.html#creating-a-server-instance

import socketio
from fastapi import FastAPI
import uvicorn

from core_archi_websocket_kube_conceplog.constants import WEB_SOCKET_MESSAGE_CANAL
from core_archi_websocket_kube_conceplog.reponse import Reponse

sio = socketio.AsyncServer(cors_allowed_origins="*",async_mode='asgi')
# Uvicorn est un serveur asgi donc il faut veiller a bien mettre un async server
app = FastAPI()
app.mount("/", socketio.ASGIApp(sio))

utilisateurs = []

@sio.event
async def connection_utilisateur(sid):
       print(f"Client connecté : {sid}")
       utilisateurs.add(sid)
@sio.event
async def deconnection_utilisateur(sid):
      print(f"Client déconnecté : {sid}")
      utilisateurs.discard(sid)
@sio.on(WEB_SOCKET_MESSAGE_CANAL,namespace="/")
def handle_message(sid, data):
      print(f"📩 Message reçu de {sid} : {data}")
          # Ensure data is a dictionary
      if isinstance(data, str):  
        import json
        try:
            data = json.loads(data)  # Convert JSON string to dictionary
        except json.JSONDecodeError as e:
            print(f"❌ Erreur de parsing JSON: {e}")
            return  # Stop execution if data is not valid JSON

      if not isinstance(data, dict):  
        print(f"❌ Mauvais format de données reçu: {data}")
        return  
      msg = Reponse(**data)
      
      sio.emit("message", f"🔁 Message reçu: {msg}")  # Réponse à tous les clients


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

