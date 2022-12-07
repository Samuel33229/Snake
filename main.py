# Imports libraries and modules
import pygame
from pygame.locals import *
import constants
import time
import random

# Creating a Apple class
class Apple():
    def __init__(self, parent_window):
        self.image = pygame.image.load("images/apple.png")
        self.parent_window = parent_window
        self.x = 120
        self.y = 120
        
    def draw(self):
        self.parent_window.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    # Move method
    def move(self):
        self.x = random.randint(24, 776)
        self.y = random.randint(24, 576)

class Snake():
    # Adding length parameter
    def __init__(self, window, length):
        self.length = length
        self.parent_window = window
        # Load the snake body image
        self.snake_body = pygame.image.load("images\snake_body.png")
        # 4.2 Initial position
        self.x = [constants.SNAKE_BODY_SIZE]*length
        self.y = [constants.SNAKE_BODY_SIZE]*length
        # Initial movement direction of the snake
        self.direction = "down"

    def increse_lenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        
    def move_left(self):
        # setting direction of the snake
        self.direction = "left"
        
    def move_right(self):
        # setting direction of the snake
        self.direction = "right"
        
    def move_up(self):
        # setting direction of the snake
        self.direction = "up"
        
    def move_down(self):
        # setting direction of the snake
        self.direction = "down"
        
    def walk(self):
        # check snakes' direction and move it
        for i in range(self.length-1,0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        if self.direction == 'left':
            self.x[0] -= constants.SNAKE_BODY_SIZE
        if self.direction == 'right':
            self.x[0] += constants.SNAKE_BODY_SIZE
        if self.direction == 'up':
            self.y[0] -= constants.SNAKE_BODY_SIZE
        if self.direction == 'down':
            self.y[0] += constants.SNAKE_BODY_SIZE
        
        # draw snake for each chance of direction
        self.draw()
        
        
    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)
        # 4.4 Draw the snake body in diferets coordinates
        for i in range(self.length):
            self.parent_window.blit(self.snake_body, (self.x[i], self.y[i]))
            pygame.display.flip()


class Game():
    
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Displaying a window
        self.window = pygame.display.set_mode(constants.SIZE)
        # Setting a window title
        self.title = pygame.display.set_caption(constants.TITLE)
        # Setting a window icon
        self.icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(self.icon)
        # Setting a background color
        self.window.fill(constants.BG_COLOR)
        
        # Creating a snake object
        self.snake = Snake(self.window, 4)
        self.snake.draw()
        
        # Draw the apple
        self.apple = Apple(self.window)
        self.apple.draw()
        
        pygame.display.update()

    # Collition logic
    def is_collition(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + constants.APPLE_SIZE:
            if y1 >= y2 and y1 < y2 + constants.APPLE_SIZE:
                return True
        return False

    # Play method
    def play(self):
        self.snake.walk()
        self.apple.draw()

        if self.is_collition(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            #print("There is collition")
            self.snake.increse_lenght()
            self.apple.move()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        running = False
                    
                    # Movement to left
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    
                    # Movement to right
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    
                    # Movement to up 
                    if event.key == K_UP:
                        self.snake.move_up()
                    
                    # Movement to down
                    if event.key == K_DOWN:
                        self.snake.move_down()  
                    
                        
                elif event.type == QUIT:
                    running = False
                  
            self.play()
            time.sleep(0.3)

# Creating a game object  
game = Game()
game.run()
    