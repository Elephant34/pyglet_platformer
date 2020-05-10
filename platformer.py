'''
Opens a pyglet window and starts the game
'''
import json
import pathlib

import glooey
import pyglet
from pyglet.window import key
from game_assets import player, coin, platform
from gui_assets.buttons import MenuButton
from gui_assets.labels import Title, Standared


class Game(pyglet.window.Window):
    '''
    The main game window
    '''

    def __init__(self, width, height, **kwargs):
        '''
        Loads the game window
        '''
        super().__init__(width, height, **kwargs)
        self.width = width
        self.height = height

        self.batches = {
            "game_batch": pyglet.graphics.Batch(),
            "menu_batch": pyglet.graphics.Batch(),
        }
        self.gui_group = pyglet.graphics.OrderedGroup(1)
        self.game_group = pyglet.graphics.OrderedGroup(0)

        self.set_caption("Pyglet Platformer")

        self.load_menu_batch()

        self.jump_keys = [
            key.W,
            key.UP
        ]
        self.left_keys = [
            key.A,
            key.LEFT
        ]
        self.right_keys = [
            key.D,
            key.RIGHT
        ]
        self.pause_keys = [
            key.P,
            key.ESCAPE
        ]

        self.current_level = 0
        self.score = 0

        self.paused = False
        self.main_menu = True

    def on_draw(self):
        '''
        Draws the window
        '''
        self.clear()
        if self.main_menu:
            self.batches["menu_batch"].draw()
        else:
            self.batches["game_batch"].draw()

    def on_key_press(self, symbol, modifiers):
        '''
        Handles key presses
        '''
        if self.main_menu:
            return

        if symbol in self.pause_keys:
            self.game_pause()

        if self.paused:
            return

        if symbol in self.jump_keys:
            self.player.key_press("jump")
        elif symbol in self.left_keys:
            self.player.key_press("left")
        elif symbol in self.right_keys:
            self.player.key_press("right")

    def on_key_release(self, symbol, modifiers):
        '''
        Handles key releases
        '''
        if symbol in self.left_keys:
            self.player.key_release("left")
        elif symbol in self.right_keys:
            self.player.key_release("right")
        elif symbol in self.jump_keys:
            self.player.key_release("jump")

    def load_menu_batch(self):
        '''
        Loads all of the items for the main menu GUI
        '''

        menu_gui = glooey.Gui(
            self,
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

        self.main_menu = False

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
            self,
            batch=self.batches["game_batch"],
            group=self.gui_group
        )
        h_container = glooey.HBox()
        h_container.alignment = "fill top"
        h_container.set_padding(10)

        self.level_lbl = Standared(
            "Level: {}".format(self.current_level)
        )
        h_container.add(self.level_lbl)

        self.score_lbl = Standared(
            "Score: {}".format(self.score)
        )
        h_container.add(self.score_lbl)

        pause_btn = MenuButton("Pause", self.game_pause)
        pause_btn.alignment = "right"
        pause_btn.set_left_padding(100)
        h_container.add(pause_btn)

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

        self.collision_dict = {
            "coins": self.coin_list,
            "platforms": self.platform_list
        }

    def game_pause(self):
        '''
        Pauses the game
        TODO: Loads an option list
        '''
        self.paused = not self.paused
        print(self.paused)

    def exit_game(self):
        '''
        Quits the game
        '''
        self.close()

    def update(self, dt):
        '''
        Updates all loaded enities and passes required data
        '''
        if self.paused or self.main_menu:
            return

        return_state = self.player.update(dt, self.collision_dict)

        if not return_state:
            return


if __name__ == "__main__":

    game = Game(800, 600)
    pyglet.clock.schedule_interval(game.update, 1/120.0)
    pyglet.app.run()
