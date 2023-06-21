import telebot
import random
import speech_recognition as sr

telegram_key = "5836999574:AAGXMmShLBarONcnDThnYBj0qyc6i_Z1OGw"

bot = telebot.TeleBot(telegram_key)

responses = {
    "greetings": {
        "hi": ["Hello!", "Hi there!", "Hey!"],
        "hello": ["Hi!", "Hello!", "Hey there!"],
        "hey": ["Hey!", "Hello!", "Hi there!"]
    },
    "commands": {
        "movie": ["Sure, let me recommend a movie for you.", "I can help you find a great movie. Give me a moment."],
        "book": ["Sure, let me recommend a book for you.", "I can help you find a great book. Give me a moment."],
        "game": ["Sure, let me recommend a game for you.", "I can help you find a great game. Give me a moment."]
    }
}

def check_for_responses(prompt, response_type):
    if response_type in responses:
        response_dict = responses[response_type]
        for keyword, response_list in response_dict.items():
            if keyword in prompt:
                return random.choice(response_list)
    return None

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_id = message.voice.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('voice_message.ogg', 'wb') as voice_file:
        voice_file.write(downloaded_file)

    text = convert_speech_to_text('voice_message.ogg')
    if text:
        handle_message(message, text)
    else:
        bot.reply_to(message, "Sorry, I couldn't convert the voice message to text.")

def convert_speech_to_text(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
            return text.lower()
        except sr.UnknownValueError:
            return None

@bot.message_handler(func=lambda message: True)
def handle_message(message, text=None):
    if not text:
        text = message.text.lower()

    greeting_response = check_for_responses(text, "greetings")
    if greeting_response:
        bot.reply_to(message, greeting_response)
        return

    command_response = check_for_responses(text, "commands")
    if command_response:
        bot.reply_to(message, command_response)
        return

    response = "Sorry, I did not understand that!"

    bot.reply_to(message, response)

bot.infinity_polling()


## telegram_key = "5836999574:AAGXMmShLBarONcnDThnYBj0qyc6i_Z1OGw"
## openai.api_key = "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"
