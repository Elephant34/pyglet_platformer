'''
A base class for all objects where collsion will be reigisted
'''
import pyglet

class CollisionObject(pyglet.sprite.Sprite):
    '''
    A sprite with collision detection
    '''

    def __init__(self, img, **kwarg):
        '''
        Sets up a sprite which can handel collions
        '''
        super().__init__(img=img, **kwarg)