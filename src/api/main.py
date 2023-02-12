# from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from src.api.routers import (sample)
# from api.routers import (app,certificates, changes, consumptions, countries,
#                          hydrogens, orders, origins, owners, places, tanks,
#                          traces)

# load_dotenv(".env")
app = FastAPI(title='UI Service Backend',
              description='ROBOCROSS/バックエンド',
              docs_url='/api/docs',
              redoc_url='/api/redoc',
              openapi_url='/api/openapi.json',
              version='1.0.0')

# Azure Static Web Apps がAPIとして認識するためには、/apiをprefixにする必要がある
app.include_router(sample.router, prefix='/api/v1')

if __name__ == "__main__":
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True, workers=1)
