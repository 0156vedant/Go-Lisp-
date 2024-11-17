from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Code(BaseModel):
    code: str

@app.post("/run_code")
async def run_code(code: Code):
    # Execute the C++ interpreter with Lisp code
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
