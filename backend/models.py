from pydantic import BaseModel,Field
# from typing import Optional

class Expense(BaseModel):
    merchant:str
    amount:float = Field(gt=0)
    date:str
    category:str

class ExpenseResponse(BaseModel):
    merchant:str
    amount:float 
    date:str
    category:str