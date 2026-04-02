from sqlalchemy.orm import Session
import models

def create_category(db: Session, name: str):
    category = models.Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def create_product(db: Session, name: str, category_id: int):
    product = models.Product(name=name, category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product