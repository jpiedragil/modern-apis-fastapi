from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "z cannot be zero"},
            status_code=400)

    value = (x + y)

    if z is not None:
        value /= z

    return {
        "x": x,
        "y": y,
        "z": z,
        "value": value
    }


uvicorn.run(api, port=8000, host="127.0.0.1")
