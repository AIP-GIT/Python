import uvicorn
import time
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return "Hello Amit"

@app.get("/items/{item_id}")
def read_item(item,q=None):
    return {"item_id" : item, "q":q}

@app.get("/items/sync/")
def read_item():
    count = 0
    for i in range(30):
        time.sleep(1)
        count += 1
    return count

@app.get("/items/async/")
async def read_item():
    count = 0
    for i in range(30):
        time.sleep(1)
        count += 1
    return count


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8123)


# From CLI
# uvicorn main:app --reload