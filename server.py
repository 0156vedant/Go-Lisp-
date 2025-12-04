from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://0156vedant.github.io"],  # Allow specific frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Code(BaseModel):
    code: str

@app.post("/run_code")
async def run_code(code: Code):
    process = subprocess.Popen(
        ['./wisp_interpreter'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=code.code)

    if process.returncode != 0:
        raise HTTPException(status_code=400, detail=stderr)
    return {"output": stdout}



