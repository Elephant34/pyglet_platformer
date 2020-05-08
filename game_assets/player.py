'''
The player controled character
'''
from game_assets import resources
from game_assets.collision_object import CollisionObject


class Player(CollisionObject):
    '''
    Creates a user interactable player
    '''

    def __init__(self, x, y, **kwarg):
        '''
        Sets up the player
        '''
        self.img = resources.images["player"]

        super().__init__(self.img, **kwarg)

        self.x = x
        self.y = y