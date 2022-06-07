'''
-----------------------------------------------
Breno Henrique
06/06/22
-----------------------------------------------
Desenha vigas e suas condições de apoio
'''
import pandas as pd
import openpyxl

def apoio(sc,x,y,cri):
  import turtle
  #Propriedades da tartaruga
  turtle.screensize(800,800)
  tar = turtle.Turtle()
  tar.pensize(1)
  tar.hideturtle()
  tar.shape('turtle')
  tar.color('red')
  tar.penup()
  tar.setpos(x,y)
  tar.pendown()
  #tar.pos(x,y) == passa a posição 

  if cri in ["primeiro grau",'primeiro genero','movel']:
    #desenhando o triangulo
    tar.left(-60)
    tar.forward(100*sc)
    tar.left(-120)
    tar.back(25*sc)
    tar.forward(150*sc)
    tar.back(25*sc)
    tar.left(-120)
    tar.forward(100*sc)
    #desenhando o risco paralelo a base
    tar.left(-60) #deixar reto
    tar.penup()
    tar.setpos(x-150/2*sc,y-0.5*100*sc*(3)**0.5-18*sc)
    tar.pendown()
    tar.forward(150*sc)
    
  elif cri in ["segundo grau","segundo genero","segundo"]:
    #desenhando o triangulo
    tar.left(-60)
    tar.forward(100*sc)
    tar.left(-120)
    tar.back(25*sc)
    tar.forward(150*sc)
    tar.back(25*sc)
    tar.left(-120)
    tar.forward(100*sc)
    #desenhando o achurado
    tar.penup()
    new_x = x-100/2*sc
    tar.setpos(new_x,y-0.5*100*sc*(3)**0.5)
    tar.left(-60) #fica reto
    tar.left(-45)
    dist = 100*sc/3
    for i in range(1,6,1):
      tar.pendown()
      tar.forward(dist)
      tar.penup()
      tar.setpos(new_x+(dist/(2)**0.5)*i,y-0.5*100*sc*(3)**0.5)

  elif cri in ['engaste','engastado','fixo']:
    #Definindo o traco continuo vertical
    tar.left(90)
    tar.pendown()
    tar.forward(50*sc)
    tar.left(-180)
    tar.forward(100*sc)

    #definindo os tracos
    if int(list(tar.pos())[0]) == 0:
      ang = -45
    else:
      ang = 45 
    tar.hideturtle()
    tar.penup()
    tar.left(180)
    tar.forward(100*sc)
    tar.left(-180+ang)
    dist =20*sc
    for i in range(1,7,1):
      tar.pendown()
      tar.forward(dist)
      tar.penup()
      tar.setpos(x,y-50*sc+dist*i)

  elif 'livre' == cri:
    pass
    
def tramo(extensao,x):
  import turtle

  #Propriedades da tartaruga
  turtle.screensize(800,800)
  tar = turtle.Turtle()
  tar.hideturtle()
  tar.pensize(1)
  tar.shape('turtle')
  tar.color('red') 
  tar.setpos(x,0)

  #Movimentacao da tartaruga
  tar.forward(extensao)

def rotula(x):
  import turtle

  #Propriedades da tartaruga
  r = 5
  turtle.screensize(800,800)
  tar = turtle.Turtle()
  tar.pensize(1)
  tar.shape('turtle')
  tar.color('red') 
  tar.penup()
  tar.setpos(x,-r)
  tar.pendown()
  #Movimentacao da tartaruga
  tar.circle(r)
  tar.hideturtle()


def elemento_estrutural(d):
  x_global = 0
  for i in range(list(d.shape)[0]+1):
    if i == list(d.shape)[0]:
      var = d.iloc[i-1]
      n = var['no2']
    else:
      var = d.iloc[i]
      n = var['no1']
      tramo(var['Comprimento'],x_global)
    if n == "rotula":
      rotula(x_global)
    else:
      apoio(0.25,x_global,0,n)
    x_global += var['Comprimento']

