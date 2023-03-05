import openai
import os
from dotenv import load_dotenv, find_dotenv
import reviews

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = "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"

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

@app.get("/reviews/{type}")
def get_reviews(type: str):
    return reviews.get_positives_and_negatives(type)