from sqlalchemy import text
from app.database import SessionLocal

with SessionLocal() as db:
    result = db.execute(text("SELECT 1"))
    print(result.scalar_one())


