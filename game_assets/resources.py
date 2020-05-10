'''
Loads all the images resources and centers them
'''
import pyglet


# Tell pyglet where to find the resources
pyglet.resource.path = ['static_assets', 'static_assets/images']
pyglet.resource.reindex()

images = {
    "player": pyglet.resource.image("player.png"),
    "coin": pyglet.resource.image("coin.png"),
    "platform": pyglet.resource.image("platform.png"),
}
