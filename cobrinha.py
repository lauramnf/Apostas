import turtle
import random

def cima():
	cursor.sety(cursor.ycor()+20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-300, 300)
		rand2 = random.randrange(-300, 300)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))
def baixo():
	cursor.sety(cursor.ycor()-20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-300, 300)
		rand2 = random.randrange(-300, 300)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))
def  direita():
	cursor.setx(cursor.xcor()+20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-300, 300)
		rand2 = random.randrange(-300, 300)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))
def  esquerda():
	cursor.setx(cursor.xcor()-20)
	if cursor.distance(comida) < 20:
		rand1 = random.randrange(-300, 300)
		rand2 = random.randrange(-300, 300)
		comida.penup()
		comida.speed(0)
		comida.goto((rand1, rand2))

#Preparando a tela
tela = turtle.Screen()
tela.title('Joguinho da cobrinha')
tela.bgcolor('#add8e6')
tela.setup(width = 600, height = 600)

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

#Não deixando rastro e relacionando movimentos com setas
cursor.penup()
turtle.onkeypress(cima, 'Up')
turtle.onkeypress(baixo, 'Down')
turtle.onkeypress(direita, 'Right')
turtle.onkeypress(esquerda, 'Left')
turtle.listen()



turtle.Screen().exitonclick()

