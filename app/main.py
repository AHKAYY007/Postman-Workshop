from fastapi import FastAPI
from app.db.database import create_database
from app.routers import books

create_database()

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)

app.include_router(books.router)


@app.get('/')
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)