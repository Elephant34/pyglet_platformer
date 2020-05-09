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
        self.speed = 500
        self.jump = 100

    def update(self, dt, collisions):
        '''
        Moves the player by player inputs
        '''

        collides = []
        hit_platform = False

        for obj_type, collision_list in collisions.items():
            for collision_object in collision_list:
                if self.collides_with(collision_object):
                    collides.append([obj_type, collision_object])

        for collision in collides:
            if collision[0] == "platforms":
                hit_platform = True

        if not hit_platform:
            self.y -= self.gravity * dt

    def collides_with(self, other_object):
        """
        Determine if this object collides with another
        """

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        collision_distance = self.image.width * 0.5 * self.scale \
            + other_object.image.width * 0.5 * other_object.scale

        # Get distance using position tuples
        actual_distance = self.distance(self.position, other_object.position)

        # Arbitaroy 0.17049 fixes alignment issue
        # I have no idea what causes it
        return (actual_distance+0.17049 <= collision_distance)

    def distance(self, point_1=(0, 0), point_2=(0, 0)):
        """
        Returns the distance between two points
        """
        return math.sqrt(
            (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2
        )
