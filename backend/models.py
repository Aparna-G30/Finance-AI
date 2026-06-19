from pydantic import BaseModel

class Expense(BaseModel):
    merchant:str
    amount:float
    date:str
    category:str

class ExpenseResponse(BaseModel):
    merchant:str
    amount:float
    date:str
    category:str