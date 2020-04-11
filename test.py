import os
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500

# store all the Tops into a file we can access and skip hidden files
ALL_TOPS = [str('tops/') + imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]


class WardrobeApp:
    def __init__(self, root):
        self.root = root

        # Show top image in the window
        self.top_images = ALL_TOPS

        # save single top
        self.top_images_path = self.top_images[0]

        # create and add top image into Frame
        self.tops_frame = tk.Frame(self.root)

        # create background
        self.create_background()

    def create_background(self):
        # add title to window and change the size
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

    def create_photo(self, imag):


root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
