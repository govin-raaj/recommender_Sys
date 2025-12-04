from fastapi import FastAPI
from app.backend.llm import recommend_gadget
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI(title="Gadget Recommender API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recommend")
async def recommend_item(item:str):
    
    response = recommend_gadget(item)
    return {"recommendations": response}


handler = Mangum(app)
