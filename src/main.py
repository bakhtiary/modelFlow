from dataclasses import dataclass

from fastapi import FastAPI

from model_server import ModelServer


def buildModelController(modelServer: ModelServer):
    app = FastAPI()
    
    @app.get("/")
    async def root(self ):
        return {"message": "Hello World"}

    @app.post("/models/{model_id}/invoke")
    async def get_model(model_id: str):
        return await modelServer.invoke(model_id)

    return app

app = buildModelController(ModelServer())