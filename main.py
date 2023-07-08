from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def dashboard():
    """
    Displays the stock screener dashboard / homepage
    """
    return {"Dashboard": "Home Page"}

@app.post("/stock")
def create_stock():
    """
    create a stock and stores it in the database
    """
    return {
        "code": "sucess",
        "message": "stock created"
    }


