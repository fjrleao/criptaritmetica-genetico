# criptaritmetica-genetico
Algoritmo genético para resolver problemas de criptaritmética 

# O que é um algoritmo genético?
De acordo com a wikipedia https://pt.wikipedia.org/wiki/Algoritmo_gen%C3%A9tico:

"Algoritmos Genéticos (AG) são implementados como uma simulação de computador em que uma população de representações abstratas de solução é selecionada em busca de soluções melhores. A evolução geralmente se inicia a partir de um conjunto de soluções criado aleatoriamente e é realizada por meio de gerações. A cada geração, a adaptação de cada solução na população é avaliada, alguns indivíduos são selecionados para a próxima geração, e recombinados ou mutados para formar uma nova população. A nova população então é utilizada como entrada para a próxima iteração do algoritmo."

# O que é criptaritmetica?
Partindo de uma explicação mais prática, suponhamos que tenhamos a seguinte espressão:

SEND+MORE=MOREY,

O papel da criptaritmética é encontrar números entre 0 e 9 e relacionar as letras da expressão de forma que a expressão fique correta.

# Como utilizar o algoritmo
O uso do algoritmo se da por meio de parâmetros passados através de linha de comando: 

-i INPUT -p POPULACAO -g GERACAO -c CROSSOVER -m MUTACAO -t TORNEIO -s SELECAO -a AVALIACAO

Um exemplo mais prático de uso seria:

python3 ag.py -i SEND+MORE=MONEY -p 100 -g 100 -c 60 -m 2 -t 0 -s 2 -a 1

# Testes do algoritmo
Alguns testes com o input SEND+MORE=MONEY foram realizados variando os parâmetros e podem ser observados na tabela a seguir:

População | Gerações | Crossover | Mutação | Resultado
----------|----------|-----------|---------|----------
50 | 50 | 40 | 0 | -
50 | 50 | 40 | 15 | -
50 | 50 | 80 | 0 | -
50 | 50 | 80 | 15 | [8, 68530721]
50 | 500 | 40 | 0 | -
50 | 500 | 40 | 15 | [212, 68530721]
50 | 500 | 80 | 0 | -
50 | 500 | 80 | 15 | -
500 | 50 | 40 | 0 | -
500 | 50 | 40 | 15 | -
500 | 50 | 80 | 0 | -
500 | 50 | 80 | 15 | -
500 | 500 | 40 | 0 | -
500 | 500 | 40 | 15 | -
500 | 500 | 80 | 0 | -
500 | 500 | 80 | 15 | [21, 75310826]

O primeiro valor no vetor resultado representa em qual população o resultado foi encontrada e o segundo valor representa o resultado, sendo que o resultado segue a ordem de letras da esquerda para a direita desconsiderando letras repetidas. 
