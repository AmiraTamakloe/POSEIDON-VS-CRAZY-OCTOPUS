import pygame
import os

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "freesansbold.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

playerImg = pygame.image.load(f"images/poseidon-2.png")
# Main Menu
def main_menu():
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_SPACE:
                    if selected == "start":
                        menu = False
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(blue)
        title = text_format("Crazy octopus vs Poseidon", font, 50, yellow)
        if selected == "start":
            text_start = text_format("START", font, 50, white)
        else:
            text_start = text_format("START", font, 50, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 50, white)
        else:
            text_quit = text_format("QUIT", font, 50, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(playerImg,(360, 215) )
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 350))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 400))
        pygame.display.update()
        clock.tick(FPS)