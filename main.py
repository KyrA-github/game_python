import sys
import random
import pygame

import json

# ДЛЯ ФПС
clock = pygame.time.Clock()
# ФПС
FPS = 70
block_cipher = None
# ИНИЦИЛИЗАЦИЯ
pygame.init()
# размер дисплея
screen = pygame.display.set_mode((1366, 718))
# НАЗВАНИЕ
pygame.display.set_caption("Battle Tanks")

# ИКОНКА импорт и замещение
icon = pygame.image.load('images/icon/icon.png').convert()
pygame.display.set_icon(icon)

# импорт изоброжений
import img
# взрыв
explosion = img.explosion
# патроны
bullet_orientation = img.bullet_orientation
# игроки
player_tank_p1 = [
    img.player_tank_1,
    img.player_tank_2,
    img.player_tank_3,
    img.player_tank_4,
    img.player_tank_5,
]
player_tank_p2 = [
    img.player_tank_1,
    img.player_tank_2,
    img.player_tank_3,
    img.player_tank_4,
    img.player_tank_5,
]

# аудио
audio_max = pygame.image.load('images/menu/audio_max.png').convert_alpha()
audio_min = pygame.image.load('images/menu/audio_min.png').convert_alpha()
# меню фон
fon_menu_img = img.fon_menu_img
fon_menu_img_shop = img.fon_menu_img_shop
# меню танк
tank_menu_img = img.tank_menu_img

# Шрифты
font_Red_Square = pygame.font.Font("fout/Red Square.ttf", 40)
font_Red_Square_60 = pygame.font.Font("fout/Red Square.ttf", 60)
font_Red_Square_70 = pygame.font.Font("fout/Red Square.ttf", 70)
font_better_vcr_60 = pygame.font.Font("fout/better-vcr_0.ttf", 45)

# надписи
text_start_button = font_Red_Square.render('PLAY', False, (255, 255, 255))
text_option_button = font_Red_Square.render('OPTIONS', False, (255, 255, 255))
text_shop_button = font_Red_Square.render('SHOP', False, (255, 255, 255))
text_exit_button = font_Red_Square.render('EXIT', False, (255, 255, 255))

LOGO = font_Red_Square_60.render('Battle Tanks', False, (32, 102, 0))

text_start_button_2 = font_Red_Square_60.render('PLAY', False, (255, 0, 255))
text_option_button_2 = font_Red_Square_60.render('OPTION', False, (255, 0, 255))
text_shop_button_2 = font_Red_Square_60.render('SHOP', False, (255, 0, 255))
text_exit_button_2 = font_Red_Square_60.render('EXIX', False, (255, 0, 255))

text_player_1_button = font_Red_Square.render('player 1', False, (255, 255, 255))
text_player_2_button = font_Red_Square.render('player 2', False, (255, 255, 255))

shop_home_text_button = font_Red_Square.render('exit', False, (200, 200, 200))

text_player_1_button_2 = font_Red_Square_60.render('player 1', False, (255, 0, 255))
text_player_2_button_2 = font_Red_Square_60.render('player 2', False, (255, 0, 255))

shop_home_text_button_2 = font_Red_Square_60.render('exit', False, (255, 0, 255))

win_player = font_Red_Square_60.render('WIN', False, (0, 112, 251))

win_player_game_win = font_Red_Square_60.render('Player 1', False, (0, 112, 251))
win_player_game_win2 = font_Red_Square_60.render('Player 2', False, (0, 112, 251))
win_player_menu = font_Red_Square_60.render('Menu', False, (255, 255, 255))
win_player_menu_1 = font_Red_Square_70.render('Menu', False, (255, 0, 255))




#изо патрона
# bullet = pygame.image.load("images/bullet.png")
# bullets = []
# bullets_num = 5

# меню


bullet = img.bullet
bullets = []
bullets_menu = 90
explosion_anim = 0
explosion_anim_1 = 0
explosion_anim_time = 0
explosion_anim_go = False
button_menu_new_text = 0



player_1_button_click = 0
player_2_button_click = 0

# # АУДИО


menu_audio_p = True
menu_audio_play = True
start_one = True
start_pvp_audio = True
audio_game_over = True

