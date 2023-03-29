import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import FastAPI
from app.api.api_v1.routes import api_router

app = FastAPI(title="", openapi_url="")
app.include_router(api_router, prefix="/api/v1", tags=["root"])
