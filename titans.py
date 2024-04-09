import pygame
import constantes

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("This is a game project of Attack on Titan")

class Jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Titan(Jugador):
    def __init__(self, nombre, edad, poder, vida, altura):
        super().__init__(nombre, edad)
        self.poder = poder
        self.vida = vida
        self.altura = altura

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con poder {self.poder}")
        objetivo.vida -= self.poder

    def defender(self):
        print(f"{self.nombre} se defiende")
      
class TitanEnemigo(Titan):
    def __init__(self, nombre, edad, poder, vida, altura):
        super().__init__(nombre, edad, poder, vida, altura)

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con poder {self.poder}")
        objetivo.vida -= self.poder

    def defender(self):
        print(f"{self.nombre} se defiende")


jugador1 = Titan("Eren", 20, 10, 100, 20)
enemigo1 = TitanEnemigo("Armin", 100, 20, 200, 50)

jugador1.atacar(enemigo1)
enemigo1.atacar(jugador1)

ejecutar  = True
while ejecutar == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False
pygame.quit()