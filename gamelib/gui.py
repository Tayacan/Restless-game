import pygame
from gamelib.input import Input

class GUI:

    @staticmethod
    def Button(text,rect,color=(0,0,0)):
        screen = pygame.display.get_surface()
        fontname = pygame.font.get_default_font()
        font = pygame.font.SysFont(fontname,30)
        surfacef = font.render(text,True,color)

        textRect = pygame.Rect((rect.width  - surfacef.get_width())/2
                              ,(rect.height - surfacef.get_height())/2
                              ,surfacef.get_width()
                              ,surfacef.get_height())

        surface = pygame.Surface(rect.size)
        surface.fill((200,200,200))
        surface.blit(surfacef,textRect)

        screen.blit(surface,rect)

        return Input.up("MB1") and rect.collidepoint(Input.mouse_pos)

    @staticmethod
    def Label(text,rect,color=(0,0,0),size=30):
        screen = pygame.display.get_surface()
        fontname = pygame.font.get_default_font()
        font = pygame.font.SysFont(fontname,size)
        surface = font.render(text,True,color)

        screen.blit(surface,rect)
