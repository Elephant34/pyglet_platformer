'''
Opens a pyglet window and starts the game
'''
import pyglet
import glooey

from gui_assets.labels import Title
from gui_assets.buttons import MenuButton

class Window(pyglet.window.Window):
    '''
    The main game window
    '''

    def __init__(self, width, height, batches, **kwargs):
        '''
        Loads the game window
        '''
        super().__init__(width, height, **kwargs)
        self.width = width
        self.height = height

        self.game_batch = batches["game_batch"]
        self.menu_batch = batches["menu_batch"]

        self.main_menu = True

    def on_draw(self):
        '''
        Draws the window
        '''
        if self.main_menu:
            self.menu_batch.draw()
        else:
            self.clear()
            self.game_batch.draw()

class Game():
    '''
    Loads the game and contains all global varibales
    '''

    def __init__(self):
        '''
        Starts the game setup
        '''
        self.batches = {
            "game_batch": pyglet.graphics.Batch(),
            "menu_batch": pyglet.graphics.Batch(),
        }


        self.window = Window(800, 600, self.batches)
        self.window.set_caption("Pyglet Platformer")

        self.load_menu_batch()
        self.load_game_batch()

        self.paused = False

    def load_menu_batch(self):
        '''
        Loads all of the items for the main menu GUI
        '''

        menu_gui = glooey.Gui(self.window, batch=self.batches["menu_batch"])

        v_container = glooey.VBox()
        v_container.alignment = "center"

        v_container.add(Title("Platformer"))
        v_container.add(MenuButton("Play", self.play))
        v_container.add(MenuButton("Exit", self.exit_game))

        menu_gui.add(v_container)

    
    def load_game_batch(self):
        '''
        Loads all of the items for the initial game
        '''

    
    def play(self):
        '''
        Loads the first level
        '''

        print("play")
    
    def exit_game(self):
        '''
        Quits the game
        '''
        self.window.close()
    
    def update(self, dt):
        '''
        Updates all loaded enities and passes required data
        '''



if __name__ == "__main__":

    game = Game()
    pyglet.clock.schedule_interval(game.update, 1/120.0)
    pyglet.app.run()