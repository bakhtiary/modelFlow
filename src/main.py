from fastapi import FastAPI, File
from fastapi import APIRouter, Depends
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import Annotated

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
async def classifyImage(file: Annotated[bytes, File()]):

    return {"cat"}


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
