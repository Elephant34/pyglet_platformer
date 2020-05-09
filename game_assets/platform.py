'''
A simple static platform for the player to wal accross
'''
import pyglet
from game_assets import resources


class Platform(pyglet.sprite.Sprite):
    '''
    A platform which the player can stand on
    '''

    def __init__(self, x, y, **kwargs):
        '''
        Sets up the platform
        '''

        self.img = resources.images["platform"]

        super().__init__(img=self.img, **kwargs)

        self.x = x
        self.y = y
