from typing import Dict, Optional, Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{items_id}")
def read_item(item_id: int,
              q: Optional[str] = None) -> Dict[str, Union[int, str, None]]:
    return {"item_id": item_id, "q": q}
