from dataclasses import dataclass

from fastapi import FastAPI, File, Request
from fastapi import APIRouter, Depends
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import Annotated
import io

app = FastAPI()
public_router = APIRouter()

api_key_header = APIKeyHeader(name="X-API-Key")


def get_user(api_key_header: str = Security(api_key_header)):
    if api_key_header == "hasankey":
        user = "hasan"
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid API key"
    )

@public_router.get("/")
async def get_testroute():
    return "OK"

app.include_router(
    public_router,
    prefix="/api/v1/public"
)

secure_router = APIRouter()

@secure_router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return user

@app.get("/")
async def root():
    return {"message": "Hello World"}


class ModelTemplateRepository:
    def __init__(self):
        self.next_id = 0
        self.model_templates = {}
    def add_model(self, param):
        self.next_id += 1
        self.model_templates[self.next_id] = param
        return self.next_id

    def get_by_id(self, template_id):
        return self.model_templates[template_id]
        pass


model_template_repository = ModelTemplateRepository()

@dataclass
class ModelTemplate:
    name: str
    location: str
    docker_image: str

@app.put("/model_template")
async def put_model_template(request: Request):
    model_template = ModelTemplate(**await request.json())
    model_id = model_template_repository.add_model(model_template)
    return {"id": model_id}


@app.get("/model_template/{template_id}")
async def get_model_template(template_id: int):
    return model_template_repository.get_by_id(template_id)

@app.get("/models/{model_id}")
async def get_model(model_id: str):
    raise HTTPException(status_code=404, detail="model not found")


@app.put("/models/{model_id}")
async def put_model(model_id: str):
    return {"detail": "model added"}


@secure_router.post("/classifyImage")
async def classifyImage(file_contents: Annotated[bytes, File()]):
    return "I don't want to classify"

app.include_router(
    secure_router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)
