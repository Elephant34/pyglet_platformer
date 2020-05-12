'''
A coin which gives points when touches the user
When all coins are collected the next level loads
'''
import pyglet
from game_assets import resources


class Coin(pyglet.sprite.Sprite):
    '''
    A coin which gives the player points
    '''

    def __init__(self, x, y, **kwargs):
        '''
        Sets up the coin
        '''

        self.img = resources.images["coin"]

        super().__init__(img=self.img, **kwargs)

        self.x = x
        self.y = y

        self.sides = {
            "top": self.position[1] + self.image.height,
            "bottom": self.position[1],
            "left": self.position[0],
            "right": self.position[0] + (self.image.width*self.scale_x)
        }
