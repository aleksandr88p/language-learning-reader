from fastapi import FastAPI
import uvicorn

from app.config import Settings
from app.routers import health

settings = Settings()
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug)

app.include_router(health.router)



if __name__ == '__main__':
    uvicorn.run(
      'app.main:app',
      host='127.0.0.1',
      port=8000,
      reload=settings.debug, 
  )