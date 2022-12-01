from utilities import dir_checker
from scraper_encuentra24 import scraper
import pandas as pd
import time
import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from secret import SLACK_TOKEN

if __name__ == '__main__':
    dir_checker()
    print('Iniciando Scrapeo...')

    data = scraper(test=True)
    data.to_csv("data/encuentra24_ventas_casas.csv", encoding="utf-8", index=False)
    now = str(datetime.datetime.now())

    decoration = '*'*len(f'*Scraper ran at {now}*')

    notif_text = f'''
    [OK {now}] Records added: {data.shape[0]} 
    '''

    slack_client = WebClient(token=SLACK_TOKEN)
    slack_client.chat_postMessage(channel='#basededatos', text=notif_text)


    print('Scrapeo y actualizacion de data completo')