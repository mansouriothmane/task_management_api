from fastapi import FastAPI
from app.routers import task, user, auth

app = FastAPI()

app.include_router(task.router)
app.include_router(user.router)
app.include_router(auth.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
