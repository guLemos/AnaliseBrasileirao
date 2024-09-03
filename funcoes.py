from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, Request

def menuInicial():
    anos = {1:2024, 2:2023, 3: 2022, 4:2021, 5:2020, 6:2019, 7:2018, 8:2017, 9:2016, 10:2015, 12:None}
    escolhas = []
    escolha = None
    print('---------- BRASILEIRÃO ----------')
    print('1 - 2024')
    print('2 - 2023')
    print('3 - 2022')
    print('4 - 2021')
    print('5 - 2020')
    print('6 - 2019')
    print('7 - 2018')
    print('8 - 2017')
    print('9 - 2016')
    print('10 - 2015\n')
    print('11 - Confirmar')
    print('0 - Sair')
    print('Selecione um ou mais anos para analisar: ')
    while escolha != 0 and escolha != 11:
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
    print('3 - Times recém chegados')
    print('4 - Artilharia')
    print('5 - ------------------')
    escolha = int(input('Escolha uma opção: '))
    # chamaFuncao[escolha]()
    if escolha == 1:
        for i in range(len(anos)):
            classificacaoGeral(anos[i])
    if escolha == 2:
        for i in range(len(anos)):
            print(mostraCampeao(anos[i]))
    if escolha == 3:
        for i in range(len(anos)):
            timesSubiram(anos[i])
    if escolha == 4:
        for i in range(len(anos)):
            artilharia(anos[i])

def obtemSiteTabelaA(ano):
    url = 'https://www.espn.com.br/futebol/classificacao/_/liga/BRA.1/temporada/'+str(ano)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def obtemSiteTabelaB(ano):
    url = 'https://www.espn.com.br/futebol/classificacao/_/liga/BRA.2/temporada/'+str(ano)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def obtemEstatisticasA(ano):
    url = 'https://www.espn.com.br/futebol/estatisticas/_/liga/BRA.1/temporada/'+str(ano)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def artilharia(ano):
    soup = obtemEstatisticasA(ano)
    artilheiro = soup.find('table', class_='Table').find('tr', class_='Table__TR Table__TR--sm Table__even')
    for j in range(4):
        artilheiroTemp = artilheiro.findAll('td')
        for i in range(1,3):
            print(artilheiroTemp[i].getText(), end='  ')
        print()
        artilheiro = artilheiro.findNext('tr')

def classificacaoGeral(ano):
    soup = obtemSiteTabelaA(ano)
    times = soup.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left').find('tbody').find('tr')
    dados = soup.find('table', class_='Table Table--align-right').find('tbody').find('tr')
    print('-'*29+str(ano)+'-'*28)
    print('     {}            {}     {}     {}     {}     {}     {}     {}'.format('TIME', 'P', 'J', 'V', 'E', 'D', 'GP', 'GC'))
    print('    ------          ---   ---   ---   ---   ---   ----   ----')

    for i in range(20):
        linha = [text for text in dados.stripped_strings]
        time = [text for text in times.stripped_strings]
        print('{:<20}{:>3}{:>6}{:>6}{:>6}{:>6}{:>6}{:>7}'.format(time[2], linha[7], linha[0], linha[1],linha[2],linha[3],linha[4],linha[5]))
        print('-'*61)
        dados = dados.findNext('tr')
        times = times.findNext('tr')
    print('')
    print('')

def mostraCampeao(ano):
    soup = obtemSiteTabelaA(ano)
    campeao = soup.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left').find('tbody').find('tr').find('td').find('span',class_='hide-mobile').getText()
    return campeao

def timesSubiram(ano):
    soup = obtemSiteTabelaB(ano-1)
    nomeTimeSubiu = soup.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left').find('tbody').find('tr').find('span', class_='hide-mobile')

    print('\nOs times que subiram da série B no ano passado foram: ', end='')

    for i in range(4):
        print(nomeTimeSubiu.getText(), end='')
        if i<2:
            print(', ' , end='')
        elif i == 2:
            print(' e',end=' ')
        nomeTimeSubiu = nomeTimeSubiu.findNext('tr').find('span', class_='hide-mobile')

def mostraZonaDeRebaixamento(ano):
    soup = obtemSiteTabelaA(ano)
    lista = soup.find