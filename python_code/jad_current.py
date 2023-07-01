import os
import logging
import responses
from dotenv import load_dotenv
from scraper_amazon import get_product_amazon
from scraper_product import get_product_newegg, get_product_dna
from scraper_book import get_5_books
from scraper_cinemas import get_trending_in_cinemas_jordan
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Voice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from scraper_other import get_quote,top_10_games_of_all_times,top_10_latest_games,get_random_joke
from movies_tv_scraper import top_action_movies, top_comedy_movies, top_horror_movies,top_10_rated_movies,top_action_tv_shows,top_comedy_tv_shows,top_horror_tv_shows,top_10_rated_tv_shows

# Getiing bot token from env file
load_dotenv()
Bot_Token = os.getenv('TELEGRAM_KEY')


'''
💡Use this version if you deploying it on repl.it
Add the bot token in secretes section
# Getiing bot token from env file
  Bot_Token = os.environ['Bot_Token']
'''


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    
    if " -" in text:
        update.message.reply_text("Please make sure to not leave a space between the command and the dash, use this format (Example- What to search for).")
        return
    if "newegg-" in text:
        products = get_product_newegg(text)
        for product in products:
            update.message.reply_text(product)
        return
    
    if "amazon-" in text:
        products = get_product_amazon(text)
        for product in products:
            update.message.reply_text(product)
        # update.message.reply_text(best_product)  
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

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)

def handle_voice_message(update, context):
    voice = update.message.voice
    
    # Extract necessary information from the voice message
    file_id = voice.file_id
    duration = voice.duration
    
    # Reply with a string
    reply_text = f"Received a voice message with file ID: {file_id} and duration: {duration} seconds"
    update.message.reply_text(reply_text)
# ...

# We defined this fuction to use as commands
# all update.message are reply from bots to user
def start(update, context):
    update.message.reply_text(
        "Good day there, I'm a Jad, a Chatbot that can communicate with you. I can suggest many things to do for entertainment, including Movies, Tvshows, Video Games, Books, products, quotes and I can also make you laugh :), more services will be added shortly..\n To start, say hey, hi, or hello.\n Get all Commands -/cmd")

def cmd(update, context):
    update.message.reply_text(
        '/start - Description on how to get started\n'
        '/quotes - Receive a random quote\n'
        '/cinema - Trending movies in Jordanian cinemas\n'
        '/movie - Choose a movie genre and receive a list of movies\n'
        '/tvshow - Choose a TV show genre and receive a list of shows\n'
        '/book - Choose a book genre and receive a list of books\n'
        '/joke - Receive a random joke\n'
        '/game - Receive the top 10 games of your choice\n'
        '/product - Look up a product on the Internet\n'
        '/help - Ask for help\n'
        '/cmd - A list of all commands\n'
        '/socials - The link for our GitHub'
    )

def socials(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="This is our organizations Git Repo:\n {Github} https://github.com/JAD-Bot-Team/JAD\n\n ")

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

# this function checks for each button pressed after selecting an option from the menu

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

    dp.add_handler(CommandHandler('socials', socials))

    dp.add_handler(CommandHandler('quotes', quote))

    dp.add_handler(CommandHandler('movie', movie))

    dp.add_handler(CommandHandler('tvshow', tv_show))

    dp.add_handler(CommandHandler('joke', joke))
    
    dp.add_handler(CommandHandler('cinema', cinema))
    
    dp.add_handler(CommandHandler('game', game))
    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    # Voices
    dp.add_handler(MessageHandler(Filters.voice, handle_voice_message))
    # CallbackQueryHandler
    dp.add_handler(CallbackQueryHandler(button))
    # Log all errors
    dp.add_error_handler(error)
    # Run the bot
    updater.start_polling(1.0)
    # Idle state give bot time to go in idle
    updater.idle()