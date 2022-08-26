from utilities import limpiar_precios,limpiar_m2, limpiar_location
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
#from scraper_encuentra24 import scraper
import time

while True:
    hoy = datetime.datetime.today()
    time.sleep(5)
    minuto_hoy = hoy.time().minute
    if minuto_hoy==17:
        #scraper()
        pass
    print(hoy.time().minute)

if __name__ == '__main__':
    print('Iniciando Scrapeo...')
    scraper()
    print('Scrapeo y actualizacion de data completo')