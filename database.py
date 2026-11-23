from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Формат: postgresql://пользователь:пароль@хост:порт/имя_базы
SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/shop_db"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Функция для получения сессии БД в эндпоинтах
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
