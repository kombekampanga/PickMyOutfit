import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random
from playsound import playsound

'''
This is a program that chooses my outfits for me
It has all the clothes in my wardrobe:
- Tops
- Bottoms
- Shoes
- Dresses
- Jackets

- Randomly choose an outfit for me based on approved combinations
    * Choose based on weather 
    * Choose based on occasion
    * Jacket optional
- Go through my tops and bottoms like from clueless so i can pick an outfit
    * Show items based on weather
'''
"""
What it needs - Brainstorming
-------------------------------
Frame with the title on the top 
a specific window size
a place to select pictures of my tops, bottoms, shoes dresses and jackets when I first set up the app (load my wardrobe)
    * Must save these pictures after I close the app
    * Can upload new pictures
        > upload all and only add the new ones - check the picture doesn't already exist before uploading
    * Should be able to create a new wardrobe if other people want to use it (feature can be added later)
a frame with my top
a frame with the bottoms
a frame with the shoes

if its a dress then take up the space of the top and the bottoms combined
a button for previous (for each clothing item separately) - beside each item's frame
a button for next (for each clothing item separately) - beside each item's frame

A button to generate "New outfit"
    * Will ask for the weather (drop box)
    * Will ask for the occasion (drop box)
 
 So each clothing item needs a weather setting and an occasion setting (can have multiple categories e.g casual and formal)
 this will be edited in the the window itself
 When you load a clothing item in it makes you say if its a top or bottom etc, what weather its for and what occasion
 

"""

#####################################   WINDOW/ROOT VARIABLES  ################################################

# Setting the window parameters for the Wardrobe application
WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 700

# frame (that displays the top and bottom takes up 30% of the page in the centre
# with 35% remaining either side of the frame
FRAME_WIDTH = WINDOW_WIDTH * 0.3
FRAME_HEIGHT = WINDOW_HEIGHT * 0.3
PERCENTAGE_EITHER_SIDE_OF_FRAME = 0.35


