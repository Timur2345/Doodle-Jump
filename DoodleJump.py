import pygame
from scripts.app import App

def main():
    pygame.init()
    app = App()
    app.run()
    pygame.quit()

#точка входа
if __name__ == "__main__":
    main()