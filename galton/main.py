import pygame

pygame.init()


class WIN_CON:
    #-------Window Constants-------#
    width = 1000
    height = 700
    title = "Galton Board Simulation"
    fps = 60
    background = (0, 0, 0)


#------------------------------#
w = WIN_CON()


class TextPrint:
    def __init__(self):
        self.reset()

    def printf(self, screen, color, _size, _font, _x, _y, textString):
        self.font = pygame.font.SysFont(_font, _size)
        textBitmap = self.font.render(textString, True, color)
        _width = textBitmap.get_width()
        screen.blit(textBitmap, [(_x - (_width / 2)), _y])

    def reset(self):
        self.y = 0


class Board:
    def __init__(self, lines):
        self.lines = lines
        self.pegColour = (0, 0, 255)
        self.pegR = 5

    def drawBoard(self, sc):
        bh = 50
        middle = w.width / 2
        margin = bh
        for l in range(1, self.lines +1):
            pegY = bh * l
            if (l == 1):
                pygame.draw.circle(sc, self.pegColour, (middle, pegY), self.pegR)
            elif(l % 2 == 0):
                for s in range(0, (l / 2)):
                    pygame.draw.circle(sc, self.pegColour, (middle + ((margin/2) + (s * margin)), pegY), self.pegR)
                    pygame.draw.circle(sc, self.pegColour, (middle - ((margin/2) + (s * margin)), pegY), self.pegR)
            else:
                pygame.draw.circle(sc, self.pegColour, (middle, pegY), self.pegR)
                for s in range(1, ((l-1)/2) +1):
                    pygame.draw.circle(sc, self.pegColour, (middle + (s * margin), pegY), self.pegR)
                    pygame.draw.circle(sc, self.pegColour, (middle - (s * margin), pegY), self.pegR)

screen = pygame.display.set_mode([w.width, w.height])
pygame.display.set_caption(w.title)
running = True
clock = pygame.time.Clock()
txt = TextPrint()
b = Board(10)

while running:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we exit this loop
    screen.fill(w.background)

    #code here
    #pygame.draw.circle(screen, (255, 0, 0), (w.width / 2, 20), 10)
    b.drawBoard(screen)

    pygame.display.flip()
    clock.tick(w.fps)

pygame.quit()
