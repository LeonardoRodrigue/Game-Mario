import pygame
import variaveis
import def_images
import random

def frames_para_tempo(frames):
    minutos = frames // (variaveis.FPS * 60)
    segundos = (frames // variaveis.FPS) % 60
    return minutos, segundos

def desenhar_cronometro(minutos, segundos):
    fonte = pygame.font.Font(None, 44)
    texto = fonte.render(f"{minutos:02}:{segundos:02}", True, variaveis.black)
    def_images.screen.blit(texto, (900, 50))

def musica():
    pygame.mixer_music.load('Music/Super Mario Bros. Theme Song(MP3_160K).mp3')
    pygame.mixer_music.set_volume(0.3)
    pygame.mixer_music.play()
    pygame.mixer_music.set_endevent(pygame.USEREVENT)

def musica_vitoria():
    pygame.mixer_music.load('Music/Super Mario Bros. Music - Level Complete(MP3_160K).mp3')
    pygame.mixer_music.set_volume(0.5)
    pygame.mixer_music.play()

def musica_derrota():
    pygame.mixer_music.load('Music/Música de Super Mario Bros. - Estás Muerto(MP3_160K).mp3')
    pygame.mixer_music.set_volume(0.3)
    pygame.mixer_music.play()

def som_pulo():
    pulo = pygame.mixer.Sound('Music/Super Mario - Som do pulo do Mário(MP3_160K).mp3')
    pulo.set_volume(0.2)
    pulo.play()

def indicador_dano():
    fundo_vermelho = pygame.image.load('Imagens/fundo vermelho.png')
    opacidade = 158
    fundo_vermelho.set_alpha(opacidade)
    def_images.screen.blit(fundo_vermelho, (0, 0))
    pygame.display.flip()

def proximo_nivel():
    prox_nivel = pygame.image.load('Imagens/next_level.png')
    def_images.screen.blit(prox_nivel, (115, 280))

def fim_jogo():
    derrota = pygame.image.load('Imagens/game over.png')
    def_images.screen.blit(derrota, (140, 150))

def vitoria_jogo():
    vitoria = pygame.image.load('Imagens/winner.png')
    def_images.screen.blit(vitoria, (100, 50))
    def_images.screen.blit(def_images.trofeu, (550, 180))

class exibir_vidas:
    def vidas_normal(vidas, fase):
        if vidas >= 5 and fase > 0:
            def_images.screen.blit(def_images.coracao, (30, 50))
            def_images.screen.blit(def_images.coracao, (70, 50))
            def_images.screen.blit(def_images.coracao, (110, 50))
            def_images.screen.blit(def_images.coracao, (150, 50))
            def_images.screen.blit(def_images.coracao, (190, 50))
        elif vidas == 4 and fase > 0:
            def_images.screen.blit(def_images.coracao, (30, 50))
            def_images.screen.blit(def_images.coracao, (70, 50))
            def_images.screen.blit(def_images.coracao, (110, 50))
            def_images.screen.blit(def_images.coracao, (150, 50))
            def_images.screen.blit(def_images.coracao_vazio, (196, 52))
        elif vidas == 3 and fase > 0:
            def_images.screen.blit(def_images.coracao, (30, 50))
            def_images.screen.blit(def_images.coracao, (70, 50))
            def_images.screen.blit(def_images.coracao, (110, 50))
            def_images.screen.blit(def_images.coracao_vazio, (156, 52))
            def_images.screen.blit(def_images.coracao_vazio, (196, 52))
        elif vidas == 2 and fase > 0:
            def_images.screen.blit(def_images.coracao, (30, 50))
            def_images.screen.blit(def_images.coracao, (70, 50))
            def_images.screen.blit(def_images.coracao_vazio, (116, 52))
            def_images.screen.blit(def_images.coracao_vazio, (156, 52))
            def_images.screen.blit(def_images.coracao_vazio, (196, 52))
        elif vidas == 1 and fase > 0:
            def_images.screen.blit(def_images.coracao, (30, 50))
            def_images.screen.blit(def_images.coracao_vazio, (76, 52))
            def_images.screen.blit(def_images.coracao_vazio, (116, 52))
            def_images.screen.blit(def_images.coracao_vazio, (156, 52))
            def_images.screen.blit(def_images.coracao_vazio, (196, 52))
        elif vidas <= 0 and fase > 0:
            def_images.screen.blit(def_images.coracao_vazio, (36, 52))
            def_images.screen.blit(def_images.coracao_vazio, (76, 52))
            def_images.screen.blit(def_images.coracao_vazio, (116, 52))
            def_images.screen.blit(def_images.coracao_vazio, (156, 52))
            def_images.screen.blit(def_images.coracao_vazio, (196, 52))

    def vidas_extra(vidas, tempo):
        if vidas == 4 and tempo < 7500:
            def_images.screen.blit(def_images.coracao, (230, 50))
            def_images.screen.blit(def_images.coracao, (270, 50))
            def_images.screen.blit(def_images.coracao, (310, 50))
            def_images.screen.blit(def_images.coracao, (350, 50))
        elif vidas == 3 and tempo < 7500:
            def_images.screen.blit(def_images.coracao, (230, 50))
            def_images.screen.blit(def_images.coracao, (270, 50))
            def_images.screen.blit(def_images.coracao, (310, 50))
            def_images.screen.blit(def_images.coracao_vazio, (356, 52))
        elif vidas == 2 and tempo < 7500:
            def_images.screen.blit(def_images.coracao, (230, 50))
            def_images.screen.blit(def_images.coracao, (270, 50))
            def_images.screen.blit(def_images.coracao_vazio, (316, 52))
            def_images.screen.blit(def_images.coracao_vazio, (356, 52))
        elif vidas == 1 and tempo < 7500:
            def_images.screen.blit(def_images.coracao, (230, 50))
            def_images.screen.blit(def_images.coracao_vazio, (276, 52))
            def_images.screen.blit(def_images.coracao_vazio, (316, 52))
            def_images.screen.blit(def_images.coracao_vazio, (356, 52))
        elif vidas == 0 and tempo < 7500:
            def_images.screen.blit(def_images.coracao_vazio, (236, 52))
            def_images.screen.blit(def_images.coracao_vazio, (276, 52))
            def_images.screen.blit(def_images.coracao_vazio, (316, 52))
            def_images.screen.blit(def_images.coracao_vazio, (356, 52))

class personagem:
    def personagem_parado(coluna, linha):
        def_images.screen.blit(def_images.personagem['parado'], (coluna, linha))
    def personagem_movimento_direta(coluna, linha, velocidade, troca_imagem):
        coluna += velocidade
        troca_imagem += 1
        if troca_imagem >= len(def_images.personagem['direita']):
            troca_imagem = 0
        def_images.screen.blit(def_images.personagem['direita'][troca_imagem], (coluna, linha))
        return coluna, linha, troca_imagem
    def personagem_movimento_esquerda(coluna, linha, velocidade, troca_imagem):
        coluna -= velocidade
        troca_imagem += 1
        if troca_imagem >= len(def_images.personagem['esquerda']):
            troca_imagem = 0
        def_images.screen.blit(def_images.personagem['esquerda'][troca_imagem], (coluna, linha))
        return coluna, linha, troca_imagem
    def personagem_agachado(coluna, linha, troca_imagem):
        troca_imagem += 1
        if troca_imagem >= len(def_images.personagem['agachado']):
            troca_imagem = len(def_images.personagem['agachado']) - 1
        def_images.screen.blit(def_images.personagem['agachado'][troca_imagem], (coluna, linha))
        return linha, troca_imagem
    def personagem_subir(coluna, linha, fundo, subir, troca_imagem):
        subir -= 2
        fundo += 2
        troca_imagem += 1
        if troca_imagem >= len(def_images.personagem['subindo']):
            troca_imagem = 0
        def_images.screen.blit(def_images.personagem['subindo'][troca_imagem], (coluna, linha))
        return coluna, linha, fundo, subir, troca_imagem

class boss:
    def donkey_kong(imagem, numero_escada, troca_imagem):
        def_images.screen.blit(def_images.moeda, (315, (imagem + 310)))
        def_images.screen.blit(def_images.donkey_kong[troca_imagem], (50, (imagem + 155)))
        troca_imagem += 1
        if troca_imagem >= len(def_images.donkey_kong):
            troca_imagem = 0
        elif numero_escada == 16:
            troca_imagem = len(def_images.donkey_kong) - 1
        return troca_imagem

    def browser(tempo, vidas, abaixar, troca_imagem):
        if tempo >= 500 and tempo < 6915 and vidas > 0:
            troca_imagem += 1
            if troca_imagem >= len(def_images.browser['lancando']):
                troca_imagem = 0
            def_images.screen.blit(def_images.browser['lancando'][troca_imagem], (687, 278))
        elif tempo >= 7200:
            troca_imagem += 1
            if abaixar <= 115:
                abaixar += 0.675
            if troca_imagem >= len(def_images.browser['derrotado']):
                troca_imagem = 175
            def_images.screen.blit(def_images.browser['derrotado'][troca_imagem], (687, (278 + abaixar)))
        else:
            troca_imagem = 0
            def_images.screen.blit(def_images.browser['normal'], (687, 278))
        return troca_imagem, abaixar

    def bombardeio(foguete1, foguete2, troca_imagem):
        if foguete1 <= 797:
            foguete1 += 10
            foguete2 += 10
            def_images.screen.blit(def_images.foguete_direita, (foguete2, 388))
            def_images.screen.blit(def_images.foguete_direita, (foguete2, 498))
            def_images.screen.blit(def_images.foguete_direita, (foguete1, 608))
            def_images.screen.blit(def_images.foguete_direita, (foguete1, 278))
        else:
            troca_imagem += 1
            if troca_imagem >= len(def_images.explosao):
                troca_imagem = len(def_images.explosao) - 1
            def_images.screen.blit(def_images.explosao[troca_imagem], ((foguete2 - 100), 316))
            def_images.screen.blit(def_images.explosao[troca_imagem], ((foguete2 - 100), 426))
            def_images.screen.blit(def_images.explosao[troca_imagem], ((foguete1 - 100), 536))
            def_images.screen.blit(def_images.explosao[troca_imagem], ((foguete1 - 100), 206))
        return troca_imagem, foguete1, foguete2

class obstaculos:
    def foguete(coluna, linha, direcao, velocidade):
        if direcao == 'v':
            linha += velocidade
            def_images.screen.blit(def_images.foguete1['baixo'], (coluna, linha))
        else:
            linha -= velocidade
            def_images.screen.blit(def_images.foguete1['cima'], (coluna, linha))
        return linha

    def foguete_horizontal(coluna, direcao):
        if direcao == 'd':
            coluna += 5
            def_images.screen.blit(def_images.foguete_direita, (coluna, 475))
        else:
            coluna -= 5
            def_images.screen.blit(def_images.foguete_esquerda, (coluna, 475))
        return coluna

    def limite_foguete_vertical_fase2(linha, limite_esquerda_posicao, limite_direita_posicao):
        linha = -110
        velocidade = random.randint(4, 6)
        coluna = random.randint(limite_esquerda_posicao, limite_direita_posicao)
        limite_esquerda = coluna - 30
        limite_direita = coluna + 80
        return limite_esquerda, limite_direita, linha, velocidade, coluna

    def barril(coluna, imagem, linha, velocidade, troca_imagem, direcao):
        troca_imagem += 1
        if troca_imagem >= len(def_images.barril):
            troca_imagem = 0

        if direcao == "e":
            coluna -= velocidade
            def_images.screen.blit(def_images.barril[troca_imagem], ((coluna), (imagem + linha)))
        else:
            coluna += velocidade
            def_images.screen.blit(def_images.barril[troca_imagem], ((coluna), (imagem + linha)))
        return coluna, linha

    def limite_barril(coluna_explosao, imagem, linha, direcao, troca_imagem_explosao):
        if direcao == "e":
            coluna = 1200
            velocidade = random.randint(2, 3)
            if troca_imagem_explosao < len(def_images.explosao_barril):
                def_images.screen.blit(def_images.explosao_barril[troca_imagem_explosao], ((coluna_explosao), (imagem + linha)))
                troca_imagem_explosao += 1
        else:
            coluna = -200
            velocidade = random.randint(2, 3)
            if troca_imagem_explosao < len(def_images.explosao_barril):
                def_images.screen.blit(def_images.explosao_barril[troca_imagem_explosao], ((coluna_explosao), (imagem + linha)))
                troca_imagem_explosao += 1
        return coluna, velocidade

    def velocidade_barril(imagem, velocidade_maxima, velocidade_minima):
        if imagem == -1264:
            velocidade_maxima += 1
        elif imagem == -866:
            velocidade_maxima += 1
        elif imagem == -450:
            velocidade_maxima += 1
        elif imagem == -200:
            velocidade_maxima += 1
            velocidade_minima += 1
        elif imagem == -96:
            velocidade_maxima += 1
            velocidade_minima += 1
        return velocidade_minima, velocidade_maxima

    def fireball_baixo(linha, coluna, velocidade):
        linha += velocidade
        def_images.screen.blit(def_images.fireball_baixo, (coluna, linha))
        return linha, coluna

    def fireball_lado(coluna, linha, velocidade):
        coluna -= velocidade
        def_images.screen.blit(def_images.fireball, (coluna, linha))
        return coluna, linha

    def limite_fireball_baixo(velocidade, limite_esquerda_posicao, limite_direita_posicao, incremento=0.5, velocidade_maxima=12):
        linha = -110
        coluna = random.randint(limite_esquerda_posicao, limite_direita_posicao)
        limite_esquerda = coluna - 35
        limite_direita = coluna + 15
        if velocidade < velocidade_maxima:
            velocidade += incremento
        return linha, coluna, limite_esquerda, limite_direita, velocidade

    def limite_fireball_lado(velocidade, incremento=1, velocidade_maxima=10):
        coluna = 1024
        if velocidade < velocidade_maxima:
            velocidade += incremento
        return coluna, velocidade