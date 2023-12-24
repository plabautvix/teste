import pygame
import os

class Velhinha:
    def __init__(self):
        self.screen = pygame.display.set_mode((612, 608))
        self.fundo = pygame.image.load("imagens/fundo.jpg")
        self.rogerio = pygame.image.load("ima   gens/X.png")
        self.rogerio_rect = self.rogerio.get_rect()
        self.nauvia = pygame.image.load("imagens/O.png")
        self.nauvia_rect = self.nauvia.get_rect()
        self.inicio = pygame.image.load("imagens/inicio.png") #tela inicial
        self.fim = pygame.image.load("imagens/fim.png")
        self.o_venceu = pygame.image.load("imagens/ovenceu.png")
        self.x_venceu = pygame.image.load("imagens/xvenceu.png")
        self.empatados = pygame.image.load("imagens/empatados.png")
        self.posicao = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.iniciodejogo = True
        self.tela1 = True
        self.clique = True
        self.jogador = "O"  # Começa com o jogador O
        pygame.mixer.init()
        self.musica = pygame.mixer.music.load("musica/musica.mp3")
        pygame.mixer.music.play(-1)

    def teladeinicio(self):
        while (self.tela1 == True):
            self.screen.blit(self.inicio, (0, 0))

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.screen.blit(self.fim, (0, 0))
                    self.tela1 = False
                    self.iniciodejogo = False
                    pygame.display.update()
                    pygame.time.delay(200) #Demora 2s pra fechar o jogo

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.iniciodejogo = True
                    self.tela1 = False
                pygame.display.update()


    def personagens(self):
        for i in range(3):
            for j in range(3):
                if self.posicao[i * 3 + j] == "X":
                    self.rogerio_rect.center = (j * 200 + 100,i * 200 + 100)
                    self.screen.blit(self.rogerio, self.rogerio_rect)
                elif self.posicao[i * 3 + j] == "O":
                    self.nauvia_rect.center = (j * 200 + 100,i * 200 + 100)
                    self.screen.blit(self.nauvia, self.nauvia_rect)


    def empate(self):
        v = ""
        if (0 not in self.posicao):
            v = "E"
            self.teladevitoria(v)


    def vencedor(self):
        v = ""
    #Separando por linha:
    #AZUL
        if (self.posicao[0] == "X" and self.posicao[1] == "X" and self.posicao[2] == "X"):
            v = "X"
            self.teladevitoria(v)
            
        if (self.posicao[0] == "O" and self.posicao[1] == "O" and self.posicao[2] == "O"):
            v = "O"
            self.teladevitoria(v)

    #VERDE 
        if (self.posicao[3] == "X" and self.posicao[4] == "X" and self.posicao[5] == "X"):
            v = "X"
            self.teladevitoria(v)
            
        if (self.posicao[3] == "O" and self.posicao[4] == "O" and self.posicao[5] == "O"):
            v = "O"
            self.teladevitoria(v)
            
    #ROSA
        if (self.posicao[6] == "X" and self.posicao[7] == "X" and self.posicao[8] == "X"):
            v = "X"
            self.teladevitoria(v)
            
        if (self.posicao[6] == "O" and self.posicao[7] == "O" and self.posicao[8] == "O"):
            v = "O"
            self.teladevitoria(v)


    #Separando por coluna:   
    #ROXO
        if (self.posicao[0] == "X" and self.posicao[3] == "X" and self.posicao[6] == "X"):
            v = "X"
            self.teladevitoria(v)
            
        if (self.posicao[0] == "O" and self.posicao[3] == "O" and self.posicao[6] == "O"):
            v = "O"
            self.teladevitoria(v)

    #CIANO
        if (self.posicao[1] == "X" and self.posicao[4] == "X" and self.posicao[7] == "X"):
            v = "X"
            self.teladevitoria(v)

        if (self.posicao[1] == "O" and self.posicao[4] == "O" and self.posicao[7] == "O"):
            v = "O"
            self.teladevitoria(v)

    #MARROM
        if (self.posicao[2] == "X" and self.posicao[5] == "X" and self.posicao[8] == "X"):
            v = "X"
            self.teladevitoria(v)

        if (self.posicao[2] == "O" and self.posicao[5] == "O" and self.posicao[8] == "O"):
            v = "O"
            self.teladevitoria(v)


    #Separando as diagonais:      
    #VERMELHO
        if (self.posicao[0] == "X" and self.posicao[4] == "X" and self.posicao[8] == "X"):
            v = "X"
            self.teladevitoria(v)
            
        if (self.posicao[0] == "O" and self.posicao[4] == "O" and self.posicao[8] == "O"):
            v = "O"
            self.teladevitoria(v)

    #AMARELO
        if (self.posicao[2] == "X" and self.posicao[4] == "X" and self.posicao[6] == "X"):
            v = "X"
            self.teladevitoria(v)
            
        if (self.posicao[2] == "O" and self.posicao[4] == "O" and self.posicao[6] == "O"):
            v = "O"
            self.teladevitoria(v)


    def teladevitoria(self, v):
        self.iniciodejogo = False
        self.clique = False
        self.vitoria = True
        while self.vitoria:

            if (v == "O"):
                self.screen.blit(self.o_venceu, (0,0))
                
            if (v == "X"):
                self.screen.blit(self.x_venceu, (0,0))
                
            if (v == "E"):
                self.screen.blit(self.empatados, (0,0))
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.screen.blit(self.fim, (0, 0))
                    self.tela1 = False
                    self.iniciodejogo = False
                    self.vitoria = False
                    pygame.display.update()
                    pygame.time.delay(200) #Demora 2s pra fechar o jogo

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.vitoria = False
                    self.iniciodejogo = True
                    self.posicao = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    self.clique = True
            pygame.display.update()
        if self.iniciodejogo:
            self.main()


    def inputmouse(self, event):
        if (event.type == pygame.QUIT):
            self.screen.blit(self.fim, (0, 0))
            self.tela1 = False
            self.iniciodejogo = False
            pygame.display.update()
            pygame.time.delay(200) #Demora 2s pra fechar o jogo
        elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            # Obtém a posição do clique do mouse
            mouseX, mouseY = event.pos
            # Converte as coordenadas do mouse para a grade do jogo
            row = mouseY // 200
            col = mouseX // 200
            index = row * 3 + col
            # Verifica se a célula está vazia antes de fazer um movimento
            if (self.posicao[index] == 0):
                self.posicao[index] = self.jogador
                # Alterna entre os jogadores "X" e "O"
                self.jogador = "O" if self.jogador == "X" else "X"
                     

    def main(self):
        self.teladeinicio() #chamando a tela inicial
        while (self.iniciodejogo == True):
            pygame.display.set_caption("Velhinha") #Nome do jogo
            self.screen.blit(self.fundo, (0, 0))
            self.personagens()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.screen.blit(self.fim, (0, 0))
                    self.tela1 = False
                    self.iniciodejogo = False
                    pygame.display.update()
                    pygame.time.delay(400) #Demora pra fechar o jogo

                elif (event.type == pygame.MOUSEBUTTONDOWN) and (self.clique == True):
                    self.inputmouse(event)
                self.vencedor() #verifica o vencedor
                self.empate() #verifica empate
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = Velhinha()
    game.main()