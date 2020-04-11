import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500

class WardrobeApp:
    def __init__(self, window):
        self.window = window

        # create background
        self.create_background()

    def create_background(self):

        # add title to window and change the size
        self.window.title(WINDOW_TITLE)
        self.window.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

window = tk.Tk()
app = WardrobeApp(window)
window.mainloop()


