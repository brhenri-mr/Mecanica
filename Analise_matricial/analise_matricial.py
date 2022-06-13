import numpy as np

def caso_carregado(bs,critrio):
  """
  bs = recebe uma base de dados com as combicoes
  criterio = combinacao escolhida para a analise 
  """
  def combinacoes(funcao):
    def esforcos_reais(*args,**kwargs):
      cri = int(cri[-1])
      caso = bs[cri-1]
      for comb in bs: #abre a base de dados
        for classe in comb: #abre a comb
          if args[-1] == classe[0]:
            args[0] == classe[1]*args[0]
      return funcao(args)
    return esforcos_reais
  return combinacoes

def rigidez_local(l, rigidez, par):
  # l = largura do vão do elemento
  #rigidez = produto entre E e 
  # par = parametro de uso da rigidez
  #gera a matriz local do elemento
	ke = np.array([[12, 6 * l, -12, 6 * l],
	               [6 * l, 4 * l**2, -6 * l, 2 * l**2],
	               [-12, -6 * l, 12, -6 * l],
	               [6 * l, 2 * l**2, -6 * l, 4 * l**2]])

	if par == "s":
		return (rigidez / pow(l, 3)) * ke
	else:
		return ke

def rigidez_global(*args):
	incremento = 0
	dim = len(args)
	z = np.zeros((4 + 2 * (dim - 1), 4 + 2 * (dim - 1)), dtype=float)
	for item in args:
		for linha in range(4):
			for coluna in range(4):

				z[linha + 2 * incremento][coluna + 2 * incremento] = round(
				    item[linha][coluna] +
				    z[linha + 2 * incremento][coluna + 2 * incremento], 3)

		incremento = 1 + incremento
	return z

def ordenador(k, d):
	global local
	local = []
	ord = []
	final = []
	for indice, item in enumerate(d):
		if item != 0:
			local.append(indice)
	for item in local:

		ord.append(k[item])

	for i in range(len(d)):
		if i in local:
			pass
		else:
			ord.append(k[i])
	ord = np.array(ord).T

	for item in local:

		final.append(ord[item])

	for i in range(len(d)):
		if i in local:
			pass
		else:
			final.append(ord[i])

	return np.array(final).T

def deslocamento(k, ford):
	criterio = len(ford)
	matriz = np.zeros((criterio, criterio), dtype=float)
	for i in range(criterio):
		for j in range(criterio):
			matriz[i][j] = k[i][j]
	vec = np.dot(np.array(ford), np.linalg.inv(matriz))
	return vec

@caso_carregado()
def vetor_local_forcas(carga,comprimento,tipo,grupo): 
  """
  Vetor dos carregamentos por engastamento perfeito no No. A funcao retorna o vetor local das forcas para o No
  Carga = carregamento atuante no No
  Comprimento = comprimento do tramo
  Tipo = Natureza do carregamento geometrica: distribuido, pontual, triangular, momento
    Distribuido = carregamento em um comprimento, necessario para dois valores [posicao inicial, posicao final]
  Grupo = Natureza do carrregamento quanto a origem: peso proprio, sobrecarga
  """
  if tipo == 'dist':
    v_um  = -carga*comprimento/2
    v_dois = v_um
    momento_um = -carga*(comprimento**2)/12
    momento_dois = -momento_um
    return [v_um,momento_um,v_dois,momento_dois]
  elif tipo =="pontual":
    a = comprimento[0]
    b = comprimento[1]
    if a == 0:
      return [carga,0,0,0]
    elif b == comprimento:
      return [0,carga,0,0]
    else:
      l = a + b
      v_um  = -carga*b**2*(3*a+b)/l**3
      v_dois = -carga*a**2*(a+3*b)/l**3
      momento_um = -carga*a*b**2/l**2
      momento_dois = carga*a*b**2/l**2
      return [v_um,momento_um,v_dois,momento_dois]
  elif tipo == 'momento':
    a = comprimento[0]
    b = comprimento[1]
    l = a + b
    v_um  = -6*carga*a*b/l**3
    v_dois = 6*carga*a*b/l**3
    momento_um = -carga*b*(2*a-b)/l**2
    momento_dois = -carga*a*(2*b-a)/l**2
    return [v_um,momento_um,v_dois,momento_dois]
  elif tipo == 'triangular':

    v_um  = -3*carga*comprimento/20
    v_dois = -7*carga*comprimento/20
    momento_um = -carga*comprimento**2/30
    momento_dois = carga*comprimento**2/30
    return [v_um,momento_um,v_dois,momento_dois]
    
def vetor_global_forcas(*args): #conferir
  r = []
  conjunto = np.array(list(args))
  for i in range(conjunto.shape[0]):
    for j in range(conjunto.shape[1]):
      if i == 0:
        r.append(conjunto[i][j])
      else:
        if j<=1:
          r[2+2*(i-1)+j]=r[2+2*(i-1)+j]+conjunto[i][j]
        else:
          r.append(conjunto[i][j])
  return r

def ordenar_forcas(forcas,des): 
  r = []
  for i in range(len(d)):
    if des[i] != 0:
      r.append(forcas[i])
  for i in range(len(d)):
    if des[i] == 0:
      r.append(forcas[i])
  return r

def reacoes(k,forcas,des): #conferir
  #Deslocamentos
  np.array(forcas)
  coef_d = len(d)-des.count(0)
  kll = k[:coef_d,:coef_d]
  forcas_d = np.array(forcas[0:coef_d])
  k_reacoes_inversa_d = np.linalg.inv(kll)
  desloc = forcas_d.dot(k_reacoes_inversa_d)
  #Reacao
  kpl = np.array(k[coef_d:,:coef_d])
  forcas_f = np.array(forcas[coef_d:])
  print()
  x = kpl.dot(desloc)
  r = x - forcas_f

  return r



#Rigidez local do elemento

ri = 10000
x = rigidez_local(6, ri, "s")
y = rigidez_local(8, ri, 's')
z = rigidez_local(5, ri, 's')


#Lembrar que o d é quando o deslocamento não é travado, ou seja, grau de indeterminação cinemática
#....[Vertical,momento]
d = [0,2,0,4,0,6,0,8]


#Rigidez global do elemento
w = rigidez_global(x, y,z)
k_ord = ordenador(w, d)

# Forcas = Engastamento perfeito/nodais equivalentes + reações + Forcas pontais
vetv1 = np.array(vetor_local_forcas(1.5,6,"dist"))
vetv2 = np.array(vetor_local_forcas(2,8,"dist"))
vetv3 = np.array(vetor_local_forcas(1,5,"dist"))
vetv4 = np.array(vetor_local_forcas(4,[2.5,2.5],"pontual"))
vetv3_1 = vetv3+vetv4

#Vetor de forcas global 
vetfglobal = vetor_global_forcas(vetv1,vetv2,vetv3_1)
vtord = ordenar_forcas(vetfglobal,d)


#Reacoes de apoio
r = reacoes(k_ord,vtord,d)
print(r)





