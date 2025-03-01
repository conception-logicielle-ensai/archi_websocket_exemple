from fastapi import FastAPI
from core_archi_websocket_kube_conceplog.constants import LOG_LEVEL_ENV_KEY
from router import router
from dotenv import load_dotenv
import os
import uvicorn
root_path = os.getenv("API_ROOT_PATH", "/") 
app = FastAPI(root_path=root_path)
app.include_router(router)

def configure_logger():
   import logging
   LOG_LEVEL = os.getenv(LOG_LEVEL_ENV_KEY, "info").upper()
   if LOG_LEVEL not in ["INFO","DEBUG"]:
      raise Exception(f"Veuillez paramétrer le logger pour pouvoir démarrer l'application via {LOG_LEVEL_ENV_KEY}")
   LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
   logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

def run_server():
    if os.getenv(LOG_LEVEL_ENV_KEY).lower() == "debug":
      uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
    else:
       uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    load_dotenv()
    configure_logger()
    run_server()