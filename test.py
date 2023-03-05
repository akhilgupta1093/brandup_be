import dal
import json
import reviews
import openai
import os
from dotenv import load_dotenv, find_dotenv

openai.api_key = ""

def read_and_save_json():
    # list all json files in data folder
    company_dirs = os.listdir("data")
    # read each file and add it to a list
    data = []
    for company in company_dirs:
        for data in os.listdir("data/{}".format(company)):
            with open("data/{}".format(data), "r") as f:
                json_data = json.load(f)
                data.extend(json.load(f))

    # save it to reviews.db
    for d in data:
        if "review" not in d or "url" not in d:
            continue

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
    print(reviews.get_positives_and_negatives("youtube"))

if __name__ == "__main__":
    main()
