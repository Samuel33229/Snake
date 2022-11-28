# Imports libraries and modules
import pygame
from pygame.locals import *
import constants
import time

class Snake():
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.snake_body = pygame.image.load("images\snake_body.png")
        self.x = 100
        self.y = 100
        self.direction = "down"


    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)
        self.parent_window.blit(self.snake_body, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        if self.direction == "left":
            self.x -= 10

        if self.direction == "right":
            self.x += 10

        if self.direction == "up":
            self.y -= 10

        if self.direction == "down":
            self.y += 10

        self.draw()





class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(constants.SIZE)
        self.title = pygame.display.set_caption(constants.TITLE)
        self.window.fill(constants.BG_COLOR)
        icon = pygame.image.load("images\icon.png")
        pygame.display.set_icon(icon)

        self.snake = Snake(self.window)
        self.snake.draw()

        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                
                
                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)

game = Game()
game.run()
