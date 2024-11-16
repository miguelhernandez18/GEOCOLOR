## Esta sera nuestra interfaz que nos invoca las funciones externas. 
## La idea es tener el main solo con los menus principales y movimientos entre opciones

import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)           # Rojo intenso
VERDE = (0, 255, 0)          # Verde brillante
AZUL = (0, 0, 255)           # Azul puro
AMARILLO = (255, 255, 0)     # Amarillo vibrante
MORADO = (153, 50, 204)      # Morado más claro
DORADO = (255, 215, 0)       # Dorado se mantiene como tono cálido brillante
NARANJA = (255, 140, 0)      # Tono de naranja más oscuro, diferente al rojo y dorado
ROSADO = (255, 105, 180)     # Rosado vibrante y distintivo
CAFE = (101, 67, 33)  # Café más oscuro
CELESTE = (0, 191, 255)      # Azul claro, distintivo de los primarios
FUCSIA = (255, 0, 255)       # Color fuerte y contrastante

# Configurar la ventana
ANCHO = 1080
ALTO = 640
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("GeoColor")

#fondo jpg de tablero
fondo = pygame.image.load("fondo_de_tablero.jpeg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

#Corazon por vida
corazon_img = pygame.image.load("corazon.png")
corazon_img = pygame.transform.scale(corazon_img, (40, 40))

# Definir fuentes
fuente_titulo = pygame.font.Font(None, 120)
fuente_grande = pygame.font.Font(None, 74) 
fuente_normal = pygame.font.Font(None, 48)
fuente_pequeña = pygame.font.Font(None, 36)

contador_completados = 0 # Variable global para contar las veces que se ha completado el nivel
contador_perdidas = 0  # Variable para guardar el contador al perder
nivel_de_juego = 0  # Variable para menu de fin de vidas y fin de juego

# Cargar sonidos
sonido_boton = pygame.mixer.Sound("sonido_boton.wav")
sonido_error = pygame.mixer.Sound("sonido_error.wav")
sonido_acierto = pygame.mixer.Sound("sonido_acierto.wav")
musica_menu =  pygame.mixer.Sound("musica_menu.wav")

# Reproducir música de menú
musica_menu.play(-1)  # -1 significa que se reproduce en bucle
musica_menu.set_volume(1)
sonido_error.set_volume(0.1)

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, fuente, color, superficie, x, y):
    texto_obj = fuente.render(texto, True, color)
    texto_rect = texto_obj.get_rect()
    texto_rect.center = (x, y)
    superficie.blit(texto_obj, texto_rect)

# Cargar la imagen del título
titulo_imagen = pygame.image.load("titulo.png")
titulo_imagen = pygame.transform.scale(titulo_imagen, (315, 130))

