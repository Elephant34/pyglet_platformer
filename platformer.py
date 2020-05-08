'''
Opens a pyglet window and starts the game
'''
import pyglet
import glooey

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
        self.pause = True

    def on_draw(self):
        '''
        Draws the window
        '''
        if self.main_menu:
            self.menu_batch.draw()
        elif not self.pause:
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

    def load_menu_batch(self):
        '''
        Loads all of the items for the main menu GUI
        '''

        return
    
    def load_game_batch(self):
        '''
        Loads all of the items for the initial game
        '''

        return
    
    def update(self, dt):
        '''
        Updates all loaded enities and passes required data
        '''

        return


if __name__ == "__main__":

    game = Game()
    pyglet.clock.schedule_interval(game.update, 1/120.0)
    pyglet.app.run()