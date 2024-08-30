# AnaliseBrasileirao
 Projeto que extrai os dados dos últimos campeonatos brasileiros, e a partir disso é possível tirar várias conclusões

Primeira rodada:
    -   Adicionando as bibliotecas necessárias: bs4, pandas. E utilizando algumas funções 'urlopen, urlretrieve, Request';
    -   Criando 'funcoes.py' para armazenar algumas funções que se repitirão no programa;
        funcoes.py:
            -   Criado a função menuInicial(), que tem como objetivo imprimir as opções do menu principal para o operador:
                    menuInicial(): - Apresenta as opções dos anos dos campeonatos;
                                   - Permitido selecionar qualquer quantidade de campeonatos(apenas 2021, 2020, 2019, 2018 todos);