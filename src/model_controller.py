from fastapi import FastAPI

from model_server import ModelServer


def build_model_controller(modelServer: ModelServer):
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.post("/models/{model_id}/invoke")
    async def get_model(model_id: str):
        return await modelServer.invoke(model_id)

    return app
