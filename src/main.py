from model_controller import build_model_controller
from model_server import ModelServer

app = build_model_controller(ModelServer())