import turtle

#Preparando a tela
tela = turtle.Screen()
tela.title('Joguinho da cobrinha')
tela.bgcolor('#add8e6')
tela.setup(width = 600, height = 600)

#Definindo um objeto Turtle (minha cobra)
cursor = turtle.Turtle()
cursor.penup()

cursor.fd(60)

turtle.Screen().exitonclick()

