import os
import subprocess
import tempfile

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

CODE_EXECUTION_TIMEOUT = 5


class CodeRequest(BaseModel):
    code: str


@app.post("/execute")
def execute_code(request: CodeRequest):
    try:
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
            f.write(request.code.encode('utf-8'))
            tmp_file_path = f.name

        result = subprocess.run(
            ["python", tmp_file_path],
            capture_output=True,
            timeout=CODE_EXECUTION_TIMEOUT,
            check=False,
            encoding="utf-8"
        )

        os.remove(tmp_file_path)

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Code timeout")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