# Función para el menú principal
def menu_principal():
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if jugar_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    menu_jugar()
                if como_jugar_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    instrucciones()
                if salir_rect.collidepoint(evento.pos):
                    sonido_boton.play
                    pygame.quit()
                    sys.exit()

        ventana.blit(fondo, (0, 0))

        # Titulo por imagen
        ventana.blit(titulo_imagen, (ANCHO // 2 - titulo_imagen.get_width() // 2, 160))  

        # Dibujar el menú
        jugar_rect = pygame.Rect(450, 305, 180, 50)
        como_jugar_rect = pygame.Rect(800, 540, 200, 40)
        salir_rect = pygame.Rect(90, 540, 80, 40)

        pygame.draw.rect(ventana, BLANCO, jugar_rect)
        pygame.draw.rect(ventana, BLANCO, como_jugar_rect)
        pygame.draw.rect(ventana, BLANCO, salir_rect)

        mostrar_texto("Jugar".upper(), fuente_normal, NEGRO, ventana, 540, 330)
        mostrar_texto("¿Cómo jugar?".upper(), fuente_pequeña, NEGRO, ventana, 900, 560)
        mostrar_texto("Salir".upper(), fuente_pequeña, NEGRO, ventana, 130, 560)

        pygame.display.flip()

# En menu_fin_de_vidas
def menu_fin_de_vidas(figura_objetivo, color_objetivo):
    global contador_completados  # Referencia a la variable global
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if volver_menu_rect.collidepoint(evento.pos):
                    musica_menu.set_volume(1)
                    menu_principal()
                    return  
                if seguir_jugando_rect.collidepoint(evento.pos):
                    # Guardar el contador antes de reiniciar
                    global contador_perdidas
                    if nivel_de_juego == 1:
                        contador_perdidas = contador_completados  # Guardar el valor del contador
                        contador_completados = 0  # Reiniciar contador al volver a jugar
                        nueva_figura_objetivo, nueva_color_objetivo = nivel_1()
                        juego_nivel_1(nueva_figura_objetivo, nueva_color_objetivo)
                        return
                    elif nivel_de_juego == 2:
                        contador_perdidas = contador_completados  # Guardar el valor del contador
                        contador_completados = 0  # Reiniciar contador al volver a jugar
                        nueva_figura_objetivo, nueva_color_objetivo = nivel_2()
                        juego_nivel_2(nueva_figura_objetivo, nueva_color_objetivo)
                        return
                    elif nivel_de_juego == 3:
                        contador_perdidas = contador_completados  # Guardar el valor del contador
                        contador_completados = 0  # Reiniciar contador al volver a jugar
                        nueva_figura_objetivo, nueva_color_objetivo = nivel_3()
                        juego_nivel_3(nueva_figura_objetivo, nueva_color_objetivo)
                        return

        ventana.fill(NEGRO)
        mostrar_texto("Se te acabaron las vidas", fuente_normal, BLANCO, ventana, 535, 130)

        # Mostrar cuántas veces has completado el nivel antes de perder
        mostrar_texto(f"Has completado el nivel {contador_perdidas} veces.", fuente_normal, BLANCO, ventana, 530, 200)

        seguir_jugando_rect = pygame.Rect(380, 290, 300, 50)
        pygame.draw.rect(ventana, BLANCO, seguir_jugando_rect)
        mostrar_texto("Seguir Jugando", fuente_pequeña, NEGRO, ventana, 540, 315)

        volver_menu_rect = pygame.Rect(380, 370, 300, 50)
        pygame.draw.rect(ventana, BLANCO, volver_menu_rect)
        mostrar_texto("Volver al Menú Principal", fuente_pequeña, NEGRO, ventana, 530, 395)

        pygame.display.flip()

def menu_fin_de_nivel():
    global nivel_de_juego
    global contador_completados
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if seguir_jugando_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    if nivel_de_juego == 1:
                        # Seguir jugando debería simplemente volver a iniciar el juego con una nueva figura
                        nueva_figura_objetivo, nueva_color_objetivo = nivel_1()
                        juego_nivel_1(nueva_figura_objetivo, nueva_color_objetivo)
                        return
                    elif nivel_de_juego == 2:
                        # Seguir jugando debería simplemente volver a iniciar el juego con una nueva figura
                        nueva_figura_objetivo, nueva_color_objetivo = nivel_2()
                        juego_nivel_2(nueva_figura_objetivo, nueva_color_objetivo)
                        return
                    elif nivel_de_juego == 3:
                        # Seguir jugando debería simplemente volver a iniciar el juego con una nueva figura
                        nueva_figura_objetivo, nueva_color_objetivo = nivel_3()
                        juego_nivel_3(nueva_figura_objetivo, nueva_color_objetivo)
                        return
                if volver_menu_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    musica_menu.set_volume(1)
                    contador_completados = 0
                    menu_principal()
                    return

        ventana.fill(NEGRO)

        # Mostrar mensaje de fin de nivel
        mostrar_texto(f"¡Has completado el nivel {contador_completados} veces!", fuente_normal, BLANCO, ventana, ANCHO // 2, 200)

        # Botón "Seguir Jugando"
        seguir_jugando_rect = pygame.Rect(400, 280, 300, 50)
        pygame.draw.rect(ventana, BLANCO, seguir_jugando_rect)
        mostrar_texto("Seguir Jugando", fuente_pequeña, NEGRO, ventana, 550, 305)

        # Botón "Volver al Menú Principal"
        volver_menu_rect = pygame.Rect(400, 360, 300, 50)
        pygame.draw.rect(ventana, BLANCO, volver_menu_rect)
        mostrar_texto("Volver al Menú Principal", fuente_pequeña, NEGRO, ventana, 550, 385)


        pygame.display.flip()

def juego_nivel_1(figura_objetivo, color_objetivo):
    musica_menu.set_volume(0)
    global contador_completados  # Referencia a la variable global

    figuras = ["cuadrado", "circulo", "triangulo", "rectangulo"]
    colores = [ROJO, AZUL, AMARILLO]
    figuras_random = []

    # Generar figuras aleatorias
    for _ in range(8):
        figura = random.choice(figuras)
        color = random.choice(colores)
        while figura == figura_objetivo and color == color_objetivo:
            color = random.choice(colores)
        figuras_random.append((figura, color))

    indice_objetivo = random.randint(0, 8)
    figuras_random.insert(indice_objetivo, (figura_objetivo, color_objetivo))

    intentos = 3  # Intentos disponibles
    ejecutando = True
    mensaje = ""
    rectangulos_figuras = []

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(rectangulos_figuras):
                    if rect.collidepoint(evento.pos):
                        if i == indice_objetivo:  # Figura correcta
                            mensaje = "¡Felicidades! Encontraste tu figura"
                            sonido_acierto.play()
                            contador_completados += 1  # Incrementar solo si es correcto
                            menu_fin_de_nivel()  # Ir al menú de fin de nivel
                            return
                        else:  # Figura incorrecta
                            sonido_error.play()
                            intentos -= 1
                            mensaje = f"Esta no es la figura buscada. Te quedan {intentos} intentos."

                            if intentos == 0:
                                # Guardar contador antes de reiniciar
                                global contador_perdidas
                                contador_perdidas = contador_completados  # Guardar el valor del contador
                                contador_completados = 0  # Reiniciar contador
                                menu_fin_de_vidas(figura_objetivo, color_objetivo)  # Fin de vidas
                                return  

        ventana.fill(NEGRO)
        
        posiciones = [(300, 150), (500, 150), (700, 150),
                      (300, 300), (500, 300), (700, 300),
                      (300, 450), (500, 450), (700, 450)]

        rectangulos_figuras = []  # Reiniciar lista de rectángulos en cada iteración
        for i, (figura, color) in enumerate(figuras_random):
            x, y = posiciones[i]
            if figura == "cuadrado":
                rect = pygame.draw.rect(ventana, color, (x, y, 100, 100))
            elif figura == "circulo":
                rect = pygame.draw.circle(ventana, color, (x + 50, y + 50), 50)
            elif figura == "triangulo":
                puntos = [(x + 50, y), (x, y + 100), (x + 100, y + 100)]
                rect = pygame.draw.polygon(ventana, color, puntos)
            elif figura == "rectangulo":
                rect = pygame.draw.rect(ventana, color, (x, y, 120, 80))
            
            rectangulos_figuras.append(rect)

        for i in range(intentos):
            ventana.blit(corazon_img, (10 + i * 50, 10))

        if mensaje:
            mostrar_texto(mensaje, fuente_normal, BLANCO, ventana, ANCHO // 2, 100)

        pygame.display.flip()

def juego_nivel_2(figura_objetivo, color_objetivo):
    musica_menu.set_volume(0)
    global contador_completados

    figuras = ["cuadrado", "circulo", "triangulo", "rectangulo"]
    colores = [ROJO, VERDE, AZUL, AMARILLO, MORADO, NARANJA]
    figuras_random = []

    # Generar figuras aleatorias para 16 posiciones (4x4)
    for _ in range(11):
        figura = random.choice(figuras)
        color = random.choice(colores)
        while figura == figura_objetivo and color == color_objetivo:
            color = random.choice(colores)
        figuras_random.append((figura, color))

    indice_objetivo = random.randint(0, 11)
    figuras_random.insert(indice_objetivo, (figura_objetivo, color_objetivo))

    intentos = 3
    ejecutando = True
    mensaje = ""
    rectangulos_figuras = []

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(rectangulos_figuras):
                    if rect.collidepoint(evento.pos):
                        if i == indice_objetivo:
                            mensaje = "¡Felicidades! Encontraste tu figura"
                            sonido_acierto.play()
                            contador_completados += 1
                            menu_fin_de_nivel()
                            return
                        else:
                            sonido_error.play()
                            intentos -= 1
                            mensaje = f"Esta no es la figura buscada. Te quedan {intentos} intentos."

                            if intentos == 0:
                                global contador_perdidas
                                contador_perdidas = contador_completados
                                contador_completados = 0
                                menu_fin_de_vidas(figura_objetivo, color_objetivo)
                                return  

        ventana.fill(NEGRO)
        
        # Posiciones para 4x3 figuras
        posiciones = [(180, 150), (380, 150), (580, 150), (780, 150),
                      (180, 300), (380, 300), (580, 300), (780, 300),
                      (180, 450), (380, 450), (580, 450), (780, 450)]

        rectangulos_figuras = []
        for i, (figura, color) in enumerate(figuras_random):
            x, y = posiciones[i]
            if figura == "cuadrado":
                rect = pygame.draw.rect(ventana, color, (x, y, 100, 100))
            elif figura == "circulo":
                rect = pygame.draw.circle(ventana, color, (x + 50, y + 50), 50)
            elif figura == "triangulo":
                puntos = [(x + 50, y), (x, y + 100), (x + 100, y + 100)]
                rect = pygame.draw.polygon(ventana, color, puntos)
            elif figura == "rectangulo":
                rect = pygame.draw.rect(ventana, color, (x, y, 120, 80))

            rectangulos_figuras.append(rect)

        for i in range(intentos):
            ventana.blit(corazon_img, (10 + i * 50, 10))

        if mensaje:
            mostrar_texto(mensaje, fuente_normal, BLANCO, ventana, ANCHO // 2, 100)

        pygame.display.flip()

def juego_nivel_3(figura_objetivo, color_objetivo):
    musica_menu.set_volume(0)
    global contador_completados

    figuras = ["cuadrado", "circulo", "triangulo", "rectangulo", "rombo", "ovalo", "pentagono"]
    colores = [ROJO, VERDE, AZUL, AMARILLO, MORADO, DORADO, NARANJA, ROSADO, CAFE, CELESTE, FUCSIA, BLANCO]
    figuras_random = []

    # Generar figuras aleatorias para 16 posiciones (4x4)
    for _ in range(19):
        figura = random.choice(figuras)
        color = random.choice(colores)
        while figura == figura_objetivo and color == color_objetivo:
            color = random.choice(colores)
        figuras_random.append((figura, color))

    indice_objetivo = random.randint(0, 11)
    figuras_random.insert(indice_objetivo, (figura_objetivo, color_objetivo))

    intentos = 3
    ejecutando = True
    mensaje = ""
    rectangulos_figuras = []

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(rectangulos_figuras):
                    if rect.collidepoint(evento.pos):
                        if i == indice_objetivo:
                            mensaje = "¡Felicidades! Encontraste tu figura"
                            sonido_acierto.play()
                            contador_completados += 1
                            menu_fin_de_nivel()
                            return
                        else:
                            sonido_error.play()
                            intentos -= 1
                            mensaje = f"Esta no es la figura buscada. Te quedan {intentos} intentos."

                            if intentos == 0:
                                global contador_perdidas
                                contador_perdidas = contador_completados
                                contador_completados = 0
                                menu_fin_de_vidas(figura_objetivo, color_objetivo)
                                return  

        ventana.fill(NEGRO)
        
        # Posiciones para 5x4 figuras
        posiciones = [
            (100, 150), (300, 150), (500, 150), (700, 150), (900, 150),
            (100, 270), (300, 270), (500, 270), (700, 270), (900, 270),
            (100, 390), (300, 390), (500, 390), (700, 390), (900, 390),
            (100, 510), (300, 510), (500, 510), (700, 510), (900, 510)
        ]
        rectangulos_figuras = []
        for i, (figura, color) in enumerate(figuras_random):
            x, y = posiciones[i]
            if figura == "cuadrado":
                rect = pygame.draw.rect(ventana, color, (x, y, 85, 85))
            elif figura == "circulo":
                rect = pygame.draw.circle(ventana, color, (x + 50, y + 50), 50)
            elif figura == "triangulo":
                puntos = [(x + 50, y), (x, y + 100), (x + 100, y + 100)]
                rect = pygame.draw.polygon(ventana, color, puntos)
            elif figura == "rectangulo":
                rect = pygame.draw.rect(ventana, color, (x, y, 105, 65))
            elif figura == "rombo":
                puntos = [(x + 50, y), (x, y + 50), (x + 50, y + 100), (x + 100, y + 50)]
                rect = pygame.draw.polygon(ventana, color, puntos)
            elif figura == "ovalo":
                rect = pygame.draw.ellipse(ventana, color, (x, y, 100, 70))
            elif figura == "pentagono":
                puntos = [
                    (x + 50, y),  
                    (x + 10, y + 40),  
                    (x + 30, y + 90),  
                    (x + 70, y + 90),  
                    (x + 90, y + 40)  
                ]
                rect = pygame.draw.polygon(ventana, color, puntos)

            rectangulos_figuras.append(rect)

        for i in range(intentos):
            ventana.blit(corazon_img, (10 + i * 50, 10))

        if mensaje:
            mostrar_texto(mensaje, fuente_normal, BLANCO, ventana, ANCHO // 2, 100)

        pygame.display.flip()

# Modificar la función nivel_1 para que abra el juego de figuras al presionar "Continuar"
def nivel_1():
    figuras = ["cuadrado", "circulo", "triangulo", "rectangulo"]
    colores = [ROJO, AZUL, AMARILLO]  # Evitamos el negro en los colores

    figura_objetivo = random.choice(figuras)
    color_objetivo = random.choice(colores)

    # Mostrar la figura objetivo
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if continuar_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    # Abrir el juego con las 9 figuras al azar
                    juego_nivel_1(figura_objetivo, color_objetivo)
                    ejecutando = False

        ventana.fill(NEGRO)  # Limpiamos la pantalla

        # Mostrar título "Busca la figura"
        mostrar_texto("Busca la figura", fuente_normal, BLANCO, ventana, ANCHO // 2, 100)

        # Dibujar la figura aleatoria
        if figura_objetivo == "cuadrado":
            pygame.draw.rect(ventana, color_objetivo, (ANCHO // 2 - 50, ALTO // 2 - 50, 100, 100))
        elif figura_objetivo == "circulo":
            pygame.draw.circle(ventana, color_objetivo, (ANCHO // 2, ALTO // 2), 50)
        elif figura_objetivo == "triangulo":
            puntos = [(ANCHO // 2, ALTO // 2 - 50), (ANCHO // 2 - 50, ALTO // 2 + 50), (ANCHO // 2 + 50, ALTO // 2 + 50)]
            pygame.draw.polygon(ventana, color_objetivo, puntos)
        elif figura_objetivo == "rectangulo":
            pygame.draw.rect(ventana, color_objetivo, (ANCHO // 2 - 75, ALTO // 2 - 50, 150, 100))

        # Dibujar botón "Continuar"
        continuar_rect = pygame.Rect(ANCHO - 200, ALTO - 100, 150, 50)
        pygame.draw.rect(ventana, BLANCO, continuar_rect)
        mostrar_texto("Continuar", fuente_pequeña, NEGRO, ventana, ANCHO - 125, ALTO - 75)

        pygame.display.flip()
    
    # retornar los valores
    return figura_objetivo, color_objetivo
def nivel_2():
    figuras = ["cuadrado", "circulo", "triangulo", "rectangulo"]
    colores = [ROJO, VERDE, AZUL, AMARILLO, MORADO, NARANJA]  # Evitamos el negro en los colores

    figura_objetivo = random.choice(figuras)
    color_objetivo = random.choice(colores)

    # Mostrar la figura objetivo
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if continuar_rect.collidepoint(evento.pos):
                    # Abrir el juego con las 9 figuras al azar
                    juego_nivel_2(figura_objetivo, color_objetivo)
                    ejecutando = False

        ventana.fill(NEGRO)  # Limpiamos la pantalla

        # Mostrar título "Busca la figura"
        mostrar_texto("Busca la figura", fuente_normal, BLANCO, ventana, ANCHO // 2, 100)

        # Dibujar la figura aleatoria
        if figura_objetivo == "cuadrado":
            pygame.draw.rect(ventana, color_objetivo, (ANCHO // 2 - 50, ALTO // 2 - 50, 100, 100))
        elif figura_objetivo == "circulo":
            pygame.draw.circle(ventana, color_objetivo, (ANCHO // 2, ALTO // 2), 50)
        elif figura_objetivo == "triangulo":
            puntos = [(ANCHO // 2, ALTO // 2 - 50), (ANCHO // 2 - 50, ALTO // 2 + 50), (ANCHO // 2 + 50, ALTO // 2 + 50)]
            pygame.draw.polygon(ventana, color_objetivo, puntos)
        elif figura_objetivo == "rectangulo":
            pygame.draw.rect(ventana, color_objetivo, (ANCHO // 2 - 75, ALTO // 2 - 50, 150, 100))

        # Dibujar botón "Continuar"
        continuar_rect = pygame.Rect(ANCHO - 200, ALTO - 100, 150, 50)
        pygame.draw.rect(ventana, BLANCO, continuar_rect)
        mostrar_texto("Continuar", fuente_pequeña, NEGRO, ventana, ANCHO - 125, ALTO - 75)

        pygame.display.flip()
    
    # retornar los valores
    return figura_objetivo, color_objetivo
def nivel_3():
    figuras = ["cuadrado", "circulo", "triangulo", "rectangulo", "rombo", "ovalo", "pentagono"]
    colores = [ROJO, VERDE, AZUL, AMARILLO, MORADO, DORADO, NARANJA, ROSADO, CAFE, CELESTE, FUCSIA, BLANCO]  # Evitamos el negro en los colores

    figura_objetivo = random.choice(figuras)
    color_objetivo = random.choice(colores)

    # Mostrar la figura objetivo
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if continuar_rect.collidepoint(evento.pos):
                    # Abrir el juego con las 9 figuras al azar
                    juego_nivel_3(figura_objetivo, color_objetivo)
                    ejecutando = False

        ventana.fill(NEGRO)  # Limpiamos la pantalla

        # Mostrar título "Busca la figura"
        mostrar_texto("Busca la figura", fuente_normal, BLANCO, ventana, ANCHO // 2, 100)

        # Dibujar la figura aleatoria
        if figura_objetivo == "cuadrado":
            pygame.draw.rect(ventana, color_objetivo, (ANCHO // 2 - 50, ALTO // 2 - 50, 100, 100))
        elif figura_objetivo == "circulo":
            pygame.draw.circle(ventana, color_objetivo, (ANCHO // 2, ALTO // 2), 50)
        elif figura_objetivo == "triangulo":
            puntos = [(ANCHO // 2, ALTO // 2 - 50), (ANCHO // 2 - 50, ALTO // 2 + 50), (ANCHO // 2 + 50, ALTO // 2 + 50)]
            pygame.draw.polygon(ventana, color_objetivo, puntos)
        elif figura_objetivo == "rectangulo":
            pygame.draw.rect(ventana, color_objetivo, (ANCHO // 2 - 75, ALTO // 2 - 50, 150, 100))
        
        elif figura_objetivo == "rombo":
            puntos = [(ANCHO // 2, ALTO // 2 - 50), (ANCHO // 2 - 50, ALTO // 2), (ANCHO // 2, ALTO // 2 + 50), (ANCHO // 2 + 50, ALTO // 2)]
            pygame.draw.polygon(ventana, color_objetivo, puntos)
        elif figura_objetivo == "ovalo":
            pygame.draw.ellipse(ventana, color_objetivo, (ANCHO // 2 - 75, ALTO // 2 - 50, 150, 100))
        elif figura_objetivo == "pentagono":
            puntos = [
                (ANCHO // 2, ALTO // 2 - 50),
                (ANCHO // 2 - 47, ALTO // 2 - 15),
                (ANCHO // 2 - 29, ALTO // 2 + 40),
                (ANCHO // 2 + 29, ALTO // 2 + 40),
                (ANCHO // 2 + 47, ALTO // 2 - 15)
            ]
            pygame.draw.polygon(ventana, color_objetivo, puntos)
            
        # Dibujar botón "Continuar"
        continuar_rect = pygame.Rect(ANCHO - 200, ALTO - 100, 150, 50)
        pygame.draw.rect(ventana, BLANCO, continuar_rect)
        mostrar_texto("Continuar", fuente_pequeña, NEGRO, ventana, ANCHO - 125, ALTO - 75)

        pygame.display.flip()
    
    # retornar los valores
    return figura_objetivo, color_objetivo

def menu_jugar():
    global nivel_de_juego
    global contador_perdidas 
    contador_perdidas = 0
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if nivel1_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    nivel_de_juego = 1
                    figura_objetivo, color_objetivo = nivel_1()  # Mantener para nivel 1
                    juego_nivel_1(figura_objetivo, color_objetivo)
                if nivel2_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    nivel_de_juego = 2
                    figura_objetivo, color_objetivo = nivel_2()  # Generar figura objetivo
                    juego_nivel_2(figura_objetivo, color_objetivo)  # Llamar a la función del nivel 2
                if nivel3_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    nivel_de_juego = 3
                    figura_objetivo, color_objetivo = nivel_3()  # Generar figura objetivo
                    juego_nivel_3(figura_objetivo, color_objetivo)  # Llamar a la función del nivel 3
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volver_rect.collidepoint(evento.pos):
                        sonido_boton.play()
                        ejecutando = False
        ventana.fill(NEGRO)

        # Dibujar el menú de niveles
        nivel1_rect = pygame.Rect(440, 150, 200, 50)
        nivel2_rect = pygame.Rect(440, 250, 200, 50)
        nivel3_rect = pygame.Rect(440, 350, 200, 50)
        volver_rect = pygame.Rect(440, 550, 200, 50)

        pygame.draw.rect(ventana, BLANCO, nivel1_rect)
        pygame.draw.rect(ventana, BLANCO, nivel2_rect)
        pygame.draw.rect(ventana, BLANCO, nivel3_rect)
        pygame.draw.rect(ventana, BLANCO, volver_rect)

        mostrar_texto("Nivel 1", fuente_normal, NEGRO, ventana, 540, 175)
        mostrar_texto("Nivel 2", fuente_normal, NEGRO, ventana, 540, 275)
        mostrar_texto("Nivel 3", fuente_normal, NEGRO, ventana, 540, 375)
        mostrar_texto("Volver", fuente_pequeña, NEGRO, ventana, 540, 575)

        pygame.display.flip()

# Función para mostrar las instrucciones
def instrucciones():
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if volver_rect.collidepoint(evento.pos):
                    sonido_boton.play()
                    ejecutando = False

        ventana.fill(NEGRO)

        # Dibujar las instrucciones
        instrucciones_texto = [
            "Instrucciones:",
            "1. Selecciona la figura geométrica objetivo.",
            "2. La figura objetivo tendrá un color específico.",
            "3. Encuentra y selecciona la misma figura con el mismo color en el tablero.",
            "4. ¡Buena suerte!"
        ]

        y = 150
        for linea in instrucciones_texto:
            mostrar_texto(linea, fuente_pequeña, BLANCO, ventana, ANCHO // 2, y)
            y += 50

        volver_rect = pygame.Rect(440, 550, 200, 50)
        pygame.draw.rect(ventana, BLANCO, volver_rect)
        mostrar_texto("Volver", fuente_pequeña, NEGRO, ventana, 540, 575)

        pygame.display.flip()

# Ejecutar el menú principal
menu_principal()
