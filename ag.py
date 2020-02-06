# -*- coding: utf-8 
# TRABALHO DE INTELIGENCIA ARTIFICIAL
# DOUGLAS FELIPE MUNARO E FÁBIO JUNIOR

from  collections import OrderedDict
import argparse
import random

#python3 ag.py -i SEND+MORE=MONEY -p 100 -g 100 -c 60 -m 2 -t 0 -s 2 -a 1

#Funçao principal
def main():
	geracoes = 0
	achou = 0
	populacao = []
	parseArg()
	retiraRepetidas()
	populacaoInicial = geraPopulacaoIni()
	avalia1 = avaliacao(populacaoInicial, metAvaliacao)
	for i in range(0, len(avalia1)):
		if avalia1[i] == 0:
			achou = 1
			print("ACHOU O RESULTADO")
			print('[1  ', populacaoIni[i],']')
			exit(0)

	populacao = populacaoInicial
	
	while geracoes < numGeracoes:
		populacao = crossover(populacao)
		populacao = mutacao(populacao)
		avalia1 = avaliacao(individuos, metAvaliacao)
		exclui_piores(avalia1)

		populacao = individuos
		for j in range(0, len(avalia1)):
			print(str(avalia1[j]) + ' -- ' + str(individuos[j]))
			if avalia1[j] == 0:
				achou = 1
				print("ACHOU O RESULTADO")
				print('[ '+ str(geracoes)+ ' ' + str(individuos[j]) + ' ]')
				exit(0)
		geracoes += 1
		print(geracoes)
		# print("geracoes: " +str(geracoes))

		
	
#Funçao para manipulaçao dos argumentos
def parseArg():
    
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser(description="Criptoartimetica")
    ap.add_argument("-i", "--input", required=True, help="Expressão a ser avaliada")
    ap.add_argument("-p", "--populacao", required=True, help="População Inicial")
    ap.add_argument("-g", "--geracao", required=True, help="Número de Gerações")
    ap.add_argument("-c", "--crossover", required=True, help="Taxa de Crossover")
    ap.add_argument("-m", "--mutacao", required=True, help="Taxa de Mutação")
    ap.add_argument("-t", "--torneio", required=True, help="Número de Torneio --> '0' se metodo de seleção não for torneio")
    ap.add_argument("-s", "--selecao", required=True, help="Método de Seleção")
    ap.add_argument("-a", "--avaliacao", required=True, help="Método de Avaliação")
    args = ap.parse_args()

    #variaveis que irao receber o conteudo dos argumentos
    global exp #recebera o input inicialmente
    global populacaoQtd #quantidade da populaçao
    global numGeracoes #numero de geraçoes 
    global taxaCrossover #taxa de crossover  
    global taxaMutacao #taxa de mutaçao
    global numTorneio #numero de torneio
    global metSelecao #metodo de seleçao
    global metAvaliacao #metodo de avaliaçao
    exp = args.input
    populacaoQtd = int(args.populacao)
    numGeracoes = int(args.geracao)
    taxaCrossover = int(args.crossover)
    taxaMutacao = int(args.mutacao)
    numTorneio = int(args.torneio)
    metSelecao = int(args.selecao)
    metAvaliacao = int(args.avaliacao)


#Funçao para retirar letras repetidas da expressao
def retiraRepetidas():

	global exp #expressao apenas com letras minusculas
	global expLimpa #expressao com letras minusculas e sem sinais de '+' e '='
	global manipulaExp #recebera o input depois de serem eliminados o sinal de '+' e '=' e eleminados todos os caracteres repetidos
    
	exp = exp.lower()
	expLimpa = exp
	expLimpa = expLimpa.replace('+',"")
	expLimpa = expLimpa.replace('=',"")
	manipulaExp = list(OrderedDict.fromkeys(expLimpa))


#Funçao para gerar populaçao inicial
def geraPopulacaoIni():

	global populacaoIni #lista que recebera a populaçao inicial
	populacaoIni = []
	global individuos
	individuos = []
	global manipulaExp
	dicionario = {}
	for i in range(int(populacaoQtd)):
		result = random.sample(range(0,9), len(manipulaExp))
		if str(result) in dicionario:
			print("INDIVIDUO DUPLICADO")
		else:
			dicionario[str(result)] = 1			
			populacaoIni.append(result)

		
		
		#print(populacaoIni[i])
		#print(i)
		#print("\n")
	
	individuos = populacaoIni
	return populacaoIni

