from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, Request

def menuInicial():
    anos = {1: 2019, 2:2018, 3: 2017, 4:2016, 5:2015, 6:2014, 9:None}
    escolhas = []
    escolha = None
    print('---------- BRASILEIRÃO ----------')
    print('1 - 2019')
    print('2 - 2018')
    print('3 - 2017')
    print('4 - 2016')
    print('5 - 2015')
    print('6 - 2014\n')
    print('9 - Confirmar')
    print('0 - Sair')
    print('Selecione um ou mais anos para analisar: ')
    while escolha != 0 and escolha != 9:
        try:
            escolha = int(input())
            if escolha == 0:
                exit()
            if anos[escolha] in escolhas:
                continue
            else:
                escolhas.append(anos[escolha])  
        except ValueError:
            print('Apenas inteiros')
        except KeyError:
            print('opção inválida')
    if None in escolhas:
        escolhas.remove(None)
    return escolhas

def obtemSite(ano):
    url = 'https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/'+str(ano)+'/jogos/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lista = soup.find('table', class_='pg-color4').find('tr')
    return soup#lista

def mostraCampeao(soup):
    lista = soup.find('table', class_='pg-color4').find('tr')
    lista = lista.findNext('tr').find('th').findNext('th').getText()
    return lista