'''
Loads all the images resources and centers them
'''
import pyglet


def center_image(image):
    """
    Sets image anchor point to its middle
    """
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['static_assets', 'static_assets/images']
pyglet.resource.reindex()

images = {
    "player": pyglet.resource.image("player.png"),
    "coin": pyglet.resource.image("coin.png"),
    "platform": pyglet.resource.image("platform.png"),
}
for image in images.values():
    center_image(image)
