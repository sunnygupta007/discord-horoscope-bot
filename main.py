from typing import Final
from random import choice, randint
import os
import requests
import json
#import discord
#from theastrologer import Horoscope
# TOKEN removed - use environment variable instead
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
'''async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)'''


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


'''def get_horoscope(sign):
    url = "https://ohmanda.com/api/horoscope/" + sign
            
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        data = response.json()
                
        if "horoscope" in data:
            return data["horoscope"]
        else:
            return "Error: Horoscope not found in response"
            
    except requests.RequestException as e:
        return f"Error: {e}"'''


ZODIAC_SIGNS = {
    "aries": 1,
    "taurus": 2,
    "gemini": 3,
    "cancer": 4,
    "leo": 5,
    "virgo": 6,
    "libra": 7,
    "scorpio": 8,
    "sagittarius": 9,
    "capricorn": 10,
    "aquarius": 11,
    "pisces": 12
}

def get_horoscope(sign_name):
    sign_name_lower = sign_name.lower()  # Convert sign name to lowercase
    sign_number = ZODIAC_SIGNS.get(sign_name_lower)  # Get the sign number
    
    if sign_number is None:
        return "Error: Invalid zodiac sign"
    
    base_url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign_number}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope_div = soup.find('div', class_='main-horoscope')
        
        if horoscope_div:
            # Find the <p> tag inside the div
            p_tag = horoscope_div.find('p')
            if p_tag:
                # Replace <br> tags with newline characters
                horoscope_text = p_tag.get_text('\n', strip=True)
                return horoscope_text.strip()  # Extract the text inside the <p> tag
            else:
                return "Error: Required content is not found inside main division"
        else:
            return "Error: Horoscope not found on the page"
            
    except requests.RequestException as e:
        return f"Error: {e}"

    

def get_weekly_horoscope(sign_name):
    sign_name_lower = sign_name.lower()  # Convert sign name to lowercase
    sign_number = ZODIAC_SIGNS.get(sign_name_lower)  # Get the sign number
    
    if sign_number is None:
        return "Error: Invalid zodiac sign"
    
    base_url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={sign_number}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope_div = soup.find('div', class_='main-horoscope')
        
        if horoscope_div:
            # Find the <p> tag inside the div
            p_tag = horoscope_div.find('p')
            if p_tag:
                # Replace <br> tags with newline characters
                horoscope_text = p_tag.get_text('\n', strip=True)
                return horoscope_text.strip()  # Extract the text inside the <p> tag
            else:
                return "Error: Required content is not found inside main division"
        else:
            return "Error: Weekly Horoscope is not found on the page"
            
    except requests.RequestException as e:
        return f"Error: {e}"
    

def get_monthly_horoscope(sign_name):
    sign_name_lower = sign_name.lower()  # Convert sign name to lowercase
    sign_number = ZODIAC_SIGNS.get(sign_name_lower)  # Get the sign number
    
    if sign_number is None:
        return "Error: Invalid zodiac sign"
    
    base_url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={sign_number}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope_div = soup.find('div', class_='main-horoscope')
        
        if horoscope_div:
            # Find the <p> tag inside the div
            p_tag = horoscope_div.find('p')
            if p_tag:
                # Replace <br> tags with newline characters
                horoscope_text = p_tag.get_text('\n', strip=True)
                return horoscope_text.strip()  # Extract the text inside the <p> tag
            else:
                return "Error: Required content is not found inside main division"
        else:
            return "Error: Monthly Horoscope is not found on the page"
            
    except requests.RequestException as e:
        return f"Error: {e}"
    

