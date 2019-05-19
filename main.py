import pygame, sys
import random

class Runner():
    
    __customes = ("player1", "player2", "player3")
    
    def __init__(self, x=0, y=0):
        
        ixCustome = random.randint(0, 2)
        
        self.custome = pygame.image.load("img/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position [0] += random.randint(1, 6)

class Game():
    runners = []
    __posY = (130, 200, 270)
    __names = ("Ferrari", "Lotus", "Mclaren")
    __starLine = -120
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("img/background.jpg")
        pygame.display.set_caption("Carrera de Bolidos")
        
        for i in range (3):
            theRunner = Runner(self.__starLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
            
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for actRunner in self.runners:
                actRunner.avanzar()
                if actRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(actRunner.name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0, 0))
            
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()    

     
        
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()