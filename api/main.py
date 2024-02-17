import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.blog import app as blog
from decouple import config, Csv

app = FastAPI()

Origins = config("HNG_API_ORIGINS", default="['localhost:3000', 'http://localhost:3000']", cast=Csv())
print(Origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=Origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog, tags=["Blogs"])


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to HNG"}


if __name__ == "__main__":
    Host = config("HNG_API_HOST", default='localhost')
    Port = config("HNG_API_PORT", default=8000, cast=int)
    uvicorn.run("main:app", host=Host, port=Port, reload=True)
