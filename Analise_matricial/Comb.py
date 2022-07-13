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

case = [{'CP':[1.35,1]},{'SCesc':[1.5,0]},{'W90':[1.5,0]}]

def comb(db: list) -> list:
    """
    Função que retorna a lista de todas as combinações possíveis para um determinado patter
    
    """
    s = []
    r= 0
    permutacao = 2**len(db)
    temp = permutacao/2

    # variaveis para correção para mais de uma carga variavel
    carr_variaveis = [] #lista dos carregamento variaives com seu nome e coeficiente de ponderação de esforço para esforço secundário
    varr = 0
    add = 0
    temp_dois = []
    e= 0
  
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
                        
                        if tipo in carr_variaveis:
                            if varr == 1:

                            else:
                                varr = 1
                            pass
                        else:
                        '''

                        s[vezes].append([tipo,coef])
                        r += 1
        r = 0     
        temp = int(temp/2)
    
    #definindo para caso de mais de um combinação variável

    for arranjo in s:
        for caso in arranjo:

            #contagem de quanto casos de carr variavel na combinação
            if caso[0] in carr_variaveis:
                add =+ 1
            else:
                pass

        if add > 1:
            for vezes in range(add-1):
                fant = arranjo.copy()
                for caso in fant:
                     if caso[0] in carr_variaveis:
                         e =+1

                         if add**vezes == e: #resolver isso aqui: uma relação entre vezes ou add com e para que garanta que sempre oule de número em número
                            
                            for tipo in carr_variaveis:
                                for carr_ in tipo:
                                    if carr_[0] == caso[0]:
                                        multi = carr_[1]
                                        break
            

                            caso[1] = caso[1]*multi

                         else:
                            pass

                temp_dois.append(fant.copy())

                         



                # é preciso clonar o caso e fazer a devida correção
                

        temp_dois.append(arranjo)



                
        


    return s



print(comb(case))