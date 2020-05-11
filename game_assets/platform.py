'''
A simple static platform for the player to wal accross
'''
import pyglet
from game_assets import resources


class Platform(pyglet.sprite.Sprite):
    '''
    A platform which the player can stand on
    '''

    def __init__(self, x, y, scale_x, **kwargs):
        '''
        Sets up the platform
        '''

        self.img = resources.images["platform"]

        super().__init__(img=self.img, **kwargs)

        self.x = x
        self.y = y
        self.scale_x = scale_x

        self.sides = {
            "top": self.position[1] + self.image.height,
            "bottom": self.position[1],
            "left": self.position[0],
            "right": self.position[0] + (self.image.width*self.scale_x)
        }
