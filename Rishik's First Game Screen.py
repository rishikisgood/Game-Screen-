import pygame

pygame.init()


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
CAPTION = "My first game screen"
BACKGROUND_COLOR = (58, 58, 58)  

IMAGE_PATH = "your_image.png"
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(CAPTION)

try:
    image = pygame.image.load(IMAGE_PATH)
    image = pygame.transform.scale(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
except pygame.error as e:
    print(f"Error loading image: {e}")
    print("Please make sure 'your_image.png' exists in the same directory as the script.")
    pygame.quit()
    exit()

image_x = (WINDOW_WIDTH - IMAGE_WIDTH) // 2
image_y = (WINDOW_HEIGHT - IMAGE_HEIGHT) // 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    screen.blit(image, (image_x, image_y))


    pygame.display.flip()

pygame.quit()