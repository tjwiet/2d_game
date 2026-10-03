import pygame




def main():
    # pygame setup
    pygame.init()
    pygame.display.set_caption("2D Game")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    # game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("Blue")

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
