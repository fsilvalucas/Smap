import os
import datetime
from datetime import datetime,date
import sys
import shutil

import un as modelo

regiao = ['Grande', 'Iguacu', 'Itaipu', 'Paranaiba', 'Paranapanema', 'SaoFrancisco', 'Tiete', 'Tocantins',
          'Uruguai']
path_chuva = r'Arq_entrada/Precipitacao'
#path_modelo = r'Arq_entrada/Modelo/Modelos_Chuva_Vazao_' + modelo.parser(1,'%Y%m%d') + r'/Modelos_Chuva_vazao/SMAP'

def chek():
	if modelo_precipitacao not in os.listdir(path_chuva):
		print('O modelo de Precipitacao não bate com os arquivos passados')
	sys.exit()

for j in regiao:
	path_modelo = r'Arq_entrada/Modelo/Modelos_Chuva_Vazao_' + modelo.parser(1,'%Y%m%d') + r'/Modelos_Chuva_Vazao/SMAP/' + j + '/ARQ_ENTRADA'
	
	

	for i in os.listdir(path_modelo):
		if 'PMEDIA_ORIG_p' in i:
			print(i)
			print(modelo.parser(0,'%d%m%y'))
			print(modelo.parser(1,'%d%m%y'))
			os.rename(path_modelo + '\\' + i, path_modelo + '\\' + i.replace(modelo.parser(0,'%d%m%y'), modelo.parser(1,'%d%m%y')))