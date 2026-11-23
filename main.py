from database import engine, get_db
from fastapi import Depends, FastAPI
import models
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Автоматически создаем таблицы в PostgreSQL при запуске приложения
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Pydantic-схема для входящих данных (валидация)
class ItemCreate(BaseModel):
  name: str
  price: float


# Pydantic-схема для ответа (включает id из базы)
class ItemResponse(ItemCreate):
  id: int

  class Config:
    from_attributes = True


# GET-запрос: получить список всех товаров из БД
@app.get("/items")
def get_items(db: Session = Depends(get_db)):
  items = db.query(models.ItemDB).all()
  return {"items": items}


# POST-запрос: добавить новый товар в БД
@app.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
  # Создаем объект модели БД
  db_item = models.ItemDB(name=item.name, price=item.price)
  db.add(db_item)  # Добавляем в сессию
  db.commit()  # Сохраняем в базу
  db.refresh(db_item)  # Обновляем объект, чтобы получить присвоенный id
  return {"message": "Товар добавлен", "item": db_item}
