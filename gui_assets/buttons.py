'''
Sets up the button themes
'''
import glooey
from gui_assets.labels import Standared

class MenuButton(glooey.Button):
    Foreground = Standared
    custom_alignment = "center"

    # Note in final these will be images
    class Base(glooey.Background):
        custom_color = '#000000'

    class Over(glooey.Background):
        custom_color = '#000000'

    class Down(glooey.Background):
        custom_color = '#000000'

    def __init__(self, text, function):
        super().__init__(text)
        self.function = function

    def on_click(self, widget):
        self.function()