menu_audio_play_1 = 1
random_audio = 0

menu_audio_click = pygame.mixer.Sound('audio/button_rect.mp3')
menu_audio = pygame.mixer.Sound('audio/audio_menu_1.mp3')
start_pvp = pygame.mixer.Sound('audio/start.mp3')

boom_audio = pygame.mixer.Sound('audio/boom_audio.mp3')
game_over_audio = [
    pygame.mixer.Sound('audio/hahahahihihihehehe.mp3'),
    # pygame.mixer.Sound('audio/happy-wheels-z_uk-pobedy.mp3'),
    pygame.mixer.Sound('audio/kirya-pomedorkas-adventures-ost-z_uk-pobedy.mp3'),
    pygame.mixer.Sound('audio/menu_mem.mp3'),
    pygame.mixer.Sound('audio/well-be-right-back_qnufczo.mp3'),
]

grass_img = pygame.image.load('images/texture/brick/free-icon-wall-698633.png')

# ХОТЬБА СКОРОСТЬ
player_speed = 1
player_tank_go_1 = 0

player_1_x = 1297
player_1_y = 640

player_2_x = 3
player_2_y = 70

player_anim_1_b = 0
player_anim_2_b = 0

win_player_game = 1

bullets_pl = []
bullets_pl2 = []

game_over = False

boom_p2 = False
boom_p1 = False

player_anim_1 = 0
player_anim_2 = 1

game_play = 2

game_loser_menu_restart = False

player_tank_start = True

tic = 350
tic2 = 350

def handle_collision(el, i):
    global map_data
    y = 0
    for row in map_data:
        x = 0
        for tile in row:
            if tile == 1:
                tile_rect = pygame.Rect(x * 64, y * 64, 64, 64)
                if el.colliderect(tile_rect):
                    # При контакте с блоком (стеной) помечаем его как исчезнувший
                    map_data[y][x] = 0
                    bullets_pl.pop(i)
            x += 1
        y += 1

def handle_collision2(el, i):
    global map_data
    y = 0
    for row in map_data:
        x = 0
        for tile in row:
            if tile == 1:
                tile_rect = pygame.Rect(x * 64, y * 64, 64, 64)
                if el.colliderect(tile_rect):
                    # При контакте с блоком (стеной) помечаем его как исчезнувший
                    map_data[y][x] = 0
                    bullets_pl2.pop(i)
            x += 1
        y += 1



tile_size = 64




