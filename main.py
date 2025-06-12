from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': "FastApi is successfully installed Farukh"}