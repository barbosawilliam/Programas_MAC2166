"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :
  NUSP :
  Turma:
  Prof.:

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
"""

# recebe uma lista x e devolve a média dos valores de x.
def media(x):
	media = 0
	for valor in x:
		media += valor
	media = media / len(x)
	return media

# recebe duas listas x e y e devolve a covariância entre x e y. Você deve usar a função media aqui.
def cov(x,y):
	mediaX = media(x)
	mediaY = media(y)
	covarianciaX_Y = 0
	for i in range(len(x)):
		covarianciaX_Y += (x[i] - mediaX) * (y[i] - mediaY)
	covarianciaX_Y = covarianciaX_Y / (len(x) - 1)

	return covarianciaX_Y

# recebe uma lista x e devolve o desvio padrão de x. Você deve usar a função media aqui.
def desvpad(x):
	mediaX = media(x)
	conta = 0
	for xi in x:
		conta += (xi - mediaX) ** 2
	conta = conta / (len(x) - 1)
	conta = conta ** (1/2)
	#OBS: daria pra fazer também chamando a função cov e passando x duas vezes como parametro
	#Depois bastaria pegar a raiz quadrada do retorno.
	return conta


# recebe duas listas x e y e devolve o coeficiente de correlação de Pearson entre x e y.
# Você deve usar as funções cov e desvpad aqui.
def pearson(x,y):
	covarianciaX_Y = cov(x, y)
	desvioPadraoX = desvpad(x)
	desvioPadraoY = desvpad(y)
	correlacaoPearson = covarianciaX_Y / (desvioPadraoX * desvioPadraoY)

	return correlacaoPearson

# recebe uma lista x e devolve o fractional ranking de x.
# Para o cálculo do posto, utilize o algoritmo de ordenação por inserção visto em aula.
# O posto de cada valor v distinto no vetor X é a média de suas 
# posições (iniciando no 1) na lista ordenada.
# Exemplo: [1.0, 1.0, 2.0, 3.0, 3.0, 4.0, 5.0, 5.0, 5.0]  (deve estar ordenado)
# * 1.0 -> (1+2)/2 = 1.5
# * 2.0 -> 3
# * 3.0 -> (4+5)/2 = 4.5
# * 4.0 -> 6
# * 5.0 -> (7+8+9)/3 = 8.0
def posto(x): #tá, deu ruim, na vdd deu bom, calculei o posto de forma certa
#mas o posto aparece na ordem que os números originalmente aparecem na lista, não na forma ordenada da lista
#a forma ordenada é só pra calcular o posto de cada valor
#criar então uma lista de listas, que vai relacionar o valor com seu posto [[valor, posto], [valor, posto]]
#e pra cada valor dentro da lista original x, vamos ver qual é o seu posto e dar um append na lista posto
	y = x[:]
	ordenacao_insercao(y) #vou usar a lista y, que é a x ordenada, pra calcular o posto de cada número
	
	posto = []

	return posto

# recebe duas listas x e y de devolve o coeficiente de correlação de Spearman entre x e y.
# Você deve usar a função Pearson aqui.
def spearman(x, y):
	postoX = posto(x)
	postoY = posto(y)

	correlacaoSpearman = pearson(postoX, postoY)
	return correlacaoSpearman


def matriz_covariancia(nome_arquivo):
	arquivo = open(nome_arquivo, "r")
	cabecalho = arquivo.readline()
	conteudo = []
	for linha in arquivo:
		conteudo.append(linha.strip().split(";"))
	arquivo.close()

	matriz = []
	for i in range(len(conteudo[0])):
		linhaDaMatriz = []
		listaI = devolve_coluna(conteudo, i)
		for j in range(len(conteudo[0])):
			listaJ = devolve_coluna(conteudo, j)
			linhaDaMatriz.append(cov(listaI, listaJ))
		matriz.append(linhaDaMatriz)

	return matriz

# -----------------------------------------------------
# funções auxiliares prontas - Não devem ser alteradas
# -----------------------------------------------------
def devolve_coluna(matriz, coluna):
	lista = []

	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if (j == coluna):
				lista.append(int(matriz[i][j]))

	return lista

def ordenacao_insercao(seq):
	n = len(seq)
	for i in range(0,n-1):
		# Insere seq[i+1] em seq[0],...,seq[i].
		x = seq[i+1]
		j = i
		while j >= 0 and seq[j] > x:
			seq[j+1] = seq[j]
			j -= 1
		seq[j+1] = x

def imprime_lista(L):
    for elem in L:
        print("%.4f"%elem,end=" ")
    print()

def imprime_matriz(M):
    m = len(M)
    n = len(M[0])
    for i in range(m):
        for j in range(n):
            print("%14.4f"%(M[i][j]), end=" ")
        print()

# ------------------------------------------
# função principal - Não deve ser alterada
# ------------------------------------------
def main():

    modo = int(input("Digite modo do programa: "))
    if modo == 1:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        print("media: %.4f"%(media(X)))
    elif modo == 2:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        print("desvpad: %.4f"%(desvpad(X)))
    elif modo == 3:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        Y = []
        for i in range(n):
            Y.append(float(input("Digite y%d: "%(i+1))))
        print("cov: %.4f"%(cov(X,Y)))
    elif modo == 4:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        Y = []
        for i in range(n):
            Y.append(float(input("Digite y%d: "%(i+1))))
        print("pearson: %.4f"%(pearson(X,Y)))
    elif modo == 5:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        P = posto(X)
        print("posto: ",end="")
        imprime_lista(P)
    elif modo == 6:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        Y = []
        for i in range(n):
            Y.append(float(input("Digite y%d: "%(i+1))))
        print("spearman: %.4f"%(spearman(X,Y)))
    elif modo == 7:
        nome_arquivo = input("Digite o nome do arquivo: ")
        M = matriz_covariancia(nome_arquivo)
        imprime_matriz(M)

	
main()
