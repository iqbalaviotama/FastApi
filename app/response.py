from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from datetime import datetime


def response(code, message, value):
    if code == 0:
        code = 200
    return JSONResponse({
        "datetime": str(datetime.now()),
        "statusCode": code,
        "statusMessage": message,
        "value": jsonable_encoder(value)
    },
        code)
