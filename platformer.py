'''
Opens a pyglet window and starts the game
'''
import json
import pathlib

import glooey
import pyglet

from game_assets import player, coin, platform
from gui_assets.buttons import MenuButton
from gui_assets.labels import Title, Standared


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
        self.clear()
        if self.main_menu:
            self.menu_batch.draw()
        else:
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
        self.gui_group = pyglet.graphics.OrderedGroup(1)
        self.game_group = pyglet.graphics.OrderedGroup(0)

        self.window = Window(800, 600, self.batches)
        self.window.set_caption("Pyglet Platformer")

        self.load_menu_batch()

        self.current_level = 0
        self.score = 0

        self.paused = False

    def load_menu_batch(self):
        '''
        Loads all of the items for the main menu GUI
        '''

        menu_gui = glooey.Gui(
            self.window,
            batch=self.batches["menu_batch"],
            group=self.gui_group
        )

        v_container = glooey.VBox()
        v_container.alignment = "center"

        v_container.add(Title("Platformer"))
        v_container.add(MenuButton("Play", self.play))
        v_container.add(MenuButton("Exit", self.exit_game))

        menu_gui.add(v_container)

    def play(self):
        '''
        Loads the level
        '''

        self.window.main_menu = False

        self.load_level()

    def load_level(self):
        '''
        Decodes the level from the level.json
        '''

        level_path = pathlib.Path(
            "static_assets/levels/level{}.json".format(self.current_level)
        )

        with level_path.open(mode="r") as data:
            level_data = json.load(data)

        # Loads the HUD of the main game
        hud_gui = glooey.Gui(
            self.window,
            batch=self.batches["game_batch"],
            group=self.gui_group
        )
        h_container = glooey.HBox()
        h_container.alignment = "fill top"

        self.level_lbl = Standared(
            "Level: {}".format(self.current_level)
        )
        h_container.add(self.level_lbl)

        self.score_lbl = Standared(
            "Score: {}".format(self.score)
        )
        h_container.add(self.score_lbl)

        hud_gui.add(h_container)

        # Loads the items to populate the game
        self.player = player.Player(
            level_data["player_spawn"]["x"],
            level_data["player_spawn"]["y"],
            batch=self.batches["game_batch"],
            group=self.game_group
        )

        self.platform_list = []
        for i in level_data["platforms"]:
            temp = platform.Platform(
                    i["x"],
                    i["y"],
                    batch=self.batches["game_batch"],
                    group=self.game_group
                )
            temp.scale_x = i["scale_x"]
            self.platform_list.append(temp)

        self.coin_list = []
        for i in level_data["coins"]:
            temp = coin.Coin(
                x=i["x"],
                y=i["y"],
                batch=self.batches["game_batch"],
                group=self.game_group
            )
            self.coin_list.append(temp)

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
