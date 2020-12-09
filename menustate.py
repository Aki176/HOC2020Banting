# Import
from state import State
from button import Button

# Draw the menu and make it interact with player
class MenuState(State):
    def __init__(self, screen, resource_manager):
        super().__init__("menu")
        self.resource_manager = resource_manager
        self.textures = resource_manager.scaled_textures
        self.screen = screen
        self.buttons = self.create_buttons()

    def update(self, dt):
        for button in self.buttons:
            button.update()

    def draw(self): # Draw main menu button
        self.screen.fill((0, 0, 0))
        for button in self.buttons:
            button.draw()

    def startup(self, screen, *args): # Startup screen
        self.screen = screen
        self.textures = self.resource_manager.scaled_textures

        self.buttons = self.create_buttons()

    def process_event(self, event):
        for i in self.buttons:
            i.process_event(event)

    def go_to_level_select(self): # After picking level
        self.done = True
        self.next = "levelselect"

    def go_to_level(self): # Choosing level
        self.next_state_args = ("level1", False)
        self.done = True
        self.next = "level"

    def exit_game(self): # Exit
        self.done = True
        self.quit = True

    # Main menu button
    def create_buttons(self):
        buttons = []

        continue_button = Button(self.screen, self.textures["button"].get_rect(
                       center=self.screen.get_rect().center),
                                         [self.textures["button"]],
                                         caption="Play",
                                         command=self.go_to_level)
        continue_button.rect.y -= 200

        buttons.append(continue_button)

        level_select = Button(self.screen, self.textures["button"].get_rect(
                       center=self.screen.get_rect().center),
                                         [self.textures["button"]],
                                         caption="Choose Level",
                                         command=self.go_to_level_select)
        buttons.append(level_select)

        exit_button = Button(self.screen, self.textures["button"].get_rect(
                             center=self.screen.get_rect().center),
                             [self.textures["button"]],
                             caption="Quit",
                             command=self.exit_game)

        exit_button.rect.y += 200

        buttons.append(exit_button)

        return buttons
