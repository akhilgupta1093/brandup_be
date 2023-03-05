import api.openai as oa
import dal

date = "2021-01-01"

def get_positives_and_negatives(type, brand):
    reviews = dal.get_reviews_by_type_brand_and_date(type, brand, date)
    # filter out reviews that are too short
    reviews = [review for review in reviews if len(review[2]) > 20]

    system_message = "You are a marketing assistant."
    system_message += "You are given a list of reviews for" + brand + "and you need to find the positives and negatives of its products."
    system_message += "You reply with JSON messages with the following format: {{\"positives\": [\"positive1\", \"positive2\"], \"negatives\": [\"negative1\", \"negative2\"]}}."
    messages = oa.add_system_message(system_message)
    for review in reviews:
        messages = oa.add_user_message(review[2], messages)
    
    messages = oa.add_user_message("Please tell me the positives and negatives of the products. You reply with JSON messages with the following format: {\"positives\": [\"positive1\", \"positive2\"], \"negatives\": [\"negative1\", \"negative2\"]}.", messages)
    
    response = oa.get_chatgpt_response(messages)
    return response