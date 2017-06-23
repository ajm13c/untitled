import pygame
import start_menu

#initialize game components
pygame.init()
CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT))

def game():
	playing = True
	while playing:
		keyin = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
		pygame.display.flip()

def quit_game():
	pygame.quit()
	quit()

def to_menu():
	pygame.display.set_caption('Game Menu')
	funcs = { 'Start': game,
		  'Quit' : quit_game }
	menu = start_menu.start_menu(funcs.keys(), funcs, CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT)
	menu.run(screen)

if __name__ == '__main__':
	to_menu()




