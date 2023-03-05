import dal
import json
import reviews
import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_and_save_json():
    # read data.json and process it
    with open("data.json", "r") as f:
        data = json.load(f)
    # save it to reviews.db
    for d in data:
        review = d['review']
        url = d['url']
        date = "2021-01-01"
        extra = json.dumps(d)
        tp = url.split("/")[2].split(".")[1]
        dal.add_review(tp, url, review, extra, date)


def main():
    #dal.create_reviews_table()
    #read_and_save_json()
    pass
    #print(dal.get_reviews_by_type_and_date("amazon", "2021-01-01"))
    print(reviews.get_positives_and_negatives("amazon"))

if __name__ == "__main__":
    main()
