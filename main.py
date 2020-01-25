import pygame 

from game_objects import Application, ApplicationConfig

def main(): 
    pygame.init()
    app = Application(ApplicationConfig) 
    app.run_forever() 

if __name__=='__main__': 
    main()