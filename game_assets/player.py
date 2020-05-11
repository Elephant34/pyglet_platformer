'''
The player controled character
'''
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

    def update(self, dt, collision_objects):
        '''
        Moves the player by player inputs
        '''

        self.sides = {
            "top": self.position[1] + self.image.height,
            "bottom": self.position[1],
            "left": self.position[0],
            "right": self.position[0] + self.image.width
        }

        for obj in collision_objects["platforms"]:
            for collision in self.get_collision_sides(obj):
                print(collision)

        self.y -= 1

        return

    def key_press(self, key):
        '''
        Handels relevant key inputs from the main window
        '''
        if key == "jump":
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

    def get_collision_sides(self, obj):
        '''
        Returns a dictionary of player surfaces in contact with object
        '''

        # Tests if the bototm is inline with obj
        if (self.sides["bottom"] <= obj.sides["top"]
           and self.sides["bottom"] > obj.sides["bottom"]):

            # Ensures player isn't to left or right
            if not (self.sides["left"] > obj.sides["right"]
                    or self.sides["right"] < obj.sides["left"]):

                yield "bottom"

        # Tests if the top is inline with obj
        if (self.sides["top"] >= obj.sides["bottom"]
           and self.sides["top"] < obj.sides["top"]):

            # Ensures player isn't to left or right
            if not (self.sides["left"] > obj.sides["right"]
                    or self.sides["right"] < obj.sides["left"]):

                yield "top"

        # Tests if right side is inline with obj
        if (self.sides["right"] > obj.sides["left"]
           and self.sides["right"] < obj.sides["right"]):

            # Tests if the object is above or below
            if not (self.sides["top"] <= obj.sides["bottom"]
                    or self.sides["bottom"] >= obj.sides["top"]):

                yield "right"

        # Tests if left side is inline with obj
        if (self.sides["left"] < obj.sides["right"]
           and self.sides["left"] > obj.sides["left"]):

            # Tests if the object is above or below
            if not (self.sides["top"] <= obj.sides["bottom"]
                    or self.sides["bottom"] >= obj.sides["top"]):

                yield "left"
