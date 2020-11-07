import turtle
import random

def cima():
	cursor.sety(cursor.ycor()+20)
def baixo():
	cursor.sety(cursor.ycor()-20)
def  direita():
	cursor.setx(cursor.xcor()+20)
def  esquerda():
	cursor.setx(cursor.xcor()-20)

#Preparando a tela
tela = turtle.Screen()
tela.title('Joguinho da cobrinha')
tela.bgcolor('#add8e6')
tela.setup(width = 600, height = 600)

#Definindo um objeto Turtle (minha cobra)
cursor = turtle.Turtle()
cursos.shape('square')

#Não deixando rastro e relacionando movimentos com setas
cursor.penup()
turtle.onkeypress(cima, 'Up')
turtle.onkeypress(baixo, 'Down')
turtle.onkeypress(direita, 'Right')
turtle.onkeypress(esquerda, 'Left')
turtle.listen()

bolinha = turtle.Turtle()
bolinha.color('yellow', 'yellow')
bolinha.shape('circle')
rand1 = random.randrange(-300, 300)
rand2 = random.randrange(-300, 300)
bolinha.penup()
bolinha.speed(0)
bolinha.setpos((rand1, rand2))


turtle.Screen().exitonclick()

