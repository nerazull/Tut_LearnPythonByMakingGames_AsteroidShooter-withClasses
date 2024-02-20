import pygame, sys

class Ship(pygame.sprite.Sprite):
	def __init__(self,groups):

		# 1. we have to init the parent class
		super().__init__(groups) 

		# 2. We need a surface -> image
		self.image = pygame.image.load('D:/Programming/Learn Python by making games/Asteroid Shooter/asteroid_shooter_files/project_4 - Image Text/graphics/ship.png').convert_alpha()

		# 3. We need a rect
		self.rect = self.image.get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT / 2))

class Laser(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('D:/Programming/Learn Python by making games/Asteroid Shooter/asteroid_shooter_files/project_4 - Image Text/graphics/laser.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)

# exercise
# Create a laser sprite
# create a new class + a new group
# when the laser object is created, you should be able to set the position via the arguments

# basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter with Classes')
clock = pygame.time.Clock()

# background
background_surf = pygame.image.load('D:/Programming/Learn Python by making games/Asteroid Shooter/asteroid_shooter_files/project_4 - Image Text/graphics/background.png').convert()

# sprite groups
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)
laser = Laser((1000,500),laser_group)

# game loop
while True:

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# delta time
	dt = clock.tick() / 1000

	# background
	display_surface.blit(background_surf,(0,0))

	# graphics
	spaceship_group.draw(display_surface)
	laser_group.draw(display_surface)

	# draw the frame
	pygame.display.update()