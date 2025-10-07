
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

janela = Window(1280, 900)
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

jogador = Sprite("jogador.png")
jogador.set_position(janela.width/2 - jogador.width/2, janela.height*7/8)

state = "string"

#tapa = Sprite("tapa.png")
#tapa.set_position(janela.width*3/4, janela.height*1/3)

branco = (255, 255, 255)
preto = (0, 0, 0)

vel_jog = 200

#click
mouse_livre = True

while True:
    if state == "string":
        janela.set_background_color(preto)
        if mouse.is_over_object(Botao_jogar) and mouse.is_button_pressed(1) and mouse_livre:
            state = "jogando"
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
    
    if state == "jogando":
        janela.set_background_color(preto)
        jogador.draw()
        janela.draw_text("JOGANDO", janela.width/2 - 120, 20, 50, branco, "Calibri", True)
        if teclado.key_pressed("esc"):
        	state = "string"
        	
        #barra esquerda controlado por W, S:
        if teclado.key_pressed("RIGHT"):
            jogador.x += vel_jog * janela.delta_time()
        if teclado.key_pressed("LEFT"):
            jogador.x -= vel_jog * janela.delta_time()

	#colisão barras:
	if jogador.x < 0:
	    jogador.x = 0


    if state == "dificuldades":
        janela.set_background_color((0, 0, 0))
        
        Facil.draw()
        Medio.draw()
        Dificil.draw()
        Impossivel.draw()
        janela.draw_text("DIFICULDADES", janela.width/2 - 200, 20, 50, branco, "Calibri", True)
        
        janela.draw_text("IMPOSSÍVEL",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*0) + nova_dist, tam, preto, "Calibri", True)
        janela.draw_text("DIFÍCIL",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*1) + nova_dist, tam, preto, "Calibri", True)
        janela.draw_text("MÉDIO",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*2) + nova_dist, tam, preto, "Calibri", True)
        janela.draw_text("FÁCIL",janela.width/2 - Botao_jogar.width/2 - 300, janela.height/2 - (distancia*3) + nova_dist, tam, preto, "Calibri", True)

        if mouse.is_over_object(Facil) and mouse.is_button_pressed(1):
            state = "jogando"
        #if mouse.is_over_object(Facil):
            #tapa.draw()
        if mouse.is_over_object(Medio) and mouse.is_button_pressed(1):
            state = "jogando"
        if mouse.is_over_object(Dificil) and mouse.is_button_pressed(1):
            state = "jogando"
        if mouse.is_over_object(Impossivel) and mouse.is_button_pressed(1):
            state = "jogando"
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


    janela.update()
