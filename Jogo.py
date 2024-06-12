import pygame
from pygame.locals import *

import random
import def_images
import variaveis
import funcoes

screen = pygame.display.set_mode((variaveis.WIDTH, variaveis.HEIGHT), RESIZABLE)
clock = pygame.time.Clock()
pygame.init()

def game_loop():
    global key, evento, retangulo_play, retangulo_quit
    executando = True
    musica_tocando = False
    funcoes.musica()

    fase = 0
    frames_vermelho = 0
    vidas = 5

    x = 0
    y = 0
    z = 0
    s = 0
    b = 0
    e = 0
    f = 0
    u = 0
    j = 0
    d = 0
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0

    score = 0
    col_fase1 = 0
    vitoria_fase_1 = 5

    col_fase2 = 550
    tempo_fase2 = 1
    vitoria_fase_2 = 10

    imagem_fase3 = -1880
    col_fase3 = 100
    lin_fase3 = 544
    subida_escada = 114
    escada = False

    col_fase4 = 100
    lin_fase4 = 556
    tempo_fase4 = 1
    #tempo_fase4 = 7000
    tempo_inicio_cronometro = 7000
    tempo_atual = tempo_inicio_cronometro
    vidas_fase4 = 4
    abaixando = 0

    pulando = False
    no_chao = True
    altura_pulo = 0
    velocidade_vertical = 0
    limite_inferior = 555

    cima1 = cima2 = cima3 = cima4 = 'v'
    linha_b1 = linha_b2 = 100
    linha_b3 = linha_b4 = 630

    velocidade_b1 = random.randint(5, 6)
    velocidade_b2 = random.randint(4, 5)
    velocidade_b3 = random.randint(4, 5)
    velocidade_b4 = random.randint(5, 6)

    if velocidade_b1 == velocidade_b2:
        velocidade_b1 = random.randint(4, 5)
        if velocidade_b1 == velocidade_b2:
            velocidade_b1 = random.randint(4, 5)
            if velocidade_b1 == velocidade_b2:
                velocidade_b1 = random.randint(4, 5)
                if velocidade_b1 == velocidade_b2:
                    velocidade_b1 = random.randint(4, 5)
    if velocidade_b3 == velocidade_b4:
        velocidade_b3 = random.randint(5, 6)
        if velocidade_b3 == velocidade_b4:
            velocidade_b3 = random.randint(5, 6)
            if velocidade_b3 == velocidade_b4:
                velocidade_b3 = random.randint(5, 6)
                if velocidade_b3 == velocidade_b4:
                    velocidade_b3 = random.randint(5, 6)

    foguete1_vertical_fase2 = -1200
    foguete2_vertical_fase2 = -1110
    foguete3_vertical_fase2 = -1300
    foguete4_horizontal_fase2 = -1024
    foguete5_horizontal_fase2 = 3048

    velocidade_foguete1 = random.randint(3, 4)
    velocidade_foguete2 = random.randint(3, 4)
    velocidade_foguete3 = random.randint(3, 4)

    posicao_foguete1_fase2 = random.randint(180, 290)
    posicao_foguete2_fase2 = random.randint(420, 490)
    posicao_foguete3_fase2 = random.randint(620, 730)

    limite_esquerda_foguete1 = posicao_foguete1_fase2 - 30
    limite_direita_foguete1 = posicao_foguete1_fase2 + 80

    limite_esquerda_foguete2 = posicao_foguete2_fase2 - 30
    limite_direita_foguete2 = posicao_foguete2_fase2 + 80

    limite_esquerda_foguete3 = posicao_foguete3_fase2 - 30
    limite_direita_foguete3 = posicao_foguete3_fase2 + 80

    escada1_x = 475
    escada2_x = 805
    escada3_x = 390
    escada4_x = 640
    num_escada = 0
    diferenca = 0

    barril1_x = barril5_x = barril9_x = barril13_x = 1500
    barril2_x = barril6_x = barril10_x = barril14_x = -300
    barril3_x = barril7_x = barril11_x = barril15_x = 1600
    barril4_x = barril8_x = barril12_x = -30
    velocidade_minima_barril = 2
    velocidade_maxima_barril = 3
    velocidade_barril1 = random.randint(velocidade_minima_barril, velocidade_maxima_barril)
    velocidade_barril2 = random.randint(velocidade_minima_barril, velocidade_maxima_barril)
    velocidade_barril3 = random.randint(velocidade_minima_barril, velocidade_maxima_barril)
    velocidade_barril4 = random.randint(velocidade_minima_barril, velocidade_maxima_barril)

    foguete_final_1 = -50
    foguete_final_2 = 0

    fireball1_vertical = -2200
    fireball2_vertical = -2600
    fireball3_vertical = -2800
    fireball4_vertical = -2400
    fireball5_vertical = -3000
    fireball6_vertical = -2800
    fireball7_vertical = -2600
    fireball8_vertical = -2200
    fireball9_horizontal = 4050
    fireball10_horizontal = 5000
    fireball11_horizontal = 5950
    fireball12_horizontal = 6900

    velocidade_fireball1 = random.randint(2, 3)
    velocidade_fireball2 = random.randint(2, 3)
    velocidade_fireball3 = random.randint(2, 3)
    velocidade_fireball4 = random.randint(2, 3)
    velocidade_fireball5 = random.randint(2, 3)
    velocidade_fireball6 = random.randint(2, 3)
    velocidade_fireball7 = random.randint(2, 3)
    velocidade_fireball8 = random.randint(2, 3)
    velocidade_fireball9 = 5
    velocidade_fireball10 = 5
    velocidade_fireball11 = 5
    velocidade_fireball12 = 5

    posicao_fireball1 = random.randint(1, 87)
    posicao_fireball2 = random.randint(137, 224)
    posicao_fireball3 = random.randint(274, 361)
    posicao_fireball4 = random.randint(411, 498)
    posicao_fireball5 = random.randint(548, 635)
    posicao_fireball6 = random.randint(685, 772)
    posicao_fireball7 = random.randint(822, 909)
    posicao_fireball8 = random.randint(959, 974)
    posicao_fireball9 = 581
    posicao_fireball10 = 516
    posicao_fireball11 = 581
    posicao_fireball12 = 516

    limite_esquerda_fireball1 = posicao_fireball1 - 35
    limite_direita_fireball1 = posicao_fireball1 + 15
    limite_esquerda_fireball2 = posicao_fireball2 - 35
    limite_direita_fireball2 = posicao_fireball2 + 15
    limite_esquerda_fireball3 = posicao_fireball3 - 35
    limite_direita_fireball3 = posicao_fireball3 + 15
    limite_esquerda_fireball4 = posicao_fireball4 - 35
    limite_direita_fireball4 = posicao_fireball4 + 15
    limite_esquerda_fireball5 = posicao_fireball5 - 35
    limite_direita_fireball5 = posicao_fireball5 + 15

    while executando:
        pygame.display.flip()
        clock.tick(variaveis.FPS)

        # INICIO
        if fase == 0:

            # Imagem de Fundo
            screen.blit(def_images.bg_inicio, (0, 0))

            # Botão play
            screen.blit(def_images.play_img, (70, 250))

            # Botão exit
            screen.blit(def_images.exit_img, (83, 370))

            # Captura de Tecla
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN] == True or key[pygame.K_KP_ENTER] == True or key[pygame.K_RIGHT] == True or key[pygame.K_SPACE] == True:
                fase+=1
            elif key[pygame.K_ESCAPE] == True:
                executando = False

        # FASE 1
        elif fase == 1:
            # Imagem de Fundo
            screen.blit(def_images.bg_fase1, (0, 0))

            # Personagem principal
            # Captura de Teclas
            if vidas > 0 and score < vitoria_fase_1:
                key = pygame.key.get_pressed()
                if key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
                    col_fase1, _, x = funcoes.personagem.personagem_movimento_direta(col_fase1, 379, 4.5, x)
                elif key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
                    col_fase1, _, y = funcoes.personagem.personagem_movimento_esquerda(col_fase1, 379, 4.5, y)
                else:
                    funcoes.personagem.personagem_parado(col_fase1, 382)
            else:
                funcoes.personagem.personagem_parado(col_fase1, 382)

            # limite na tela
            if col_fase1 > 1024:
                col_fase1 = -20
                score += 1
                z += 1
                velocidade_b1 += 1
                velocidade_b2 += 1
                velocidade_b3 += 1
                velocidade_b4 += 1
            elif col_fase1 < -20:
                col_fase1 += 3.5

            # foguete 1
            linha_b1 = funcoes.obstaculos.foguete(120, linha_b1, cima1, velocidade_b1)
            if linha_b1 > 580:
                cima1 = 'f'
            elif linha_b1 < 50:
                cima1 = 'v'

            # foguete 2
            linha_b2 = funcoes.obstaculos.foguete(320, linha_b2, cima2, velocidade_b2)
            if linha_b2 > 580:
                cima2 = 'f'
            if linha_b2 < 50:
                cima2 = 'v'

            # foguete 3
            linha_b3 = funcoes.obstaculos.foguete(620, linha_b3, cima3, velocidade_b3)
            if linha_b3 > 580:
                cima3 = 'f'
            if linha_b3 < 50:
                cima3 = 'v'

            # foguete 4
            linha_b4 = funcoes.obstaculos.foguete(820, linha_b4, cima4, velocidade_b4)
            if linha_b4 > 580:
                cima4 = 'f'
            if linha_b4 < 50:
                cima4 = 'v'

            # Colisão
            # Foguete 1
            if ((col_fase1 >= 80 and col_fase1 <= 204) and (linha_b1 >= 292 and linha_b1 <= 456)):
                vidas -= 1
                col_fase1 = -20
                frames_vermelho = 2.5
            # Foguete 2
            elif ((col_fase1 >= 280 and col_fase1 <= 404) and (linha_b2 >= 292 and linha_b2 <= 456)):
                vidas -= 1
                col_fase1 = -20
                frames_vermelho = 2.5
            # Foguete 3
            elif ((col_fase1 >= 580 and col_fase1 <= 704) and (linha_b3 >= 292 and linha_b3 <= 456)):
                vidas -= 1
                col_fase1 = -20
                frames_vermelho = 2.5
            # Foguete 4
            elif ((col_fase1 >= 780 and col_fase1 <= 904) and (linha_b4 >= 292 and linha_b4 <= 456)):
                vidas -= 1
                col_fase1 = -20
                frames_vermelho = 2.5

            # Pontuação
            screen.blit(def_images.numeros[z], (900, 40))
            if score >= vitoria_fase_1:
                if not musica_tocando:
                    funcoes.musica_vitoria()
                    musica_tocando = True
                funcoes.proximo_nivel()
                fase += 1
                vidas = 5
                score = 0
                z = 0
                f += 1
                pygame.display.flip()
                pygame.time.delay(6500)

        # FASE 2
        elif fase == 2:
            #Imagem fundo
            screen.blit(def_images.bg_fase2, (0, 0))
            tempo_fase2 += 1

            if musica_tocando:
                funcoes.musica()
                musica_tocando = False

            # Pontuação
            if score < vitoria_fase_2:
                if score % 2 == 0:
                    screen.blit(def_images.star, (160, 590))
                    if col_fase2 <= 195:
                        score +=1
                        z += 1
                elif score % 2 == 1:
                    screen.blit(def_images.star, (850, 590))
                    if col_fase2 >= 785:
                        score +=1
                        z += 1

            # Movimento do Personagem
            if vidas > 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_DOWN] == True or key[pygame.K_s] == True:
                    _, s = funcoes.personagem.personagem_agachado(col_fase2, 560, s)
                elif key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
                    col_fase2, _, x = funcoes.personagem.personagem_movimento_direta(col_fase2, 556, 4.5, x)
                elif key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
                    col_fase2, _, y = funcoes.personagem.personagem_movimento_esquerda(col_fase2, 556, 4.5, y)
                else:
                    s = 0
                    funcoes.personagem.personagem_parado(col_fase2, 556)
            else:
                s = 0
                funcoes.personagem.personagem_parado(col_fase2, 556)

            # Limite na tela
            if col_fase2 > 880:
                col_fase2 -= 4.5
            elif col_fase2 < 80:
                col_fase2 += 4.5

            # Foguetes
            # foguete 1
            foguete1_vertical_fase2 = funcoes.obstaculos.foguete(posicao_foguete1_fase2, foguete1_vertical_fase2, "v", velocidade_foguete1)
            if foguete1_vertical_fase2 > 968:
                limite_esquerda_foguete1, limite_direita_foguete1, foguete1_vertical_fase2, velocidade_foguete1, posicao_foguete1_fase2 = funcoes.obstaculos.limite_foguete_vertical_fase2(
                    foguete1_vertical_fase2,120,275)

            # foguete 2
            foguete2_vertical_fase2 = funcoes.obstaculos.foguete(posicao_foguete2_fase2, foguete2_vertical_fase2, "v", velocidade_foguete2)
            if foguete2_vertical_fase2 > 968:
                limite_esquerda_foguete2, limite_direita_foguete2, foguete2_vertical_fase2, velocidade_foguete2, posicao_foguete2_fase2 = funcoes.obstaculos.limite_foguete_vertical_fase2(
                    foguete2_vertical_fase2,400,515)

            # foguete 3
            foguete3_vertical_fase2 = funcoes.obstaculos.foguete(posicao_foguete3_fase2, foguete3_vertical_fase2, "v", velocidade_foguete3)
            if foguete3_vertical_fase2 > 968:
                limite_esquerda_foguete3, limite_direita_foguete3, foguete3_vertical_fase2, velocidade_foguete3, posicao_foguete3_fase2 = funcoes.obstaculos.limite_foguete_vertical_fase2(
                    foguete3_vertical_fase2, 640, 795)

            # foguete 4
            foguete4_horizontal_fase2 = funcoes.obstaculos.foguete_horizontal(foguete4_horizontal_fase2, "d")
            if foguete4_horizontal_fase2 >= 2048:
                foguete4_horizontal_fase2 = -256

            # foguete 5
            foguete5_horizontal_fase2 = funcoes.obstaculos.foguete_horizontal(foguete5_horizontal_fase2, "e")
            if foguete5_horizontal_fase2 <= -1024:
                foguete5_horizontal_fase2 = 1280

            # Colisão
            if ((col_fase2 >= limite_esquerda_foguete1 and col_fase2 <= limite_direita_foguete1) and (foguete1_vertical_fase2 >= 470 and foguete1_vertical_fase2 <= 634)):
                col_fase2 = 447
                foguete2_vertical_fase2 = -210
                vidas -= 1
                frames_vermelho = 2.5
            if ((col_fase2 >= limite_esquerda_foguete2 and col_fase2 <= limite_direita_foguete2) and (foguete2_vertical_fase2 >= 470 and foguete2_vertical_fase2 <= 634)):
                col_fase2 = 447
                foguete2_vertical_fase2 = -210
                vidas -= 1
                frames_vermelho = 2.5
            if ((col_fase2 >= limite_esquerda_foguete3 and col_fase2 <= limite_direita_foguete3) and (foguete3_vertical_fase2 >= 470 and foguete3_vertical_fase2 <= 634)):
                col_fase2 = 447
                foguete2_vertical_fase2 = -210
                vidas -= 1
                frames_vermelho = 2.5
            if ((col_fase2 >= (foguete4_horizontal_fase2) and col_fase2 <= (foguete4_horizontal_fase2 + 110)) and (key[pygame.K_DOWN] == False and key[pygame.K_s] == False)):
                col_fase2 = 447
                foguete2_vertical_fase2 = -210
                foguete4_horizontal_fase2 = -256
                foguete5_horizontal_fase2 = 2304
                vidas -= 1
                frames_vermelho = 2.5
            if ((col_fase2 >= (foguete5_horizontal_fase2) and col_fase2 <= (foguete5_horizontal_fase2 + 110)) and (key[pygame.K_DOWN] == False and key[pygame.K_s] == False)):
                col_fase2 = 447
                foguete2_vertical_fase2 = -210
                foguete4_horizontal_fase2 = -256
                foguete5_horizontal_fase2 = 2304
                vidas -= 1
                frames_vermelho = 2.5

            # Imagem tubo
            screen.blit(def_images.tubulcao_direita, (-70, 435))
            screen.blit(def_images.tubulcao_esquerda, (918, 435))

            # Orientação
            if tempo_fase2 < 500:
                screen.blit(def_images.orientacao_agacho, (350, 180))
                screen.blit(def_images.orientacao_fase2, (150, 150))

            # Pontuação
            screen.blit(def_images.numeros[z], (900, 40))
            if score >= vitoria_fase_2:
                if not musica_tocando:
                    funcoes.musica_vitoria()
                    musica_tocando = True
                funcoes.proximo_nivel()
                fase += 1
                vidas = 5
                score = 0
                f += 1
                pygame.display.flip()
                pygame.time.delay(6500)

        # FASE 3
        elif fase == 3:
            # Imagem fundo
            screen.blit(def_images.black_screen, (0, 0))
            screen.blit(def_images.bg_fase3, (0, imagem_fase3))

            # Musica
            if musica_tocando:
                funcoes.musica()
                musica_tocando = False

            # Subindo as escadas
            # Escada 1
            if col_fase3 >= escada1_x and col_fase3 <= (escada1_x + 35):
                escada = True
                diferenca = 24
                if subida_escada == 0:
                    num_escada += 1
                    subida_escada = -1
            # Escada 2
            elif col_fase3 >= escada2_x and col_fase3 <= (escada2_x + 35):
                escada = True
                diferenca = 50
                if subida_escada == 0:
                    num_escada += 1
                    subida_escada = -1
            # Escada 3
            elif col_fase3 >= escada3_x and col_fase3 <= (escada3_x + 35):
                escada = True
                diferenca = 20
                if subida_escada == 0:
                    num_escada += 1
                    subida_escada = -1
            # Escada 4
            elif col_fase3 >= escada4_x and col_fase3 <= (escada4_x + 35):
                escada = True
                diferenca = 0
                if subida_escada == 0:
                    num_escada += 1
                    subida_escada = -1
            else:
                escada = False
            if escada == False and subida_escada == -1:
                subida_escada = (110 + diferenca)

            # Movimento do Personagem
            if vidas > 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
                    col_fase3, _, x = funcoes.personagem.personagem_movimento_direta(col_fase3, (lin_fase3 - 3), 5, x)
                elif key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
                    col_fase3, _, y = funcoes.personagem.personagem_movimento_esquerda(col_fase3, (lin_fase3 - 3), 5, y)
                elif escada == True and subida_escada >= 0 and num_escada < 16 and (key[pygame.K_UP] == True or key[pygame.K_w] == True):
                    col_fase3, _, imagem_fase3, subida_escada, u = funcoes.personagem.personagem_subir(col_fase3, lin_fase3, imagem_fase3, subida_escada, u)
                else:
                    funcoes.personagem.personagem_parado(col_fase3, lin_fase3)
            else:
                funcoes.personagem.personagem_parado(col_fase3, lin_fase3)

            # limite na tela
            if num_escada == 0:
                if col_fase3 > 980:
                    col_fase3 -= 4.5
                elif col_fase3 < -20:
                    col_fase3 += 4.5
            elif num_escada == 1 or num_escada == 5 or num_escada == 9 or num_escada == 13:
                if col_fase3 > 980:
                    col_fase3 -= 4.5
                elif col_fase3 < 475:
                    col_fase3 += 4.5
            elif num_escada == 2 or num_escada == 6 or num_escada == 10 or num_escada == 14:
                if col_fase3 > 820:
                    col_fase3 -= 4.5
                elif col_fase3 < -20:
                    col_fase3 += 4.5
            elif num_escada == 3 or num_escada == 7 or num_escada == 11 or num_escada == 15:
                if col_fase3 > 980:
                    col_fase3 -= 4.5
                elif col_fase3 < 390:
                    col_fase3 += 4.5
            elif num_escada == 4 or num_escada == 8 or num_escada == 12 or num_escada == 16:
                if col_fase3 > 832:
                    col_fase3 -= 4.5
                elif col_fase3 < -20:
                    col_fase3 += 4.5

            # Barril
            if vidas > 0:
                j += 1
                if j >= len(def_images.barril):
                    j = 0
                # Barril 1
                barril1_x, _ = funcoes.obstaculos.barril(barril1_x, imagem_fase3, 2350, velocidade_barril1, j, "e")
                if barril1_x < 544:
                    barril1_x, velocidade_barril1 = funcoes.obstaculos.limite_barril(544, imagem_fase3, 2350, "e", b1)
                else:
                    b1 = 0
                # Barril 2
                barril2_x, _ = funcoes.obstaculos.barril(barril2_x, imagem_fase3, 2216, velocidade_barril2, j, "d")
                if barril2_x > 754:
                    barril2_x, velocidade_barril2 = funcoes.obstaculos.limite_barril(754, imagem_fase3, 2216, "d", b2)
                else:
                    b2 = 0
                # Barril 3
                barril3_x, _ = funcoes.obstaculos.barril(barril3_x, imagem_fase3, 2057, velocidade_barril3, j, "e")
                if barril3_x < 468:
                    barril3_x, velocidade_barril3 = funcoes.obstaculos.limite_barril(468, imagem_fase3, 2057, "e", b3)
                else:
                    b3 = 0
                # Barril 4
                barril4_x, _ = funcoes.obstaculos.barril(barril4_x, imagem_fase3, 1927, velocidade_barril4, j, "d")
                if barril4_x > 588:
                    barril4_x, velocidade_barril4 = funcoes.obstaculos.limite_barril(588, imagem_fase3, 1927, "d", b4)
                else:
                    b4 = 0
                # Barril 5
                barril5_x, _ = funcoes.obstaculos.barril(barril5_x, imagem_fase3, 1816, velocidade_barril1, j, "e")
                if barril5_x < 544:
                    barril5_x, velocidade_barril1 = funcoes.obstaculos.limite_barril(544, imagem_fase3, 1816, "e", b1)
                # Barril 6
                barril6_x, _ = funcoes.obstaculos.barril(barril6_x, imagem_fase3, 1681, velocidade_barril2, j, "d")
                if barril6_x > 754:
                    barril6_x, velocidade_barril2 = funcoes.obstaculos.limite_barril(754, imagem_fase3, 1681, "d", b2)
                # Barril 7
                barril7_x, _ = funcoes.obstaculos.barril(barril7_x, imagem_fase3, 1524, velocidade_barril3, j, "e")
                if barril7_x < 468:
                    barril7_x, velocidade_barril3 = funcoes.obstaculos.limite_barril(468, imagem_fase3, 1524, "e", b3)
                # Barril 8
                barril8_x, _ = funcoes.obstaculos.barril(barril8_x, imagem_fase3, 1394, velocidade_barril4, j, "d")
                if barril8_x > 588:
                    barril8_x, velocidade_barril4 = funcoes.obstaculos.limite_barril(588, imagem_fase3, 1394, "d", b4)
                # Barril 9
                barril9_x, _ = funcoes.obstaculos.barril(barril9_x, imagem_fase3, 1283, velocidade_barril1, j, "e")
                if barril9_x < 544:
                    barril9_x, velocidade_barril1 = funcoes.obstaculos.limite_barril(544, imagem_fase3, 1283, "e", b1)
                # Barril 10
                barril10_x, _ = funcoes.obstaculos.barril(barril10_x, imagem_fase3, 1148, velocidade_barril2, j, "d")
                if barril10_x > 754:
                    barril10_x, velocidade_barril2 = funcoes.obstaculos.limite_barril(754, imagem_fase3, 1148, "d", b2)
                # Barril 11
                barril11_x, _ = funcoes.obstaculos.barril(barril11_x, imagem_fase3, 991, velocidade_barril3, j, "e")
                if barril11_x < 468:
                    barril11_x, velocidade_barril3 = funcoes.obstaculos.limite_barril(468, imagem_fase3, 991, "e", b3)
                # Barril 12
                barril12_x, _ = funcoes.obstaculos.barril(barril12_x, imagem_fase3, 861, velocidade_barril4, j, "d")
                if barril12_x > 588:
                    barril12_x, velocidade_barril4 = funcoes.obstaculos.limite_barril(588, imagem_fase3, 861, "d", b4)
                # Barril 13
                barril13_x, _ = funcoes.obstaculos.barril(barril13_x, imagem_fase3, 750, velocidade_barril1, j, "e")
                if barril13_x < 544:
                    barril13_x, velocidade_barril1 = funcoes.obstaculos.limite_barril(544, imagem_fase3, 750, "e", b1)
                # Barril 14
                barril14_x, _ = funcoes.obstaculos.barril(barril14_x, imagem_fase3, 615, velocidade_barril2, j, "d")
                if barril14_x > 754:
                    barril14_x, velocidade_barril2 = funcoes.obstaculos.limite_barril(754, imagem_fase3, 615, "d", b2)
                # Barril 15
                barril15_x, _ = funcoes.obstaculos.barril(barril15_x, imagem_fase3, 457, velocidade_barril3, j, "e")
                if barril15_x < 468:
                    barril15_x, velocidade_barril3 = funcoes.obstaculos.limite_barril(468, imagem_fase3, 457, "e", b3)

            # Velocidade Barril
            velocidade_minima_barril, velocidade_maxima_barril = funcoes.obstaculos.velocidade_barril(imagem_fase3, velocidade_maxima_barril, velocidade_minima_barril)

            # Colisão
            if vidas > 0:
                # Barril 1
                if (((col_fase3 + 55) >= barril1_x and col_fase3 <= (barril1_x + 40)) and (subida_escada >= 106 or subida_escada == -1) and num_escada == 1):
                    barril1_x = 1400
                    col_fase3 = 475
                    imagem_fase3 = -1766
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 2
                if (((col_fase3 + 55) >= barril2_x and col_fase3 <= (barril2_x + 40)) and (subida_escada >= 132 or subida_escada == -1) and num_escada == 2):
                    barril2_x = -400
                    col_fase3 = 820
                    imagem_fase3 = -1632
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 3
                if (((col_fase3 + 55) >= barril3_x and col_fase3 <= (barril3_x + 40)) and (subida_escada >= 102 or subida_escada == -1) and num_escada == 3):
                    barril3_x = 1400
                    col_fase3 = 390
                    imagem_fase3 = -1472
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 4
                if (((col_fase3 + 55) >= barril4_x and col_fase3 <= (barril4_x + 40)) and (subida_escada >= 82 or subida_escada == -1) and num_escada == 4):
                    barril4_x = -400
                    col_fase3 = 832
                    imagem_fase3 = -1342
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 5
                if (((col_fase3 + 55) >= barril5_x and col_fase3 <= (barril5_x + 40)) and (subida_escada >= 106 or subida_escada == -1) and num_escada == 5):
                    barril5_x = 1400
                    col_fase3 = 475
                    imagem_fase3 = -1232
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 6
                if (((col_fase3 + 55) >= barril6_x and col_fase3 <= (barril6_x + 40)) and (subida_escada >= 132 or subida_escada == -1) and num_escada == 6):
                    barril6_x = -400
                    col_fase3 = 820
                    imagem_fase3 = -1098
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 7
                if (((col_fase3 + 55) >= barril7_x and col_fase3 <= (barril7_x + 40)) and (subida_escada >= 102 or subida_escada == -1) and num_escada == 7):
                    barril7_x = 1400
                    col_fase3 = 390
                    imagem_fase3 = -938
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 8
                if (((col_fase3 + 55) >= barril8_x and col_fase3 <= (barril8_x + 40)) and (subida_escada >= 82 or subida_escada == -1) and num_escada == 8):
                    barril8_x = -400
                    col_fase3 = 832
                    imagem_fase3 = -808
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 9
                if (((col_fase3 + 55) >= barril9_x and col_fase3 <= (barril9_x + 40)) and (subida_escada >= 106 or subida_escada == -1) and num_escada == 9):
                    barril9_x = 1400
                    col_fase3 = 475
                    imagem_fase3 = -698
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 10
                if (((col_fase3 + 55) >= barril10_x and col_fase3 <= (barril10_x + 40)) and (subida_escada >= 132 or subida_escada == -1) and num_escada == 10):
                    barril10_x = -400
                    col_fase3 = 820
                    imagem_fase3 = -564
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 11
                if (((col_fase3 + 55) >= barril11_x and col_fase3 <= (barril11_x + 40)) and (subida_escada >= 102 or subida_escada == -1) and num_escada == 11):
                    barril11_x = 1400
                    col_fase3 = 390
                    imagem_fase3 = -404
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 12
                if (((col_fase3 + 55) >= barril12_x and col_fase3 <= (barril12_x + 40)) and (subida_escada >= 82 or subida_escada == -1) and num_escada == 12):
                    barril12_x = -400
                    col_fase3 = 832
                    imagem_fase3 = -274
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 13
                if (((col_fase3 + 55) >= barril13_x and col_fase3 <= (barril13_x + 40)) and (subida_escada >= 106 or subida_escada == -1) and num_escada == 13):
                    barril13_x = 1400
                    col_fase3 = 475
                    imagem_fase3 = -164
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 14
                if (((col_fase3 + 55) >= barril14_x and col_fase3 <= (barril14_x + 40)) and (subida_escada >= 132 or subida_escada == -1) and num_escada == 14):
                    barril14_x = -400
                    col_fase3 = 820
                    imagem_fase3 = -30
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5
                # Barril 15
                if (((col_fase3 + 55) >= barril15_x and col_fase3 <= (barril15_x + 40)) and (subida_escada >= 102 or subida_escada == -1) and num_escada == 15):
                    barril15_x = 1400
                    col_fase3 = 390
                    imagem_fase3 = 130
                    vidas -= 1
                    subida_escada = -1
                    frames_vermelho = 2.5

            # Donkey Kong
            if num_escada >= 11:
                d = funcoes.boss.donkey_kong(imagem_fase3, num_escada, d)

            # Vitoria
            if num_escada == 16 and col_fase3 <= 340:
                if not musica_tocando:
                    funcoes.musica_vitoria()
                    musica_tocando = True
                funcoes.proximo_nivel()
                fase += 1
                vidas = 5
                f += 1
                pygame.display.flip()
                pygame.time.delay(6500)

        # FASE 4
        elif fase == 4:
            # Imagem fundo
            screen.blit(def_images.bg_fase4, (0, 0))
            # Tempo de fase
            if vidas > 0:
                tempo_fase4 +=1

            # Musica
            if musica_tocando:
                funcoes.musica()
                musica_tocando = False

            # Movimento do Personagem
            if vidas > 0 and tempo_fase4 < 7500:
                key = pygame.key.get_pressed()
                if key[pygame.K_DOWN] == True or key[pygame.K_s] == True:
                    _, s = funcoes.personagem.personagem_agachado(col_fase4, (lin_fase4 + 3), s)
                elif key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
                    col_fase4, _, x = funcoes.personagem.personagem_movimento_direta(col_fase4, (lin_fase4 - 3), 4.5, x)
                elif key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
                    col_fase4, _, y = funcoes.personagem.personagem_movimento_esquerda(col_fase4, (lin_fase4 - 3), 4.5, y)
                else:
                    s = 0
                    funcoes.personagem.personagem_parado(col_fase4, lin_fase4)
            else:
                funcoes.personagem.personagem_parado(col_fase4, lin_fase4)

            # limite na tela
            if col_fase4 > 687:
                col_fase4 -= 4.5
            elif col_fase4 < -20:
                col_fase4 += 4.5

            # Pulo do Personagem
            if pulando and vidas > 0 and tempo_fase4 < 7500:
                altura_pulo += abs(velocidade_vertical)
                lin_fase4 += velocidade_vertical
                velocidade_vertical += 1

                if altura_pulo >= 500:
                    velocidade_vertical = 10  # Velocidade de queda
                    pulando = False

                if lin_fase4 > limite_inferior:
                    lin_fase4 = limite_inferior
                    no_chao = True

                if no_chao and (evento.type == KEYDOWN and (evento.key == K_UP or evento.key == K_w)):
                    pulando = True
                    altura_pulo = 0
                    velocidade_vertical = -15 # Velocidade do pulo
                    no_chao = False
                    funcoes.som_pulo()

            # Fogos
            # fireball1
            fireball1_vertical, posicao_fireball1 = funcoes.obstaculos.fireball_baixo(fireball1_vertical, posicao_fireball1, velocidade_fireball1)
            if fireball1_vertical >= 968 and tempo_fase4 <= 6850 and vidas > 0 and tempo_fase4 < 7500:
                fireball1_vertical, posicao_fireball1, limite_esquerda_fireball1, limite_direita_fireball1, velocidade_fireball1 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball1,1, 87)

            # fireball2
            fireball2_vertical, posicao_fireball2 = funcoes.obstaculos.fireball_baixo(fireball2_vertical, posicao_fireball2, velocidade_fireball2)
            if fireball2_vertical > 968 and tempo_fase4 <= 6850 and vidas > 0 and tempo_fase4 < 7500:
                fireball2_vertical, posicao_fireball2, limite_esquerda_fireball2, limite_direita_fireball2, velocidade_fireball2 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball2,137, 244)

            # fireball3
            fireball3_vertical, posicao_fireball3 = funcoes.obstaculos.fireball_baixo(fireball3_vertical, posicao_fireball3, velocidade_fireball3)
            if fireball3_vertical > 968 and tempo_fase4 <= 6850 and vidas > 0 and tempo_fase4 < 7500:
                fireball3_vertical, posicao_fireball3, limite_esquerda_fireball3, limite_direita_fireball3, velocidade_fireball3 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball3, 274, 361)

            # fireball4
            fireball4_vertical, posicao_fireball4 = funcoes.obstaculos.fireball_baixo(fireball4_vertical, posicao_fireball4, velocidade_fireball4)
            if fireball4_vertical > 968 and tempo_fase4 <= 6850 and vidas > 0 and tempo_fase4 < 7500:
                fireball4_vertical, posicao_fireball4, limite_esquerda_fireball4, limite_direita_fireball4, velocidade_fireball4 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball4, 411, 498)

            # fireball5
            fireball5_vertical, posicao_fireball5 = funcoes.obstaculos.fireball_baixo(fireball5_vertical, posicao_fireball5, velocidade_fireball5)
            if fireball5_vertical > 968 and tempo_fase4 <= 6850 and vidas > 0 and tempo_fase4 < 7500:
                fireball5_vertical, posicao_fireball5, limite_esquerda_fireball5, limite_direita_fireball5, velocidade_fireball5 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball5, 548, 635)

            # fireball6
            fireball6_vertical, posicao_fireball6 = funcoes.obstaculos.fireball_baixo(fireball6_vertical, posicao_fireball6, velocidade_fireball6)
            if fireball6_vertical > 968 and tempo_fase4 <= 6850 and vidas > 0 and tempo_fase4 < 7500:
                fireball6_vertical, posicao_fireball6, _, _, velocidade_fireball6 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball6, 685, 772)

            # fireball7
            fireball7_vertical, posicao_fireball7 = funcoes.obstaculos.fireball_baixo(fireball7_vertical, posicao_fireball7, velocidade_fireball7)
            if fireball7_vertical > 968 and tempo_fase4 <= 6850 and vidas > 0 and tempo_fase4 < 7500:
                fireball7_vertical, posicao_fireball7, _, _, velocidade_fireball7 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball7, 822, 909)

            # fireball8
            fireball8_vertical, posicao_fireball8 = funcoes.obstaculos.fireball_baixo(fireball8_vertical, posicao_fireball8, velocidade_fireball8)
            if fireball8_vertical > 968 and tempo_fase4 <= 6850 and vidas > 0:
                fireball8_vertical, posicao_fireball8, _, _, velocidade_fireball8 = funcoes.obstaculos.limite_fireball_baixo(
                    velocidade_fireball8, 959, 979)

            # fireball9
            if tempo_fase4 <= 6850:
                fireball9_horizontal, posicao_fireball9 = funcoes.obstaculos.fireball_lado(fireball9_horizontal, posicao_fireball9, velocidade_fireball9)
            if fireball9_horizontal < -2850 and tempo_fase4 <= 6850 and vidas > 0:
                fireball9_horizontal, velocidade_fireball9 = funcoes.obstaculos.limite_fireball_lado(velocidade_fireball9)

            # fireball10
            if tempo_fase4 <= 6850:
                fireball10_horizontal, posicao_fireball10 = funcoes.obstaculos.fireball_lado(fireball10_horizontal, posicao_fireball10, velocidade_fireball10)
            if fireball10_horizontal < -3800 and tempo_fase4 <= 6850 and vidas > 0:
                fireball10_horizontal, velocidade_fireball10 = funcoes.obstaculos.limite_fireball_lado(velocidade_fireball10)

            # fireball11
            if tempo_fase4 <= 6850:
                fireball11_horizontal, posicao_fireball11 = funcoes.obstaculos.fireball_lado(fireball11_horizontal, posicao_fireball11, velocidade_fireball11)
            if fireball11_horizontal < -4750 and tempo_fase4 <= 6850 and vidas > 0:
                fireball11_horizontal, velocidade_fireball11 = funcoes.obstaculos.limite_fireball_lado(velocidade_fireball11)

            # fireball12
            if tempo_fase4 <= 6850:
                fireball12_horizontal, posicao_fireball12 = funcoes.obstaculos.fireball_lado(fireball12_horizontal, posicao_fireball12, velocidade_fireball12)
            if fireball12_horizontal < -5700 and tempo_fase4 <= 6850 and vidas > 0:
                fireball12_horizontal, velocidade_fireball12 = funcoes.obstaculos.limite_fireball_lado(velocidade_fireball12)

            # Browser
            b, abaixando = funcoes.boss.browser(tempo_fase4, vidas, abaixando, b)

            # Colisão
            # Fireball 1
            if ((col_fase4 >= limite_esquerda_fireball1 and col_fase4 <= limite_direita_fireball1) and (
                    fireball1_vertical >= 541 and fireball1_vertical <= 640) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball1_vertical = 0
                fireball3_vertical = 0
                frames_vermelho = 2.5
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 2
            if ((col_fase4 >= limite_esquerda_fireball2 and col_fase4 <= limite_direita_fireball2) and (
                    fireball2_vertical >= 541 and fireball2_vertical <= 640) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball2_vertical = 0
                fireball3_vertical = 0
                frames_vermelho = 2.5
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 3
            if ((col_fase4 >= limite_esquerda_fireball3 and col_fase4 <= limite_direita_fireball3) and (
                    fireball3_vertical >= 541 and fireball3_vertical <= 640) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball3_vertical = 0
                frames_vermelho = 2.5
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 4
            if ((col_fase4 >= limite_esquerda_fireball4 and col_fase4 <= limite_direita_fireball4) and (
                    fireball4_vertical >= 541 and fireball4_vertical <= 640) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball4_vertical = 0
                fireball3_vertical = 0
                frames_vermelho = 2.5
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 5
            if ((col_fase4 >= limite_esquerda_fireball5 and col_fase4 <= limite_direita_fireball5) and (
                    fireball5_vertical >= 541 and fireball5_vertical <= 640) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball5_vertical = 0
                fireball3_vertical = 0
                frames_vermelho = 2.5
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 9
            if ((col_fase4 >= (fireball9_horizontal) and col_fase4 <= (fireball9_horizontal + 110)) and (
                    pulando == False) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball3_vertical = 0
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                frames_vermelho = 2.5
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 10
            if ((col_fase4 >= (fireball10_horizontal) and col_fase4 <= (fireball10_horizontal + 110)) and (
                    key[pygame.K_DOWN] == False and key[pygame.K_s] == False) and (pulando == False) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball3_vertical = 0
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                frames_vermelho = 2.5
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 11
            if ((col_fase4 >= (fireball11_horizontal) and col_fase4 <= (fireball11_horizontal + 110)) and (
                    pulando == False) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball3_vertical = 0
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                frames_vermelho = 2.5
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1
            # Fireball 12
            if ((col_fase4 >= (fireball12_horizontal) and col_fase4 <= (fireball12_horizontal + 110)) and (
                    key[pygame.K_DOWN] == False and key[pygame.K_s] == False) and (pulando == False) and vidas > 0 and tempo_fase4 < 6850):
                col_fase4 = 300
                fireball3_vertical = 0
                fireball9_horizontal = 1024
                fireball10_horizontal = 1974
                fireball11_horizontal = 2924
                fireball12_horizontal = 3874
                frames_vermelho = 2.5
                if vidas_fase4 > 0:
                    vidas_fase4 -= 1
                else:
                    vidas -= 1

            # Vidas extra
            funcoes.exibir_vidas.vidas_extra(vidas_fase4,tempo_fase4)
            # Cronometro
            minutos, segundos = funcoes.frames_para_tempo(tempo_atual)
            if tempo_fase4 < 7500:
                funcoes.desenhar_cronometro(minutos, segundos)
            if vidas > 0:
                tempo_atual -= 1
                if tempo_atual < 0:
                    tempo_atual = 0

            # Bombardeio
            if tempo_fase4 > 7030:
                e, foguete_final_1, foguete_final_2 = funcoes.boss.bombardeio(foguete_final_1, foguete_final_2, e)

            # Vitoria
            if tempo_fase4 >= 7500:
                if not musica_tocando:
                    funcoes.musica_vitoria()
                    musica_tocando = True
                funcoes.vitoria_jogo()
                pygame.display.flip()
                pygame.time.delay(8000)
                executando = False

            # Orientação
            if tempo_fase4 < 400:
                screen.blit(def_images.orientacao_pulo, (350, 585))
                screen.blit(def_images.orientacao_fase3, (320, 170))

        #Indicador de Vidas
        funcoes.exibir_vidas.vidas_normal(vidas, fase)

        # Indicador de Fase
        if fase > 0:
            screen.blit(def_images.indicador_fase[f], (440, 30))

        # Simulação Dano
        if frames_vermelho > 0 and fase > 0:
            funcoes.indicador_dano()
            frames_vermelho -= 1

        # Derrota
        if vidas <= 0:
            if not musica_tocando:
                funcoes.musica_derrota()
                musica_tocando = True
            funcoes.fim_jogo()
            pygame.display.flip()
            pygame.time.delay(8000)
            executando = False

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                executando = False
            elif evento.type == USEREVENT:
                pygame.mixer_music.play()
            elif evento.type == KEYDOWN:
                if fase == 4:
                    if evento.key == K_UP or evento.key == K_w and pulando == False:
                        pulando = True
                        altura_pulo = 0
                        velocidade_vertical = -10

    pygame.quit()
    import sys
    sys.exit()

if __name__ == '__main__':
    game_loop()

# Leonardo Rodrigues