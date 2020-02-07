import os
import datetime
from datetime import datetime
from src.funcoes import searchBinary, escreve

def tamanho(lista):
	return range(len(lista))

def organizaArquivosDeChuva(cxv,prec, metodologia): # Classe chuva x vazao, classe precipitacao
	
	cont = 0
	path_to_model = cxv.path
	path_to_prec = prec.path

	caso = prec.state
	
	iter_model_regioes = [path_to_model + '//' + x + '//ARQ_ENTRADA' for x in cxv.regioes]
	iter_model_bases = ['base//' + caso + '//' + x + '//Base.dat' for x in cxv.regioes]

	for i in tamanho(iter_model_regioes):

		for j in os.listdir(iter_model_regioes[i]):

			if prec.nome in j:

				aplicado = metodologia(iter_model_regioes[i] + '//' + j)
				aplicado.sort(key=lambda x: (x[0],x[1]))
				base = metodologia(iter_model_bases[i])
				base.sort(key=lambda x: (x[0],x[1]))
				print(base)
				lista_auxiliar = []

				for k in base:

					print('Região: ', cont) 
					cont += cont
					aux =  searchBinary(k[0:2], aplicado) # Para cada valor (x,y) dentro da base, procura a precipitação correspondente nos arquivos de chuva
					print(aux)
					k[2] = aux
					lista_auxiliar.append(k) # com o valor achado, é feita a substituição criando uma nova lista

				for k in range(len(lista_auxiliar)): # Para cada iteração na lista, o valor é substituido por uma string = 'lat long  precipitacao'

					lista_auxiliar[k] = str(lista_auxiliar[k][0]) + ' ' + str(lista_auxiliar[k][1]) + '  ' + str(lista_auxiliar[k][2]) + '\n'

				escreve(iter_model_regioes[i] + '//' + j, lista_auxiliar) # Escrita da lista no lugar dos arquivos antigos

					# a ideia da busca binaria e da troca dos arquivos é melhorar o funcionamento do Chuva vazao. Assim só serão usados os arquivos referentes a propria bacia




			

