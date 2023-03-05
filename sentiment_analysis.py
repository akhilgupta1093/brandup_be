from monkeylearn import MonkeyLearn

ml = MonkeyLearn('5f13e298f35ffb39764bdb5618655b319e10c28c')
model_id = 'cl_pi3C7JiL'

def get_aggregated_sentiment(text_list):
    result = ml.classifiers.classify(model_id, text_list)

    classifications = [val['classifications'][0] for val in result.body]

    aggregated = {}
    for classification in classifications:
        tag_name = classification['tag_name']
        confidence = float(classification['confidence'])
        if tag_name in aggregated:
            aggregated[tag_name]['count'] += 1
            aggregated[tag_name]['confidence'] += confidence
        else:
            aggregated[tag_name] = {
                'count': 0,
                'confidence': confidence
            }

    for tag_name in aggregated:
        aggregated[tag_name]['confidence'] /= aggregated[tag_name]['count']

    return aggregated