# Wardrobe class that contains the window for the clothes to be displayed
class WardrobeApp:
    def __init__(self, root):
        # make the wardrobe window/GUI
        self.root = root

        # Create the file path for the images
        self.file_path = ''

        # Create list of weather categories
        self.weather_categories = ['Show All', 'Hot', 'Warm', 'Cold and Windy', 'Cold and Rainy']
        # Create list of occasion categories
        self.occasion_categories = ['Show All', 'Work', 'House Party', 'Town', '21st', 'Everyday', 'Family']

        # Create lists containing images for different categories
        self.all_clothes = []
        self.all_tops = []
        self.all_bottoms = []
        # Master lists - these will be updated in the program (when weather and/or occasions are selected)
        # and used in the create_photo function to display the appropriate pictures
        self.master_tops_list = []
        self.master_bottoms_list = []
        # Initialise weather category lists
        self.weather_tops_list = []
        self.weather_bottoms_list = []

        self.hot_tops = []
        self.hot_bottoms = []

        self.warm_tops = []
        self.warm_bottoms = []

        self.windy_tops = []
        self.windy_bottoms = []

        self.rainy_tops = []
        self.rainy_bottoms = []

        # Initialise occasion category lists
        self.occasion_tops_list = []
        self.occasion_bottoms_list = []

        self.work_tops = []
        self.work_bottoms = []

        self.house_party_tops = []
        self.house_party_bottoms = []

        self.town_tops = []
        self.town_bottoms = []

        self.twenty_first_tops = []
        self.twenty_first_bottoms = []

        self.everyday_tops = []
        self.everyday_bottoms = []

        self.family_tops = []
        self.family_bottoms = []

        # create variables to hold which radio button is selected (to track which option is selected)
        # These variables hold the "label" text for each radio button, so its updated based on which one is clicked
        self.weather_selection = tk.StringVar()
        self.occasion_selection = tk.StringVar()

        # variable to hold image labels
        self.top_image_label = tk.Label()
        self.bottom_image_label = tk.Label()

        # Index numbers to keep track of which top/bottom item we are looking at
        # So when we click next and previous we can move through the items
        self.bottom_index = 0
        self.top_index = 0

        # Create the details for the window
        self.create_frame()
        self.create_buttons()
        # self.CreateLabels()
        self.create_menu_buttons()
        self.create_menubar()

        # Load clothes into the wardrobe

        # First check if another wardrobe was loaded last time (if Directory (DO NOT EDIT).txt exists)
        try:
            with open('Directory (DO NOT EDIT.txt', 'r') as f:
                # if it exists then get the file path from there
                self.file_path = f.read()
        # if it doesn't exist then get the user to pick a folder
        except FileNotFoundError:
            # Open file explore to get the user to choose the folder that contains the clothing
            self.file_path = filedialog.askdirectory()
            # Check if a file path was chosen
            try:
                self.all_clothes = os.listdir(self.file_path)
            # if no path was chosen
            except FileNotFoundError:
                # keep asking until a path is chosen
                while self.file_path == '':
                    self.file_path = filedialog.askdirectory()

            # When they select a folder then the while loop will stop
            # Then write a file called "Directory (DO NOT EDIT).txt", save the file path in it and save it to the
            # Working directory
            with open('Directory (DO NOT EDIT.txt', "w") as f:
                f.write(self.file_path)

        # Load a the wardrobe
        self.load_wardrobe()

        # Upload the initial top and the bottom picture into the frame (indices initially = 0)
        if self.file_path != '':
            self.create_photo(self.master_tops_list[self.top_index])
            self.create_photo(self.master_bottoms_list[self.bottom_index])

        # self.edit_categories.menu = tk.Canvas()
        # When you right click the image you are able to edit the categories
        self.top_image_label.bind("<Button-3>", self.right_clicked_image_top)
        self.bottom_image_label.bind("<Button-3>", self.right_clicked_image_bottom)

    def create_frame(self):
        # add title to window
        self.root.title(WINDOW_TITLE)
        # change the size of the window
        # self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.canvas = tk.Canvas(self.root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        self.canvas.pack()

        # create a frame for the tops
        self.frame_top = tk.Frame(self.root, bg='#80c1ff')
        self.frame_top.place(relx=PERCENTAGE_EITHER_SIDE_OF_FRAME, rely=0.1, width=FRAME_WIDTH, height=FRAME_HEIGHT)

        # create a frame for the bottoms
        self.frame_bottom = tk.Frame(self.root, bg='#80c1ff')
        self.frame_bottom.place(relx=PERCENTAGE_EITHER_SIDE_OF_FRAME, rely=0.5, width=FRAME_WIDTH, height=FRAME_HEIGHT)

    def create_buttons(self):
        # create a previous and next buttons for each item and add them to the root

        # buttons for tops
        self.button_prev_top = tk.Button(self.root, text="Prev", bg='pink', command=self.top_prev_photo)
        # Previous button should start off being disabled since the very first image is shown at the start
        self.button_prev_top.config(state='disabled')
        self.button_prev_top.place(relx=0.25, rely=0.25, relwidth=0.08, relheight=0.05)

        self.button_next_top = tk.Button(self.root, text="Next", bg='pink', command=self.top_next_photo)
        self.button_next_top.place(relx=0.67, rely=0.25, relwidth=0.08, relheight=0.05)

        # buttons for bottoms
        self.button_prev_bottom = tk.Button(self.root, text="Prev", bg="#BDA0CB", command=self.bottom_prev_photo)

        # Previous button should start off being disabled since the very first image is shown at the start
        self.button_prev_bottom.config(state='disabled')
        self.button_prev_bottom.place(relx=0.25, rely=0.65, relwidth=0.08, relheight=0.05)

        self.button_next_bottom = tk.Button(self.root, text="Next", bg='#BDA0CB', command=self.bottom_next_photo)
        self.button_next_bottom.place(relx=0.67, rely=0.65, relwidth=0.08, relheight=0.05)

        # Random outfit button
        self.button_random_outfit = tk.Button(self.root, text="Random Outfit", bg='light green',
                                              command=self.random_outfit)
        self.button_random_outfit.place(relx=0.05, rely=0.05)

    def create_labels(self):
        # Create label for the tops area
        self.label_top = tk.Label(self.frame_top, text="Tops", bg='white')
        self.label_top.place(relx=0.3, rely=0.02, relwidth=0.4, height=0.1)

        # Create label for the tops area
        self.label_bottom = tk.Label(self.frame_bottom, text="Bottoms", bg='white')
        self.label_bottom.place(relx=0.3, rely=0.02, relwidth=0.4, relheight=0.1)

    def create_menu_buttons(self):
        # Create a drop down menu to select the weather
        # Create a main weather menu button that displays weather options when clicked
        self.weather_menubutton = tk.Menubutton(self.root, text="Weather", bg='light blue')
        # Create a menu to list all the weather options (tear off = 0 removes a weird line at the top)
        # and attach it to the weather menu button
        self.weather_menu = tk.Menu(self.weather_menubutton, tearoff=0)
        # Add the weather options
        for category in self.weather_categories:
            self.weather_menu.add_radiobutton(label=category, variable=self.weather_selection,
                                              command=self.weather_selected)

        # add the menu feature to the menu button
        self.weather_menubutton.config(menu=self.weather_menu)
        # Place weather menu button on the root
        self.weather_menubutton.place(relx=0.05, rely=0.2)

        # Create an drop down menu to select the occasion
        # Create a main occasion menu button that displays weather options when clicked
        self.occasion_menubutton = tk.Menubutton(self.root, text="Occasion", bg='light yellow')
        # Create a menu to list all the occasion options (tear off = 0 removes a weird line at the top)
        # and attach it to the occasion menu button
        self.occasion_menu = tk.Menu(self.occasion_menubutton, tearoff=0)
        # Add the occasion options
        for category in self.occasion_categories:
            self.occasion_menu.add_radiobutton(label=category, variable=self.occasion_selection,
                                               command=self.occasion_selected)

        # add the menu feature to the menu button
        self.occasion_menubutton.config(menu=self.occasion_menu)
        # Place occasion menu button on the root
        self.occasion_menubutton.place(relx=0.05, rely=0.3)

    def create_menubar(self):
        # Create a menu bar that appears at the top right hand corner
        self.menubar = tk.Menu(self.root)
        # Create "file" menu that appears in the top right hand corner (in the menu bar)
        self.file = tk.Menu(self.menubar, tearoff=0)
        # Attach file to the menu bar
        self.menubar.add_cascade(label="File", menu=self.file)
        # Add the "Load Wardrobe" option
        self.file.add_command(label="Load Wardrobe", command=self.load_new_wardrobe)
        # Add the "Exit" option
        self.file.add_command(label="Exit", command=self.root.destroy)

        # Create "Edit" menu that appears next to "file"
        self.edit = tk.Menu(self.menubar, tearoff=0)
        # Attach edit to the menu bar
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        # Add the "Add New Top" option
        self.edit.add_command(label="Add New Top", command=None)
        # Add the "Add New Bottom" option
        self.edit.add_command(label="Add New Bottom", command=None)

        self.root.config(menu=self.menubar)

    # function to load the initial wardrobe into the program (change the file path)
    def load_wardrobe(self):
        """'
        # Open file explore to get the user to choose the folder that contains the clothing
        new_file_path = filedialog.askdirectory()

        # Get all the clothes from the folder - check if a file path was chosen
        try:
            self.all_clothes = os.listdir(new_file_path)
        # if no path was chosen
        except FileNotFoundError:
            # keep asking until a path is chosen
            error = FileNotFoundError
            # using this while loop because if the program is first starting then we want it to asking until a path
            # is chosen. But if they are loading a new wardrobe and they change their mind, they can still use the old
            # file path saved in self.file_path
            while new_file_path == '' and self.file_path == '':
                new_file_path = filedialog.askdirectory()
                if new_file_path != '':
                    self.file_path = new_file_path

            self.all_clothes = os.listdir(self.file_path)
        """
        # Get all the clothes from the folder
        self.all_clothes = os.listdir(self.file_path)
        # Get all the tops from the tops folder
        # Empty the tops list first
        self.all_tops = []
        for item in self.all_clothes:
            if 'top' in item:
                self.all_tops.append(item)

        # Get all the bottoms from the bottoms folder
        # Empty the bottoms list first
        self.all_bottoms = []
        for item in self.all_clothes:
            if 'bottom' in item:
                self.all_bottoms.append(item)

        # To begin with these will show all the tops and bottoms because no weather/occasion selection has been made
        self.master_tops_list = self.all_tops
        self.master_bottoms_list = self.all_bottoms

        # Empty the category lists
        self.hot_tops = []
        self.hot_bottoms = []

        self.warm_tops = []
        self.warm_bottoms = []

        self.windy_tops = []
        self.windy_bottoms = []

        self.rainy_tops = []
        self.rainy_bottoms = []

        self.occasion_tops_list = []
        self.occasion_bottoms_list = []

        self.work_tops = []
        self.work_bottoms = []

        self.house_party_tops = []
        self.house_party_bottoms = []

        self.town_tops = []
        self.town_bottoms = []

        self.twenty_first_tops = []
        self.twenty_first_bottoms = []

        self.everyday_tops = []
        self.everyday_bottoms = []

        self.family_tops = []
        self.family_bottoms = []

        # check the weather category listed in the top names and add it to the appropriate lists
        for image_title in self.all_tops:
            if 'hot' in image_title:
                self.hot_tops.append(image_title)
            if 'warm' in image_title:
                self.warm_tops.append(image_title)
            if 'windy' in image_title:
                self.windy_tops.append(image_title)
            if 'rainy' in image_title:
                self.rainy_tops.append(image_title)

        # check the weather category listed in the bottom names and add it to the appropriate lists
        for image_title in self.all_bottoms:
            if 'hot' in image_title:
                self.hot_bottoms.append(image_title)
            if 'warm' in image_title:
                self.warm_bottoms.append(image_title)
            if 'windy' in image_title:
                self.windy_bottoms.append(image_title)
            if 'rainy' in image_title:
                self.rainy_bottoms.append(image_title)

        # check the occasion category listed in the top names and add it to the appropriate lists
        for image_title in self.all_tops:
            if 'work' in image_title:
                self.work_tops.append(image_title)
            if 'house party' in image_title:
                self.house_party_tops.append(image_title)
            if 'town' in image_title:
                self.town_tops.append(image_title)
            if '21st' in image_title:
                self.twenty_first_tops.append(image_title)
            if 'everyday' in image_title:
                self.everyday_tops.append(image_title)
            if 'family' in image_title:
                self.family_tops.append(image_title)

        # check the occasion category listed in the bottom names and add it to the appropriate lists
        for image_title in self.all_bottoms:
            if 'work' in image_title:
                self.work_bottoms.append(image_title)
            if 'house party' in image_title:
                self.house_party_bottoms.append(image_title)
            if 'town' in image_title:
                self.town_bottoms.append(image_title)
            if '21st' in image_title:
                self.twenty_first_bottoms.append(image_title)
            if 'everyday' in image_title:
                self.everyday_bottoms.append(image_title)
            if 'family' in image_title:
                self.family_bottoms.append(image_title)

    def create_photo(self, image_name):
        # load the image in
        load = Image.open(self.file_path + "\\" + image_name)
        # Resize the image so it fits in the frame
        image_resized = load.resize((int(FRAME_WIDTH), int(FRAME_HEIGHT)), Image.ANTIALIAS)
        # Create the image so tkinter can read it
        photo = ImageTk.PhotoImage(image_resized)

        # check if the image is a top or bottom and put it in the appropriate frame
        # Place the image into a label so it can be displayed (tkinter rule)
        if "top" in image_name:
            self.top_image_label = tk.Label(self.frame_top, image=photo)
            # Save a reference so that tkinter doesnt doesn't send it to the garbage collector
            # when the function closes (so the widget can still hold onto the image
            self.top_image_label.image = photo
            # Place the image into the root
            self.top_image_label.place(x=0, y=0)
        else:
            self.bottom_image_label = tk.Label(self.frame_bottom, image=photo)
            # Save a reference so that tkinter doesnt doesn't send it to the garbage collector
            # when the function closes (so the widget can still hold onto the image)
            self.bottom_image_label.image = photo
            # Place the image into the root
            self.bottom_image_label.place(x=0, y=0)

    # function to go to the previous top
    def top_prev_photo(self):
        self.prev_photo('top')

    # function to go to the next top
    def top_next_photo(self):
        self.next_photo('top')

    # function to go to the previous bottoms
    def bottom_prev_photo(self):
        self.prev_photo('bottom')

    # function to go to the next bottoms
    def bottom_next_photo(self):
        self.next_photo('bottom')

    # function to get random outfit
    def random_outfit(self):

        # get a random index for the top and bottom
        self.top_index = random.randint(0, len(self.master_tops_list) - 1)
        self.bottom_index = random.randint(0, len(self.master_bottoms_list) - 1)

        # Place the random top and bottom images on the screen
        self.update_photo(self.master_tops_list[self.top_index])
        self.update_photo(self.master_bottoms_list[self.bottom_index])

        # If this is the first image then disable the prev button, otherwise make sure its normal
        if self.top_index == 0:
            self.button_prev_top.config(state='disabled')
        else:
            self.button_prev_top.config(state='normal')
        if self.bottom_index == 0:
            self.button_prev_bottom.config(state='disabled')
        else:
            self.button_prev_bottom.config(state='normal')

        # If this is the last image then disable the next button, otherwise make sure its normal
        if self.top_index == len(self.master_tops_list) - 1:
            self.button_next_top.config(state="disabled")
        else:
            self.button_next_top.config(state="normal")

        if self.bottom_index == len(self.master_bottoms_list) - 1:
            self.button_next_bottom.config(state='disabled')
        else:
            self.button_next_bottom.config(state="normal")

    # function to get the next photo
    def next_photo(self, item):

        # check if you're changing the top or bottom photo
        # and get the appropriate index and image list
        if item == 'top':
            index = self.top_index
            image_names = self.master_tops_list
        elif item == 'bottom':
            index = self.bottom_index
            image_names = self.master_bottoms_list

        # Make sure you aren't at the last photo
        if index < len(image_names):
            # Move on to the next image (increase index)
            index += 1
            # Make sure to increase the global variable for the index as well
            if item == 'top':
                self.top_index += 1
            elif item == 'bottom':
                self.bottom_index += 1
            # Put the next image in the frame
            self.update_photo(image_names[index])
            # If this is now the last image then disable the next button
            if index == len(image_names) - 1:
                if item == 'bottom':
                    self.button_next_bottom.config(state='disabled')
                elif item == 'top':
                    self.button_next_top.config(state='disabled')

            # If this is now the second image then stop disabling the previous button
            if index == 1:
                if item == 'bottom':
                    self.button_prev_bottom.config(state='normal')
                elif item == 'top':
                    self.button_prev_top.config(state='normal')

    # function to get the previous photo
    def prev_photo(self, item):
        # check if you're changing the top or bottom photo
        # and get the appropriate index and image list
        if item == 'top':
            index = self.top_index
            image_names = self.master_tops_list
        elif item == 'bottom':
            index = self.bottom_index
            image_names = self.master_bottoms_list

        # Make sure you aren't at the first photo
        if index != 0:
            # Go back to the previous image (decrease index)
            index -= 1
            # Make sure to decrease the global variable for the index as well
            if item == 'top':
                self.top_index -= 1
            elif item == 'bottom':
                self.bottom_index -= 1
            # Put the previous image in the frame
            self.update_photo(image_names[index])
            # If this is now the first image then disable the previous button
            if index == 0:
                if item == 'bottom':
                    self.button_prev_bottom.config(state='disabled')
                elif item == 'top':
                    self.button_prev_top.config(state='disabled')

            # If this no longer last image then stop disabling the next button
            if index == len(image_names) - 2:
                if item == 'bottom':
                    self.button_next_bottom.config(state='normal')
                elif item == 'top':
                    self.button_next_top.config(state='normal')

    # function to update the photo when a button is pressed
    def update_photo(self, image_name):
        # load the image in
        load = Image.open(self.file_path + "\\" + image_name)
        # Resize the image so it fits in the frame
        image_resized = load.resize((int(FRAME_WIDTH), int(FRAME_HEIGHT)), Image.ANTIALIAS)
        # Create the image so tkinter can read it
        photo = ImageTk.PhotoImage(image_resized)

        # check if the image is a top or bottom and put it in the appropriate frame
        # Place the image into a label so it can be displayed (tkinter rule)
        if "top" in image_name:
            self.top_image_label.config(image=photo)
            self.top_image_label.image = photo
        elif "bottom" in image_name:
            self.bottom_image_label.config(image=photo)
            self.bottom_image_label.image = photo

    # function when weather filter is selected
    def weather_selected(self):
        self.filter('weather')

    # function when occasion filter is selected
    def occasion_selected(self):
        self.filter('occasion')

    # function to apply filter based on weather and/or occasion selection
    def filter(self, selection):
        # If the selection made was to filter the weather then get the appropriate list based on what weather
        # type was selected
        if selection == 'weather':
            if self.weather_selection.get() == 'Show All':
                self.weather_tops_list = self.all_tops
                self.weather_bottoms_list = self.all_bottoms
            elif self.weather_selection.get() == 'Hot':
                self.weather_tops_list = self.hot_tops
                self.weather_bottoms_list = self.hot_bottoms
            elif self.weather_selection.get() == 'Warm':
                self.weather_tops_list = self.warm_tops
                self.weather_bottoms_list = self.warm_bottoms
            elif self.weather_selection.get() == 'Cold and Windy':
                self.weather_tops_list = self.windy_tops
                self.weather_bottoms_list = self.windy_bottoms
            elif self.weather_selection.get() == 'Cold and Rainy':
                self.weather_tops_list = self.rainy_tops
                self.weather_bottoms_list = self.rainy_bottoms

        # If the selection made was to filter the occasion then get the appropriate list based on what occasion
        # type was selected
        if selection == 'occasion':
            if self.occasion_selection.get() == 'Show All':
                self.occasion_tops_list = self.all_tops
                self.occasion_bottoms_list = self.all_bottoms
            elif self.occasion_selection.get() == 'Work':
                self.occasion_tops_list = self.work_tops
                self.occasion_bottoms_list = self.work_bottoms
            elif self.occasion_selection.get() == 'House Party':
                self.occasion_tops_list = self.house_party_tops
                self.occasion_bottoms_list = self.house_party_bottoms
            elif self.occasion_selection.get() == 'Town':
                self.occasion_tops_list = self.town_tops
                self.occasion_bottoms_list = self.town_bottoms
            elif self.occasion_selection.get() == '21st':
                self.occasion_tops_list = self.twenty_first_tops
                self.occasion_bottoms_list = self.twenty_first_bottoms
            elif self.occasion_selection.get() == 'Everyday':
                self.occasion_tops_list = self.everyday_tops
                self.occasion_bottoms_list = self.everyday_bottoms
            elif self.occasion_selection.get() == 'Family':
                self.occasion_tops_list = self.family_tops
                self.occasion_bottoms_list = self.family_bottoms

        # If both a weather and a occasion are selected
        # Check if specific weather and occasion filters are applied (not just show all)
        # Also have to check if a selection has been made because at the start self.weather_selection and
        # self.occasion_selection are empty
        if (self.weather_selection.get() != 'Show All') and (self.occasion_selection.get() != 'Show All') and \
                (self.weather_selection.get() != '') and (self.occasion_selection.get() != ''):
            # Empty the master_tops_list and fill it only with tops common to both the weather category
            # and the occasion category selected
            self.master_tops_list = []
            for top in self.occasion_tops_list:
                if top in self.weather_tops_list:
                    self.master_tops_list.append(top)

            self.master_bottoms_list = []
            for bottom in self.occasion_bottoms_list:
                if bottom in self.weather_bottoms_list:
                    self.master_bottoms_list.append(bottom)

        # Else if only an occasion is selected then update the master list to be clothes for that occasion
        elif ((self.occasion_selection.get() != 'Show All') and (self.occasion_selection.get() != '')) and \
                ((self.weather_selection.get() == 'Show All') or (self.weather_selection.get() == '')):
            # Update master list
            self.master_tops_list = self.occasion_tops_list
            self.master_bottoms_list = self.occasion_bottoms_list

        # Else if only a weather type is selected then update the master list to be clothes for that weather
        elif ((self.weather_selection.get() != 'Show All') and (self.weather_selection.get() != '')) and \
                ((self.occasion_selection.get() == 'Show All') or (self.occasion_selection.get() == '')):
            # Update master list
            self.master_tops_list = self.weather_tops_list
            self.master_bottoms_list = self.weather_bottoms_list

        # Else if both weather and occasion are show all then master_lists = all_tops and all_bottoms
        elif ((self.weather_selection.get() == 'Show All') or (self.weather_selection.get() == '')) and \
                ((self.occasion_selection.get() == 'Show All') or (self.occasion_selection.get() == '')):
            # Update master list
            self.master_tops_list = self.all_tops
            self.master_bottoms_list = self.all_bottoms

        # Update indices to start from the beginning
        self.top_index = 0
        self.bottom_index = 0

        # check the tops list is empty, and if it is then show an empty white frame saying "No tops"
        # Otherwise run create_photo to add the first photo to the frame
        if len(self.master_tops_list) == 0:
            self.image_label = tk.Label(self.frame_top, text="No tops", bg="white", width=int(FRAME_WIDTH),
                                        height=int(FRAME_HEIGHT))
            # self.top_image_label.place_forget()
        else:
            self.update_photo(self.master_tops_list[self.top_index])

        # check the bottoms list is empty, and if it is then show an empty white frame saying "No tops"
        # otherwise run create_photo to add the first photo to the frame
        if len(self.master_bottoms_list) == 0:
            self.image_label = tk.Label(self.frame_bottom, text="No Bottoms", bg='white', width=int(FRAME_WIDTH),
                                        height=int(FRAME_HEIGHT))
            # self.bottom_image_label.place_forget()
        else:
            self.update_photo(self.master_bottoms_list[self.bottom_index])

        # Make the previous buttons disabled as we are at the first image of the filtered images
        self.button_prev_top.config(state='disabled')
        self.button_prev_bottom.config(state='disabled')

        # Enable the next button just in case it was disabled before (e.g we reached the end of the photos
        # and THEN we changed the filter
        self.button_next_top.config(state='normal')
        self.button_next_bottom.config(state='normal')

        # If there is only 1 image (or no images) when clothes are filtered then disable the next button as well
        if len(self.master_tops_list) <= 1:
            self.button_next_top.config(state='disabled')
        if len(self.master_bottoms_list) <= 1:
            self.button_next_bottom.config(state='disabled')

    # function to load a new wardrobe into the program (change the file path)
    def load_new_wardrobe(self):

        # Get the new folder that contains the clothes
        try:
            self.file_path = filedialog.askdirectory()
            # Save the new wardrobe in the "Directory (DO NOT EDIT).txt" file
            with open('Directory (DO NOT EDIT.txt', "w") as f:
                f.write(self.file_path)
        # if the user doesn't choose a folder let it pass (they can still use the old one currently loaded)
        except FileNotFoundError:
            pass
        # Use the load_wardrobe function to get the new file path and new images
        self.load_wardrobe()

        # Start the image indices at 0 (so it starts with the first image)
        self.top_index = 0
        self.bottom_index = 0

        # update the frames with the new photos
        self.update_photo(self.master_tops_list[self.top_index])
        self.update_photo(self.master_bottoms_list[self.bottom_index])

        # Make the previous buttons disabled as we are at the first image of the filtered images
        self.button_prev_top.config(state='disabled')
        self.button_prev_bottom.config(state='disabled')

        # Enable the next button just in case it was disabled before (e.g we reached the end of the photos
        # and THEN we changed the filter
        self.button_next_top.config(state='normal')
        self.button_next_bottom.config(state='normal')

        # If there is only 1 image (or no images) when clothes are filtered then disable the next button as well
        if len(self.master_tops_list) <= 1:
            self.button_next_top.config(state='disabled')
        if len(self.master_bottoms_list) <= 1:
            self.button_next_bottom.config(state='disabled')

    # function called when user right clicks a tops image
    def right_clicked_image_top(self, event):
        # Set image_type to be a top so we know we are editing tops
        self.image_type = 'bottom'

        print("right click top!")
        # Call the edit image function and tell it that you are editing a top item
        # Make sure it doesn't keep creating menus when you right click
        # If the menu already exists, then forget it an make a new one
        try:
            print("working")
            self.edit_categories.place_forget()
            self.edit_image_options()
        except Exception:
            self.edit_image_options()

    # function called when user right clicks a bottoms image
    def right_clicked_image_bottom(self, event):
        # Set image_type to be a bottom so we know we are editing bottoms
        self.image_type = 'bottom'

        print("right click bottom!")
        # Call the edit image function and tell it that you are editing a bottom item
        # Make sure it doesn't keep creating menus when you right click
        # If the menu already exists, then forget it an make a new one
        try:
            print("working")
            self.edit_categories.place_forget()
            self.edit_image_options()
        except Exception:
            self.edit_image_options()

    # Function that creates the menu to edit image categories when you right click an image (called by right_clicked..)
    def edit_image_options(self):
        # Get the x and y coordinated of the cursor
        cursor_x = int(self.root.winfo_pointerx() - self.root.winfo_rootx())
        cursor_y = int(self.root.winfo_pointery() - self.root.winfo_rooty())

        # Create "edit_categories" menu that appears when you right click
        self.edit_categories = tk.Canvas(self.root, width=150, height=50, highlightbackground="gray",
                                         highlightthickness=1)
        self.edit_categories.place(x=cursor_x, y=cursor_y)

        self.edit_image_selection = tk.StringVar()

        self.R1 = tk.Radiobutton(self.edit_categories, text="Edit Weather Filters", variable=self.edit_image_selection,
                                 value='weather', indicator=0, command=self.category_editor)
        self.R1.pack(anchor="w", fill='x')

        self.R2 = tk.Radiobutton(self.edit_categories, text="Edit Occasion Filters", variable=self.edit_image_selection,
                                 value='occasion', indicator=0, command=self.category_editor)
        self.R2.pack(anchor="w", fill='x')

    # Function that
    def category_editor(self):
        # Close the menu
        self.edit_categories.place_forget()

        # if a top was selected then set all the widget variables to display top things

        # if it is weather set all the widget variables to display weather things

        # Open a new canvas that shows all the categories and asks which one you want to add
        self.editor = tk.Toplevel()
        # add title to window
        self.editor.title("Edit Weather Categories")
        # change the size of the window
        self.editor_canvas = tk.Canvas(self.editor, height=400, width=600)
        self.editor_canvas.pack()

        # Show the image of the selected top
        # Set the frame
        self.frame_top_edit = tk.Frame(self.editor, bg='#80c1ff')
        self.frame_top_edit.place(relx=0.1, rely=0.1, width=FRAME_WIDTH, height=FRAME_HEIGHT)

        # Put the top image inside the frame (remember the image photo is saved in the original top_image_label.image
        self.image_label = tk.Label(self.frame_top_edit, image=self.top_image_label.image)
        # Save a reference so that tkinter doesnt doesn't send it to the garbage collector
        # when the function closes (so the widget can still hold onto the image)
        self.image_label.image = self.top_image_label.image
        self.image_label.place(x=0, y=0)

        # Show the Edit Weather Categories window
        self.editor.mainloop()
        print(self.edit_image_selection.get())



'''
Things for the future:
Fix what happens if there are no options for the weather and occasion combination

Be able to add an item to the wardrobe from within the app (go file, add item):
    when you add the item you can choose:
    1. if its a top or bottom
    2. select which weather categories it falls under
    3. select which occasion categories it falls under
    Then it is automatically added to the appropriate folder and named based on if its a top or bottom + 
    the length of the all tops list +1 (since you're adding a new item) + weather categories + occasion categories

Be able to change the file path where the images are stored
- DONE Go to file, change directory and it will make you choose where "All Tops" and "All Bottoms" are located

Be able to edit the categories within the app
- view the categories an item falls under and add/remove a category accordingly
    - this would be done by right clicking and going to an edit categories option to display the current categories
    - can either "add new" or "remove"
    - DONE add: then the title of the image gets edited to have the new category appended to it (title + ", " + category)
    - DONE remove: then the title of the image gets edited to remove the category
    
DONE When you first start the program it will ask you to choose the filepath. 
DONE Then it will remember it for next time.
DONE When you want a new file path you go to file - Load Wardrobe
            
'''
root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
