from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

janela = Window(1440, 900)
janela.set_title("Futuro space invaders")
mouse = janela.get_mouse()
distancia = 40
nova_dist = 120
outra_dsit = 50
tam = 17
distancia_ini = 50
dis_lat_ini = 100
pulo = 50

teclado = janela.get_keyboard()

Titulo = Sprite("titulo.png")
Titulo.set_position((janela.width / 2 - Titulo.width / 2), (0 - 40))

Botao_jogar = Sprite("ranking.png")
Botao_jogar.set_position(janela.width / 2 - Botao_jogar.width / 2, janela.height / 2 + nova_dist)

Botao_dificuldade = Sprite("ranking.png")
Botao_dificuldade.set_position(janela.width / 2 - Botao_jogar.width / 2, janela.height / 2 + distancia + nova_dist)

Botao_rank = Sprite("ranking.png")
Botao_rank.set_position(janela.width / 2 - Botao_jogar.width / 2, janela.height / 2 + (distancia * 2) + nova_dist)

Botao_sair = Sprite("ranking.png")
Botao_sair.set_position(janela.width / 2 - Botao_jogar.width / 2, janela.height / 2 + (distancia * 3) + nova_dist)

Facil = Sprite("ranking.png")
Facil.set_position(janela.width / 2 - Botao_jogar.width / 2 - 300, janela.height / 2 - (distancia * 0) + nova_dist)

Medio = Sprite("ranking.png")
Medio.set_position(janela.width / 2 - Botao_jogar.width / 2 - 300, janela.height / 2 - (distancia * 1) + nova_dist)

Dificil = Sprite("ranking.png")
Dificil.set_position(janela.width / 2 - Botao_jogar.width / 2 - 300, janela.height / 2 - (distancia * 2) + nova_dist)

Impossivel = Sprite("ranking.png")
Impossivel.set_position(janela.width / 2 - Botao_jogar.width / 2 - 300, janela.height / 2 - (distancia * 3) + nova_dist)

jogador = Sprite("jogador.xcf")
jogador.set_position(janela.width / 2 - jogador.width / 2, janela.height * 7 / 8)

state = "string"

branco = (255, 255, 255)
preto = (0, 0, 0)


vel_jog = 350
vel_tiro = 120
vel_ini = 50
tempo_dif = 4

delta_time = janela.delta_time()

mouse_livre = True

tiros = []
matriz_de_mons = []
timer = 0
esc_press = False
inimigos_criados = False


def preenche_inimigos(n, m):
    matriz_de_mons.clear()
    for i in range(n):
        linha = []
        for c in range(m):
            inimigo = Sprite("inimigo.xcf", 2)
            inimigo.set_total_duration(500)
            inimigo.set_position(janela.width / 2 - 500 + (distancia_ini * c) + (dis_lat_ini * c), janela.height * 1 / 12 + (distancia_ini * i))
            linha.append(inimigo)
        matriz_de_mons.append(linha)


def da_tiro():
    tiro = Sprite("projetil.xcf")
    tiro.set_position(jogador.x + jogador.width / 2 - tiro.width / 2, jogador.y)
    tiros.append(tiro)


