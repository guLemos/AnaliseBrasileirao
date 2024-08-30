from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd
from funcoes import menuInicial, obtemSite, mostraCampeao




lista = menuInicial()
lista.sort(key=int)
enderecos = []
# for i in range(len(lista)):
#     enderecos.append('https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/'+str(lista[i])+'/jogos/')
# print(enderecos)
print(lista)

print(mostraCampeao(obtemSite(lista[0])))