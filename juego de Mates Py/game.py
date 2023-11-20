import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Tablero con Fichas")


# Clase para representar un sprite de ficha
class Ficha(pygame.sprite.Sprite):
    def __init__(self, ruta_imagen, posicion, escala):
        super().__init__()
        self.image = pygame.image.load(ruta_imagen)
        self.image = pygame.transform.scale(self.image, (escala, escala))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.velocidad = 2  # Velocidad de movimiento reducida
        self.turno_activo = False

    def activar_turno(self):
        self.turno_activo = True

    def desactivar_turno(self):
        self.turno_activo = False

    def update(self):
        if self.turno_activo:
            # Manejar eventos de teclado para mover la ficha
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                self.rect.x -= self.velocidad
            if teclas[pygame.K_RIGHT]:
                self.rect.x += self.velocidad
            if teclas[pygame.K_UP]:
                self.rect.y -= self.velocidad
            if teclas[pygame.K_DOWN]:
                self.rect.y += self.velocidad

            # Limitar la posición de la ficha para que no salga de la pantalla
            self.rect.x = max(0, min(self.rect.x, ancho - self.rect.width))
            self.rect.y = max(0, min(self.rect.y, alto - self.rect.height))


# Cargar el fondo del tablero
fondo_tablero = pygame.image.load(
    "img/cohete.jfif"
)  # Reemplaza con la ruta de tu imagen de fondo
fondo_tablero = pygame.transform.scale(fondo_tablero, (ancho, alto))

# Crear un grupo de sprites para las fichas
grupo_fichas = pygame.sprite.Group()

# Crear fichas y agregarlas al grupo
ficha_1 = Ficha(
    "img/pencil.png", (100, 100), 50
)  # Reemplaza con la ruta de tu imagen de ficha
ficha_2 = Ficha(
    "img/eraser.png", (200, 200), 50
)  # Reemplaza con la ruta de tu otra imagen de ficha
grupo_fichas.add(ficha_1, ficha_2)

# Índice de la ficha activa
indice_ficha_activa = 0

# Fuente y tamaño del texto
fuente = pygame.font.Font(None, 36)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el fondo del tablero
    pantalla.blit(fondo_tablero, (0, 0))

    # Obtener la ficha activa actual
    ficha_activa = grupo_fichas.sprites()[indice_ficha_activa]

    # Actualizar y dibujar la ficha activa
    ficha_activa.update()
    grupo_fichas.draw(pantalla)

    # Mostrar el mensaje del turno actual
    mensaje_turno = fuente.render(f"Turno {indice_ficha_activa + 1}", True, (0, 0, 0))
    pantalla.blit(mensaje_turno, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos de teclado para cambiar el turno activo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_1]:
        indice_ficha_activa = 0
    elif teclas[pygame.K_2]:
        indice_ficha_activa = 1

    # Pasar al siguiente turno al presionar la barra espaciadora
    if teclas[pygame.K_SPACE]:
        ficha_activa.desactivar_turno()
        indice_ficha_activa = (indice_ficha_activa + 1) % len(grupo_fichas)
        grupo_fichas.sprites()[indice_ficha_activa].activar_turno()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)
