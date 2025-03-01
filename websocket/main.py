import socketio
from fastapi import FastAPI
import uvicorn

# Création du serveur Socket.IO en mode ASGI (compatible FastAPI)
sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")

# Création de l'application FastAPI
app = FastAPI()

# Montage de Socket.IO sur FastAPI
app.mount("/", socketio.ASGIApp(sio, other_asgi_app=app))

# Stockage des clients connectés
utilisateurs = set()

# Gestion de la connexion des clients
@sio.event
async def connect(sid, environ):
    print(f"✅ Client connecté : {sid}")
    utilisateurs.add(sid)

# Gestion de la déconnexion des clients
@sio.event
async def disconnect(sid):
    print(f"❌ Client déconnecté : {sid}")
    utilisateurs.discard(sid)

# Gestion des messages reçus
@sio.on("message")
async def handle_message(sid, data):
    print(f"📩 Message reçu de {sid} : {data}")
    
    # Diffuser le message à tous les clients connectés
    await sio.emit("message", f"🔁 {sid} a dit : {data}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)