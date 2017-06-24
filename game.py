import pygame
import start_menu
import player

#initialize game components
pygame.init()
CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT = 1000, 1000
screen = pygame.display.set_mode((CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT))
clock = pygame.time.Clock()

RED = (255, 0, 0)
BLACK = (0, 0, 0)

init_vel = 10

dude = player.Player(CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT)
background = pygame.Surface([CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT])
background.fill(BLACK)

def game():
	playing = True

	sprites = pygame.sprite.Group()
	sprites.add(dude)
	traj = 0

	while playing:
		keyin = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					dude.vel = init_vel
					traj = dude.angle

		if dude.vel > 0:
			dude.update(traj)
			dude.vel = dude.vel - ((.01 * init_vel) * (dude.vel)) + (.013 * init_vel)
		#	print (dude.vel)
			if dude.vel < .1 * init_vel:
				dude.vel = 0

		dude.angle += 3

		update_screen()

	quit_game()

def update_screen():
	screen.blit(background, (0, 0))
	print_rot_player()
	pygame.display.flip()
	clock.tick(60)

def print_rot_player():
	rot_img = pygame.transform.rotate(dude.image, dude.angle * -1)
	rot_rect = rot_img.get_rect(center = dude.rect.center)
	screen.blit(rot_img, (rot_rect.x, rot_rect.y))

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
