import os
import logging
import tempfile
import pyttsx3
import uuid
from dotenv import load_dotenv
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    Voice,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    CallbackContext,
)
import responses
from scrapers.scraper_trip import scrape_trips
from scrapers.scraper_amazon import get_product_amazon,get_product_by_image_amazon
from scrapers.scraper_product import get_product_dna
from scrapers.scraper_book import get_5_books
from scrapers.scraper_cinemas import get_trending_in_cinemas_jordan
from scrapers.scraper_anime import get_anime
from scrapers.scraper_animations import get_3_Animations
from scrapers.scraper_taj_cinema import get_movie_details
from object_detection import perform_object_detection
from scrapers.scraper_opensouq import get_product_open_souq
from scrapers.scraper_events import scrape_events_from_url
from scrapers.scraper_other import (
    get_quote,
    top_10_games_of_all_times,
    top_10_latest_games,
    get_random_joke,
)
from scrapers.movies_tv_scraper import (
    top_action_movies,
    top_comedy_movies,
    top_horror_movies,
    top_10_rated_movies,
    top_action_tv_shows,
    top_comedy_tv_shows,
    top_horror_tv_shows,
    top_10_rated_tv_shows,
)
from handle_voice_message import (
    convert_ogg_to_wav,
    convert_speech_to_text,
)

# Getiing bot token from env file
load_dotenv()
Bot_Token = os.getenv('TELEGRAM_KEY')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

## Text messages handling
def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    
    if " -" in text:
        update.message.reply_text("Please make sure to not leave a space between the command and the dash, use this format (Example- What to search for).")
        return
    
    if "amazon-" in text:
        products = get_product_amazon(text)
        for product in products:
            update.message.reply_text(product)
        return
    
    if "book-" in text:
        products = get_5_books(text)
        for product in products:
            update.message.reply_text(product)
        return
    
    if "dna-" in text:
        products = get_product_dna(text)
        for product in products:
            update.message.reply_text(product)
        return
    
    if "opensouq-" in text:
        products = get_product_open_souq(text)
        for product in products:
            update.message.reply_text(product)
        return
    
    if "joke" in text:
        response = get_random_joke()
        update.message.reply_text(response)
        return
    
    if "quote" in text:
        data = get_quote()
        update.message.reply_text(data)
        return

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)

## Image handling
def image_handler(update: Update, context: CallbackContext):
    message = update.message

    if message.photo:  # Check if the message contains an image
        # Handle image message
        photo = message.photo[-1]
        photo_file_id = photo.file_id

        # Create the 'downloaded_images' directory if it doesn't exist
        os.makedirs('downloaded_images', exist_ok=True)

        # Generate a unique filename
        filename = 'image.jpg'
        file_path = os.path.join('downloaded_images', filename)

        # Download the image
        photo_file = context.bot.get_file(photo_file_id)
        photo_file.download(file_path)

        # Perform object detection and get the detected objects
        detected_objects = perform_object_detection(file_path)

        # Extract the names of the detected objects
        detected_object_names = [obj['name'] for obj in detected_objects]

        # Reply with the names of the detected objects
        print(detected_object_names)
        if detected_object_names:
            # reply_message = "Detected objects:\n" + "\n".join(detected_object_names)
            products = get_product_by_image_amazon(detected_object_names[0])
            for product in products:
                update.message.reply_text(product)
            # return
        else:
            update.message.reply_text("No objects detected in the image.")
   
## Voice messages handling
def voice_processing(update: Update, context: CallbackContext):
    file_id = update.message.voice.file_id
    file = context.bot.get_file(file_id)
    file.download('voice_message.ogg')

    convert_ogg_to_wav('voice_message.ogg', 'voice_message.wav')
    text = convert_speech_to_text('voice_message.wav')

    if text:
        response = responses.get_response(text)
        if "joke" in text:
            response = get_random_joke()

        # Convert the response to speech
        engine = pyttsx3.init()
        temp_audio_path = tempfile.mktemp(suffix='.wav')
        engine.save_to_file(response, temp_audio_path)
        engine.runAndWait()

        # Send the voice message
        with open(temp_audio_path, 'rb') as audio_file:
            update.message.reply_voice(voice=audio_file)
            update.message.reply_text(response)
    else:
        update.message.reply_text("Sorry, I couldn't convert the voice message to text.")


def start(update, context):
    # Send a string message
    update.message.reply_text("Good day there, I'm JAD, a Chatbot that can communicate with you.")
    
    # Send an image
    image_path = '../JAD.jpg'  # Replace with the actual path to your image

    with open(image_path, 'rb') as image_file:
        update.message.reply_photo(photo=image_file)

    # Additional message
    update.message.reply_text("I can suggest many things to do for entertainment, including Movies, Tvshows, Video Games, Books, products, quotes and I can also make you laugh :)")

def cmd(update, context):
    update.message.reply_text(
        '/start - Get started\n'
        '/quotes - Receive a random quote\n'
        '/cinema - Trending movies in Jordanian cinemas\n'
        '/tajcinema - Movies on tajcinema\n'
        '/movie - Choose a movie genre and receive a list of movies\n'
        '/tvshow - Choose a TV show genre and receive a list of shows\n'
        '/anime - Get random 3 from top Anime\n'
        '/animation - Get random 3 Animation movies\n'
        '/tvshow - Choose a TV show genre and receive a list of shows\n'
        '/joke - Get a random joke\n'
        '/trip - Display local trip plans with prices\n'
        '/events - Show all upcoming events in Jordan\n'
        '/game - Get the top 10 games of your choice\n'
        '/help - Ask for help\n'
        '/cmd - A list of all commands\n'
        '/contact - Authors of this project and the link to our GitHub Orgaization\n'
    )

