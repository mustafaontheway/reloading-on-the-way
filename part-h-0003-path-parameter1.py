from fastapi import FastAPI

app = FastAPI()

fake_inventory_data = [
     {"id": 5, "name": "TV", "quantity": 14, "per_price": 16_000},
     {"id": 9, "name": "laptop", "quantity": 6, "per_price": 33_500},
     {"id": 16, "name": "mobile phone", "quantity": 17, "per_price": 9_500},
]

@app.get("/first-endpoint")
async def first_func():
     return {"First Message": "Hello AI Worldsss!"}

@app.get("/inventory/{item_id}")
async def get_inventory_item(item_id: int):
     for item in fake_inventory_data:
          if item["id"] == item_id:
               return {"item": item}
     return {"error": "Item not found!"}

# fastapi dev
