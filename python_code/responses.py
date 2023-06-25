import json
import spacy
nlp = spacy.load('en_core_web_md')
def calculate_similarity(message, triggers):
    message_doc = nlp(message.lower())
    trigger_docs = [nlp(trigger.lower()) for trigger in triggers]
    similarities = [message_doc.similarity(trigger_doc) for trigger_doc in trigger_docs]
    return similarities



def get_response(message):
    # Load responses from JSON file
    with open('../responses.json', 'r') as file:
        response_data = json.load(file)

    # Check the response scores and find the best matching response
    best_similarity = 0
    best_response = None
    for data in response_data:
        similarities = calculate_similarity(message, data['triggers'])
        max_similarity = max(similarities)
        if max_similarity > best_similarity:
            best_similarity = max_similarity
            best_response = data['response']

        print("Question:", message)
        print("Triggers:", data['triggers'])
        print("Similarities:", similarities)
        print()

    # Define the threshold similarity score
    threshold_similarity = 0.80

    # Return the matching response or "I didn't understand what you wrote."
    if best_similarity >= threshold_similarity:
        bot_response = best_response
    else:
        bot_response = "I didn't understand what you wrote."

    print('Bot response:', bot_response)
    print(max_similarity)
    return bot_response