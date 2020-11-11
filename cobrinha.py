import turtle
import random
import time

def cima():
	direcao = 'rt'
	cursor.sety(cursor.ycor()+20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-290, 290)
		rand2 = random.randrange(-290, 290)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))
		pedaco_novo = turtle.Turtle()
		pedaco_novo.speed(0)
		pedaco_novo.shape('square')
		pedaco_novo.penup()
		corpo.append(pedaco_novo)
	for i in range(len(corpo)-1, 0, -1):
		corpo[i].goto(corpo[i-1].xcor(), corpo[i-1].ycor())
	if len(corpo) > 0:
		corpo[0].goto(cursor.xcor(), cursor.ycor())
def baixo():
	direcao = 'lt'
	cursor.sety(cursor.ycor()-20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-290, 290)
		rand2 = random.randrange(-290, 290)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))
		pedaco_novo = turtle.Turtle()
		pedaco_novo.speed(0)
		pedaco_novo.shape('square')
		pedaco_novo.penup()
		corpo.append(pedaco_novo)
	for i in range(len(corpo)-1, 0, -1):
		corpo[i].goto(corpo[i-1].xcor(), corpo[i-1].ycor())
	if len(corpo) > 0:
		corpo[0].goto(cursor.xcor(), cursor.ycor())
def  direita():
	direcao = 'fd'
	cursor.setx(cursor.xcor()+20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-290, 290)
		rand2 = random.randrange(-290, 290)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))
		pedaco_novo = turtle.Turtle()
		pedaco_novo.speed(0)
		pedaco_novo.shape('square')
		pedaco_novo.penup()
		corpo.append(pedaco_novo)
	for i in range(len(corpo)-1, 0, -1):
		corpo[i].goto(corpo[i-1].xcor(), corpo[i-1].ycor())
	if len(corpo) > 0:
		corpo[0].goto(cursor.xcor(), cursor.ycor())
def  esquerda():
	direcao = 'bd'
	cursor.setx(cursor.xcor()-20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-290, 290)
		rand2 = random.randrange(-290, 290)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))
		pedaco_novo = turtle.Turtle()
		pedaco_novo.speed(0)
		pedaco_novo.shape('square')
		pedaco_novo.penup()
		corpo.append(pedaco_novo)
	for i in range(len(corpo)-1, 0, -1):
		corpo[i].goto(corpo[i-1].xcor(), corpo[i-1].ycor())
	if len(corpo) > 0:
		corpo[0].goto(cursor.xcor(), cursor.ycor())
#Preparando a tela
tela = turtle.Screen()
tela.title('Joguinho da cobrinha')
tela.bgcolor('#add8e6')
tela.setup(width = 600, height = 600)

corpo = []

comida = turtle.Turtle()
comida.color('yellow', 'yellow')
comida.shape('circle')
rand1 = random.randrange(-290, 290)
rand2 = random.randrange(-290, 290)
comida.penup()
comida.speed(0)
comida.goto((rand1, rand2))
#Definindo um objeto Turtle (minha cobra)
cursor = turtle.Turtle()
cursor.shape('square')
cursor.speed(0)
direcao = 'fd'
while True:
#Não deixando rastro e relacionando movimentos com setas
	cursor.fd(20)
	if direcao == 'fd':
		cursor.penup()
		turtle.onkeypress(cima, 'Up')
		turtle.onkeypress(baixo, 'Down')
		turtle.onkeypress(esquerda, 'Left')
		turtle.onkeypress(direita, 'Right')
		time.sleep(0.1)
	elif direcao == 'bd':
		cursor.bd(20)
		cursor.penup()
		turtle.onkeypress(cima, 'Up')
		turtle.onkeypress(baixo, 'Down')
		turtle.onkeypress(esquerda, 'Left')
		turtle.onkeypress(direita, 'Right')
		time.sleep(0.1)
	elif direcao == 'ft':
		cursor.ft(20)
		cursor.penup()
		turtle.onkeypress(cima, 'Up')
		turtle.onkeypress(baixo, 'Down')
		turtle.onkeypress(esquerda, 'Left')
		turtle.onkeypress(direita, 'Right')
		time.sleep(0.1)
	elif direcao == 'rt':
		cursor.ft(20)
		cursor.penup()
		turtle.onkeypress(cima, 'Up')
		turtle.onkeypress(baixo, 'Down')
		turtle.onkeypress(esquerda, 'Left')
		turtle.onkeypress(direita, 'Right')
		time.sleep(0.1)

	turtle.listen()
	turtle.Screen().exitonclick()




