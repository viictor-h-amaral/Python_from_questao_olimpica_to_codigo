import algoritmoCombinacoes
import copy

def TomarDuasADuas(lista):
	return algoritmoCombinacoes.Combinar(2, lista)

def CasoEhValido (listaComOCaso): #retorna false caso encontre falha ou true se der boa	

	todasNotasQuestoes1 = []
	todasNotasQuestoes2 = []
	todasNotasQuestoes3 = []
	
	for prova in listaComOCaso:
		try:
			todasNotasQuestoes1.append( prova[0] ) #apenas notas questões 1
			todasNotasQuestoes2.append( prova[1] ) #apenas notas questões 2
			todasNotasQuestoes3.append( prova[2] ) #apenas notas questões 3
		except:
			print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
			print(listaComOCaso)
			print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	
	indexQuestoes1SeparadasPorNota = SepararQuestoesPorNota(todasNotasQuestoes1) #ex.: [ [1,4,5] , [2,3] , [0] ]
	indexQuestoes2SeparadasPorNota = SepararQuestoesPorNota(todasNotasQuestoes2)
	indexQuestoes3SeparadasPorNota = SepararQuestoesPorNota(todasNotasQuestoes3)
	
	#faz pares de indexes em que a nota na questao eh igual


	#Q1

	paresIndexesQuestao1ComNota1 = TomarDuasADuas(indexQuestoes1SeparadasPorNota[1])
	paresIndexesQuestao1ComNota0 = TomarDuasADuas(indexQuestoes1SeparadasPorNota[0])
	
	paresIndexesQuestao1ComNota2 = TomarDuasADuas(indexQuestoes1SeparadasPorNota[2])
	
	paresAlunosQuestao1NotasIguais = []
	paresAlunosQuestao1NotasIguais.extend(paresIndexesQuestao1ComNota0)
	paresAlunosQuestao1NotasIguais.extend(paresIndexesQuestao1ComNota1)
	paresAlunosQuestao1NotasIguais.extend(paresIndexesQuestao1ComNota2)

	#Q2
	paresIndexesQuestao2ComNota0 = TomarDuasADuas(indexQuestoes2SeparadasPorNota[0])
	paresIndexesQuestao2ComNota1 = TomarDuasADuas(indexQuestoes2SeparadasPorNota[1])
	paresIndexesQuestao2ComNota2 = TomarDuasADuas(indexQuestoes2SeparadasPorNota[2])

	
	paresAlunosQuestao2NotasIguais = []
	paresAlunosQuestao2NotasIguais.extend(paresIndexesQuestao2ComNota0)
	paresAlunosQuestao2NotasIguais.extend(paresIndexesQuestao2ComNota1)
	paresAlunosQuestao2NotasIguais.extend(paresIndexesQuestao2ComNota2)

	#Q3
	paresIndexesQuestao3ComNota0 = TomarDuasADuas(indexQuestoes3SeparadasPorNota[0])
	paresIndexesQuestao3ComNota1 = TomarDuasADuas(indexQuestoes3SeparadasPorNota[1])
	paresIndexesQuestao3ComNota2 = TomarDuasADuas(indexQuestoes3SeparadasPorNota[2])
	
	paresAlunosQuestao3NotasIguais = []
	paresAlunosQuestao3NotasIguais.extend(paresIndexesQuestao3ComNota0)
	paresAlunosQuestao3NotasIguais.extend(paresIndexesQuestao3ComNota1)
	paresAlunosQuestao3NotasIguais.extend(paresIndexesQuestao3ComNota2)

	return not ExistemDuasProvasComDuasMesmasQuestoesComMesmaNota(
		paresAlunosQuestao1NotasIguais,
		paresAlunosQuestao2NotasIguais,
		paresAlunosQuestao3NotasIguais)
	
	
def SepararQuestoesPorNota(questoes):

	notas0 = []
	notas1 = []
	notas2 = []

	for indexQuestao in range( len(questoes) ):
		
		match questoes[indexQuestao]:
			case 0:
				notas0.append(indexQuestao)
			case 1:
				notas1.append(indexQuestao)
			case 2:
				notas2.append(indexQuestao)
	
	indexesSeparadosPorNota = [notas0, notas1, notas2]
	
	return indexesSeparadosPorNota
	
def ExistemDuasProvasComDuasMesmasQuestoesComMesmaNota(lista1, lista2, lista3):
	for parAlunos in lista1: #validação para caso exista um par de notas iguais nas questoes (1 e 2) e (1 e 3)
		if(parAlunos in lista2 or parAlunos in lista3): return True
	
	for parAlunos in lista2: #validação para caso exista um par de notas iguais nas questoes (2 e 3)
		if(parAlunos in lista3): return True		

	return False


#casoTeste = [   [0,0,0],[0,1,1],[0,2,2],[1,1,1] ]
#resultado = CasoEhValido(casoTeste)
#print(resultado)