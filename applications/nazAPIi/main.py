from fastapi import FastAPI
from database_handler.database_handler import DatabaseHandler
import os

os.listdir

database = DatabaseHandler()
app = FastAPI()



@app.get("/user/")
async def get_all_users():
    return database.get_all_users()

@app.get("/user/{search_term}")
async def get_user_by_search(search_term: str):
    return database.get_user_by_search(search_term)