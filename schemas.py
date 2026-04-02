from pydantic import BaseModel

class CategoryBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    id: int
    name: str
    category: CategoryBase

    class Config:
        orm_mode = True
