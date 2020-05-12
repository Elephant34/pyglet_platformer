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
        self.jump_speed = 700

        self.on_bottom = False
        self.jump_timer = 0

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

        move = {
            "up": self.jump_speed if self.movement["jump"] else 0,
            "down": self.gravity,
            "left": self.walk_speed if self.movement["left"] else 0,
            "right": self.walk_speed if self.movement["right"] else 0,
        }

        if self.jump_timer > 0.3:
            move["up"] = 0

        for obj in collision_objects["platforms"]:
            collisions = [
                collision for collision in self.get_collision_sides(obj)
            ]

            if "bottom" in collisions:
                move["down"] = 0
                self.y = obj.sides["top"]
                self.on_bottom = True
            if "top" in collisions:
                move["up"] = 0
                self.y = obj.sides["bottom"] - self.image.height
                self.jump_timer = 10
            if "left" in collisions:
                move["right"] = 0
                self.x = obj.sides["left"] - self.image.width
            if "right" in collisions:
                move["left"] = 0
                self.x = obj.sides["right"]

        y_speed = move["up"] - move["down"]
        x_speed = move["right"] - move["left"]

        if y_speed != 0:
            self.on_bottom = False

        self.y += y_speed * dt
        self.x += x_speed * dt

        self.jump_timer += dt

        return

    def key_press(self, key):
        '''
        Handels relevant key inputs from the main window
        '''
        if key == "jump" and self.on_bottom:
            self.movement["jump"] = True
            self.jump_timer = 0
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
        if (self.sides["right"] >= obj.sides["left"]
           and self.sides["right"] < obj.sides["left"]+20):

            # Tests if the object is above or below
            if not (self.sides["top"] <= obj.sides["bottom"]
                    or self.sides["bottom"] >= obj.sides["top"]):

                yield "left"

        # Tests if left side is inline with obj
        if (self.sides["left"] <= obj.sides["right"]
           and self.sides["left"] > obj.sides["right"]-20):

            # Tests if the object is above or below
            if not (self.sides["top"] <= obj.sides["bottom"]
                    or self.sides["bottom"] >= obj.sides["top"]):

                yield "right"
