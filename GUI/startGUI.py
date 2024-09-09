import pygame
import pygame_gui


class StartGUI:
    def __init__(self, width: int, height:int) -> None:
        self.__width: int = width
        self.__height: int = height
        self.__background_image = (
            pygame.transform.scale(pygame.image.load('./GUI/static/background.jpg'), (self.__width, self.__height)))

    def while_loop(self) -> bool:
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        window_size = (self.__width, self.__height)
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Deo\'s chess')

        # Set up the UI manager
        ui_manager = pygame_gui.UIManager(window_size, theme_path='./GUI/static/theme.json')

        # Set up the clock
        clock = pygame.time.Clock()

        # Create a button
        button_rect = pygame.Rect(250, 275, 300, 100)
        button = pygame_gui.elements.UIButton(relative_rect=button_rect,
                                              text='Start game',
                                              manager=ui_manager)

        # Create a label
        label_rect = pygame.Rect(250, 100, 300, 50)  # Position and size of the label
        label = pygame_gui.elements.UILabel(
            relative_rect=label_rect,
            text="Welcome to Deo's Chess",
            manager=ui_manager,
            object_id="#welcome_label"
        )

        to_return: bool = False
        running = True
        while running:
            time_delta = clock.tick(60) / 1000.0  # Manage time for the game loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    to_return = False

                # Handle UI events
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button:
                        to_return = True
                        running = False

                ui_manager.process_events(event)

            # Update the UI manager
            ui_manager.update(time_delta)

            screen.blit(self.__background_image, (0, 0))

            # Draw the UI elements
            ui_manager.draw_ui(screen)

            # Update the display
            pygame.display.flip()

        pygame.quit()
        return to_return
