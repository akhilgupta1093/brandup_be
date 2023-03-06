import dal
import json
import reviews
import openai
import os

openai.api_key = "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"

def read_and_save_json():
    # list all json files in data folder
    company_dirs = os.listdir("data")
    # read each file and add it to a list
    data = []
    for company in company_dirs:
        for datafile in os.listdir("data/{}".format(company)):
            with open("data/{}/{}".format(company, datafile), "r") as f:
                json_data = json.load(f)
                for d in json_data:
                    d['brand'] = company
                    data.append(d)

    # save it to reviews.db
    for d in data:
        if "review" not in d or "url" not in d:
            continue

        review = d['review']
        url = d['url']
        date = "2021-01-01"
        extra = json.dumps(d)
        tp = url.split("/")[2].split(".")[1]
        brand = d['brand']
        dal.add_review(tp, url, review, extra, date, brand)


def main():
    #dal.create_reviews_table()
    #read_and_save_json()
    pass
    #print(reviews.get_positives_and_negatives("youtube", "caraway"))
    #print(reviews.get_sentiment("caraway"))

if __name__ == "__main__":
    main()
