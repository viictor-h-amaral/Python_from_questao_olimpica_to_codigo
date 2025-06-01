import algoritmo_combinacoes
import copy

def tomar_duas_a_duas(lista):
	return algoritmo_combinacoes.combinar(2, lista)

def caso_eh_valido (lista_com_o_caso):

	todas_notas_questoes1 = []
	todas_notas_questoes2 = []
	todas_notas_questoes3 = []
	
	for prova in lista_com_o_caso:
		todas_notas_questoes1.append( prova[0] ) #apenas notas questões 1
		todas_notas_questoes2.append( prova[1] ) #apenas notas questões 2
		todas_notas_questoes3.append( prova[2] ) #apenas notas questões 3
	
	index_questoes1_separadas_por_nota = separar_questoes_por_nota(todas_notas_questoes1) #ex.: [ [1,4,5] , [2,3] , [0] ]
	index_questoes2_separadas_por_nota = separar_questoes_por_nota(todas_notas_questoes2)
	index_questoes3_separadas_por_nota = separar_questoes_por_nota(todas_notas_questoes3)
	
	#faz pares de indexes em que a nota na questao eh igual


	#Q1

	pares_indexes_questao1_com_nota0 = tomar_duas_a_duas(index_questoes1_separadas_por_nota[0])
	pares_indexes_questao1_com_nota1 = tomar_duas_a_duas(index_questoes1_separadas_por_nota[1])
	pares_indexes_questao1_com_nota2 = tomar_duas_a_duas(index_questoes1_separadas_por_nota[2])
	
	pares_alunos_questao1_notas_iguais = []
	pares_alunos_questao1_notas_iguais.extend(pares_indexes_questao1_com_nota0)
	pares_alunos_questao1_notas_iguais.extend(pares_indexes_questao1_com_nota1)
	pares_alunos_questao1_notas_iguais.extend(pares_indexes_questao1_com_nota2)

	#Q2
	pares_indexes_questao2_com_nota0 = tomar_duas_a_duas(index_questoes2_separadas_por_nota[0])
	pares_indexes_questao2_com_nota1 = tomar_duas_a_duas(index_questoes2_separadas_por_nota[1])
	pares_indexes_questao2_com_nota2 = tomar_duas_a_duas(index_questoes2_separadas_por_nota[2])

	
	pares_alunos_questao2_notas_iguais = []
	pares_alunos_questao2_notas_iguais.extend(pares_indexes_questao2_com_nota0)
	pares_alunos_questao2_notas_iguais.extend(pares_indexes_questao2_com_nota1)
	pares_alunos_questao2_notas_iguais.extend(pares_indexes_questao2_com_nota2)

	#Q3
	pares_indexes_questao3_com_nota0 = tomar_duas_a_duas(index_questoes3_separadas_por_nota[0])
	pares_indexes_questao3_com_nota1 = tomar_duas_a_duas(index_questoes3_separadas_por_nota[1])
	pares_indexes_questao3_com_nota2 = tomar_duas_a_duas(index_questoes3_separadas_por_nota[2])
	
	pares_alunos_questao3_notas_iguais = []
	pares_alunos_questao3_notas_iguais.extend(pares_indexes_questao3_com_nota0)
	pares_alunos_questao3_notas_iguais.extend(pares_indexes_questao3_com_nota1)
	pares_alunos_questao3_notas_iguais.extend(pares_indexes_questao3_com_nota2)

	return not existem_duas_provas_com_duas_mesmas_questoes_com_mesma_nota(
		pares_alunos_questao1_notas_iguais,
		pares_alunos_questao2_notas_iguais,
		pares_alunos_questao3_notas_iguais)
	
	
def separar_questoes_por_nota(questoes):

	notas0 = []
	notas1 = []
	notas2 = []

	for index_questao in range( len(questoes) ):
		
		match questoes[index_questao]:
			case 0:
				notas0.append(index_questao)
			case 1:
				notas1.append(index_questao)
			case 2:
				notas2.append(index_questao)
	
	indexes_separados_por_nota = [notas0, notas1, notas2]
	
	return indexes_separados_por_nota
	
def existem_duas_provas_com_duas_mesmas_questoes_com_mesma_nota(lista1, lista2, lista3):
	for par_alunos in lista1: #validação para caso exista um par de notas iguais nas questoes (1 e 2) e (1 e 3)
		if(par_alunos in lista2 or par_alunos in lista3): return True
	
	for par_alunos in lista2: #validação para caso exista um par de notas iguais nas questoes (2 e 3)
		if(par_alunos in lista3): return True		

	return False


#caso_teste = [   [0,0,0],[0,1,1],[0,2,2],[1,1,1] ]
#resultado = caso_eh_valido(caso_teste)
#print(resultado)