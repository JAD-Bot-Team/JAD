import json
import requests
from bs4 import BeautifulSoup
import random


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n - by " + json_data[0]['a']
    print('Quotes Sent Successfully')
    return quote


def top_10_games_of_all_times():
    url = "https://www.imdb.com/list/ls054383657/?st_dt=&mode=detail&page=1&sort=list_order,asc"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the game titles within <h3> tags and class "lister-item-header"
    game_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store game details
    games = []

    # Extract the details for each game
    for title in game_titles[:10]:
        game = {}

        # Get the game title
        game['title'] = title.a.text.strip()

        # Get the IMDb link for the game
        game['link'] = "https://www.imdb.com" + title.a['href']

        # Get the game description
        description_elem = title.find_next_sibling("div", class_="item_description")
        game['description'] = description_elem.text.strip() if description_elem else "Description not available"

        # Add the game details to the list
        games.append(game)

    # Return the top ten games as separate strings
    top_ten_games = []
    for game in games:
        game_str = ""
        game_str += f"Title: {game['title']}\n"
        game_str += f"IMDb Link: {game['link']}\n"
        game_str += f"Description: {game['description']}\n"
        top_ten_games.append(game_str)

    print("Sent top 10 games of all time 🚀")
    return top_ten_games

def top_10_latest_games():
    url = "https://www.imdb.com/list/ls054383657/?st_dt=&mode=detail&page=1&sort=release_date,desc"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the game titles within <h3> tags and class "lister-item-header"
    game_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store game details
    games = []

    # Extract the details for each game
    for title in game_titles[:10]:
        game = {}

        # Get the game title
        game['title'] = title.a.text.strip()

        # Get the IMDb link for the game
        game['link'] = "https://www.imdb.com" + title.a['href']

        # Get the game description
        description_elem = title.find_next_sibling("div", class_="item_description")
        game['description'] = description_elem.text.strip() if description_elem else "Description not available"

        # Add the game details to the list
        games.append(game)

    # Return the top ten games as separate strings
    top_ten_games = []
    for game in games:
        game_str = ""
        game_str += f"Title: {game['title']}\n"
        game_str += f"IMDb Link: {game['link']}\n"
        game_str += f"Description: {game['description']}\n"
        top_ten_games.append(game_str)

    print("Sent top 10 latest games 🚀")
    return top_ten_games