def get_career(sign_name):
    sign_name_lower = sign_name.lower()  # Convert sign name to lowercase
    sign_number = ZODIAC_SIGNS.get(sign_name_lower)  # Get the sign number
    
    if sign_number is None:
        return "Error: Invalid zodiac sign"
    
    base_url = f"https://www.horoscope.com/us/horoscopes/career/horoscope-career-daily-today.aspx?sign={sign_number}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope_div = soup.find('div', class_='main-horoscope')
        
        if horoscope_div:
            # Find the <p> tag inside the div
            p_tag = horoscope_div.find('p')
            if p_tag:
                # Replace <br> tags with newline characters
                horoscope_text = p_tag.get_text('\n', strip=True)
                return horoscope_text.strip()  # Extract the text inside the <p> tag
            else:
                return "Error: Required content is not found inside main division"
        else:
            return "Error: Career is not found on the page"
            
    except requests.RequestException as e:
        return f"Error: {e}"
    

def get_money(sign_name):
    sign_name_lower = sign_name.lower()  # Convert sign name to lowercase
    sign_number = ZODIAC_SIGNS.get(sign_name_lower)  # Get the sign number
    
    if sign_number is None:
        return "Error: Invalid zodiac sign"
    
    base_url = f"https://www.horoscope.com/us/horoscopes/money/horoscope-money-weekly.aspx?sign={sign_number}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope_div = soup.find('div', class_='main-horoscope')
        
        if horoscope_div:
            # Find the <p> tag inside the div
            p_tag = horoscope_div.find('p')
            if p_tag:
                # Replace <br> tags with newline characters
                horoscope_text = p_tag.get_text('\n', strip=True)
                return horoscope_text.strip()  # Extract the text inside the <p> tag
            else:
                return "Error: Required content is not found inside main division"
        else:
            return "Error: Money is not found on the page"
            
    except requests.RequestException as e:
        return f"Error: {e}"
    

def get_health(sign_name):
    sign_name_lower = sign_name.lower()  # Convert sign name to lowercase
    sign_number = ZODIAC_SIGNS.get(sign_name_lower)  # Get the sign number
    
    if sign_number is None:
        return "Error: Invalid zodiac sign"
    
    base_url = f"https://www.horoscope.com/us/horoscopes/wellness/horoscope-wellness-daily-today.aspx?sign={sign_number}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        horoscope_div = soup.find('div', class_='main-horoscope')
        
        if horoscope_div:
            # Find the <p> tag inside the div
            p_tag = horoscope_div.find('p')
            if p_tag:
                # Replace <br> tags with newline characters
                horoscope_text = p_tag.get_text('\n', strip=True)
                return horoscope_text.strip()  # Extract the text inside the <p> tag
            else:
                return "Error: Required content is not found inside main division"
        else:
            return "Error: Health is not found on the page"
            
    except requests.RequestException as e:
        return f"Error: {e}"
    

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quotelist = []
    quotelist.append(json_data[0]['q']) #quote
    quotelist.append(" -" + json_data[0]['a']) #author

    return (quotelist)

# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:

    content = message.content.lower()

    if message.author == client.user:
        return
    
    elif content.startswith('$hello'):
        msg = 'Hello {0.author.mention} how are you? 😁\nType $ping to know all the available commands'.format(message)
        await message.channel.send(msg)


    elif content.startswith('$ping'):
        commands_list = (
            "Pong 🤣\n"
            "Just Kidding, here is the list of all commands you can use to control me\n\n"
            ".\n"
            "*******MAIN COMMANDS*******\n"
            "$daily  <your_zodiac_sign>\n$weekly   <your_zodiac_sign>\n$monthly   <your_zodiac_sign>\n$career     <your_zodiac_sign>\n$money   <your_zodiac_sign>\n$health   <your_zodiac_sign>\n$inspire\n\n"
            ".\n"
            "*******OTHER COMMANDS*******\n"
            "$hello\n$hey\n$ping\n$thanks\n$how are you\n$bye\n$sorry\n$no\n$roll dice"
            )

        await message.channel.send(commands_list)


        
    elif content.startswith('$daily'): #original daily
        await message.channel.send("Getting Horoscope...")
        sign_name = message.content.split(' ', 1)[1].lower()  # Extract zodiac sign from message
        print(sign_name)

        Horoscope = get_horoscope(sign_name)

        #horoscope = Horoscope(sign)
        #today = horoscope.today()
        await message.channel.send(f'Hello {message.author.mention}, Taino says that your Horoscope will be:')
        #msg2 = today['horoscope']
        await message.channel.send(Horoscope)


    elif content.startswith('$weekly'): #weekly
        await message.channel.send("Getting Weekly Horoscope...")
        sign_name = message.content.split(' ', 1)[1].lower()  # Extract zodiac sign from message
        print(sign_name)

        Weekly_Horoscope = get_weekly_horoscope(sign_name)

        await message.channel.send(f'Hello {message.author.mention}, Taino says that your Weekly Horoscope will be:')
        await message.channel.send(Weekly_Horoscope)


    elif content.startswith('$monthly'): #monthly
        await message.channel.send("Getting Monthly Horoscope...")
        sign_name = message.content.split(' ', 1)[1].lower()  # Extract zodiac sign from message
        print(sign_name)

        Monthly_Horoscope = get_monthly_horoscope(sign_name)

        await message.channel.send(f'Hello {message.author.mention}, Taino says that your Monthly Horoscope will be:')
        await message.channel.send(Monthly_Horoscope)


    elif content.startswith('$career'):
        await message.channel.send("Getting Career Insights...")
        sign_name = message.content.split(' ', 1)[1].lower()  # Extract zodiac sign from message
        print(sign_name)

        Career = get_career(sign_name)

        await message.channel.send(f'Hello {message.author.mention}, Taino says that your Career insights will be:')
        await message.channel.send(Career)


    elif content.startswith('$money'):
        #await message.channel.send("Hmm Money...")
        sign_name = message.content.split(' ', 1)[1].lower()  # Extract zodiac sign from message
        print(sign_name)

        Money = get_money(sign_name)

        await message.channel.send(f'Hello {message.author.mention}, Taino says "Hmmm I like Money" :')
        await message.channel.send(Money)


    elif content.startswith('$health'):
        #await message.channel.send("Health is Wealth...")
        sign_name = message.content.split(' ', 1)[1].lower()  # Extract zodiac sign from message
        print(sign_name)

        Health = get_health(sign_name)

        await message.channel.send(f'Hello {message.author.mention}, Taino says "Health is Wealth" :')
        await message.channel.send(Health)


    elif message.content.startswith('$inspire'):
        await message.channel.send("Let me think... 🤔")
        msg = get_quote()
        await message.channel.send("\n" + msg[0])
        await message.channel.send(msg[1])


    elif content.startswith('$thanks'): #original thanks case
        msg = "Glad I could assist! All credit goes to my creater Mr.Sunny 😊"
        await message.channel.send(msg)


    elif message.content.startswith('$hey'):
        msg = "Heyy there!"
        await message.channel.send(msg)


    elif message.content.startswith('$how are you'):
        msg = "Good, thanks!"
        await message.channel.send(msg)


    elif message.content.startswith('$bye'):
        msg = "See you! 👀"
        await message.channel.send(msg)


    elif message.content.startswith('$sorry'):
        msg = "Its okay. I am kind hearted 😊"
        await message.channel.send(msg)


    elif message.content.startswith('$no'):
        msg = "Someone has to do it buddy, that\'s the rule of the life 🫠"
        await message.channel.send(msg)


    elif message.content.startswith('$roll dice'):
        #msg = 'You rolled: {randint(1, 12)}
        await message.channel.send(f'You rolled: {randint(1, 12)}')


    elif message.content.startswith('$'):
        await message.channel.send(choice(["I do not understand...",
                        "What are you talking about?",
                        "Are you trying to annoy me? 😑 I do have feelings",
                        "Do you mind rephrasing that?",
                        "Could you clarify?",
                        "I'm not quite following. Could you elaborate?",
                        "That's unclear. Can you provide more context?",
                        "I'm sorry, I'm having trouble grasping that.",
                        "It seems I'm missing something. Can you explain further?",
                        "I'm not sure I understand. Could you simplify?",
                        "I'm having difficulty comprehending. Can you clarify?"
                        ]))
        '''username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)

        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)'''


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()