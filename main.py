import openai
import os
import reviews

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = ""

app = FastAPI()
origins = [
    "*",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/reviews/{type}/{brand}")
def get_reviews(type: str, brand: str):
    return reviews.get_positives_and_negatives(type, brand)

# sentiment analysis for a brand


@app.get("/sentiment/{brand}")
def get_sentiment(brand: str):
    return reviews.get_sentiment(brand)
