from utilities import limpiar_precios,limpiar_m2, limpiar_location
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

from scraper_encuentra24 import scraper


print('Iniciando Scrapeo...')
scraper()
print('Scrapeo y actualizacion de data completo')