while True:
    
    if state != "pausa":
        delta_time = janela.delta_time()
    else:
        delta_time = 0
        
    timer += delta_time

    if state == "string":
        janela.set_background_color(preto)
        if mouse.is_over_object(Botao_jogar) and mouse.is_button_pressed(1) and mouse_livre:
            state = "jogando"
            tempo_dif = 0.5
            vel_ini = 100
            inimigos_criados = False
            mouse_livre = False
        if mouse.is_over_object(Botao_dificuldade) and mouse.is_button_pressed(1) and mouse_livre:
            state = "dificuldades"
            mouse_livre = False
        if mouse.is_over_object(Botao_rank) and mouse.is_button_pressed(1) and mouse_livre:
            state = "rank"
            mouse_livre = False
        if mouse.is_over_object(Botao_sair) and mouse.is_button_pressed(1) and mouse_livre:
            state = "saiu"
            mouse_livre = False

        Botao_jogar.draw()
        janela.draw_text("JOGAR", janela.width / 2 - Botao_jogar.width / 2 + 63, janela.height / 2 + nova_dist, tam,
                         preto, "Calibri", True)

        Botao_dificuldade.draw()
        janela.draw_text("DIFICULDADE", janela.width / 2 - Botao_jogar.width / 2 + 40,
                         janela.height / 2 + distancia + nova_dist, tam, preto, "Calibri", True)

        Botao_rank.draw()
        janela.draw_text("RANK", janela.width / 2 - Botao_jogar.width / 2 + 68,
                         janela.height / 2 + (distancia * 2) + nova_dist, tam, preto, "Calibri", True)

        Botao_sair.draw()
        janela.draw_text("SAIR", janela.width / 2 - Botao_jogar.width / 2 + 68,
                         janela.height / 2 + (distancia * 3) + nova_dist, tam, preto, "Calibri", True)

        Titulo.draw()
    
    if state == "pausa":
        menu_pausa = Sprite("pausa.xcf")
        menu_pausa.set_position(janela.width / 2 - menu_pausa.width / 2, janela.height / 2 - menu_pausa.height / 2)
        menu_pausa.draw()
        janela.draw_text("Esc para voltar ao jogo", janela.width / 2 - 90,
                         janela.height / 2 + (distancia * 3) + nova_dist, tam, branco, "Calibri", True)

        if teclado.key_pressed("esc") and not esc_press:
            state = "jogando"
        esc_press = teclado.key_pressed("esc")
    
    if state == "jogando":
        vel_jog = 350
        vel_tiro = 400
        
        janela.set_background_color(preto)
        
        if not inimigos_criados:
            preenche_inimigos(7, 7)
            inimigos_criados = True
        
        jogador.draw()
        if teclado.key_pressed("esc") and not esc_press:
            state = "pausa"
        esc_press = teclado.key_pressed("esc")


        for f in range(len(matriz_de_mons)):
            for t in range(len(matriz_de_mons[f])):
                inimigo = matriz_de_mons[f][t]
                inimigo.draw()
                inimigo.update()
                inimigo.x += vel_ini * delta_time
                if inimigo.x <= 0 or inimigo.x + inimigo.width >= janela.width:
                    pass
        
        inverter = False
        for f in range(len(matriz_de_mons)):
            for t in range(len(matriz_de_mons[f])):
                inimigo = matriz_de_mons[f][t]
                if inimigo.x <= 0 or inimigo.x + inimigo.width >= janela.width:
                    inverter = True
                    break
            if inverter:
                break
        
        if inverter:
            
            ajuste_x = 0
            if vel_ini > 0:
                ajuste_x = -1
            else: 
                ajuste_x = 1

            vel_ini *= -1
            
            for f in range(len(matriz_de_mons)):
                for t in range(len(matriz_de_mons[f])):
                    matriz_de_mons[f][t].y += pulo
                    matriz_de_mons[f][t].x += ajuste_x

        if teclado.key_pressed("space"):
            if timer >= tempo_dif:
                timer = 0
                da_tiro()

        for tiro in tiros:
            tiro.draw()
            tiro.y -= vel_tiro * delta_time
            
        
        tiros_a_manter = []
        for tiro in tiros:
            tiro.y -= vel_tiro * delta_time
            if tiro.y > 0:
                tiros_a_manter.append(tiro)
        tiros = tiros_a_manter


        if teclado.key_pressed("RIGHT"):
            jogador.x += vel_jog * delta_time
        if teclado.key_pressed("LEFT"):
            jogador.x -= vel_jog * delta_time

    if jogador.x < 0:
        jogador.x = 0
    if jogador.x > janela.width - jogador.width:
        jogador.x = janela.width - jogador.width

    if state == "dificuldades":
        janela.set_background_color((0, 0, 0))

        Facil.draw()
        Medio.draw()
        Dificil.draw()
        Impossivel.draw()
        
        janela.draw_text("FÁCIL", Facil.x + 63, Facil.y, tam, preto, "Calibri", True)
        janela.draw_text("MÉDIO", Medio.x + 63, Medio.y, tam, preto, "Calibri", True)
        janela.draw_text("DIFÍCIL", Dificil.x + 63, Dificil.y, tam, preto, "Calibri", True)
        janela.draw_text("IMPOSSÍVEL", Impossivel.x + 40, Impossivel.y, tam, preto, "Calibri", True)
        
        if mouse.is_over_object(Facil) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 0.5
            vel_ini = 100
            inimigos_criados = False
        
        if mouse.is_over_object(Medio) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 0.3
            vel_ini = 150
            inimigos_criados = False
        
        if mouse.is_over_object(Dificil) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 0.2
            vel_ini = 200
            inimigos_criados = False
        
        if mouse.is_over_object(Impossivel) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 0.1
            vel_ini = 300
            inimigos_criados = False
            
        if teclado.key_pressed("esc"):
            state = "string"

    if state == "rank":
        janela.set_background_color((0, 0, 0))

        janela.draw_text("RANK", janela.width / 2 - 80, 20, 50, branco, "Calibri", True)
        if teclado.key_pressed("esc"):
            state = "string"

    if not mouse.is_button_pressed(1):
        mouse_livre = True

    if state == "saiu":
        break

    janela.update()
