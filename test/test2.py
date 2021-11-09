import telegram
import telegram

bot = telegram.Bot(token='input tokent value')
chat_id = -692460691

bot.send_message(chat_id=chat_id,text="Let's get started!")
updates = bot.get_updates()
#print(updates[0])
