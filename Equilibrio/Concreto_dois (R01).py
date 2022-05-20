import sympy as sp
import pandas as pd
class Momento():

    def __init__(self,codigo,formula_tramo_A,formula_tramo_B,formula_tramo_C,valores_constantes) -> None:

        import sympy as sp


        self.codigo = codigo
        try:
            self.formula_tramo_A = sp.sympify(formula_tramo_A) # um string q se resolve com sp.sympify
            self.tramo_A = self.Tramo(valores_constantes,self.formula_tramo_A)
        except:
            pass
        try:
            self.formula_tramo_B = sp.sympify(formula_tramo_B) # um string q se resolve com sp.sympify
            self.tramo_B = self.Tramo(valores_constantes,self.formula_tramo_B)
        except:
            pass
        try:
            self.formula_tramo_C = sp.sympify(formula_tramo_C) # um string q se resolve com sp.sympify
            self.tramo_C = self.Tramo(valores_constantes,self.formula_tramo_B)
        except:
            pass
    
    class Tramo:

        def __init__(self,valores_constantes,formula):

            import sympy as sp

            simbolos = ['b','w','L','a','F','M']
            Ma,b,w,L,a,x,F,M = sp.symbols('Ma,b,w,L,a,x,F,M,')
            for valor, nome in list(zip(valores_constantes,simbolos)):
                formula = formula.subs(nome,valor)
            self.base = formula
            temp = sp.Eq(formula,Ma) #vira uma equação ----> pode ser manipulada
            temp = sp.solve(temp,x)
            self.formula_certa = temp #fica certinho para ser usada

        def posicao(self,valor): #certo
            #a função volta o valor de x referente a um momento na curva
            import sympy as sp
            equacoes = []
            saida = []
            Ma,b,w,L,a,x,F,M = sp.symbols('Ma,b,w,L,a,x,F,M')
            for equacao in self.formula_certa:
                funcao = sp.lambdify(Ma,equacao,'numpy')
                saida.append(funcao(valor))
                equacoes.append(equacao)
            return saida,equacoes
    
        def max(self):#certo
            import sympy as sp
            Ma,b,w,L,a,x,F,M = sp.symbols('Ma,b,w,L,a,x,F,M')
            #fazer a expressão derivada
            formula_derivada = sp.Eq(self.base,0)
            formula_derivada = sp.diff(self.base) #expressao
            #teorema de Roll
            xs = sp.solve(formula_derivada,x) 
            saida = sp.lambdify(x,self.base)
            return saida(xs[0])

        def raizes(self):#certo
            import sympy as sp
            saida = []
            Ma,b,w,L,a,x,F,M = sp.symbols('Ma,b,w,L,a,x,F,M')
            for equacao in self.formula_certa:
                #montar a equação
                x = sp.lambdify(Ma,equacao)
                saida.append(x(0))
            return saida

#..................................valores constrantes = ['b','w','L','a','F','M']
m = Momento('BA1-w',"-1.31625*x**2+1053*x-157950",'nao tem', 'nao tem',[0,3,8,0,0,0])

#a função volta o valor de x referente a um momento na curva


#função posição tem um erro inerente ao calculo (mto preciso) ----> vai ter um erro na margem de 10% (vou dar um jeito)
#função raizes está perfeita --> conferido
#função max está perfeita ---> conferida

print(m.tramo_A.base)
print(m.tramo_A.max())


dados = []
x = []
saida = []
barras = 7
saida_dois = []
momento_unico = 6995.098

barras = barras + 1
for i in range(barras):
    dados.append(momento_unico*i)
x = []
saida = []


for dado in dados:
    valores, funcao =m.tramo_A.posicao(dado)
    [saida_dois.append(item) for item in funcao]
    for valor in valores:
        saida.append(dado)
        x.append(valor)



df = pd.DataFrame({'Momento':saida,'x':x,'formula':saida_dois})   
writer = pd.ExcelWriter('saida.xlsx')
df.to_excel(writer)
writer.save()
