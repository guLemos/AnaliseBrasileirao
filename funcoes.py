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

def menuEscolhas(anos):
    chamaFuncao = {1:mostraCampeao}
    print('---------- ESCOLHA UMA OPÇÃO ----------')
    print('1 - Classificação(s)')
    print('2 - Campeão(s)')
    print('3 - ------------------')
    print('4 - ------------------')
    print('5 - ------------------')
    escolha = int(input('Escolha uma opção: '))
    # chamaFuncao[escolha]()
    if escolha == 1:
        for i in range(len(anos)):
            classificacaoGeral(anos[i])
    if escolha == 2:
        for i in range(len(anos)):
            print(mostraCampeao(anos[i]))

def obtemSite(ano):
    url = 'https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/'+str(ano)+'/jogos/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def classificacaoGeral(ano):
    soup = obtemSite(ano)
    dados = soup.find('table', class_='pg-color4').find('tr').findNext('tr')
    print('-'*29+str(ano)+'-'*28)
    print('     {}            {}     {}     {}     {}     {}     {}     {}'.format('TIME', 'P', 'J', 'V', 'E', 'D', 'GP', 'GC'))
    print('    ------          ---   ---   ---   ---   ---   ----   ----')

    for i in range(20):
        linha = [text for text in dados.stripped_strings]
        print('{:<20}{:>3}{:>6}{:>6}{:>6}{:>6}{:>6}{:>7}'.format(linha[1], linha[2], linha[3], linha[4],linha[5],linha[6],linha[7],linha[8]))
        print('-'*61)
        dados = dados.findNext('tr')
    print('')
    print('')
    

def mostraCampeao(ano):
    soup = obtemSite(ano)
    campeao = soup.find('table', class_='pg-color4').find('tr').findNext('tr').find('th').findNext('th').getText()
    return campeao

def mostraZonaDeRebaixamento(ano):
    soup = obtemSite(ano)
    lista = soup.find