def contact(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                                text ='''
Our Team Members:\n
- Malik Alhudrub
- Leena Alzaben
- Maysa'a Al Batayneh
- Hasan Alrawaqa
- Mones Odetallah
- Al Mutaz Billah Abu Taha\n
This is our organizations Git Repo:\n {Github} https://github.com/JAD-Bot-Team/JAD\n
                                ''')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="This is our organizations Git Repo:\n {Github} https://github.com/JAD-Bot-Team/JAD\n\n ")

# return a random quote
def quote(update, context):
    data = get_quote()
    update.message.reply_text(data)

# Return a random joke
def joke(update, context):
    random_joke = get_random_joke()
    update.message.reply_text(random_joke)

def cinema(update, context):
    trending_movies = get_trending_in_cinemas_jordan()
    for movie in trending_movies:
        update.message.reply_text(movie)

# movies
def movie(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Action", callback_data='action'),
            InlineKeyboardButton("Horror", callback_data='horror'),
            InlineKeyboardButton("Comedy", callback_data='comedy'),
            InlineKeyboardButton("ByRating", callback_data='byrating')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('💡Choose a Genre:', reply_markup=reply_markup)

# tv shows
def tv_show(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Action", callback_data='tv_show_action'),
            InlineKeyboardButton("Horror", callback_data='tv_show_horror'),
            InlineKeyboardButton("Comedy", callback_data='tv_show_comedy'),
            InlineKeyboardButton("ByRating", callback_data='tv_show_byrating')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('💡Choose a Genre:', reply_markup=reply_markup)

# games 
def game(update, context) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Top 10 games of all time", callback_data='top_10_games'),
            InlineKeyboardButton("Top 10 latest games", callback_data='top_10_latest_games'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('💡Choose a Category:',reply_markup=reply_markup)

def anime(update, context):
    animes = get_anime()
    for anime in animes:
        update.message.reply_text(anime)
    
def animation(update, context):
    animations = get_3_Animations()
    for animation in animations:
        update.message.reply_text(animation)
    
# this function checks for each button pressed after selecting an option from the menu
def trip(update, context):
    trips = scrape_trips()
    for trip in trips:
        update.message.reply_text(trip)
    return

def tajcinema(update, context):
    movies = get_movie_details()
    for movie in movies:
        update.message.reply_text(movie)
    return

def events(update, context):
    events = scrape_events_from_url()
    for event in events:
        update.message.reply_text(event)
    return
    
def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer()
    # print(f"Query message: {query.message}")

    # Now we can use context.bot, context.args and query.message
    if query.data == 'top_10_games':
        games = top_10_games_of_all_times()
        for game in games:
            context.bot.send_message(chat_id=query.message.chat_id, text=game)
    elif query.data == 'top_10_latest_games':
        games = top_10_latest_games()
        for game in games:
            context.bot.send_message(chat_id=query.message.chat_id, text=game)
    elif query.data == 'action':
        movies = top_action_movies()
        for movie in movies:
            context.bot.send_message(chat_id=query.message.chat_id, text=movie)
    elif query.data == 'horror':
        movies = top_horror_movies()
        for movie in movies:
            context.bot.send_message(chat_id=query.message.chat_id, text=movie)
    elif query.data == 'comedy':
        movies = top_comedy_movies()
        for movie in movies:
            context.bot.send_message(chat_id=query.message.chat_id, text=movie)
    elif query.data == 'byrating':
        movies = top_10_rated_movies()
        for movie in movies:
            context.bot.send_message(chat_id=query.message.chat_id, text=movie)
    elif query.data == 'tv_show_action':
        tvshows = top_action_tv_shows()
        for show in tvshows:
            context.bot.send_message(chat_id=query.message.chat_id, text=show)
    elif query.data == 'tv_show_horror':
        tvshows = top_horror_tv_shows()
        for show in tvshows:
            context.bot.send_message(chat_id=query.message.chat_id, text=show)
    elif query.data == 'tv_show_comedy':
        tvshows = top_comedy_tv_shows()
        for show in tvshows:
            context.bot.send_message(chat_id=query.message.chat_id, text=show)
    elif query.data == 'tv_show_byrating':
        tvshows = top_10_rated_tv_shows()
        for show in tvshows:
            context.bot.send_message(chat_id=query.message.chat_id, text=show)

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')



# Run the programms from here
if __name__ == '__main__':
    updater = Updater(Bot_Token, use_context=True)
    dp = updater.dispatcher
    # Commands handler which callback our commands when user ask for it
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('cmd', cmd))
    dp.add_handler(CommandHandler('contact', contact))
    dp.add_handler(CommandHandler('quotes', quote))
    dp.add_handler(CommandHandler('movie', movie))
    dp.add_handler(CommandHandler('tvshow', tv_show))
    dp.add_handler(CommandHandler('joke', joke))
    dp.add_handler(CommandHandler('cinema', cinema))
    dp.add_handler(CommandHandler('game', game))
    dp.add_handler(CommandHandler('anime', anime))
    dp.add_handler(CommandHandler('animation', animation))
    dp.add_handler(CommandHandler('tajcinema', tajcinema))
    dp.add_handler(CommandHandler('trip', trip))
    dp.add_handler(CommandHandler('events', events))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.voice, voice_processing))
    dp.add_handler(MessageHandler(Filters.photo, image_handler))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_error_handler(error)
    updater.start_polling(1.0)
    updater.idle()
    