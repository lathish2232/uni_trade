from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def health_check():
    return {"message": "Hello World"}

if __name__ == '__main__':
    #uvicorn.run(app, port=8080, host='127.0.0.1')
    uvicorn.run(app, port=8080, host='0.0.0.0')

# To run server use this bellow cmd (use any one )

# -$> python -m uvicorn main:app --reload
# -$> uvicorn main:app --reload