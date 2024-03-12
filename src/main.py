import asyncio
import datetime as dt
from typing import Annotated

import uvicorn
from fastapi import Body
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Path
from fastapi import Query
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI Params"}


class Period(BaseModel):
    start: dt.datetime
    end: dt.datetime

    def __str__(self):
        return f"{self.start} - {self.end}"


class Sleep(BaseModel):
    number: Annotated[int, Query(title="Number query", gt=0, le=10)]
    micro: Annotated[bool, Query(title="Micro query")] = False


@app.get("/params/{name}")
async def test_name(
    name: Annotated[str, Path(..., title="Name path")],
    period: Annotated[Period, Body(..., title="Period body", embed=True)],
    sleep: Sleep = Depends(),  # noqa: B008
):
    print(
        f"GET on /params endpoint with Path parameter name={name}, "
        f"Query parameter sleep={sleep}, and Body parameter period={period}"
    )

    number = sleep.number / 10 if sleep.micro else sleep.number
    await asyncio.sleep(number)

    return {name: period}


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