#Funcao de avaliaçao
#metAvaliacao = 1  -->  Diferença entre a soma desejada e a soma real no valor total
#metAvaliacao = 2  -->  Soma das diferenças entre a soma desejada e a soma real dígito a dígito
#metAvaliacao = 3  -->  Produto das diferenças entre a soma desejada e a soma real dígito a dígito
def avaliacao(pop, avaliacao):

	auxExp = "" #auxExp sera usada para dividir os valores da expressao para poder ser feito a soma
	aux1 = "" #aux1 sera utilizada para receber o valor antes do sinal de '+'
	aux2 = "" #aux2 sera utilizada para receber o valor depois do sinal de '+'
	listaAvaliacao = []
	listaAvaliacao.clear()

	if avaliacao == 1:

		for k in range(0, len(pop)):
			auxExp = ""
			listaAux = pop[k]
			for i in range(0, len(exp)):
				for j in range(0, len(manipulaExp)):
					if exp[i] == manipulaExp[j]:
						auxExp = auxExp + str(listaAux[j])

				if exp[i] == '+':
					aux1 = auxExp
					auxExp = ""
				if exp[i] == '=':
					aux2 = auxExp
					auxExp = ""
					somaDesejada = int(aux1) + int(aux2) #somaDesejada recebe a soma de aux1 + aux2

				if i == int(len(exp))-1:
					somaReal = int(auxExp) #somaReal recebe auxExp pois sera o valor que ira sobrar depois da manipulaçao e é justamente o valor da soma real
					diferenca = abs(somaDesejada -somaReal)
					listaAvaliacao.append(diferenca)
					
		return listaAvaliacao

	if avaliacao == 2:

		for k in range(0, len(pop)):
			auxExp = ""
			listaAux = pop[k]
			for i in range(0, len(exp)):
				for j in range(0, len(manipulaExp)):
					if exp[i] == manipulaExp[j]:
						auxExp = auxExp + str(listaAux[j])

				if exp[i] == '+':
					aux1 = auxExp
					auxExp = ""
				if exp[i] == '=':
					aux2 = auxExp
					auxExp = ""
					somaDesejada = int(aux1) + int(aux2) #somaDesejada recebe a soma de aux1 + aux2

				if i == int(len(exp))-1:
					somaReal = int(auxExp) #somaReal recebe auxExp pois sera o valor que ira sobrar depois da manipulaçao e é justamente o valor da soma real
					diferenca = abs(somaDesejada -somaReal)
					diferenca = somarDigitos(diferenca)
					listaAvaliacao.append(diferenca)
					
		return listaAvaliacao

	if avaliacao == 3:

		for k in range(len(pop)):
			auxExp = ""
			listaAux = pop[k]
			for i in range(len(exp)):
				for j in range(len(manipulaExp)):
					if exp[i] == manipulaExp[j]:
						auxExp = auxExp + str(listaAux[j])

				if exp[i] == '+':
					aux1 = auxExp
					auxExp = ""
				if exp[i] == '=':
					aux2 = auxExp
					auxExp = ""
					somaDesejada = int(aux1) + int(aux2) #somaDesejada recebe a soma de aux1 + aux2

				if i == int(len(exp))-1:
					somaReal = int(auxExp) #somaReal recebe auxExp pois sera o valor que ira sobrar depois da manipulaçao e é justamente o valor da soma real
					diferenca = abs(somaDesejada -somaReal)
					diferenca = multDigitos(diferenca)
					listaAvaliacao.append(diferenca)
					
		return listaAvaliacao
						

def roleta(pop):

	resultados_invertidos = []
	resultados_invertidos = [-1] * len(pop)
	vetor_intervalos = []
	vetor_intervalos = [-1] * len(pop)
	vetor = []
	vetor = [-1] * len(pop)
	resultado = 0
	total_valores = 0
	vetor = avaliacao(pop, metAvaliacao)
	# print(vetor)
	
	for k in range(0, len(pop)):
		try:
			aux_roleta = float( 1/ vetor[k] )
		except:
			aux_roleta = 0
			print("ACHOU O RESULTADO: " +str(individuos[k]))
			exit(0)
		resultados_invertidos[k] = round(aux_roleta,2)
	
	# coloca os valores obtidos na avaliação dentro do vetor
	for i in range(0, len(pop)):		
		total_valores = total_valores + resultados_invertidos[i]
		vetor_intervalos[i] = total_valores
	
	roleta = random.uniform(1,total_valores)

	for i in range(0, len(pop)):
		if roleta >= vetor_intervalos[i] and roleta <= vetor_intervalos[i+1]: 
			resultado = i
			break

	resultados_invertidos.clear()
	vetor_intervalos.clear()
	vetor.clear()
	
	return individuos[resultado]

