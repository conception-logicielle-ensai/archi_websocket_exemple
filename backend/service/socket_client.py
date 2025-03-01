from core_archi_websocket_kube_conceplog.constants import WEB_SOCKET_MESSAGE_CANAL, WEB_SOCKET_URL_KEY
import socketio
import logging

from core_archi_websocket_kube_conceplog.reponse import Reponse
class SocketClient:
    def __init__(self, url):
        self.url = url
        self.sio = socketio.Client()
        @self.sio.event
        def connect():
            logging.debug("Appli connectée au websocket server")

        @self.sio.event
        def disconnect():
            logging.debug("Appli déconnectée du websocket server")

        @self.sio.on(WEB_SOCKET_MESSAGE_CANAL)
        def on_message(data):
            logging.debug(f"Message reçu du websocket : {data}")

    # Pour rendre l'instance "ressource" et éviter des fuites de connexion
    def __enter__(self):
        self.sio.connect(self.url)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sio.disconnect()

    def broadcast_message(self, message: str):
        logging.debug(f"Broadcast d'un message {message} ")
        self.sio.emit(WEB_SOCKET_MESSAGE_CANAL, message)
    
    def broadcast_reponse(self, reponse: Reponse):
        logging.debug(f"Broadcast d'un message reponse {reponse} ")
        self.sio.emit(WEB_SOCKET_MESSAGE_CANAL, reponse.model_dump_json())


    @classmethod
    def from_env(cls):
        """
        Factory method, si vous vous rappelez bien.
        """
        import os
        websocket_url = os.getenv(WEB_SOCKET_URL_KEY)
        logging.info(f"Création du socket client : {websocket_url}")
        return cls(url=websocket_url)