import turtle

def frente():
	cursor.fd(20)
def tras():
	cursor.bk(20)
def  direita():
	cursor.rt(90)
def  esquerda():
	cursor.lt(90)

#Preparando a tela
tela = turtle.Screen()
tela.title('Joguinho da cobrinha')
tela.bgcolor('#add8e6')
tela.setup(width = 600, height = 600)

#Definindo um objeto Turtle (minha cobra)
cursor = turtle.Turtle()

#Não deixando rastro e relacionando movimentos com setas
cursor.penup()
turtle.onkeypress(frente, 'Up')
turtle.onkeypress(tras, 'Down')
turtle.onkeypress(direita, 'Right')
turtle.onkeypress(esquerda, 'Left')
turtle.listen()

turtle.Screen().exitonclick()

