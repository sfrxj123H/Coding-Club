import pygame  # Import game

pygame.init()  # Start pygame
screen = pygame.display.set_mode((500, 600))  # Set screen size to 500 x 600
running = True  # Continue running
bgColor = (150, 150, 150)  # Set variable for bgColor - Color => (R, B ,G)
font = pygame.font.SysFont('timesnewroman',  30)
plusSign = font.render("+", True, (150, 150, 150))
minusSign = font.render("-", True, (150, 150, 150))
startSign = font.render("Start", True, (150, 150, 150))
resetSign = font.render("Reset", True, (150, 150, 150))
while running:  # Check events and prevent instance end
    screen.fill(bgColor)  # Set background with var bgColor

    pygame.draw.rect(screen, (255, 255, 0), (100, 50, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), (100, 200, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), (200, 50, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), (200, 200, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), (300, 50, 150, 50))
    pygame.draw.rect(screen, (255, 255, 0), (300, 200, 150, 50))

    screen.blit(plusSign, (100, 50))
    screen.blit(minusSign, (100, 200))
    screen.blit(plusSign, (200, 50))
    screen.blit(minusSign, (200, 200))
    screen.blit(startSign, (300, 50))
    screen.blit(resetSign, (300, 200))

    pygame.draw.rect(screen, (0, 0, 0), (50, 520, 400, 50))
    pygame.draw.rect(screen, (255, 255, 255), (60, 530, 380, 30))
    pygame.draw.circle(screen, (0, 0, 0), (250, 400), 100)
    pygame.draw.circle(screen, (255, 255, 255), (250, 400), 90)
    pygame.draw.line(screen, (0, 0, 0), (250, 400), (250, 320), 5)
    pygame.draw.circle(screen, (0, 0, 0), (250, 400), 10)

    for event in pygame.event.get():  # Check anytime if an event happens
        if event.type == pygame.QUIT:  # Check for user exit request
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Check for any mouse clicks
            if event.button == 1:
                print("XXX")
    pygame.display.flip()
pygame.quit()
