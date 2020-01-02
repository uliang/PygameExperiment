import pygame
import math

pygame.init()


def title(app):
    title_font = pygame.font.SysFont(None, 60)
    title_color = (255, 255, 255)
    title = title_font.render(
        "Joe Dever's Lone Wolf", True, title_color)
    titlepos = title.get_rect(centerx=app.screen.get_width()/2,
                              centery=app.screen.get_height()/2)
    app.background.blit(title, titlepos)

    subtitle_font = pygame.font.SysFont(None, 30)
    subtitle = subtitle_font.render(
        "Press any key", True, title_color)
    subtitle_offset = 50

    if app.manager.wipe:
        subtitle = pygame.Surface(subtitle.get_rect().size)

    subtitlepos = subtitle.get_rect(centerx=app.screen.get_width()/2,
                                    centery=app.screen.get_height()/2+subtitle_offset)
    app.background.blit(subtitle, subtitlepos)
