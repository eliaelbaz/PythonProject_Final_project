from fastapi import FastAPI
import user_router
import ml_router

app = FastAPI(title="ML Model Server - Simple Version")

app.include_router(user_router.router)

app.include_router(ml_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to the ML API Server"}