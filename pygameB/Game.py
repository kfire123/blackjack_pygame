from Player import Player
from Dealer import Dealer
import pygame as pg
from pygame.locals import QUIT
import os

# INITALIZING PYGAME
pg.init()

# setting up the screen
HEIGHT = 600
WIDTH = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))

# setting the caption
pg.display.set_caption("Blackjack")

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# game mechanics
CLOCK = pg.time.Clock()
FPS = 60 

# images
cardback = pg.image.load(os.path.join("images", "card_image.png"))

card_height = cardback.get_height()


# boolean used to exit the game
running = True

# drawing the screen
def draw_window():
    screen.fill(BLUE)
    screen.blit(cardback, (WIDTH // 2, HEIGHT//2 - (card_height // 2)))

    pg.display.update()

# handle the events
def handle_events():
    global running
    for event in pg.event.get():
        if event.type == QUIT:
            running = False


def main():
    while running:
        draw_window()
        handle_events()

if __name__ == "__main__":
    main()
    pg.quit()
