from fastapi import FastAPI, File
from fastapi import APIRouter, Depends
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import Annotated
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
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


@secure_router.post("/classifyImage")
async def classifyImage(file_contents: Annotated[bytes, File()]):
    image = Image.open(io.BytesIO(file_contents))

    processor = AutoImageProcessor.from_pretrained("google/efficientnet-b7")
    model = AutoModelForImageClassification.from_pretrained("google/efficientnet-b7")
    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits
    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    return model.config.id2label[predicted_label]


app.include_router(
    secure_router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)
# async def classifyImage(file: UploadFile = File()):
#     try:
#         contents = await file.read()
#
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         await file.close()
#
#     return {"message": f"Successfuly uploaded {file.filename}"}
