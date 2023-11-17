import telebot
import openai
from config import OPENAI_API_KEY,BOT_API
from openai import OpenAI


openai.api_key = OPENAI_API_KEY

chatStr = ''

def ChatModel(prompt):
    global chatStr
    chatStr += f"Manas:{prompt}\nJarvis:"
    client = OpenAI()

    response = client.completions.create(
        model="text-davinci-003",
        prompt="",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response)
    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, 'Hello Welcome to AI Bot that created by Manas!')

@bot.message_handler()
def chat(message):
    try:
        replay = ChatModel(message.text)
        bot.reply_to(message, replay)
    except Exception as e:
        print(e)
        bot.reply_to(message, str(e))

print('Bot Started.......')
bot.polling()
