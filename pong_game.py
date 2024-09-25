import turtle

# Función para reiniciar el juego
def reiniciar_juego():
    global juego_terminado, puntos_a, puntos_b
    juego_terminado = False
    puntos_a = 0
    puntos_b = 0
    bola.goto(0, 0)
    bola.dx = 0.2
    bola.dy = 0.2
    mensaje.clear()  # Limpiar el mensaje de ganador
    actualizar_marcador()  # Restablecer el marcador
    mainloop()

# Función para cerrar la ventana
def cerrar_ventana():
    win.bye()  # Cerrar la ventana de Turtle

# Configurar la ventana
win = turtle.Screen()
win.title("Pong en Python")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Detener la actualización automática de la ventana

# Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("red")
paleta_a.shapesize(stretch_wid=6, stretch_len=1)
paleta_a.penup()
paleta_a.goto(-350, 0)

# Paleta B
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("blue")
paleta_b.shapesize(stretch_wid=6, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(40)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2

# Marcador de puntos
puntos_a = 0
puntos_b = 0

# Funciones para mover las paletas
def paleta_a_arriba():
    y = paleta_a.ycor()
    if y < 250:
        y += 20
    paleta_a.sety(y)

def paleta_a_abajo():
    y = paleta_a.ycor()
    if y > -240:
        y -= 20
    paleta_a.sety(y)

def paleta_b_arriba():
    y = paleta_b.ycor()
    if y < 250:
        y += 20
    paleta_b.sety(y)

def paleta_b_abajo():
    y = paleta_b.ycor()
    if y > -240:
        y -= 20
    paleta_b.sety(y)

# Controles del teclado
win.listen()
win.onkeypress(paleta_a_arriba, "w")
win.onkeypress(paleta_a_abajo, "s")
win.onkeypress(paleta_b_arriba, "Up")
win.onkeypress(paleta_b_abajo, "Down")

# Crear el marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)

def actualizar_marcador():
    marcador.clear()
    marcador.write("Ganador con 5 puntos\n",align="center", font=("Courier", 24, "normal"))
    marcador.write(f"Jugador Rojo: {puntos_a}  Jugador Azul: {puntos_b}", align="center", font=("Courier", 32, "normal"))

# Crear el mensaje de fin de juego
mensaje = turtle.Turtle()
mensaje.color("white")
mensaje.penup()
mensaje.hideturtle()

# Bucle principal del juego
juego_terminado = False  # Variable para controlar si el juego ha terminado
ganador = ""  # Variable para almacenar al ganador

def mainloop():
    global juego_terminado, ganador, puntos_a, puntos_b

    actualizar_marcador()  # Actualizar el marcador al iniciar

    while not juego_terminado:
        win.update()  # Actualizar la pantalla

        # Mover la bola
        bola.setx(bola.xcor() + bola.dx)
        bola.sety(bola.ycor() + bola.dy)

        # Bordes superior e inferior
        if bola.ycor() > 290:
            bola.sety(290)
            bola.dy *= -1

        if bola.ycor() < -290:
            bola.sety(-290)
            bola.dy *= -1

        # Bordes laterales (Punto)
        if bola.xcor() > 390:  # Punto para el jugador Rojo
            bola.goto(0, 0)
            bola.dx *= -1
            puntos_a += 1  # Aumentar el puntaje del jugador Rojo
            actualizar_marcador()  # Actualizar marcador

        if bola.xcor() < -390:  # Punto para el jugador Azul
            bola.goto(0, 0)
            bola.dx *= -1
            puntos_b += 1  # Aumentar el puntaje del jugador Azul
            actualizar_marcador()  # Actualizar marcador

        # Verificar si alguien ha ganado (5 puntos)
        if puntos_a >= 5:
            ganador = "Jugador Rojo"
            juego_terminado = True
        elif puntos_b >= 5:
            ganador = "Jugador Azul"
            juego_terminado = True

        # Colisiones con las paletas
        if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paleta_b.ycor() + 50 and bola.ycor() > paleta_b.ycor() - 50):
            bola.setx(340)
            bola.dx *= -1
            bola.dx *= 1.1  # Aumentar la velocidad en la dirección horizontal
            bola.dy *= 1.1  # Aumentar la velocidad en la dirección vertical

        if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paleta_a.ycor() + 50 and bola.ycor() > paleta_a.ycor() - 50):
            bola.setx(-340)
            bola.dx *= -1
            bola.dx *= 1.1  # Aumentar la velocidad en la dirección horizontal
            bola.dy *= 1.1  # Aumentar la velocidad en la dirección vertical

    # Mostrar mensaje de ganador
    mensaje.goto(0, 0)
    mensaje.write(f"Juego Terminado\nHa ganado el {ganador}", align="center", font=("Courier", 24, "normal"))

    # Mostrar opciones de reinicio o cierre
    mensaje.goto(0, -50)
    mensaje.write("Presiona 'r' para reiniciar o 'q' para salir", align="center", font=("Courier", 18, "normal"))

    # Asignar teclas para reiniciar o salir
    win.onkeypress(reiniciar_juego, "r")
    win.onkeypress(cerrar_ventana, "q")

# Iniciar el bucle principal del juego
mainloop()

# Mantener la ventana abierta
win.mainloop()
