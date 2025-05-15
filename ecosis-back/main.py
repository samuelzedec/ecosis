from fastapi import FastAPI

app = FastAPI()

@app.get("/doacao")
def doacao():
    return {"Hello": "World"}