import pygame

EVENTLIST = set(range(pygame.NUMEVENTS))
ENTRY = pygame.USEREVENT+0
BLINK = pygame.USEREVENT+1
EXIT = pygame.USEREVENT+2
TRANS = pygame.USEREVENT+3


START_SIG = pygame.event.Event(ENTRY)
BLINK_SIG = pygame.event.Event(BLINK)
MOUSEDOWN_SIG = pygame.event.Event(pygame.MOUSEBUTTONDOWN)
