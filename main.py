from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd
from funcoes import *



anos = menuInicial()
anos.sort(key=int)

menuEscolhas(anos)