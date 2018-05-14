import pygame
import random
import time

class MainWindow:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.display=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Soccer Run")     

mainWindow = MainWindow(600,826)      