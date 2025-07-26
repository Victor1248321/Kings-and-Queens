import pygame
from screen_data import *

pygame.init()


def draw_board():
    #Size of Each Square of the Board is Calculated
    square_size = WIDTH // 8 

    for row in range(8):
        for col in range(8):
            
            #Square Color is Determined
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            
            
            pygame.draw.rect(SCREEN, color, (col * square_size, row * square_size, square_size, square_size))

def main():
    #Welcome Message
    print("Welcome to Kings and Queens!")

    #Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Board is Drawn
        draw_board()  
        #The Display is Updated
        pygame.display.flip() 

    pygame.quit()



if __name__ == "__main__":
    main()