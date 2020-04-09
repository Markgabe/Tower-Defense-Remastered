class GameState:
    def __init__(self):
        self.MENU_STATE = self.RUNNING = True
        self.OPTIONS_STATE = False

    def exit_game(self):
        self.MENU_STATE = self.OPTIONS_STATE = self.RUNNING = False

    def enter_options(self):
        self.OPTIONS_STATE = True
        self.MENU_STATE = False

    def enter_menu(self):
        self.OPTIONS_STATE = False
        self.MENU_STATE = True
