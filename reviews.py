import api.openai as oa
import dal

date = "2021-01-01"

def get_positives_and_negatives(type):
    reviews = dal.get_reviews_by_type_and_date(type, date)

    messages = oa.add_system_message("You are a marketing assistant. You are given a list of reviews and you need to find the positives and negatives of the product. You reply with JSON messages with the following format: {\"positives\": [\"positive1\", \"positive2\"], \"negatives\": [\"negative1\", \"negative2\"]}.")
    for review in reviews:
        messages = oa.add_user_message(review[2], messages)
    
    messages = oa.add_user_message("Please tell me the positives and negatives of the product. You reply with JSON messages with the following format: {\"positives\": [\"positive1\", \"positive2\"], \"negatives\": [\"negative1\", \"negative2\"]}.", messages)
    
    response = oa.get_chatgpt_response(messages)
    return response