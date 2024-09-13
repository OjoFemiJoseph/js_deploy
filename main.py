from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
import os

app = FastAPI()

@app.get('/')
def index():
    return "Hello World"