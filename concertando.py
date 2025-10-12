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

teclado = janela.get_keyboard()

Titulo = Sprite("titulo.png")
Titulo.set_position((janela.width/2 - Titulo.width/2), (0-40))

Botao_jogar = Sprite("ranking.png")
Botao_jogar.set_position(janela.width/2 - Botao_jogar.width/2, janela.height/2 + nova_dist)

Botao_dificuldade = Sprite("ranking.png")
Botao_dificuldade.set_position(janela.width/2 - Botao_jogar.width/2, janela.height/2 + distancia + nova_dist)

Botao_rank = Sprite("ranking.png")
Botao_rank.set_position(janela.width/2 - Botao_jogar.width/2, janela.height/2 + (distancia*2) + nova_dist)

Botao_sair = Sprite("ranking.png")
Botao_sair.set_position(janela.width/2 - Botao_jogar.width/2, janela.height/2 + (distancia*3) + nova_dist)

Facil = Sprite("ranking.png")
Facil.set_position(janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*0) + nova_dist)

Medio = Sprite("ranking.png")
Medio.set_position(janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*1) + nova_dist)

Dificil = Sprite("ranking.png")
Dificil.set_position(janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*2) + nova_dist)

Impossivel = Sprite("ranking.png")
Impossivel.set_position(janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*3) + nova_dist)

jogador = Sprite("jogador.xcf")
jogador.set_position(janela.width/2 - jogador.width/2, janela.height*7/8)

state = "string"

#tapa = Sprite("tapa.png")
#tapa.set_position(janela.width*3/4, janela.height*1/3)

branco = (255, 255, 255)
preto = (0, 0, 0)
delta_time = janela.delta_time()
#click
mouse_livre = True

tiros = []

timer = 0
esc_press = False
def da_tiro():
    tiro = Sprite("projetil.xcf")
    tiro.set_position(jogador.x + jogador.width/2 - tiro.width/2, janela.height*7/8 - jogador.width + 50)
    tiros.append(tiro)

while True:
    if state == "string":
        janela.set_background_color(preto)
        if mouse.is_over_object(Botao_jogar) and mouse.is_button_pressed(1) and mouse_livre:
            state = "jogando"
            tempo_dif = 1
            mouse_livre =False
        if mouse.is_over_object(Botao_dificuldade) and mouse.is_button_pressed(1) and mouse_livre:
            state = "dificuldades"
            mouse_livre =False
        if mouse.is_over_object(Botao_rank) and mouse.is_button_pressed(1) and mouse_livre:
            state = "rank"
            mouse_livre =False
        if mouse.is_over_object(Botao_sair) and mouse.is_button_pressed(1) and mouse_livre:
            state = "saiu"
            mouse_livre =False
            
        Botao_jogar.draw()
        janela.draw_text("JOGAR", janela.width/2 - Botao_jogar.width/2 + 63, janela.height/2 + nova_dist, tam, preto, "Calibri", True)
        
        Botao_dificuldade.draw()
        janela.draw_text("DIFICULDADE", janela.width/2 - Botao_jogar.width/2 + 40, janela.height/2 + distancia + nova_dist, tam, preto, "Calibri", True)
        
        Botao_rank.draw()
        janela.draw_text("RANK", janela.width/2 - Botao_jogar.width/2 + 68, janela.height/2 + (distancia*2) + nova_dist, tam, preto, "Calibri", True)
        
        Botao_sair.draw()
        janela.draw_text("SAIR", janela.width/2 - Botao_jogar.width/2 + 68, janela.height/2 + (distancia*3) + nova_dist, tam, preto, "Calibri", True)
        
        Titulo.draw()
    if state == "pausa":
        vel_jog = 0
        vel_tiro = 0
        delta_time = 0
        menu_pausa = Sprite("pausa.xcf")
        menu_pausa.set_position(janela.width/2 - menu_pausa.width/2, janela.height/2 - menu_pausa.height/2)
        menu_pausa.draw()
        janela.draw_text("Esc para voltar ao jogo", janela.width/2 - 90, janela.height/2 + (distancia*3) + nova_dist, tam, branco, "Calibri", True)

        if teclado.key_pressed("esc") and not esc_press:
            state = "jogando"
        esc_press = teclado.key_pressed("esc")
            

    if state == "jogando":
        vel_jog = 350
        vel_tiro = 120
        delta_time = janela.delta_time()
        janela.set_background_color(preto)
        jogador.draw()
        if teclado.key_pressed("esc") and not esc_press:
            state = "pausa"
        esc_press = teclado.key_pressed("esc")
            

        #dando tiros
        if teclado.key_pressed("space"):
            if timer >= tempo_dif:
                timer = 0
                da_tiro()
        
        for tiro in tiros:
            tiro.draw()
            tiro.y -= vel_tiro*delta_time
            if tiro.y <= 0:
                tiros.pop(0)
        	
        #barra esquerda controlado por W, S:
        if teclado.key_pressed("RIGHT"):
            jogador.x += vel_jog * delta_time
        if teclado.key_pressed("LEFT"):
            jogador.x -= vel_jog * delta_time

	#colisão barras:
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
        
        janela.draw_text("IMPOSSÍVEL",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*0) + nova_dist, tam, preto, "Calibri", True)
        janela.draw_text("DIFÍCIL",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*1) + nova_dist, tam, preto, "Calibri", True)
        janela.draw_text("MÉDIO",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*2) + nova_dist, tam, preto, "Calibri", True)
        janela.draw_text("FÁCIL",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*3) + nova_dist, tam, preto, "Calibri", True)

        if mouse.is_over_object(Facil) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 4
        #if mouse.is_over_object(Facil):
            #tapa.draw()
        if mouse.is_over_object(Medio) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 3
        if mouse.is_over_object(Dificil) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 2
        if mouse.is_over_object(Impossivel) and mouse.is_button_pressed(1):
            state = "jogando"
            tempo_dif = 1
        if teclado.key_pressed("esc"):
        	state = "string"

    if state == "rank":
        janela.set_background_color((0, 0, 0))
        
        janela.draw_text("RANK", janela.width/2 - 80, 20, 50, branco, "Calibri", True)
        if teclado.key_pressed("esc"):
        	state = "string"
    
    if not mouse.is_button_pressed(1):
    	mouse_livre = True

    if state == "saiu":
        break

    timer += delta_time


    janela.update()