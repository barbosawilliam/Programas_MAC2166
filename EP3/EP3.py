import math
######################################################################
#Definição de funções auxiliares
def valorMaximo (lista):
  valorMaximo = lista[0]
  for valor in lista:
    if valor > valorMaximo:
      valorMaximo = valor
  return valorMaximo


######################################################################
#Funções principais
def SIR (N, Beta, Gama, Tmax): #Done
    s0 = N - 1
    i0 = 1
    r0 = 0

    #Cálculo das listas
    S = [s0]
    I = [i0]
    R = [r0]

    for t in range(Tmax-1):
      
      proximoS = S[t] - (Beta * S[t] * I[t])/N
      proximoI = I[t] + (Beta * S[t] * I[t])/N - Gama * I[t]
      proximoR = R[t] + Gama * I[t]
      
      S.append(proximoS)
      I.append(proximoI)
      R.append(proximoR)

    return S,I,R


def critic_SIR (N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta): #Done
    beta_auxiliar = Beta_MIN
    lista_Betas = []
    i = 0
    while (beta_auxiliar < Beta_MAX):
      beta_auxiliar = Beta_MIN + i * Beta_delta
      lista_Betas.append(beta_auxiliar)
      i += 1
    
    lista_Is = []
    for beta in lista_Betas:
      S,I,R = SIR(N, beta, Gama, Tmax)
      lista_Is.append(valorMaximo(I))

    return lista_Is


def gera_grafico_simples(L): #Done.
    X_MAX = len(L) - 1
    X_MIN = 0
    Y_MIN = 0
    #Pegando o teto do maior número da lista L
    Y_MAX = valorMaximo(L)
    if round(Y_MAX) != Y_MAX: #significa que Y_MAX não é um número inteiro
      Y_MAX = int(Y_MAX) + 1


    #Montando uma matriz com (m x n) zeros
    m = Y_MAX - Y_MIN + 1 #Número de linhas
    n = X_MAX - X_MIN + 1 #Ou n = len(L)
    matriz = []
    for i in range(m):
      linha = []
      for j in range(n):
        linha.append(0)
      matriz.append(linha)

    #Desenhando o gráfico
    for k in range(len(L)):
      j = k
      i = round(Y_MAX - L[k])
      matriz[i][j] = 255

    #Exportando para um arquivo externo .pgm
    arquivo = open("graf_simples.pgm", 'w')
    arquivo.write("P2\n")
    arquivo.write(str(n) + ' ' + str(m) + '\n')
    arquivo.write("255\n")
    for i in range(m):
      str_linha = ''
      for j in range(n):
        str_linha += ' ' + str(matriz[i][j])
      str_linha += '\n'
      arquivo.write(str_linha)
    arquivo.close()

    return matriz


def gera_grafico_composto(S, I, R): #Done.
    X_MIN = 0
    X_MAX = len(S) - 1
    Y_MIN = 0

    Y_MAX = valorMaximo(S)
    if (Y_MAX < valorMaximo(I)):
      Y_MAX = valorMaximo(I)
    if (Y_MAX < valorMaximo(R)):
      Y_MAX = valorMaximo(R)
    if (round(Y_MAX) != Y_MAX):
      Y_MAX = int(Y_MAX) + 1

    #Montando uma matriz com (m x 3n) zeros
    m = Y_MAX - Y_MIN + 1 #Número de linhas
    n = X_MAX - X_MIN + 1 #Ou n = len(L). Número de colunas.
    matriz = []
    for i in range(m):
      linha = []
      for j in range(3*n):
        linha.append(0)
      matriz.append(linha)

    #Desenhando o gráfico
    for k in range(len(S)):
      j = 3*k
      iS = round(Y_MAX - S[k])
      iI = round(Y_MAX - I[k])
      iR = round(Y_MAX - R[k])
      
      matriz[iS][j] = 255
      matriz[iI][j+1] = 255
      matriz[iR][j+2] = 255

    #Exportando para um arquivo externo .ppm
    arquivo = open('graf_composto.ppm', 'w')
    arquivo.write("P3\n")
    arquivo.write(str(n) + ' ' + str(m) + '\n')
    arquivo.write("255\n")
    for i in range(m):
      str_linha = ''
      for j in range(3*n):
        str_linha += ' ' + str(matriz[i][j])
      str_linha += '\n'
      arquivo.write(str_linha)
    arquivo.close()

    return matriz


def leitura_de_valores(nome_de_arquivo): #Done.
    arquivo = open(nome_de_arquivo, 'r')
    N = float(arquivo.readline().split('\n')[0])
    if int(N) == N:
      N = int(N)
    Gama = float(arquivo.readline().split('\n')[0])
    if int(Gama) == Gama:
      Gama = int(Gama)
    Tmax = float(arquivo.readline().split('\n')[0])
    if int(Tmax) == Tmax:
      Tmax = int(Tmax)
    Beta_MIN = float(arquivo.readline().split('\n')[0])
    if int(Beta_MIN) == Beta_MIN:
      Beta_MIN = int(Beta_MIN)
    Beta_MAX = float(arquivo.readline().split('\n')[0])
    if int(Beta_MAX) == Beta_MAX:
      Beta_MAX = int(Beta_MAX)
    Beta_delta = float(arquivo.readline().split('\n')[0])
    if int(Beta_delta) == Beta_delta:
      Beta_delta = int(Beta_delta)
    arquivo.close()

    return N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta



# Opções
# 1: Calcular 'SIR' e imprimir os vetores S, I e R - leitura de teclado
# 2: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de teclado
# 3: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de arquivo
# 4: Calcular 'critic_SIR', testar matriz devolvida por 'gera_grafico_simples' - leitura de teclado
# 5: Calcular 'critic_SIR', testar arquivo PGM no disco por 'gera_grafico_simples' - leitura de teclado
# 6: Calcular 'SIR', testar matriz devolvida por 'gera_grafico_composto' - leitura de teclado
# 7: Calcular 'SIR', testar arquivo PPM no disco por 'gera_grafico_composto' - leitura de teclado

#Não altere as funções abaixo:
def imprimeLista(L) : 
    for i in range(len(L)):
      print("%.4f " % L[i], end=""); # usar apenas 4 digitos apos ponto
    print()

def main():
    #cSIR = critic_SIR(10, 0.1, 10, 0.05, 0.50, 0.05)
    #cSIR = critic_SIR(100, 0.2, 100, 0.05, 0.90, 0.05)
    #print(gera_grafico_simples(cSIR))

    #S,I,R = SIR(100, 0.5, 0.2, 100)
    #print(gera_grafico_composto(S, I, R))

    Opt = int(input("Digite modo do programa: "))
    if (Opt == 1): # saida - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        print("S = ", end="")
        imprimeLista(S) 
        print("I = ", end="")
        imprimeLista(I)
        print("R = ", end="")
        imprimeLista(R)
    elif (Opt == 2): # saida - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 3): # saida - critic_SIR; entrada - arquivo
        Dados = input("Digite nome do arquivo: "); 
        N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leitura_de_valores(Dados)
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 4): # grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        print(M_grafico)
    elif (Opt == 5): # PGM - grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: ")) 
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        g = open("graf_simples.pgm", "r")
        print(g.read())
        g.close()
    elif (Opt == 6): # grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        print(M_grafico)
    elif (Opt == 7): # PPM - grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: ")) 
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: ")) 
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        g = open("graf_composto.ppm", "r")
        print(g.read())
        g.close()
main()
