from fastapi import FastAPI
app = FastAPI()



# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Hello world!@!!!"}