def get_random_joke():
    jokes = [
        "How do all the oceans say hello to each other? They wave!",
        "How do you talk to a giant? Use big words!",
        "Why are balloons so expensive? Inflation!",
        "What did one wall say to the other wall? I’ll meet you at the corner!",
        "What do you call a bear with no teeth? A gummy bear!",
        "What do you call cheese that isn’t yours? Nacho cheese!",
        "Where do cows go for entertainment? To the moo-vies!",
        "Knock, knock. Who’s there? Cows go. Cows go who? No, cows go MOO!",
        "What do you call a cow with no legs? Ground beef!",
        "What do you call a cow with two legs? Lean meat!",
        "What do you call a pig that knows karate? A pork chop!",
        "Why are ghosts bad liars? Because you can see right through them!",
        "What animal needs to wear a wig? A bald eagle!",
        "What do you call a fly without wings? A walk!",
        "Knock knock. Who’s there? A little old lady? A little old lady who? I didn’t know you could yodel!",
        "Why do bees have sticky hair? Because they use honey combs!",
        "What do you call an alligator in a vest? An investigator!",
        "Why can’t you give Elsa a balloon? Because she will let it go!",
        "What do you get when you cross a snowman with a vampire? Frostbite!",
        "What has four wheels and flies? A garbage truck!",
        "Why did the man run around his bed? Because he was trying to catch up on his sleep!",
        "Why did the math book look so sad? Because it had so many problems!",
        "What do librarians take when they go fishing? Book worms!",
        "Can a kangaroo jump higher than the Empire State Building? Of course! The Empire State Building can’t jump!",
        "If April showers bring Mayflowers, what do Mayflowers bring? Pilgrims!",
        "What do you call a sleeping bull? A bulldozer!",
        "What did the zero say to the eight? Nice belt!",
        "Why do sharks swim in saltwater? Because pepper water makes them sneeze!",
        "Where do you find a dog with no legs? Right where you left him!",
        "Where do fish keep their money? In the river bank!",
        "Why did the gum cross the road? It was stuck to the chicken’s foot!",
        "What is brown and sticky? A stick!",
        "Why did the picture go to jail? It was framed!",
        "How do you know if there’s an elephant under your bed? Your head hits the ceiling!",
        "Why are elephants so wrinkled? Because they take too long to iron!",
        "How do you keep an elephant from charging? Take away her credit card!",
        "Why did the elephant paint himself different colors? So he could hide in the crayon box!",
        "How can you tell if an elephant has been in your refrigerator? By the footprints in the butter!",
        "What is the difference between elephants and grapes? Grapes are purple.",
        "What did Tarzan say when he saw the elephants coming? “Here come the elephants!”",
        "What did Jane say when she saw the elephants coming? “Here come the grapes!” (She was colorblind.)",
        "Why did the chicken cross the playground? To get to the other slide!",
        "What can you catch but not throw? A cold!",
        "What has hands but can’t clap? A clock!",
        "What do you call a dog that can tell time? A watch dog!",
        "What did one hat say to the other? Stay here, I’m going on ahead. (going on a head)",
        "What side of a turkey has the most feathers? The outside!",
        "What falls in winter but never gets hurt? The snow!",
        "Why did the teacher put on sunglasses? Because her students were so bright!",
        "How did Benjamin Franklin feel when he discovered electricity? Shocked!",
        "Why do strings never win a race? Because they always tie!",
        "What kind of shoes do ninjas wear? Sneakers!",
        "What do you call a flower that runs on electricity? A power plant!",
        "Why couldn’t the pony sing in the choir? Because she was a little horse!",
        "Why did the cookie go to the nurse? Because he felt crummy!",
        "What kind of room doesn’t have doors? A mushroom!",
        "How do you keep a bull from charging? Take away its credit card!",
        "What did one plate say to the other? Dinner is on me!",
        "How do you make a lemon drop? Just let go of it!",
        "Why did the boy throw his clock out the window? Because he wanted to see time fly!",
        "What does an evil hen lay? Deviled eggs!",
        "Which hand is better to write with? Neither. It’s better to write with a pencil!",
        "What did the traffic light say to the truck? Don’t look! I’m changing!",
        "What is the witch’s favorite school subject? Spelling!",
        "What did the frog order for lunch? A burger and a diet croak!",
        "Why did the teddy bear not want any dessert? Because she was stuffed!",
        "What do you call a fly without wings? A walk.",
        "Why should you never trust a pig with a secret? Because it’s bound to squeal.",
        "What do cows order from? Cattle-logs!",
        "What’s the difference between broccoli and boogers? Kids don’t eat broccoli!",
        "What kind of haircuts do bees get? Buzzzzcuts!",
        "How can you tell if someone is a good farmer? He is outstanding in his field!",
        "What do you call a man with a shovel? Doug.",
        "How do mountains stay warm in winter? Snowcaps!",
        "Why can’t a person’s nose be 12 inches long? Because then it would be a foot!",
        "What has a ton of ears but can’t hear a thing? A corn field.",
        "What do you call the horse that lives next door? Your neighbor!",
        "What kind of shoes do spies wear? Sneakers!",
        "Why did the man put sugar on his pillow? He wanted to have sweet dreams!",
        "Why did the computer sneeze? Because it had a virus!",
        "What do you call two banana peels? A pair of slippers!",
        "What do you call a cow who gets her way all the time? Spoiled milk!",
        "How does a scientist freshen her breath? With experiments! (experi-mints!)",
        "What is a computer programmer’s favorite snack? Computer chips!",
        "Why do hummingbirds hum? Because they don’t know the words!",
        "What do you call a mad elephant? An earthquake!",
        "Why do birds fly south in the winter? Because it’s too far to walk!",
        "What do you get on every birthday? A year older!",
        "Why should you not talk to circles? Because there is no point!",
        "Why is it dangerous to play cards in the jungle? Because there are so many CHEETAHS! (cheaters)",
        "How do you fix a cracked pumpkin? With a pumpkin patch!",
        "Why do seagulls fly over the sea? Because if they flew over the bay, they would be bagels.",
        "How many apples grow on a tree? All of them!",
        "What’s gray and goes round and round? An elephant in a washing machine!",
        "Why can’t an egg tell a joke? It will crack up!",
        "Why did the golfer wear two pairs of pants? In case he got a hole in one!",
        "What do fish play on the piano? Scales!",
        "Where do hamburgers go dancing? A meat ball!",
        "How do billboards talk? Sign language!",
        "What do snakes like to study in school? Hissss-tory!",
        "What kind of music do balloons hate? Pop music.",
        "What do you call a sad strawberry? A blueberry!",
        "What do you call a cow that can’t moo? A milk dud.",
        "What did the pig say on a hot day? I’m bacon!",
        "What did the cowboy say when his dog ran away? Doggone it!",
        "What do cowboys put on their salads? Ranch dressing!",
        "What do you call a dinosaur in a cowboy hat? Tyrannosaurus Tex!",
        "What do you call a happy cowboy? A jolly rancher!",
        "What time is it when a lion walks into a room? Time to leave!",
        "What’s green and not heavy? Light green!",
        "What do you give a hurt lemon? Lemon aid!",
        "What is the most valuable type of fish? A gold fish!",
        "What did the pirate say on his 80th birthday? Aye matey.",
        "What kind of music do whales like? They listen to the orca-stra!",
        "Why did the baker put the cake in the freezer? She wanted to ice it!",
        "What’s red and bad for your teeth? A brick!",
        "What a king’s favorite kind of weather? Rain! (reign)",
        "Why can’t the music teacher start his car? He left his keys on his piano!",
        "What do Alexander the Great and Winnie the Pooh have in common? Their middle name!",
        "What is brown, hairy, and wears sunglasses? A cool coconut!",
        "What do you call a retired vegetable? A has-bean!",
        "What’s blue and smells like red paint? Blue paint!",
        "What do you call a hen who counts her eggs? A mathema-chicken!",
        "What kind of lion doesn’t roar? A dandelion!",
        "Why did the baker go to therapy? She had too many turnovers!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a bear without any teeth? A gummy bear!",
        "What do you call fake spaghetti? An impasta!",
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What do you call a pile of cats? A meowtain!",
        "Why did the bicycle fall over? It was two-tired!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "What do you call a bear with no ears? B!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the bicycle fall over? It was two-tired!",
        "What do you call fake spaghetti? An impasta!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What do you call a pile of cats? A meowtain!",
        "Why was the math book sad? Because it had too many problems!",
        "Why did the golfer bring two pairs of pants? In case he got a hole-in-one!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why couldn't the leopard play hide and seek? Because he was always spotted!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An impasta!",
        "Why did the bike fall over? Because it was two-tired!",
        "What's orange and sounds like a parrot? A carrot!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the golfer bring two pairs of pants? In case he got a hole-in-one!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why couldn't the leopard play hide and seek? Because he was always spotted!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An impasta!",
        "Why did the bike fall over? Because it was two-tired!",
        "What's orange and sounds like a parrot? A carrot!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the golfer bring two pairs of pants? In case he got a hole-in-one!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why couldn't the leopard play hide and seek? Because he was always spotted!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An impasta!",
        "Why did the bike fall over? Because it was two-tired!",
        "What's orange and sounds like a parrot? A carrot!"
    ]
    
    # Return a random joke from the list
    return random.choice(jokes)
# print(get_random_joke())
