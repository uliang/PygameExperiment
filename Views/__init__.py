import pygame

pygame.init()


def title(app):
    title_font = pygame.font.SysFont(None, 60)
    title_color = (255, 255, 255)
    title = title_font.render(
        "Joe Dever's Lone Wolf", True, title_color)
    titlepos = title.get_rect(centerx=app.screen.get_width()/2,
                              centery=app.screen.get_height()/2)
    app.background.blit(title, titlepos)
