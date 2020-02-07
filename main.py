import os
#import un as modelo
import datetime
import sys
from datetime import date, datetime
from src.funcoes import base_geral as b1
from src.funcoes import base_comun as b2
from src.funcoes import searchBinary, escreve
#print(os.path.dirname(os.path.realpath(__file__)))
#path = r'Arq_entrada/Modelo/Modelos_Chuva_vazao_' + datetime.strftime(date.today(), '%Y%m%d') + r'Modelos_Chuva_vazao/SMAP'
regiao = ['Grande', 'Iguacu', 'Itaipu', 'Paranaiba', 'Paranapanema', 'SaoFrancisco', 'Tiete', 'Tocantins',
          'Uruguai']

#for j in regiao:
#	path_modelo = r'Arq_entrada/Modelo/Modelos_Chuva_Vazao_' + modelo.parser(1,'%Y%m%d') + r'/Modelos_Chuva_Vazao/SMAP/' + j + '/ARQ_ENTRADA'
#	modelo.inicializacao(path_modelo, modelo.parser(1,'%Y%m%d'), 'PMEDIA_ORIG')
#	modelo.precipitacao(path_modelo)

if __name__ == '__main__':
	
	print('Insira a o ano do modelo CxV:')
	ano = int(input())
	print('Insira a o mes do modelo CxV:')
	mes = int(input())
	print('Insira a o dia do modelo CxV:')
	dia = int(input())
	
	data = date(ano,mes,dia)

	modelo = date.strftime(data,'%Y%m%d')

	for j in regiao: # Itera sobre cada regiao para definir os caminhos
		
		path_modelo = r'Arq_entrada/Modelo/Modelos_Chuva_Vazao_' + modelo + r'/Modelos_Chuva_Vazao/SMAP/' + j + '/ARQ_ENTRADA'
		path_base = r'base/1/' + j + r'/Base.dat'
		
		for i in os.listdir(path_modelo): # Dentro dos modelos SMAP procuramos os arquivos de chuva presentes
			
			if 'PMEDIA_ORIG' in i: # Ao achar o arquivo de chuva ele é lido pela função b1 ou b2 assim como as bases
				
				aplicado = b2(path_modelo + '//' + i)
				aplicado.sort(key=lambda x: (x[0],x[1])) # Ordena em função de (lat, long)
				base = b2(path_base)
				base.sort(key=lambda x: (x[0],x[1])) # Ordena em função de (lat, long)
				lista_auxiliar = []

				for k in base:
					
					print('Região: ', j) 
					aux =  searchBinary(k[0:2], aplicado) # Para cada valor (x,y) dentro da base, procura a precipitação correspondente nos arquivos de chuva
					print(aux)
					k[2] = aux
					lista_auxiliar.append(k) # com o valor achado, é feita a substituição criando uma nova lista

				for k in range(len(lista_auxiliar)): # Para cada iteração na lista, o valor é substituido por uma string = 'lat long  precipitacao'

					lista_auxiliar[k] = str(lista_auxiliar[k][0]) + ' ' + str(lista_auxiliar[k][1]) + '  ' + str(lista_auxiliar[k][2] + '\n')
				
				escreve(path_modelo + '//' + i, lista_auxiliar) # Escrita da lista no lugar dos arquivos antigos

				# a ideia da busca binaria e da troca dos arquivos é melhorar o funcionamento do Chuva vazao. Assim só serão usados os arquivos referentes a propria bacia