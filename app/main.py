from fastapi import FastAPI
import uvicorn

app = FastAPI()


data_base_json = {
    '1': 'Gui',
    '2': 'Victor',
    '3': 'Petrobras'
}

@app.get('/')
def home():
    return data_base_json


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080)