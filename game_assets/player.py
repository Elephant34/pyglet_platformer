'''
The player controled character
'''
import math

import pyglet

from game_assets import resources


class Player(pyglet.sprite.Sprite):
    '''
    Creates a user interactable player
    '''

    def __init__(self, x, y, **kwargs):
        '''
        Sets up the player
        '''
        self.img = resources.images["player"]

        super().__init__(self.img, **kwargs)

        self.x = x
        self.y = y

        self.gravity = 300
        self.walk_speed = 500
        self.jump_speed = 600

        self.movement = {
            "left": False,
            "right": False,
            "jump": False,
        }

    def update(self, dt, collisions):
        '''
        Moves the player by player inputs
        '''

        collides = []
        in_air = True

        if not in_air:
            self.y -= self.gravity * dt

    def key_press(self, key):
        '''
        Handels relevant key inputs from the main window
        '''
        if key == "space":
            self.movement["jump"] = True
        elif key == "left":
            self.movement["left"] = True
        elif key == "right":
            self.movement["right"] = True

    def key_release(self, key):
        '''
        Handles the release of keys
        '''
        if key == "left":
            self.movement["left"] = False
        elif key == "right":
            self.movement["right"] = False
        elif key == "jump":
            self.movement["jump"] = False
