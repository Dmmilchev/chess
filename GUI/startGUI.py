import pygame
import pygame_gui


class StartGUI:
    def __init__(self, width: int, height:int) -> None:
        self.__width: int = width
        self.__height: int = height
        self.__background_image = (
            pygame.transform.scale(pygame.image.load('./static/background.jpg'), (self.__width, self.__height)))

    def while_loop(self) -> None:
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        window_size = (self.__width, self.__height)
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Deo\'s chess')

        # Set up the UI manager
        ui_manager = pygame_gui.UIManager(window_size, theme_path='./static/theme.json')

        # Set up the clock
        clock = pygame.time.Clock()

        # Create a button
        button_rect = pygame.Rect(350, 275, 100, 50)
        button = pygame_gui.elements.UIButton(relative_rect=button_rect,
                                              text='Click Me',
                                              manager=ui_manager)

        # Create a text box
        text_input_rect = pygame.Rect(250, 200, 300, 50)
        text_input = pygame_gui.elements.UITextEntryLine(relative_rect=text_input_rect,
                                                         manager=ui_manager)

        # Create a label
        label_rect = pygame.Rect(250, 100, 300, 50)  # Position and size of the label
        label = pygame_gui.elements.UILabel(
            relative_rect=label_rect,
            text="Welcome to Deo's Chess",
            manager=ui_manager,
            object_id="#welcome_label"
        )

        # Set the font and font size
        #ui_manager.ui_theme.font_dictionary.default_font = pygame.font.SysFont("Arial", 20)

        running = True
        while running:
            time_delta = clock.tick(60) / 1000.0  # Manage time for the game loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle UI events
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button:
                        print('Button pressed!')

                ui_manager.process_events(event)

            # Update the UI manager
            ui_manager.update(time_delta)

            screen.blit(self.__background_image, (0, 0))

            # Draw the UI elements
            ui_manager.draw_ui(screen)

            # Update the display
            pygame.display.flip()

        pygame.quit()


gui = StartGUI(800, 800)
gui.while_loop()