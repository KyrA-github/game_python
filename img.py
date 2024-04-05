import pygame

# Импортируйте sys, если вам нужно использовать sys.path
# import sys

# Вынесите инициализацию pygame.init() в этот файл, если это необходимо
# pygame.init()

# Загрузите изображения в отдельные переменные
explosion = [
    pygame.image.load('images/texture/explosion/explosion-animation-cartoon-explosive-smoke-sprite-frame-for-game-puff-motion-effect-explode-bomb-comic-boom-flash-fire-storyboard-atomic-blast-hit-energy-neat-vector_81894-7935 (4)_preview_rev_1.png').convert_alpha(),
]
# патроны
bullet_orientation = [
    pygame.image.load('images/texture/bullet/bullet_up.png').convert_alpha(),
    pygame.image.load('images/texture/bullet/bullet_down.png').convert_alpha(),
    pygame.image.load('images/texture/bullet/bullet_left.png').convert_alpha(),
    pygame.image.load('images/texture/bullet/bullet_right.png').convert_alpha(),
]

player_tank_1 = [
    pygame.image.load('images/texture/tank/p1/tank_up_p1.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p1/tank_down_p1.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p1/tank_left_p1.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p1/tank_right_p1.png').convert_alpha(),
]

player_tank_2 = [
    pygame.image.load('images/texture/tank/p2/tank_up_p2.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p2/tank_down_p2.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p2/tank_left_p2.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p2/tank_right_p2.png').convert_alpha(),
]
player_tank_3 = [
    pygame.image.load('images/texture/tank/p3/tank_up_p3.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p3/tank_down_p3.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p3/tank_left_p3.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p3/tank_right_p3.png').convert_alpha(),
]

player_tank_4 = [
    pygame.image.load('images/texture/tank/p4/tank_up_p4.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p4/tank_down_p4.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p4/tank_left_p4.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p4/tank_right_p4.png').convert_alpha(),
]

player_tank_5 = [
    pygame.image.load('images/texture/tank/p5/tank_up_p5.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p5/tank_down_p5.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p5/tank_left_p5.png').convert_alpha(),
    pygame.image.load('images/texture/tank/p5/tank_right_p5.png').convert_alpha(),
]


fon_menu_img = pygame.image.load('images/menu/menu_fon.jpg').convert_alpha()
fon_menu_img_shop = pygame.image.load('images/menu/menu_fon_shop.jpg').convert_alpha()

tank_menu_img = pygame.image.load('images/menu/menu_tank.png').convert_alpha()

bullet = pygame.image.load('images/texture/bullet/bullet_right.png')
