import schedule
import time
from pyrogram import Client
from scraper import scrape
from env import API_ID, API_HASH, CHAT_ID

BOT = Client(
    session_name = "KLExchanger",
    api_id = API_ID,
    api_hash = API_HASH
)
BOT.start()

def send_rates():
    kl_rates = scrape()
    full_message = "<b>Latest KL Exchange Rates</b>\n"
    for kl_rate in kl_rates:
        name = kl_rate['name']
        rate = kl_rate['rate']
        message = f"<b>{name}</b> | {rate}\n"
        full_message = full_message + message
    BOT.send_message(CHAT_ID, full_message)


schedule.every().hour.do(send_rates)

while True:
    schedule.run_pending()
    time.sleep(1)