bool = True
while bool:
    mouse = pygame.mouse.get_pos()
    screen.fill((182, 178, 150))

    if game_play == 1:
        menu_audio.stop()
        if start_pvp_audio:
            start_one = True
            start_pvp.play()
            start_pvp_audio = False

            with open('map/map.json', 'r') as file:
                data = json.load(file)
                file.close()
            # Теперь у нас есть доступ к данным из JSON
            layers_data = data["layers"][0]['data']
            map_data_w = data["layers"][0]["width"]
            map_data_widht = map_data_w
            tile_size = data["tilewidth"]  # размер тайла
            chunked_data = [layers_data[i:i + map_data_widht] for i in range(0, len(layers_data), map_data_widht)]
            map_data = [chunk[:-1] for chunk in chunked_data]
            print(map_data)

        keys = pygame.key.get_pressed()
        player_rect = pygame.Rect(player_1_x, player_1_y, 60, 60)
        player_rect2 = pygame.Rect(player_2_x, player_2_y, 60, 60)
        tile_rects = []
        y = 0
        for row in map_data:
            x = 0
            for tile in row:
                if tile == 1:
                    screen.blit(grass_img, (x * 64, y * 64))
                    tile_rect = pygame.Rect(x * 64, y * 64, 64, 64)
                    tile_rects.append(tile_rect)

                x += 1
            y += 1

        # Сохраняем предыдущие позиции игрока для обработки столкновений
        player_x_prev, player_y_prev = player_1_x, player_1_y
        player_x_prev2, player_y_prev2 = player_2_x, player_2_y

        if game_over:
            game_over = False
            menu_audio_play = True
            game_play = 6
            player_1_x = 1297
            player_1_y = 640
            player_2_x = 3
            player_2_y = 70


        if keys[pygame.K_LEFT]:
            if player_1_x >= 0:
                player_1_x -= player_speed
            player_anim_1 = 2
        elif keys[pygame.K_RIGHT]:
            if player_1_x <= 1302:
                player_1_x += player_speed
            player_anim_1 = 3
        elif keys[pygame.K_UP]:
            if player_1_y >= 0:
                player_1_y -= player_speed
            player_anim_1 = 0
        elif keys[pygame.K_DOWN]:
            if player_1_y <= 654:
                player_1_y += player_speed
            player_anim_1 = 1

        if keys[pygame.K_a]:
            if player_2_x >= 0:
                player_2_x -= player_speed
            player_anim_2 = 2
        elif keys[pygame.K_d]:
            if player_2_x <= 1302:
                player_2_x += player_speed
            player_anim_2 = 3
        elif keys[pygame.K_w]:
            if player_2_y >= 0:
                player_2_y -= player_speed
            player_anim_2 = 0
        elif keys[pygame.K_s]:
            if player_2_y <= 654:
                player_2_y += player_speed
            player_anim_2 = 1

        # Проверка на столкновение с препятствиями (стенами)
        player_rect = pygame.Rect(player_1_x, player_1_y, 60, 60)
        for tile_rect in tile_rects:
            if player_rect.colliderect(tile_rect):
                player_1_x, player_1_y = player_x_prev, player_y_prev
                break

        player_rect2 = pygame.Rect(player_2_x, player_2_y, 60, 60)
        for tile_rect in tile_rects:
            if player_rect2.colliderect(tile_rect):
                player_2_x, player_2_y = player_x_prev2, player_y_prev2
                break

        # Рисуем игрока
        screen.blit(player_tank_p2[player_2_button_click][player_anim_2], (player_2_x, player_2_y))
        screen.blit(player_tank_p1[player_1_button_click][player_anim_1], (player_1_x, player_1_y))


        if bullets_pl:
            for (i, el) in enumerate(bullets_pl):
                screen.blit(bullet_orientation[player_anim_1_b], (el.x, el.y))

                if el.x >= 1370:
                    bullets_pl.pop(i)
                elif el.x <= 0:
                    bullets_pl.pop(i)
                elif el.y >= 720:
                    bullets_pl.pop(i)
                elif el.y <= 0:
                    bullets_pl.pop(i)

                if player_anim_1_b == 0:
                    el.y -= 10
                elif player_anim_1_b == 1:
                    el.y += 10
                elif player_anim_1_b == 2:
                    el.x -= 10
                elif player_anim_1_b == 3:
                    el.x += 10
                handle_collision(el, i)

                if player_rect2.colliderect(el):
                    bullets_pl.pop(i)
                    boom_p2 = True
        if bullets_pl2:
            for (i, el) in enumerate(bullets_pl2):
                screen.blit(bullet_orientation[player_anim_2_b], (el.x, el.y))

                if el.x >= 1370:
                    bullets_pl2.pop(i)
                elif el.x <= 0:
                    bullets_pl2.pop(i)
                elif el.y >= 720:
                    bullets_pl2.pop(i)
                elif el.y <= 0:
                    bullets_pl2.pop(i)

                if player_anim_2_b == 0:
                    el.y -= 10
                elif player_anim_2_b == 1:
                    el.y += 10
                elif player_anim_2_b == 2:
                    el.x -= 10
                elif player_anim_2_b == 3:
                    el.x += 10
                handle_collision2(el, i)

                if player_rect.colliderect(el):
                    bullets_pl2.pop(i)
                    boom_p1 = True

        if tic <= 150:
            tic += 1
        if tic2 <= 150:
            tic2 += 1

        if boom_p2:
            if explosion_anim <= 30:
                screen.blit(explosion[0], (player_2_x, player_2_y))
                explosion_anim += 1
            else:
                explosion_anim = 0
                boom_p2 = False
                game_over = True
                win_player_game = 1
        if boom_p1:
            if explosion_anim_1 <= 30:
                screen.blit(explosion[0], (player_1_x, player_1_y))
                explosion_anim_1 += 1
            else:
                explosion_anim_1 = 0
                boom_p1 = False
                game_over = True
                win_player_game = 2

        # Отобразите изменения на экране
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.KEYUP and event.key == pygame.K_KP1:
                if tic >= 150:
                    player_anim_1_b = player_anim_1
                    if player_anim_1_b == 0:
                        bullets_pl.append(
                            bullet_orientation[player_anim_1_b].get_rect(topleft=(player_1_x + 25, player_1_y)))
                    elif player_anim_1_b == 1:
                        bullets_pl.append(
                            bullet_orientation[player_anim_1_b].get_rect(topleft=(player_1_x + 25, player_1_y + 60)))
                    elif player_anim_1_b == 2:
                        bullets_pl.append(
                            bullet_orientation[player_anim_1_b].get_rect(topleft=(player_1_x, player_1_y + 25)))
                    elif player_anim_1_b == 3:
                        bullets_pl.append(
                            bullet_orientation[player_anim_1_b].get_rect(topleft=(player_1_x + 60, player_1_y + 25)))
                    boom_audio.play()
                    tic = 0
            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                if tic2 >= 150:
                    player_anim_2_b = player_anim_2
                    if player_anim_2_b == 0:
                        bullets_pl2.append(
                            bullet_orientation[player_anim_2_b].get_rect(topleft=(player_2_x + 25, player_2_y)))
                    elif player_anim_2_b == 1:
                        bullets_pl2.append(
                            bullet_orientation[player_anim_2_b].get_rect(topleft=(player_2_x + 25, player_2_y + 60)))
                    elif player_anim_2_b == 2:
                        bullets_pl2.append(
                            bullet_orientation[player_anim_2_b].get_rect(topleft=(player_2_x, player_2_y + 25)))
                    elif player_anim_2_b == 3:
                        bullets_pl2.append(
                            bullet_orientation[player_anim_2_b].get_rect(topleft=(player_2_x + 60, player_2_y + 25)))
                    boom_audio.play()
                    tic2 = 0
    elif game_play == 2:
        game_over_audio[random_audio].stop()
        start_pvp_audio = True
        player_anim_1 = 0
        player_anim_2 = 1
        audio_game_over = True


        start_button_rect = text_start_button.get_rect(topleft=(100, 50))
        option_button_rect = text_option_button.get_rect(topleft=(100, 100))
        shop_button_rect = text_shop_button.get_rect(topleft=(100, 150))
        exit_button_rect = text_exit_button.get_rect(topleft=(100, 200))
        audio_rect = audio_max.get_rect(topleft=(1292, 644))

        screen.blit(fon_menu_img, (0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if start_button_rect.collidepoint(mouse_x, mouse_y):
            button_menu_new_text = 1
            if menu_audio_p:
                menu_audio_click.play(0)
                menu_audio_p = False
        elif option_button_rect.collidepoint(mouse_x, mouse_y):
            button_menu_new_text = 2
            if menu_audio_p:
                menu_audio_click.play(0)
                menu_audio_p = False
        elif shop_button_rect.collidepoint(mouse_x, mouse_y):
            button_menu_new_text = 3
            if menu_audio_p:
                menu_audio_click.play(0)
                menu_audio_p = False
        elif exit_button_rect.collidepoint(mouse_x, mouse_y):
            button_menu_new_text = 4
            if menu_audio_p:
                menu_audio_click.play(0)
                menu_audio_p = False
        else:
            button_menu_new_text = 0
            menu_audio_p = True



        if button_menu_new_text == 1:
            screen.blit(text_start_button_2, (100, 50))
            screen.blit(text_option_button, (100, 110))
            screen.blit(text_shop_button, (100, 160))
            screen.blit(text_exit_button, (100, 210))

        elif button_menu_new_text == 2:
            screen.blit(text_start_button, (100, 40))
            screen.blit(text_option_button_2, (100, 100))
            screen.blit(text_shop_button, (100, 160))
            screen.blit(text_exit_button, (100, 210))

        elif button_menu_new_text == 3:
            screen.blit(text_start_button, (100, 40))
            screen.blit(text_option_button, (100, 90))
            screen.blit(text_shop_button_2, (100, 150))
            screen.blit(text_exit_button, (100, 210))

        elif button_menu_new_text == 4:
            screen.blit(text_start_button, (100, 40))
            screen.blit(text_option_button, (100, 90))
            screen.blit(text_shop_button, (100, 140))
            screen.blit(text_exit_button_2, (100, 200))

        else:
            screen.blit(text_start_button, (100, 50))
            screen.blit(text_option_button, (100, 100))
            screen.blit(text_shop_button, (100, 150))
            screen.blit(text_exit_button, (100, 200))

        screen.blit(LOGO, (870, 50))

        if menu_audio_play:
            screen.blit(audio_max, (1292, 644))
            if start_one:
                menu_audio.play(-1)
                menu_audio_play_1 = 2
                start_one = False
        else:
            screen.blit(audio_min, (1292, 644))


        screen.blit(tank_menu_img, (200, 555))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and start_button_rect.collidepoint(mouse):
                if event.button == 1:
                    game_play = 1
                    player_tank_start = True
            elif event.type == pygame.MOUSEBUTTONUP and option_button_rect.collidepoint(mouse):
                if event.button == 1:
                    game_play = 6
            elif event.type == pygame.MOUSEBUTTONUP and shop_button_rect.collidepoint(mouse):
                if event.button == 1:
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and exit_button_rect.collidepoint(mouse):
                if event.button == 1:
                    bool = False
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and audio_rect.collidepoint(mouse):
                if event.button == 1:
                    if menu_audio_play_1 == 1:
                        menu_audio.play(-1)
                        menu_audio_play_1 = 2
                        menu_audio_play = True
                    else:
                        menu_audio.stop()
                        menu_audio_play_1 = 1
                        menu_audio_play = False
            elif event.type == pygame.QUIT:
                bool = False
                pygame.quit()
                sys.exit()

        if bullets_menu == 300:
            bullets_menu = 0
            bullets.append(bullet.get_rect(topleft=(200 + 65, 555 + 20)))
        else:
            bullets_menu += 1

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet,(el.x, el.y))
                el.x += 10
                if el.x > 1200:
                    bullets.pop(i)
                    explosion_anim_go = True

        if explosion_anim_go:
            if explosion_anim <= 30:
                screen.blit(explosion[0],(1200, 550))
                explosion_anim +=1
                explosion_anim_time = 0
            else:
                explosion_anim = 0
                explosion_anim_go = False






        # if start_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        #     print(12)
    elif game_play == 3:

        screen.blit(fon_menu_img, (0, 0))

        audio_rect = audio_max.get_rect(topleft=(1292, 644))
        player_1_button_rect_p1 = text_player_1_button.get_rect(topleft=(100, 50))
        player_2_button_rect_p2 = text_player_2_button.get_rect(topleft=(100, 150))
        text_rect_exit_menu = shop_home_text_button.get_rect(topleft=(100, 250))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if player_1_button_rect_p1.collidepoint(mouse_x, mouse_y):
            button_menu_new_text = 1
            if menu_audio_p:
                menu_audio_click.play(0)
                menu_audio_p = False
        elif player_2_button_rect_p2.collidepoint(mouse_x, mouse_y):
            button_menu_new_text = 2
            if menu_audio_p:
                menu_audio_click.play(0)
                menu_audio_p = False
        elif text_rect_exit_menu.collidepoint(mouse_x, mouse_y):
            button_menu_new_text = 3
            if menu_audio_p:
                menu_audio_click.play(0)
                menu_audio_p = False
        else:
            button_menu_new_text = 0
            menu_audio_p = True

        if button_menu_new_text == 1:
            screen.blit(text_player_1_button_2, (100, 50))
            screen.blit(player_tank_p1[player_1_button_click][0], (400, 35))
            screen.blit(text_player_2_button, (100, 160))
            screen.blit(shop_home_text_button, (100, 260))
            screen.blit(player_tank_p2[player_2_button_click][0], (300, 145))
        elif button_menu_new_text == 2:
            screen.blit(text_player_1_button, (100, 40))
            screen.blit(text_player_2_button_2, (100, 150))
            screen.blit(player_tank_p2[player_2_button_click][0], (400, 135))
            screen.blit(shop_home_text_button, (100, 260))
            screen.blit(player_tank_p1[player_1_button_click][0], (300, 25))
        elif button_menu_new_text == 3:
            screen.blit(text_player_1_button, (100, 40))
            screen.blit(text_player_2_button, (100, 140))
            screen.blit(shop_home_text_button_2, (100, 250))
            screen.blit(player_tank_p1[player_1_button_click][0], (300, 25))
            screen.blit(player_tank_p2[player_2_button_click][0], (300, 125))
        else:
            screen.blit(shop_home_text_button, (100, 250))
            screen.blit(text_player_1_button, (100, 50))
            screen.blit(text_player_2_button, (100, 150))
            screen.blit(player_tank_p1[player_1_button_click][0], (300, 35))
            screen.blit(player_tank_p2[player_2_button_click][0], (300, 135))


        if menu_audio_play:
            screen.blit(audio_max, (1292, 644))
            if start_one:
                menu_audio.play(-1)
                menu_audio_play_1 = 2
                start_one = False
        else:
            screen.blit(audio_min, (1292, 644))

        screen.blit(tank_menu_img, (200, 555))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and player_1_button_rect_p1.collidepoint(mouse):
                if event.button == 1:
                    game_play = 4
            elif event.type == pygame.MOUSEBUTTONUP and player_2_button_rect_p2.collidepoint(mouse):
                if event.button == 1:
                    game_play = 5
            elif event.type == pygame.MOUSEBUTTONUP and text_rect_exit_menu.collidepoint(mouse):
                if event.button == 1:
                    game_play = 2
            elif event.type == pygame.MOUSEBUTTONUP and audio_rect.collidepoint(mouse):
                if event.button == 1:
                    if menu_audio_play_1 == 1:
                        menu_audio.play(-1)
                        menu_audio_play_1 = 2
                        menu_audio_play = True
                    else:
                        menu_audio.stop()
                        menu_audio_play_1 = 1
                        menu_audio_play = False
            elif event.type == pygame.QUIT:
                bool = False
                pygame.quit()
                sys.exit()


        if bullets_menu == 300:
            bullets_menu = 0
            bullets.append(bullet.get_rect(topleft=(200 + 65, 555 + 20)))
        else:
            bullets_menu += 1

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet,(el.x, el.y))
                el.x += 10
                if el.x > 1200:
                    bullets.pop(i)
                    explosion_anim_go = True

        if explosion_anim_go:
            if explosion_anim <= 30:
                screen.blit(explosion[0],(1200, 550))
                explosion_anim +=1
                explosion_anim_time = 0
            else:
                explosion_anim = 0
                explosion_anim_go = False
    elif game_play == 4:
        screen.blit(fon_menu_img, (0, 0))

        audio_rect = audio_max.get_rect(topleft=(1292, 644))
        player_rect_1_button = player_tank_p1[0][0].get_rect(topleft=(100, 35))
        player_rect_2_button = player_tank_p1[1][0].get_rect(topleft=(200, 35))
        player_rect_3_button = player_tank_p1[2][0].get_rect(topleft=(300, 35))
        player_rect_4_button = player_tank_p1[3][0].get_rect(topleft=(400, 35))
        player_rect_5_button = player_tank_p1[4][0].get_rect(topleft=(500, 35))

        screen.blit(player_tank_p1[0][0], (100, 35))
        screen.blit(player_tank_p1[1][0], (200, 35))
        screen.blit(player_tank_p1[2][0], (300, 35))
        screen.blit(player_tank_p1[3][0], (400, 35))
        screen.blit(player_tank_p1[4][0], (500, 35))





        if menu_audio_play:
            screen.blit(audio_max, (1292, 644))
            if start_one:
                menu_audio.play(-1)
                menu_audio_play_1 = 2
                start_one = False
        else:
            screen.blit(audio_min, (1292, 644))

        screen.blit(tank_menu_img, (200, 555))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP and audio_rect.collidepoint(mouse):
                if event.button == 1:
                    if menu_audio_play_1 == 1:
                        menu_audio.play(-1)
                        menu_audio_play_1 = 2
                        menu_audio_play = True
                    else:
                        menu_audio.stop()
                        menu_audio_play_1 = 1
                        menu_audio_play = False

            elif event.type == pygame.MOUSEBUTTONUP and player_rect_1_button.collidepoint(mouse):
                if event.button == 1:
                    player_1_button_click = 0
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_2_button.collidepoint(mouse):
                if event.button == 1:
                    player_1_button_click = 1
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_3_button.collidepoint(mouse):
                if event.button == 1:
                    player_1_button_click = 2
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_4_button.collidepoint(mouse):
                if event.button == 1:
                    player_1_button_click = 3
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_5_button.collidepoint(mouse):
                if event.button == 1:
                    player_1_button_click = 4
                    game_play = 3


            elif event.type == pygame.QUIT:
                bool = False
                pygame.quit()
                sys.exit()

        if bullets_menu == 300:
            bullets_menu = 0
            bullets.append(bullet.get_rect(topleft=(200 + 65, 555 + 20)))
        else:
            bullets_menu += 1

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 10
                if el.x > 1200:
                    bullets.pop(i)
                    explosion_anim_go = True

        if explosion_anim_go:
            if explosion_anim <= 30:
                screen.blit(explosion[0], (1200, 550))
                explosion_anim += 1
                explosion_anim_time = 0
            else:
                explosion_anim = 0
                explosion_anim_go = False
    elif game_play == 5:
        screen.blit(fon_menu_img, (0, 0))

        audio_rect = audio_max.get_rect(topleft=(1292, 644))

        player_rect_1_button = player_tank_p2[0][0].get_rect(topleft=(100, 35))
        player_rect_2_button = player_tank_p2[1][0].get_rect(topleft=(200, 35))
        player_rect_3_button = player_tank_p2[2][0].get_rect(topleft=(300, 35))
        player_rect_4_button = player_tank_p2[3][0].get_rect(topleft=(400, 35))
        player_rect_5_button = player_tank_p2[4][0].get_rect(topleft=(500, 35))

        screen.blit(player_tank_p2[0][0], (100, 35))
        screen.blit(player_tank_p2[1][0], (200, 35))
        screen.blit(player_tank_p2[2][0], (300, 35))
        screen.blit(player_tank_p2[3][0], (400, 35))
        screen.blit(player_tank_p2[4][0], (500, 35))

        if menu_audio_play:
            screen.blit(audio_max, (1292, 644))
            if start_one:
                menu_audio.play(-1)
                menu_audio_play_1 = 2
                start_one = False
        else:
            screen.blit(audio_min, (1292, 644))

        screen.blit(tank_menu_img, (200, 555))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP and audio_rect.collidepoint(mouse):
                if event.button == 1:
                    if menu_audio_play_1 == 1:
                        menu_audio.play(-1)
                        menu_audio_play_1 = 2
                        menu_audio_play = True
                    else:
                        menu_audio.stop()
                        menu_audio_play_1 = 1
                        menu_audio_play = False

            elif event.type == pygame.MOUSEBUTTONUP and player_rect_1_button.collidepoint(mouse):
                if event.button == 1:
                    player_2_button_click = 0
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_2_button.collidepoint(mouse):
                if event.button == 1:
                    player_2_button_click = 1
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_3_button.collidepoint(mouse):
                if event.button == 1:
                    player_2_button_click = 2
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_4_button.collidepoint(mouse):
                if event.button == 1:
                    player_2_button_click = 3
                    game_play = 3
            elif event.type == pygame.MOUSEBUTTONUP and player_rect_5_button.collidepoint(mouse):
                if event.button == 1:
                    player_2_button_click = 4
                    game_play = 3


            elif event.type == pygame.QUIT:
                bool = False
                pygame.quit()
                sys.exit()

        if bullets_menu == 300:
            bullets_menu = 0
            bullets.append(bullet.get_rect(topleft=(200 + 65, 555 + 20)))
        else:
            bullets_menu += 1

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 10
                if el.x > 1200:
                    bullets.pop(i)
                    explosion_anim_go = True

        if explosion_anim_go:
            if explosion_anim <= 30:
                screen.blit(explosion[0], (1200, 550))
                explosion_anim += 1
                explosion_anim_time = 0
            else:
                explosion_anim = 0
                explosion_anim_go = False
    elif game_play == 6:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_rect_menu = win_player_menu.get_rect(topleft=(565, 400))



        if audio_game_over:
            random_audio = random.randint(0, 3)
            game_over_audio[random_audio].play()
            audio_game_over = False

        if player_rect_menu.collidepoint(mouse_x, mouse_y):
            screen.blit(win_player_menu_1, (545, 400))
        else:
            screen.blit(win_player_menu, (565, 400))

        if win_player_game == 1:
            screen.blit(win_player,(585, 280))
            screen.blit(win_player_game_win,(520, 340))
        elif win_player_game == 2:
            screen.blit(win_player, (585, 280))
            screen.blit(win_player_game_win2, (520, 340))



        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and player_rect_menu.collidepoint(mouse):
                if event.button == 1:
                    game_play = 2
            elif event.type == pygame.QUIT:
                bool = False
                pygame.quit()
                sys.exit()



        


    # ОБНОВЛЕНИЯ ДИСПЛЕЯ
    pygame.display.update()

    #  ОТСЛЕЖИВАНИЯ эвентов

    for event in pygame.event.get():
        #  ВЫХОД
        if event.type == pygame.QUIT:
            bool = False
            pygame.quit()
            sys.exit()

    # ЛИМИН ФПС
    clock.tick(FPS)

    # elif event.type == pygame.MOUSEBUTTONUP and start_button_rect.collidepoint(mouse):
    #     if event.button == 1:
    #         game_play = 1
    #         player_tank_start = True
    # elif event.type == pygame.MOUSEBUTTONUP and option_button_rect.collidepoint(mouse):
    #     if event.button == 1:
    #         print('option')
    # elif event.type == pygame.MOUSEBUTTONUP and shop_button_rect.collidepoint(mouse):
    #     if event.button == 1:
    #         print('shop')
    # elif event.type == pygame.MOUSEBUTTONUP and exit_button_rect.collidepoint(mouse):
    #     if event.button == 1:
    #         bool = False
    #         pygame.quit()
    #         sys.exit()
    # elif start_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
    #     print(1)






    # отслежуем выполнени таймера врагов
    # if game_play and event.type == pygame.KEYUP and event.key == pygame.K_DOWN and bullets_num > 0:
    #     bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 20)))
    #     bullets_num -= 1


        #хитбоксы
        # player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))
        # #враг
        # if ghost_list_in_game:
        #     for(i, el) in enumerate(ghost_list_in_game):
        #         screen.blit(ghost, el)
        #         el.x -= 10
        #         if el.x < -20:
        #             ghost_list_in_game.pop(i)
                #жизнь
                # #отслеживание соприкосновения хитбоксов
                # if player_rect.colliderect(el):
                #     game_play = False

    # ОТСЛЕЖОВАНИЕ КЛАВИШ

    # #АНИМАЦИЯ ХОТЬБЫ
    #     if keys[pygame.K_LEFT]:
    #         screen.blit(walk_left[player_anim], (player_x, player_y))
    #     elif keys[pygame.K_RIGHT]:
    #         screen.blit(walk_rigth[player_anim], (player_x, player_y))
    #     else:
    #         screen.blit(player_stop_walk_animet, (player_x, player_y))
    #     # ХОТЬБА
    #     if keys[pygame.K_LEFT] and player_x > 20:
    #         player_x -= player_speed
    #     elif keys[pygame.K_RIGHT] and player_x < 600:
    #         player_x += player_speed



        # АНИМАЦИЯ игрока
        # if player_anim == 3:
        #     player_anim = 0
        # else:
        #     player_anim += 1


        #
        # if bullets:
        #     for (i, el) in enumerate(bullets):
        #         screen.blit(bullet,(el.x, el.y))
        #         el.x += 10
        #         if el.x > 620:
        #             bullets.pop(i)
        #         if ghost_list_in_game:
        #             for (index, ghost_el) in enumerate(ghost_list_in_game):
        #                 if el.colliderect(ghost_el):
        #                     ghost_list_in_game.pop(index)
        #                     bullets.pop(i)









#
    # pygame.draw.circle(screen, 'Red', (2, 1), 30)
    # screen.blit(square, (10, 10))
    # screen.blit(text_surface,(100,100))

# elif event.type == pygame.KEYDOWN:
#     if event.key == pygame.K_a:
#         screen.fill((255, 0, 255))