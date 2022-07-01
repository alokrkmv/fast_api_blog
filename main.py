from fastapi import FastAPI

from typing import Optional
app = FastAPI()

@app.get("/blog")
def index(limit: int=10,published:bool = True,sort: Optional[str]=None):
    if published:
        return {"data":f"{str(limit)} published blogs fetched from db"}
    else:
        return {"data": f"{str(limit)} blogs from database"}

@app.get("/about")
def about():
    return {"data":"about page"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"unpublished blogs"}

@app.get("/blog/{id}")
def fetch_id(id : int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def comments(id :int):
    return {"data":["1","2"]}

