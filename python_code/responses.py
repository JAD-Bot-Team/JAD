import json
import difflib

# Load the trigger-response data from responses.json
def load_responses():
    with open("../responses.json", "r") as file:
        data = json.load(file)
    return data

# Get the best matching response based on user input
def get_response(user_input):
    data = load_responses()
    best_ratio = 0
    best_response = ""
    
    for item in data:
        triggers = item["triggers"]
        for trigger in triggers:
            ratio = difflib.SequenceMatcher(None, user_input, trigger).ratio()
            if ratio > best_ratio :
                best_ratio = ratio
                best_response = item["response"]

    if (best_ratio >= 0.66):
        print(best_ratio)
        return best_response
    else :
        return "I didn't understand can you re-phrase what you said"

# Example usage
# response = get_response("hello")
# print(response)