from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import Settings

settings = Settings()

engine = create_engine(url=settings.db_url)




SessionLocal = sessionmaker(bind=engine)