def torneio_de_3(pop, taxa_torneio):
	posicao = 0
	finalistas = []
	finalistas = [-1] * len(pop)
	torneio = []
	torneio = [-1] * len(pop)
	vetor = avaliacao(pop, metAvaliacao)
	total_valores = 0
	for j in range(0, taxa_torneio):
		for i in range(0, taxa_torneio):
			valor = random.randint(1, len(vetor)-1)
			torneio[i] = vetor[valor]

		melhor = torneio[0]
		for i in range(0, taxa_torneio):
			if(melhor > torneio[i] ):
				melhor = torneio[i]
		finalistas.append(melhor)	

	resultado = finalistas[0]
	for i in range(0, len(finalistas)):
			if(resultado > finalistas[i]):
				resultado = finalistas[i]

	for k in range(0, len(vetor)):
		if ( vetor[k] == resultado):
			posicao = k	
			break

	return individuos[posicao]		


def crossover(pop):

	pai1 = []
	pai1 = [-1] * len(pop)
	pai2 = []
	pai2 = [-1] * len(pop)
	filho1 = []
	filho2 = []

	taxa = 0
	taxa = int((( len(individuos) * taxaCrossover) / 100) / 2)

	# for para trocar de posições
	for k in range(0, taxa):	
		pai1 = roleta(pop)
		pai2 = roleta(pop)
		while pai1 == pai2:
			pai2 = roleta(pop)

		ponto1 = random.randint(1, len(pai1)-2)
		ponto2 = random.randint(1, len(pai1)-2) 
		if ponto2 < ponto1:
			aux = ponto1			
			ponto1 = ponto2
			ponto2 = ponto1
	
		while  ( ponto2 - ponto1) < 2 or (ponto2 - ponto1) > 3:
			ponto1 = random.randint(1, len(pai1)-2)
			ponto2 = random.randint(1, len(pai1)-2)
		
		# print("Ponto1: " +str(ponto1))
		# print("Ponto2: " +str(ponto2))

		filho1 = list(pai1)
		filho2 = list(pai2)
		# print("PAI: " +str(filho1))
		# print("PAI 2: " +str(filho2))
		# print(filho1[ponto1:ponto2])
		# print(filho2[ponto1:ponto2])
		filho1[ponto1:ponto2] = pai2[ponto1:ponto2]
		filho2[ponto1:ponto2] = pai1[ponto1:ponto2]
		
		# for para fazer as mudanças, para não existir valores repetidos
		for k in range(0, len(filho1)):
			if(k < ponto1 or k >= ponto2):
				m = ponto1 
				while(m < ponto2):
					if(filho1[k] == filho1[m]):
						filho1[k] = filho2[m]
						m = ponto1
					else:
						m += 1

		for r in range(0, len(filho2)):
			if(r < ponto1 or r >= ponto2):
				o = ponto1
				while(o < ponto2):
					if(filho2[r] == filho2[o]):
						filho2[r] = filho1[o]
						o = ponto1
					else:
						o += 1
		# print(filho1)
		# print(filho2)
		individuos.append(filho1)
		individuos.append(filho2)

def mutacao(pop):	
	taxa = ( len(individuos) * taxaMutacao) / 100
	for i in range (0, int(taxa)):	
		inicio = len(individuos) - int((len(individuos) * taxaMutacao) / 100) / 2
		
		indice_filho  = random.randint(int(inicio), len(individuos)-1)
		
		filho = individuos[indice_filho]
		indice1 = random.randint(0, len(filho)-1)
		indice2 = random.randint(0, len(filho)-1)
	
		aux = filho[indice1]
		filho[indice1] = filho[indice2]
		filho[indice2] = aux
		
		individuos[indice_filho] = filho

def exclui_piores(avalia1):
	for i in range(0, len(avalia1)-100):
		pior = max(avalia1)
		pos = avalia1.index(pior)
		del avalia1[pos]
		del individuos[pos]
	


def somarDigitos(n):
    s = 0
    while n:
        s += n % 10
        n //= 10 
    return s

def multDigitos(n):
	s = 1
	while n:
		aux = n % 10
		if aux == 0:
			s *= 1
			n //= 10
		else:
			s *= aux
			n //= 10
	return s



if __name__ == "__main__":
	main()
