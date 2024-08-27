from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def _main():
    return 'Hello World!'