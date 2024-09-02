# AnaliseBrasileirao
 Projeto que extrai os dados dos últimos campeonatos brasileiros, e a partir disso é possível tirar várias conclusões

Possíveis melhorias:
    - Função para tratar as escolhas - Opção inválida, apenas inteiros, ...;
    OK- Na função "menuEscolhas" melhorar a chamada dupla das funções "mostrarCampeao" e "obtemSite", para que uma função chame a outra, assim não sendo necessário a dupla chamada;
    - Encontrar outro meio que não sejam vários IFs para o menuInicial;
    - Apresentar a posição do time após a chamada da função "classificacaoGeral"

Primeira rodada:
    -   Adicionando as bibliotecas necessárias: bs4, pandas. E utilizando algumas funções 'urlopen, urlretrieve, Request';
    -   Criando 'funcoes.py' para armazenar algumas funções que se repitirão no programa;
        funcoes.py:
            -   Criado a função menuInicial(), que tem como objetivo imprimir as opções do menu principal para o operador:
                    menuInicial(): - Apresenta as opções dos anos dos campeonatos;
                                   - Permitido selecionar qualquer quantidade de campeonatos(apenas 2019, 2018, 2017, 2016, 2015, 2014, todos);
            -   Criado a função menuEscolhas(), que tem como objetivo imprimir as opções:
                    menuEscolhas(): - Classificação(s) - Apresenta a classificação geral dos anos selecionados;
                                    - Campeão(s) - Apresenta cada campeão dos anos selecionados;

Onde parei:
    - 02/09/2024 13:26 - Início da opção em que mostra a classificação geral dos campeonatos;