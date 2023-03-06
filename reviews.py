import api.openai as oa
import dal
import sentiment_analysis
import json

date = "2021-01-01"

def get_positives_and_negatives_helper(reviews, brand, prev=None):
    #print(prev)
    system_message = "You are a marketing assistant."
    system_message += "You are given a list of reviews for " + brand + \
        "and you need to find top 3 positives and negatives of its products. Ignore any competitor products which are not related to " + brand + "."
    messages = []
    messages = oa.add_system_message(system_message, messages)
    for review in reviews:
        messages = oa.add_user_message(review[2], messages)

    if prev is None:
        subsequent_message = ""
    else:
        subsequent_message = "This was the previous response: " + prev
        subsequent_message += "Integrate the previous positives and negatives into your response."
    messages = oa.add_system_message(subsequent_message, messages)

    second_system_message = "You reply with JSON messages with the following format: {{\"positives\": [\"positive1\", \"positive2\"], \"negatives\": [\"negative1\", \"negative2\"]}}."
    messages = oa.add_system_message(second_system_message, messages)

    #print(messages)
    response = oa.get_chatgpt_response(messages)
    #print(response)

    return response

def fix_final_result(result):
    system_message = "You are a json formatting assistant."
    messages = []
    messages = oa.add_system_message(system_message, messages)

    messages = oa.add_user_message(result)
    messages = oa.add_user_message("Format the above into the following JSON format: {{\"positives\": [\"positive1\", \"positive2\"], \"negatives\": [\"negative1\", \"negative2\"]}}.")

    response = oa.get_chatgpt_response(messages)
    return response

def get_positives_and_negatives(type, brand):
    reviews = dal.get_reviews_by_type_brand_and_date(type, brand, date)
    # filter out reviews that are too short
    filtered_reviews = []
    for review in reviews:
        if len(review) < 3:
            continue
        if len(review[2]) > 20:
            filtered_reviews.append(review)
    reviews = filtered_reviews

    # split the reviews array into arrays with up to 1500 characters of reviews
    # this is because the OpenAI API has a limit of 1500 characters per request
    reviews_split = []
    curr_split = []
    curr_split_length = 0
    for review in reviews:
        if curr_split_length + len(review[2]) > 1000:
            reviews_split.append(curr_split)
            curr_split = []
            curr_split_length = 0
        curr_split.append(review)
        curr_split_length += len(review[2])
    reviews_split.append(curr_split)

    # get the initial positives and negatives
    print("Doing initial positives and negatives for " + brand + " " + type)
    positives_and_negatives = get_positives_and_negatives_helper(reviews_split[0], brand)

    # get the subsequent positives and negatives
    for i in range(1, len(reviews_split)):
        print("Doing subsequent positives and negatives for " + brand + " " + type + " " + str(i) + "/" + str(len(reviews_split)))
        positives_and_negatives = get_positives_and_negatives_helper(reviews_split[i], brand, positives_and_negatives)

    try:
        json_response = json.loads(positives_and_negatives)
    except:
        print("Error parsing JSON, trying to fix it")
        print(positives_and_negatives)
        positives_and_negatives = fix_final_result(positives_and_negatives)
        print("Fixed JSON: " + positives_and_negatives)
        json_response = json.loads(positives_and_negatives)

    print(json_response)
    return json_response

def get_sentiment(brand):
    reviews = dal.get_reviews_by_brand_and_date(brand, date)
    # filter out reviews that are too short
    reviews = [review[2] for review in reviews if len(review[2]) > 20]

    sentiment = sentiment_analysis.get_aggregated_sentiment(reviews)

    return sentiment
