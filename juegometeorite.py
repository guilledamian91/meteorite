import pygame, random, sys

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Posición inicial del jugador
PLAYER_INITIAL_X = 450
PLAYER_INITIAL_Y = 510

# Anchura de la pantalla
SCREEN_WIDTH = 900

# Configuración de la pantalla
screen = pygame.display.set_mode([SCREEN_WIDTH, 600])
pygame.display.set_caption("Juego de Meteoritos")

# Inicialización del reloj
clock = pygame.time.Clock()

# Variables de control
done = False
score = 0

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Grupo de sprites
all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
meteor_shot_list = pygame.sprite.Group()

# Cargar imágenes
background_image = pygame.image.load("asset/imagenes/background2.png").convert()
player_image = pygame.image.load("asset/imagenes/player.png").convert()
player_image.set_colorkey(BLACK)
meteor_image = pygame.image.load("asset/imagenes/meteor.png").convert()
meteor_image.set_colorkey(BLACK)
laser_image = pygame.image.load("asset/imagenes/laser.png").convert()
laser_image.set_colorkey(BLACK)
meteor_shot_image = pygame.image.load("asset/imagenes/meteor_shot.png").convert()
meteor_shot_image.set_colorkey(BLACK)

# Sonido del láser
sound = pygame.mixer.Sound("asset/sonido/laser5.ogg")



class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = meteor_image
        self.rect = self.image.get_rect()
        self.shoot_delay = 60
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.rect.x += random.randint(-1, 1)
        if pygame.time.get_ticks() - self.last_shot > self.shoot_delay and player.rect.x == self.rect.x:
            self.last_shot = pygame.time.get_ticks()
            meteor_shot = MeteorShot(self.rect.centerx, self.rect.bottom)
            all_sprite_list.add(meteor_shot)
            meteor_shot_list.add(meteor_shot)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.health = 10
        self.max_health = 10

    def changespeed(self, x):
        self.speed_x += x

    def update(self):
        self.rect.x += self.speed_x
        player.rect.y = 510
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            
            
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = laser_image
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y -= 5

class MeteorShot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = meteor_shot_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.rect.y += 2

def game_over_screen():
    screen.fill(WHITE)
    text = font.render("Game Over", True, BLACK)
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
    screen.blit(text, text_rect)

    retry_text = font.render("Press 'R' to Retry", True, BLACK)
    retry_text_rect = retry_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
    screen.blit(retry_text, retry_text_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        clock.tick(30)

def start_screen():
    screen.fill(WHITE)
    title_text = font.render("Juego de Meteoritos", True, BLACK)
    title_rect = title_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
    screen.blit(title_text, title_rect)

    controls_text = font.render("Controles:", True, BLACK)
    controls_rect = controls_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 20))
    screen.blit(controls_text, controls_rect)

    control_left_text = font.render("Izquierda: Flecha Izquierda", True, BLACK)
    control_left_rect = control_left_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
    screen.blit(control_left_text, control_left_rect)

    control_right_text = font.render("Derecha: Flecha Derecha", True, BLACK)
    control_right_rect = control_right_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 80))
    screen.blit(control_right_text, control_right_rect)

    control_fire_text = font.render("Disparar: Barra Espaciadora", True, BLACK)
    control_fire_rect = control_fire_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 110))
    screen.blit(control_fire_text, control_fire_rect)

    start_text = font.render("Presiona ESPACIO para empezar", True, BLACK)
    start_rect = start_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 160))
    screen.blit(start_text, start_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_input = False

        clock.tick(30)

def victory_screen():
    screen.fill(WHITE)
    text = font.render("¡Has Ganado!", True, BLACK)
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
    screen.blit(text, text_rect)

    retry_text = font.render("Presiona 'R' para reiniciar", True, BLACK)
    retry_text_rect = retry_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
    screen.blit(retry_text, retry_text_rect)

    quit_text = font.render("Presiona 'Q' para salir", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
    screen.blit(quit_text, quit_text_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        clock.tick(30)

def generate_meteorites():
    for i in range(50):
        meteor = Meteor()
        meteor.rect.x = random.randrange(50,850)
        meteor.rect.y = random.randrange(50,450)
        meteor_list.add(meteor)
        all_sprite_list.add(meteor)

def restart_game():
    player.rect.x = PLAYER_INITIAL_X
    player.rect.y = PLAYER_INITIAL_Y
    player.health = player.max_health
    player.speed_x = 0
    score = 0
    meteor_list.empty()
    laser_list.empty()
    meteor_shot_list.empty()
    all_sprite_list.empty()
    all_sprite_list.add(player)
    generate_meteorites()

# Creación del jugador
player = Player()
all_sprite_list.add(player)

background_image = pygame.image.load("asset/imagenes/background2.png").convert()

# Generar meteoritos
generate_meteorites()

# Llamar a la función de inicio antes del bucle principal
start_screen()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3)
            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 20
                all_sprite_list.add(laser)
                laser_list.add(laser)
                sound.play()
            if event.key == pygame.K_r:
                restart_game()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3)
    
    all_sprite_list.update()

    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 1
    
    if len(meteor_list) == 0:
        victory_screen()
        
    player_hit_list = pygame.sprite.spritecollide(player, meteor_shot_list, True)
    for meteor_shot in player_hit_list:
        all_sprite_list.remove(meteor_shot)
        meteor_shot_list.remove(meteor_shot)
        player.health -= 1
        
    if player.health <= 0:
        continue_game = game_over_screen()
        if continue_game:
            restart_game()
        else:
            done = True
            
    screen.blit(background_image, (0, 0))
    all_sprite_list.draw(screen)
    
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 200, 20))
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, 20 * player.health, 20))
    
    text = font.render(f"Vida: {player.health}", True, BLACK)
    screen.blit(text, (10, 40))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
