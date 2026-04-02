from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi import HTTPException

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/categories")
def create_category(category: schemas.CategoryBase, db: Session = Depends(get_db)):
    return crud.create_category(db, category.name)

@app.post("/products")
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    return crud.create_product(db, product.name, product.category_id)


@app.get("/categories")
def get_categories(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * limit
    categories = db.query(models.Category).offset(skip).limit(limit).all()
    return categories
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")


@app.get("/products")
def get_products(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * limit
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products


@app.get("/products/{id}", response_model=schemas.ProductBase)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

@app.put("/products/{id}")
def update_product(id: int, product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    db_product.name = product.name
    db_product.category_id = product.category_id
    db.commit()
    return db_product

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    db.delete(product)
    db.commit()
    return {"message": "Deleted"}

