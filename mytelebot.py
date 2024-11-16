import telebot
from datetime import datetime
from dotenv import load_dotenv
import os
# Load các biến môi trường từ tệp .env
load_dotenv()
# Replace 'YOUR_API_TOKEN' with the API token you received from the BotFather
API_TOKEN = os.getenv("API_TOKEN")


bot = telebot.TeleBot(API_TOKEN)
# Define a function to get the current date, month, and year
def get_current_date():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    return f"Dạ thưa bố, hôm nay là {day}/{month}/{year}."

# Define a command handler for /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Type /date to get today's date.")

# Define a command handler for /date
@bot.message_handler(commands=['date'])
def send_date(message):
    date_info = get_current_date()
    bot.reply_to(message, date_info)

# Define a message handler for all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.polling()
