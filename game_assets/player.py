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

        self.top_right = (
            self.position[0]+self.image.width,
            self.position[1]+self.image.height
        )
        self.bottom_left = self.position

        move_left = self.walk_speed if self.movement["left"] else 0
        move_right = self.walk_speed if self.movement["right"] else 0
        move_down = self.gravity
        move_up = self.jump_speed if self.movement["jump"] else 0

        # Tests if the player has hit any of the platforms and from where
        for obj in collision_objects["platforms"]:
            collision = self.get_collisions(obj)

            print(collision)

            if collision["left"]:
                move_left = 0
            if collision["right"]:
                move_right = 0
            if (collision["bottom"]
               and not (collision["left"] or collision["right"])):
                move_down = 0
            if collision["top"]:
                move_up = 0

        self.x += (move_right - move_left) * dt
        self.y += (move_up - move_down) * dt

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

    def get_collisions(self, obj):
        '''
        Tests is the player and object have collided
        '''

        obj_top_right = (
            obj.position[0]+obj.image.width,
            obj.position[1]+obj.image.height
        )
        obj_bottom_left = obj.position

        # Presumes collisions on all sides of player
        collision = {
            "right": False,
            "left": False,
            "top": False,
            "bottom": False
        }

        if (self.bottom_left[1] <= obj_top_right[1]
           and self.top_right[1] > obj_top_right[1]):

            collision["bottom"] = True

        elif (self.top_right[1] <= obj_bottom_left[1]
              and self.bottom_left[1] > obj_bottom_left[1]):

            collision["top"] = True

        elif (self.bottom_left[0] <= obj_top_right[0]
              and self.top_right[0] > obj_top_right[0]):

            collision["right"] = True

        elif (self.top_right[0] <= obj_bottom_left[0]
              and self.bottom_left[0] > obj_bottom_left[0]):

            collision["left"] = True

        return collision
