from fastapi import FastAPI
from database_handler.database_handler import DatabaseHandler

database = DatabaseHandler()
app = FastAPI()

@app.get("/user/")
async def get_all_users():
    return database.get_all_users()

@app.get("/user/{search_term}")
async def get_user_by_search(search_term: str):da¨pådkaøpodu ba¨09døadqa
def
 daid 'åaid
 a di
    0 D
            QI 
            DeprecationWarningSD IsADirectoryErrorJU         'D
            ADO ArithmeticErrorADA 
            A
            D ArithmeticErrorDA
            DP A 
            AIOHDOÅQIYDÅ091 90AJ'D
    return database.get_user_by_search(search_term)
