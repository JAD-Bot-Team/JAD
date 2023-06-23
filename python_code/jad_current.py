import os
import logging
import responses
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from scraper_other import get_quote,top_10_games_of_all_times,top_10_latest_games,get_random_joke,get_5_books,get_5_novels,get_product
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


# We defined this fuction to use as commands
# all update.message are reply from bots to user
def start(update, context):
    update.message.reply_text(
        "Good day there, I'm a bot that can communicate with you. You can get the most up-to-date tech news from devto or tldr, and more services will be added shortly..\n To start, say hey, hi, or hello.\n Get all Commands -/cmd")

# To Do Functionality ... Malik
def cmd(update, context):
    update.message.reply_text(
        '/start - Description on how to get started\n/quotes recieve a random quote\n/movie - choose a movie genre and recive a list of movies\n/tvshow - choose a tvshow genre and recive a list of shows\n/book - choose a book genre and recive a list of book\n/joke - Recive a random joke\n/game - Recive the top 10 games of your choice\n/product - Look up a product on the Internet\n/help - Ask for help\n/cmd - A list of all commands\n/socials - The link for Our Github')
def socials(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="This is our organizations Git Repo:\n {Github} https://github.com/JAD-Bot-Team/JAD\n\n ")
    '''
    start - Description
    quotes - get a random quote
    movie - Suggest a movie
    tvshow - Suggest a tv show
    book - Suggest a book
    joke - tell a joke
    product - Search for a product
    game - Search for a game
    help - Get help
    cmd - Commands
    socials - socials
    '''


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)

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
    update.message.reply_text(
        '💡Choose a Genre:', reply_markup=reply_markup)

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
    
def book(update, context) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Top 5 books", callback_data='top_5_books'),
            InlineKeyboardButton("Top 5 novels", callback_data='top_5_novels'),
        ]
    ]
def product(update, context) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Amazon", callback_data='product_amazon'),
            InlineKeyboardButton("Bestbuy", callback_data='product_bestbuy'),
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
        game1, game2, game3, game4, game5, game6, game7, game8, game9, game10 = top_10_games_of_all_times()
        context.bot.send_message(chat_id=query.message.chat_id, text=game1)
        context.bot.send_message(chat_id=query.message.chat_id, text=game2)
        context.bot.send_message(chat_id=query.message.chat_id, text=game3)
        context.bot.send_message(chat_id=query.message.chat_id, text=game4)
        context.bot.send_message(chat_id=query.message.chat_id, text=game5)
        context.bot.send_message(chat_id=query.message.chat_id, text=game6)
        context.bot.send_message(chat_id=query.message.chat_id, text=game7)
        context.bot.send_message(chat_id=query.message.chat_id, text=game8)
        context.bot.send_message(chat_id=query.message.chat_id, text=game9)
        context.bot.send_message(chat_id=query.message.chat_id, text=game10)
    elif query.data == 'top_10_latest_games':
        game1, game2, game3, game4, game5, game6, game7, game8, game9, game10 = top_10_latest_games()
        context.bot.send_message(chat_id=query.message.chat_id, text=game1)
        context.bot.send_message(chat_id=query.message.chat_id, text=game2)
        context.bot.send_message(chat_id=query.message.chat_id, text=game3)
        context.bot.send_message(chat_id=query.message.chat_id, text=game4)
        context.bot.send_message(chat_id=query.message.chat_id, text=game5)
        context.bot.send_message(chat_id=query.message.chat_id, text=game6)
        context.bot.send_message(chat_id=query.message.chat_id, text=game7)
        context.bot.send_message(chat_id=query.message.chat_id, text=game8)
        context.bot.send_message(chat_id=query.message.chat_id, text=game9)
        context.bot.send_message(chat_id=query.message.chat_id, text=game10)
    elif query.data == 'action':
        movie1, movie2, movie3, movie4, movie5 = top_action_movies()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
    elif query.data == 'horror':
        movie1, movie2, movie3, movie4, movie5 = top_horror_movies()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
    elif query.data == 'comedy':
        movie1, movie2, movie3, movie4, movie5 = top_comedy_movies()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
    elif query.data == 'byrating':
        movie1, movie2, movie3, movie4, movie5,movie6, movie7, movie8, movie9, movie10 = top_10_rated_movies()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie6)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie7)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie8)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie9)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie10)
    elif query.data == 'tv_show_action':
        movie1, movie2, movie3, movie4, movie5 = top_action_tv_shows()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
    elif query.data == 'tv_show_horror':
        movie1, movie2, movie3, movie4, movie5 = top_horror_tv_shows()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
    elif query.data == 'tv_show_comedy':
        movie1, movie2, movie3, movie4, movie5 = top_comedy_tv_shows()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
    elif query.data == 'tv_show_byrating':
        movie1, movie2, movie3, movie4, movie5,movie6, movie7, movie8, movie9, movie10 = top_10_rated_tv_shows()
        context.bot.send_message(chat_id=query.message.chat_id, text=movie1)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie2)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie3)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie4)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie5)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie6)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie7)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie8)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie9)
        context.bot.send_message(chat_id=query.message.chat_id, text=movie10)
    elif query.data == 'top_5_books':
        book1, book2, book3, book4, book5, = get_5_books()
        context.bot.send_message(chat_id=query.message.chat_id, text=book1)
        context.bot.send_message(chat_id=query.message.chat_id, text=book2)
        context.bot.send_message(chat_id=query.message.chat_id, text=book3)
        context.bot.send_message(chat_id=query.message.chat_id, text=book4)
        context.bot.send_message(chat_id=query.message.chat_id, text=book5)
    elif query.data == 'top_5_novels':
        book1, book2, book3, book4, book5, = get_5_novels()
        context.bot.send_message(chat_id=query.message.chat_id, text=book1)
        context.bot.send_message(chat_id=query.message.chat_id, text=book2)
        context.bot.send_message(chat_id=query.message.chat_id, text=book3)
        context.bot.send_message(chat_id=query.message.chat_id, text=book4)
        context.bot.send_message(chat_id=query.message.chat_id, text=book5)
    elif query.data == 'product_amazon':
        product = get_product()
        context.bot.send_message(chat_id=query.message.chat_id, text=product)
    elif query.data == 'product_bestbuy':
        product = get_product()
        context.bot.send_message(chat_id=query.message.chat_id, text=product)


# there two methods to crete functions to get repond from bot this is 2nd one

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

    dp.add_handler(CommandHandler('book', book))

    dp.add_handler(CommandHandler('joke', joke))

    dp.add_handler(CommandHandler('product', product))
    
    dp.add_handler(CommandHandler('game', game))
    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # CallbackQueryHandler
    dp.add_handler(CallbackQueryHandler(button))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    # Idle state give bot time to go in idle
    updater.idle()