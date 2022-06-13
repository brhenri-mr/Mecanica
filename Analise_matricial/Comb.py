import numpy as np

#Combinações segundo a nbr8681

fact = {
  'Permamente':{
  'Peso próprio de estruturas metálicas':1.25,
  'Peso próprio de estruturas pré-moldadas':1.30,
  'Peso próprio de estruturas moldadas no local':1.35,
  'Elementos construtivos industrializados)':1.35,
  'Elementos construtivos industrializados com adições in loco':1.40,
  'Elementos construtivos em geral e equipamentos)':1.5
  },
  'Variavel':{
          'Acao do vento':1.4,
          'Efeito de temperatura':1.2,
          'Ações truncadas':1.2,
          'Ações variáveis em geral':1.5
  
    }}

case = [{'CP':[1.35,1]},{'SC':[1.5,0]},{'W':[1.5,0]}]


def comb(db):
  
    s = []
    r= 0
    permutacao = 2**len(db)
    temp = permutacao/2
  
    # definir os 2 primeiros casos

    for caso in db: #abri o vector principal
        for tipo,carr in caso.items(): #abri o dicionario
            for coef in carr: #abri o vetor dos coeficientes
                for vezes in range(int(permutacao/2)): #quantidade de vezes que vou colocar um mesmo vetor
                    if len(s) < int(permutacao):
                        s.append([[tipo,coef]])
                    else:
                        if db[-1] == caso: #ultimo caso
                            if r<int(permutacao/2): #primeira entrada - par
                                vezes = vezes * 2
                            else: #segundara entrada - impar
                                vezes = vezes * 2 +1 if vezes != 0 else 1
                        else: # caso intermediario
                            if r<int(permutacao/2):
                                cri = (r//temp)*temp
                            else:
                                cri = temp +((r-int(permutacao/2))//temp)*temp
                            vezes = vezes + cri
                            '''
                            if r>int(permutacao/2):
                                vezes = vezes + int(permutacao/2)
                                vezes  = vezes + 
                            else:
                                vezes = vezes + (r//temp)*temp
                            '''
                        s[vezes].append([tipo,coef])
                        r += 1
        r = 0     
        temp = int(temp/2)
    return s
        