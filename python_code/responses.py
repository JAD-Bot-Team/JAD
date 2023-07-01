# import re


# def Bot_Response(message, response_array, response):
#     # Splits the message and the punctuation into an array
#     list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

#     # Scores the amount of words in the message
#     score = 0
#     for word in list_message:
#         if word in response_array:
#             score = score + 1

#     # Returns the response and the score of the response
#     # print(score, response)
#     return [score, response]


# def get_response(message):
#     # Add your custom responses here
#     response_list = [
#         Bot_Response(message, ['hello','helloo','helli', 'hi','hii','heyy', 'hey', 'sup'],
#                      'Hello there, JAD is here to serve you.\nYou can talk normally or Type (cmd) to get started '),

#         Bot_Response(message, ['bye', 'goodbye'], 'Please don\'t go!'),

#         Bot_Response(message, ['cmd', 'type cmd'], 'click me /list'),

#         Bot_Response(message, ['how', 'are', 'you'],
#                      'I\'m doing fine thanks!'),
#         # new
#         Bot_Response(message, ['how', 'you', 'created'],
#                      'I was created by using python and got deployed on Herkou'),
#         # Name
#         Bot_Response(message, ['your', 'name'],
#                      'My name is Rohan\'s Bot, nice to meet you!'),
#         # Help
#         Bot_Response(message, ['help', 'please'],
#                      'I will do my best to assist you!'),
#         # Website
#         Bot_Response(message, ['link', 'links', ], 'website https://rohan.ml'),

#         # Song
#         Bot_Response(message, ['play', 'song', ],
#                      'https://youtu.be/edzt82nC45k'),

#         # Notes
#         Bot_Response(message, ['notes', 'note', ],
#                      'Soon, notes will be available'),

#         Bot_Response(message, ['socials', 'socials', ],
#                      'Here you Go\n /socials'),

#         Bot_Response(message, ['source', 'code', ],
#                      'Here you Go\n /source_code'),

#         # When Querry
#         Bot_Response(message, ['when', '?', 'query', 'question', 'inform',
#                      'developer'], 'Inquire with the developer about this. @amrohan'),

#         # When Website
#         Bot_Response(message, ['website', 'amrohan', 'web', 'developer'],
#                      'https://www.rohan.ml'),

#         # When Projects
#         Bot_Response(message, ['projects', 'project', 'proj','pro','projec', 'proje'],
#                      'Here you Go\n /projects'),

#     ]

#     # Checks all of the response scores and returns the best matching response
#     response_scores = []
#     for response in response_list:
#         response_scores.append(response[0])

#     # Get the max value for the best response and store it into a variable
#     winning_response = max(response_scores)
#     matching_response = response_list[response_scores.index(winning_response)]

#     # Return the matching response to the user
#     if winning_response == 0:
#         bot_response = 'I didn\'t understand what you wrote.'
#     else:
#         bot_response = matching_response[1]

#     print('Bot response:', bot_response)
#     return bot_response

# import json
# import spacy
# nlp = spacy.load('en_core_web_md')
# def calculate_similarity(message, triggers):
#     message_doc = nlp(message.lower())
#     trigger_docs = [nlp(trigger.lower()) for trigger in triggers]
#     similarities = [message_doc.similarity(trigger_doc) for trigger_doc in trigger_docs]
#     return similarities



# def get_response(message):
#     # Load responses from JSON file
#     with open('responses.json', 'r') as file:
#         response_data = json.load(file)

#     # Check the response scores and find the best matching response
#     best_similarity = 0
#     best_response = None
#     for data in response_data:
#         similarities = calculate_similarity(message, data['triggers'])
#         max_similarity = max(similarities)
#         if max_similarity > best_similarity:
#             best_similarity = max_similarity
#             best_response = data['response']

#         print("Question:", message)
#         print("Triggers:", data['triggers'])
#         print("Similarities:", similarities)
#         print()

#     # Define the threshold similarity score
#     threshold_similarity = 0.80

#     # Return the matching response or "I didn't understand what you wrote."
#     if best_similarity >= threshold_similarity:
#         bot_response = best_response
#     else:
#         bot_response = "I didn't understand what you wrote."

#     print('Bot response:', bot_response)
#     print(max_similarity)
#     return bot_response




import json
import difflib

# Load the trigger-response data from responses.json
def load_responses():
    with open("responses.json", "r") as file:
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
            if ratio > best_ratio:
                best_ratio = ratio
                best_response = item["response"]
    
    return best_response

# Example usage
# response = get_response("hello")
# print(response)

