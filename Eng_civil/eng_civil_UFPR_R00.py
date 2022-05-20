#Seria criar uma biblioteca minha para resolução de problemas da eng_civil


class Estruturas():

    def __init__(self) -> None:
        pass

class Concreto:
    #parametros...
    def __init__(self,fck,fyd,cnom,dmax):
        from numpy import log
        
        #entrada
        self.fck = fck
        self.fyd = fyd
        self.cnom = cnom
        self.dmax = dmax 

        #Resistência ...
        if fck>=5.5:
            self.fctm = (0.3*((fck*10)**2)**(1/3))/10
            self.zeta = 0.8
            self.a = 0.85
        elif fck<5.5 and fck>=1.5:
            self.fctm = 2.12*log(1+fck*1.1)/10
            self.zeta = 0.8-(self.fck-50)/400
            self.a = 0.85*(1-(self.fck*10-50)/200)

        #Resistencia
        self.fctmsup = 1,3*self.fctm
        self.fctkinf = 0.7*self.fctm

class Madeira:

    def __init__(self) -> None:
        pass
    
class Metalicas:
    
    def __init__(self,fyd,fub) -> None:

        self.fyd = fyd
        self.fub = fub   

class Geometria:

    def __init__(self) -> None:
        pass

    def momento_de_inercia():
        pass

    def momento_estatico_de_area():
        pass

class Analise:

    def __init__(self):
        pass

    def matricial():
        pass

    def cross():
        pass

    def tres_momentos():
        pass

    def euler_bernoulli(): #verificação de flechas 
        pass

    def involtaria_de_columb():
        pass
    
class Efeitos_de_Segunda_Ordem():
    pass

class Combinacoes():
    pass
