from pydantic import BaseModel

class CategoryBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    category_id: int
    
class ProductBase(BaseModel):
    id: int
    name: str
    category: CategoryBase

    class Config:
        orm_mode = True
