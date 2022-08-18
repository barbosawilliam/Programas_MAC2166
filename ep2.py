# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente  neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================
def polinomioComRaiz(p,b): #Done.
    """Devolve True se b é raiz do polinômio representado pela lista p, 
       ou False no caso contrário.
       
       p -- a lista dos coeficientes do polinômio       
       b -- o número a ser testado como raiz
    """
  
    grauPolinomio = len(p) - 1
    resultado = 0
    for i in range(grauPolinomio, -1, -1):
      resultado += p[i]*(b**i)

    if (resultado == 0):
      return True
    else:
      return False
# ======================================================================

def polinomioQuociente(p,b): #Done.
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(x-b), onde p(x) é o polinômio cujos coeficientes estão na 
       lista p e b é uma raiz de p(x). 
       
       p -- a lista dos coeficientes do polinômio a ser dividido      
       b -- a raiz a ser usada como divisor
      
      p(x) = 1x^2 - 3.5x + 3  = [3, -3.5, 1]

      1.5 | 1  -3.5  3
      -----------------
          | 1   -2 | 0   ->   q(x) = 1x^2 - 2 = [-2, 1]
    """
    
    grauPolinomio = len(p) - 1
    briotRuffini = []
    auxiliar = 0
    for i in range(grauPolinomio, 0, -1):
      if (i == grauPolinomio):
        briotRuffini.append(p[i]) 

      else:
        proximo = briotRuffini[auxiliar] * b + p[i]  
        briotRuffini.append(proximo)
        auxiliar += 1
    
    q = []
    for i in range(len(briotRuffini) - 1, -1, -1):
      q.append(int(briotRuffini[i]))

    return q

# ======================================================================
def listaCanonicaDeRaizes(p): #Done.
    """Devolve a lista canônica de raízes inteiras do polinômio 
       representado pela lista p.
       p -- a lista dos coeficientes do polinômios
    """
    listaRaizes = []
    q = p[:]

    #Tirando todos os 0's que são raizes do polinômio
    termoIndependente = q[0]
    while (termoIndependente == 0):
      listaRaizes.append(0)
      q = polinomioQuociente(q, 0)
      termoIndependente = q[0]

    #Agora tenho que pegar todos os divisores do termo independente. Se houver raízes inteiras, estarão nessa lista.
    listaDivisores = []
    possivelDivisor = 1
    if (termoIndependente < 1):
        termoIndependente = -termoIndependente
    while (possivelDivisor <= termoIndependente):
      if (termoIndependente % possivelDivisor == 0):
        listaDivisores.append(-possivelDivisor)
        listaDivisores.append(possivelDivisor)
      possivelDivisor += 1  

    #Agora precisa testar quais elementos da listaDivisores são de fato raízes do polinômio q(x), que é quociente de p(x)
    i = 0 
    while (i < len(listaDivisores)):
      if (polinomioComRaiz(q, listaDivisores[i])):
        listaRaizes.append(listaDivisores[i])
        q = polinomioQuociente(q, listaDivisores[i])
      else:
        i += 1

    return listaRaizes 

# ======================================================================
def polinomioQuocienteRacional(p,b,a): #Done.
    """Devolve a lista que representa o polinômio quociente da divisão
       p(x)/(ax-b) e o resto dessa divisão, onde p(x) é o polinômio 
       cujos coeficientes estão na lista p e b/a é uma raiz de p(x). 

       p -- a lista dos coeficientes do polinômio a ser dividido
       b -- numerador da raiz a ser usada como divisor
       a -- denominador da raiz a ser usada como divisor
    """
    
    grauPolinomio = len(p) - 1

    if (grauPolinomio < 1):
      return None, -1

    raiz = b/a
    briotRuffini = []
    resto = 0
    auxiliar = 0

    #Pegando o quociente a*q(x)
    for i in range(grauPolinomio, 0, -1):
      if (i == grauPolinomio):
        briotRuffini.append(p[i])
      else:
        proximo = briotRuffini[auxiliar]*raiz + p[i]
        briotRuffini.append(proximo)
        auxiliar += 1

    #Pegando o resto:
    resto = briotRuffini[auxiliar]*raiz + p[0]

    #Pegando o polinômio quoeficiente (q(x)) do briotRuffini, basta inverter e dividir por a.
    q = []
    for i in range(len(briotRuffini) - 1, -1, -1):
      q.append(briotRuffini[i]/a)

    return q, resto

# ======================================================================
def listaRaizesRacionais(p): #Done.
    """Devolve a lista canônica de raízes racionais do polinômio 
       representado pela lista p.
       
       p -- a lista dos coeficientes do polinômio
    """
    
    listaRaizes = []
    q = p[:]

    #Tirando os 0's do polinômio
    termoIndependente = q[0]
    while (termoIndependente == 0):
      qlinha, resto = polinomioQuocienteRacional(q, 0, 1)
      if (resto == 0):
        listaRaizes.append(0)
        q = qlinha[:]
        termoIndependente = q[0]
    
    p0 = q[0] #b é um divisor de p0
    pn = q[len(q)-1] #a é um divisor de pn
   
    #Pegando todos os valores possíveis a 'b'
    candidatos_bs = []
    possivelDivisor = 1
    if (p0 < 0): #Para ver quais são os divisores, basta olhar os valores absolutos
      p0 = -p0
    while (possivelDivisor <= p0):
      if (p0 % possivelDivisor == 0):
        candidatos_bs.append(-possivelDivisor)
        candidatos_bs.append(possivelDivisor)  
      possivelDivisor += 1
    #print("bs: ", candidatos_bs)

    #Pegando todos os valores possíveis a 'a'
    candidatos_as = []
    possivelDivisor = 1
    while (possivelDivisor <= pn):
      if (pn % possivelDivisor == 0):
        candidatos_as.append(possivelDivisor)
      possivelDivisor += 1
    #print("as: ", candidatos_as)

    #Agora testo se as combinações dos candidatos a 'b' e 'a' são de fato raizes do polinômio
    i = 0
    while (i < len(candidatos_as)):
      a = candidatos_as[i]
      j = 0
      while (j < len(candidatos_bs)):
        b = candidatos_bs[j]
        #print("q: ", q)
        #print("b: ", b)
        #print("a: ", a)
        #print("b/a: ", b/a)
        qlinha, resto = polinomioQuocienteRacional(q, b, a)
        #print("qlinha: ", qlinha)
        #print("resto: ", resto)
        if (resto == 0.0):
          q = qlinha[:]
          listaRaizes.append(b/a)
        else:
          j += 1
      i += 1

    return listaRaizes

# ======================================================================
def racionalToString(pn,r): #Done.
    """Devolve uma string que apresenta a raiz r do polinômio do qual pn 
       é o coeficiente de maior grau como:
        - um inteiro, caso r seja inteiro
        - na forma b/a, com b e a primos entre si e a > 0, caso contrário

       pn -- coeficiente de maior grau do polinômio
       r -- uma raiz do polinômio
    """
    
    if (round(r) == r):
      return str(int(r))
    
    numerador = round(pn*r)
    maximoDivisorComum = acheMDC(numerador, pn)
    #print(maximoDivisorComum)
    #print(numerador, numerador/maximoDivisorComum)
    #print(pn)
    strNumerador = str(int(numerador/maximoDivisorComum))
    strDenominador = str(int(pn/maximoDivisorComum))
    return strNumerador + '/' + strDenominador

# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================


# ======================================================================
# FUNÇÕES ADICIONAIS
# Implemente neste bloco as funções adicionais às obrigatórias do EP2.
# Duas funções desse tipo (a polinomioToString e a sig) foram 
# fornecidas no próprio enunciado do EP.
# ======================================================================
def polinomioToString(p):
    """Devolve uma string que representa o polinômio em um formato 
       legível para humanos.
       
       p -- a lista dos coeficientes do polinômio
    """
    n = len(p)-1
    s = ""
    for m in range(n-1):
        if p[n-m] != 0:
            s = "%s%s%dx^%d " % (s, sig(m,p[n-m]), p[n-m], n-m)
    if p[1] != 0:
        s = "%s%s%dx " % (s, sig(n-1,p[1]), p[1])
    if p[0] != 0:
        s = "%s%s%d" % (s, sig(n,p[0]), p[0])
    return s

# ======================================================================
def sig(nTermAnte,coef):
    """Devolve '+' se coef não é negativo e existe termo anterior ao
       termo dele no polinômio. Devolve '' (string vazia) no caso
       contrário. Usado para determinar se o '+' deve aparecer antes
       de coef na string que representa o polinômio.
       
       nTermAnte -- expoente de x no termo anterior ao termo do coef
       coef -- coeficiente de um termo do polinômio 
    """
    if nTermAnte > 0 and coef >= 0:
        return "+"
    else:
        return ""

def acheMDC(numero1, numero2): #Criei essa função
  listaDivisoresNum1 = listaDeDivisores(numero1)
  listaDivisoresNum2 = listaDeDivisores(numero2)
  MDC = 1
  for i in range(len(listaDivisoresNum1) - 1, -1, -1):
    for j in range(len(listaDivisoresNum2) - 1, -1, -1):
      if (listaDivisoresNum1[i] == listaDivisoresNum2[j]):
        if (listaDivisoresNum1[i] > MDC):
          MDC = listaDivisoresNum1[i]

  return MDC

def listaDeDivisores(numero): #Criei essa função
  listaDivisores = []
  possivelDivisor = 1
  if (numero < 1):
    numero = -numero
  while (possivelDivisor <= numero):
    if (numero % possivelDivisor == 0):
      listaDivisores.append(possivelDivisor)
    possivelDivisor += 1  

  return listaDivisores


# ======================================================================
# FIM DO BLOCO DE FUNÇÕES ADICIONAIS
# ======================================================================


# ======================================================================
# FUNÇÃO MAIN 
# Escreva dentro da função main() o código que quiser para testar suas 
# demais funções.
# Somente dentro da função main() você pode usar as funções print e
# input.     
# O código da função main() NÃO será avaliado.
# ======================================================================
def main():

  #p = [20, 0]
  
  #print(polinomioComRaiz(p, b))
  #q = polinomioQuociente(p, b)
  #print(q)
  #raizes = listaCanonicaDeRaizes(p)
  #print(raizes)
  #q, resto = polinomioQuocienteRacional(p, b, a)
  #print(q)
  #print(resto)
  #lista = listaRaizesRacionais(p)
  #print(lista)
  #num = racionalToString(400, -0.6)
  #print(num)
  #print(type(num))

    n = int(input("Digite o grau: "))
    
    # Lê os coeficientes do polinômio
    p = []
    for i in range(n+1):
        p.append(float(input("Digite p["+str(i)+"]: ")))
        i += 1
        
    # Obtém a lista de raízes
    if p[n] == 1:
        raizes = listaCanonicaDeRaizes(p)
        print( 'A lista canonica das raizes inteiras de p(x) =',
               polinomioToString(p), 'eh:')
    else:
        raizes = listaRaizesRacionais(p)
        print( 'A lista canonica das raizes racionais de p(x) =',
               polinomioToString(p), 'eh:')
    
    # Imprime a lista canônica de raízes
    for raiz in raizes:
        s = racionalToString(p[n],raiz)
        print(s, end=" ")
        
    print()      

# ======================================================================
# FIM DA FUNÇÃO MAIN 
# ======================================================================


# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN 
# ======================================================================