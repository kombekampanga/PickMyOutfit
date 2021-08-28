import os
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random
'''from playsound import playsound'''

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


# WardrobeApp class that contains the window for the clothes to be displayed with all the buttons
class WardrobeApp:
    # Wardrobe class that contains the clothes and categories
    class MyWardrobe:
        def __init__(self):

            # Create list of weather categories
            self.weather_categories = [
                'Show All', 'Hot', 'Warm', 'Cold and Windy', 'Cold and Rainy']
            # Create list of occasion categories
            self.occasion_categories = [
                'Show All', 'Work', 'House Party', 'Town', '21st', 'Everyday', 'Family']

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

        # function to load the initial wardrobe into the program (change the file path)
        def load_wardrobe(self, file_path):
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
            self.all_clothes = os.listdir(file_path)
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

    def __init__(self, root):
        # Create a variable to store whether its a top or bottom
        self.image_type = tk.StringVar()

        # make the wardrobe window/GUI
        self.root = root

        # create a canvas to specify the size of the window
        self.canvas = tk.Canvas(
            self.root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

        # Create a frame to display the tops
        self.frame_top = tk.Frame(self.root, bg='#80c1ff')

        # create a frame to display bottoms
        self.frame_bottom = tk.Frame(self.root, bg='#80c1ff')

        # Create the file path for the images
        self.file_path = ''

        # buttons to cycle through tops (previous and next)
        self.button_prev_top = tk.Button(
            self.root, text="Prev", bg='pink', command=self.top_prev_photo)
        self.button_next_top = tk.Button(
            self.root, text="Next", bg='pink', command=self.top_next_photo)

        # buttons to cycle through bottoms (previous and next)
        self.button_prev_bottom = tk.Button(
            self.root, text="Prev", bg="#BDA0CB", command=self.bottom_prev_photo)
        self.button_next_bottom = tk.Button(
            self.root, text="Next", bg='#BDA0CB', command=self.bottom_next_photo)

        # Random outfit button
        self.button_random_outfit = tk.Button(self.root, text="Random Outfit", bg='light green',
                                              command=self.random_outfit)

        # Create label for the tops area
        self.label_top = tk.Label(self.frame_top, text="Tops", bg='white')

        # Create label for the bottoms area
        self.label_bottom = tk.Label(
            self.frame_bottom, text="Bottoms", bg='white')

        # Create a drop down menu to select the weather:
        # ------------------------------------------------------------------
        # Create a main weather menu button that displays weather options when clicked
        self.weather_menubutton = tk.Menubutton(
            self.root, text="Weather", bg='light blue')
        # Create a menu to list all the weather options (tear off = 0 removes a weird line at the top)
        # and attach it to the weather menu button
        self.weather_menu = tk.Menu(self.weather_menubutton, tearoff=0)

        # Create an drop down menu to select the occasion:
        # -------------------------------------------------------------------
        # Create a main occasion menu button that displays weather options when clicked
        self.occasion_menubutton = tk.Menubutton(
            self.root, text="Occasion", bg='light yellow')
        # Create a menu to list all the occasion options (tear off = 0 removes a weird line at the top)
        # and attach it to the occasion menu button
        self.occasion_menu = tk.Menu(self.occasion_menubutton, tearoff=0)

        # Create menu bar:
        # --------------------------------------------------------------------
        # Create a menu bar that appears at the top right hand corner
        self.menubar = tk.Menu(self.root)
        # Create "file" menu that appears in the top right hand corner (in the menu bar)
        self.file = tk.Menu(self.menubar, tearoff=0)
        # Create "Edit" menu that appears next to "file"
        self.edit = tk.Menu(self.menubar, tearoff=0)

        # create variables to hold which radio button is selected (to track which option is selected)
        # These variables hold the "label" text for each radio button, so its updated based on which one is clicked
        self.weather_selection = tk.StringVar()
        self.occasion_selection = tk.StringVar()

        # variable to hold image labels
        self.top_image_label = tk.Label()
        self.bottom_image_label = tk.Label()

        # Editing an images categories
        # ------------------------------------------------------------------------------------------
        # Create "edit_categories" menu that appears when you right click
        self.edit_categories = tk.Canvas(self.root, width=150, height=50, highlightbackground="gray",
                                         highlightthickness=1)
        # Create variables to hold which edit function is selected (edit weather or edit category)
        self.edit_image_selection = tk.StringVar()

        # Create Radio buttons that open the category editor
        self.R1 = tk.Radiobutton(self.edit_categories, text="Edit Weather Filters", variable=self.edit_image_selection,
                                 value='weather', indicator=0, command=self.category_editor)

        self.R2 = tk.Radiobutton(self.edit_categories, text="Edit Occasion Filters", variable=self.edit_image_selection,
                                 value='occasion', indicator=0, command=self.category_editor)

        # Index numbers to keep track of which top/bottom item we are looking at
        # So when we click next and previous we can move through the items
        self.bottom_index = 0
        self.top_index = 0

        # Load clothes into the wardrobe

        # First check if another wardrobe was loaded last time (if Directory (DO NOT EDIT).txt exists)
        try:
            with open('Directory (DO NOT EDIT).txt', 'r') as f:
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
            with open('Directory (DO NOT EDIT).txt', "w") as f:
                f.write(self.file_path)

        # Create a wardrobe full of clothes
        self.mywardrobe = WardrobeApp.MyWardrobe()

        # Load the wardrobe
        self.mywardrobe.load_wardrobe(self.file_path)

        # Upload the initial top and the bottom picture into the frame (indices initially = 0)
        if self.file_path != '':
            self.create_photo(self.mywardrobe.master_tops_list[self.top_index])
            self.create_photo(
                self.mywardrobe.master_bottoms_list[self.bottom_index])

        # Create the details for the window
        self.create_frame()
        self.create_buttons()
        # self.CreateLabels()
        self.create_menu_buttons()
        self.create_menubar()

        # self.edit_categories.menu = tk.Canvas()
        # When you right click the image you are able to edit the categories
        self.top_image_label.bind("<Button-3>", self.right_clicked_image_top)
        self.bottom_image_label.bind(
            "<Button-3>", self.right_clicked_image_bottom)
        # when you left click out of the image then get off the edit categories option
        self.canvas.bind("<Button-1>", self.left_clicked)
        self.canvas.bind("<Button-1>", self.left_clicked)

    # Function to create the frames that display the tops and the bottoms
    def create_frame(self):
        # add title to window
        self.root.title(WINDOW_TITLE)

        # Put the canvas onto the frame
        self.canvas.pack()

        # Place the frame for the tops
        self.frame_top.place(relx=PERCENTAGE_EITHER_SIDE_OF_FRAME,
                             rely=0.1, width=FRAME_WIDTH, height=FRAME_HEIGHT)

        # Place the frame for the bottoms
        self.frame_bottom.place(relx=PERCENTAGE_EITHER_SIDE_OF_FRAME,
                                rely=0.5, width=FRAME_WIDTH, height=FRAME_HEIGHT)

    # Function to create a previous and next buttons for each item and add them to the root
    def create_buttons(self):

        # Place the previous and next buttons for the tops in the frame to cycle through tops
        # Previous button should start off being disabled since the very first image is shown at the start
        self.button_prev_top.config(state='disabled')
        self.button_prev_top.place(
            relx=0.25, rely=0.25, relwidth=0.08, relheight=0.05)

        self.button_next_top.place(
            relx=0.67, rely=0.25, relwidth=0.08, relheight=0.05)

        # Place the previous and next buttons for the bottoms in the frame to cycle through bottoms
        # Previous button should start off being disabled since the very first image is shown at the start
        self.button_prev_bottom.config(state='disabled')
        self.button_prev_bottom.place(
            relx=0.25, rely=0.65, relwidth=0.08, relheight=0.05)

        self.button_next_bottom.place(
            relx=0.67, rely=0.65, relwidth=0.08, relheight=0.05)

        # Place the random outfit button in the frame
        self.button_random_outfit.place(relx=0.05, rely=0.05)

    def create_labels(self):
        # Place label for tops area
        self.label_top.place(relx=0.3, rely=0.02, relwidth=0.4, height=0.1)

        # Place label for bottoms area
        self.label_bottom.place(relx=0.3, rely=0.02,
                                relwidth=0.4, relheight=0.1)

    def create_menu_buttons(self):

        # Add the weather options to the weather drop-down menu
        print(self.mywardrobe)
        for category in self.mywardrobe.weather_categories:
            self.weather_menu.add_radiobutton(label=category, variable=self.weather_selection,
                                              command=self.weather_selected)

        # add the menu feature to the menu button
        self.weather_menubutton.config(menu=self.weather_menu)
        # Place weather menu button on the root
        self.weather_menubutton.place(relx=0.05, rely=0.2)

        # Add the occasion options to the occasion drop-down menu
        for category in self.mywardrobe.occasion_categories:
            self.occasion_menu.add_radiobutton(label=category, variable=self.occasion_selection,
                                               command=self.occasion_selected)

        # add the menu feature to the menu button
        self.occasion_menubutton.config(menu=self.occasion_menu)
        # Place occasion menu button on the root
        self.occasion_menubutton.place(relx=0.05, rely=0.3)

    def create_menubar(self):
        # Attach file to the menu bar
        self.menubar.add_cascade(label="File", menu=self.file)
        # Add the "Load Wardrobe" option
        self.file.add_command(label="Load Wardrobe",
                              command=self.load_new_wardrobe)
        # Add the "Exit" option
        self.file.add_command(label="Exit", command=self.root.destroy)

        # Attach edit menu to the menu bar
        self.menubar.add_cascade(label="Edit", menu=self.edit)

        # Add the "Add New Top" option
        self.edit.add_command(label="Add New Top", command=self.new_top)
        # Add the "Add New Bottom" option
        self.edit.add_command(label="Add New Bottom", command=self.new_bottom)

        self.root.config(menu=self.menubar)

    def create_photo(self, image_name):
        # load the image in
        load = Image.open(self.file_path + "\\" + image_name)
        # Resize the image so it fits in the frame
        image_resized = load.resize(
            (int(FRAME_WIDTH), int(FRAME_HEIGHT)), Image.ANTIALIAS)
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
        self.top_index = random.randint(
            0, len(self.mywardrobe.master_tops_list) - 1)
        self.bottom_index = random.randint(
            0, len(self.mywardrobe.master_bottoms_list) - 1)

        # Place the random top and bottom images on the screen
        self.update_photo(self.mywardrobe.master_tops_list[self.top_index])
        self.update_photo(
            self.mywardrobe.master_bottoms_list[self.bottom_index])

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
        if self.top_index == len(self.mywardrobe.master_tops_list) - 1:
            self.button_next_top.config(state="disabled")
        else:
            self.button_next_top.config(state="normal")

        if self.bottom_index == len(self.mywardrobe.master_bottoms_list) - 1:
            self.button_next_bottom.config(state='disabled')
        else:
            self.button_next_bottom.config(state="normal")

    # function to get the next photo
    def next_photo(self, item):

        # check if you're changing the top or bottom photo
        # and get the appropriate index and image list
        if item == 'top':
            index = self.top_index
            image_names = self.mywardrobe.master_tops_list
        else:
            index = self.bottom_index
            image_names = self.mywardrobe.master_bottoms_list

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
            image_names = self.mywardrobe.master_tops_list
        else:
            index = self.bottom_index
            image_names = self.mywardrobe.master_bottoms_list

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
        image_resized = load.resize(
            (int(FRAME_WIDTH), int(FRAME_HEIGHT)), Image.ANTIALIAS)
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
                self.mywardrobe.weather_tops_list = self.mywardrobe.all_tops
                self.mywardrobe.weather_bottoms_list = self.mywardrobe.all_bottoms
            elif self.weather_selection.get() == 'Hot':
                self.mywardrobe.weather_tops_list = self.mywardrobe.hot_tops
                self.mywardrobe.weather_bottoms_list = self.mywardrobe.hot_bottoms
            elif self.weather_selection.get() == 'Warm':
                self.mywardrobe.weather_tops_list = self.mywardrobe.warm_tops
                self.mywardrobe.weather_bottoms_list = self.mywardrobe.warm_bottoms
            elif self.weather_selection.get() == 'Cold and Windy':
                self.mywardrobe.weather_tops_list = self.mywardrobe.windy_tops
                self.mywardrobe.weather_bottoms_list = self.mywardrobe.windy_bottoms
            elif self.weather_selection.get() == 'Cold and Rainy':
                self.mywardrobe.weather_tops_list = self.mywardrobe.rainy_tops
                self.mywardrobe.weather_bottoms_list = self.mywardrobe.rainy_bottoms

        # If the selection made was to filter the occasion then get the appropriate list based on what occasion
        # type was selected
        if selection == 'occasion':
            if self.occasion_selection.get() == 'Show All':
                self.mywardrobe.occasion_tops_list = self.mywardrobe.all_tops
                self.mywardrobe.occasion_bottoms_list = self.mywardrobe.all_bottoms
            elif self.occasion_selection.get() == 'Work':
                self.mywardrobe.occasion_tops_list = self.mywardrobe.work_tops
                self.mywardrobe.occasion_bottoms_list = self.mywardrobe.work_bottoms
            elif self.occasion_selection.get() == 'House Party':
                self.mywardrobe.occasion_tops_list = self.mywardrobe.house_party_tops
                self.mywardrobe.occasion_bottoms_list = self.mywardrobe.house_party_bottoms
            elif self.occasion_selection.get() == 'Town':
                self.mywardrobe.occasion_tops_list = self.mywardrobe.town_tops
                self.mywardrobe.occasion_bottoms_list = self.mywardrobe.town_bottoms
            elif self.occasion_selection.get() == '21st':
                self.mywardrobe.occasion_tops_list = self.mywardrobe.twenty_first_tops
                self.mywardrobe.occasion_bottoms_list = self.mywardrobe.twenty_first_bottoms
            elif self.occasion_selection.get() == 'Everyday':
                self.mywardrobe.occasion_tops_list = self.mywardrobe.everyday_tops
                self.mywardrobe.occasion_bottoms_list = self.mywardrobe.everyday_bottoms
            elif self.occasion_selection.get() == 'Family':
                self.mywardrobe.occasion_tops_list = self.mywardrobe.family_tops
                self.mywardrobe.occasion_bottoms_list = self.mywardrobe.family_bottoms

        # If both a weather and a occasion are selected
        # Check if specific weather and occasion filters are applied (not just show all)
        # Also have to check if a selection has been made because at the start self.weather_selection and
        # self.occasion_selection are empty
        if (self.weather_selection.get() != 'Show All') and (self.occasion_selection.get() != 'Show All') and \
                (self.weather_selection.get() != '') and (self.occasion_selection.get() != ''):
            # Empty the master_tops_list and fill it only with tops common to both the weather category
            # and the occasion category selected
            self.mywardrobe.master_tops_list = []
            for top in self.mywardrobe.occasion_tops_list:
                if top in self.mywardrobe.weather_tops_list:
                    self.mywardrobe.master_tops_list.append(top)

            self.mywardrobe.master_bottoms_list = []
            for bottom in self.mywardrobe.occasion_bottoms_list:
                if bottom in self.mywardrobe.weather_bottoms_list:
                    self.mywardrobe.master_bottoms_list.append(bottom)

        # Else if only an occasion is selected then update the master list to be clothes for that occasion
        elif ((self.occasion_selection.get() != 'Show All') and (self.occasion_selection.get() != '')) and \
                ((self.weather_selection.get() == 'Show All') or (self.weather_selection.get() == '')):
            # Update master list
            self.mywardrobe.master_tops_list = self.mywardrobe.occasion_tops_list
            self.mywardrobe.master_bottoms_list = self.mywardrobe.occasion_bottoms_list

        # Else if only a weather type is selected then update the master list to be clothes for that weather
        elif ((self.weather_selection.get() != 'Show All') and (self.weather_selection.get() != '')) and \
                ((self.occasion_selection.get() == 'Show All') or (self.occasion_selection.get() == '')):
            # Update master list
            self.mywardrobe.master_tops_list = self.mywardrobe.weather_tops_list
            self.mywardrobe.master_bottoms_list = self.mywardrobe.weather_bottoms_list

        # Else if both weather and occasion are show all then master_lists = all_tops and all_bottoms
        elif ((self.weather_selection.get() == 'Show All') or (self.weather_selection.get() == '')) and \
                ((self.occasion_selection.get() == 'Show All') or (self.occasion_selection.get() == '')):
            # Update master list
            self.mywardrobe.master_tops_list = self.mywardrobe.all_tops
            self.mywardrobe.master_bottoms_list = self.mywardrobe.all_bottoms

        # Update indices to start from the beginning
        self.top_index = 0
        self.bottom_index = 0

        # check the tops list is empty, and if it is then show an empty white frame saying "No tops"
        # Otherwise run create_photo to add the first photo to the frame
        if len(self.mywardrobe.master_tops_list) == 0:
            self.image_label = tk.Label(self.frame_top, text="No tops", bg="white", width=int(FRAME_WIDTH),
                                        height=int(FRAME_HEIGHT))
            # self.top_image_label.place_forget()
        else:
            self.update_photo(self.mywardrobe.master_tops_list[self.top_index])

        # check the bottoms list is empty, and if it is then show an empty white frame saying "No tops"
        # otherwise run create_photo to add the first photo to the frame
        if len(self.mywardrobe.master_bottoms_list) == 0:
            self.image_label = tk.Label(self.frame_bottom, text="No Bottoms", bg='white', width=int(FRAME_WIDTH),
                                        height=int(FRAME_HEIGHT))
            # self.bottom_image_label.place_forget()
        else:
            self.update_photo(
                self.mywardrobe.master_bottoms_list[self.bottom_index])

        # Make the previous buttons disabled as we are at the first image of the filtered images
        self.button_prev_top.config(state='disabled')
        self.button_prev_bottom.config(state='disabled')

        # Enable the next button just in case it was disabled before (e.g we reached the end of the photos
        # and THEN we changed the filter
        self.button_next_top.config(state='normal')
        self.button_next_bottom.config(state='normal')

        # If there is only 1 image (or no images) when clothes are filtered then disable the next button as well
        if len(self.mywardrobe.master_tops_list) <= 1:
            self.button_next_top.config(state='disabled')
        if len(self.mywardrobe.master_bottoms_list) <= 1:
            self.button_next_bottom.config(state='disabled')

    # function to load a new wardrobe into the program (change the file path)
    def load_new_wardrobe(self):

        # Get the new folder that contains the clothes
        try:
            self.file_path = filedialog.askdirectory()
            # Save the new wardrobe in the "Directory (DO NOT EDIT).txt" file
            with open('Directory (DO NOT EDIT).txt', "w") as f:
                f.write(self.file_path)
        # if the user doesn't choose a folder let it pass (they can still use the old one currently loaded)
        except FileNotFoundError:
            pass
        # Use the load_wardrobe function to get the new file path and new images
        self.mywardrobe.load_wardrobe(self.file_path)

        # Start the image indices at 0 (so it starts with the first image)
        self.top_index = 0
        self.bottom_index = 0

        # update the frames with the new photos
        self.update_photo(self.mywardrobe.master_tops_list[self.top_index])
        self.update_photo(
            self.mywardrobe.master_bottoms_list[self.bottom_index])

        # Make the previous buttons disabled as we are at the first image of the filtered images
        self.button_prev_top.config(state='disabled')
        self.button_prev_bottom.config(state='disabled')

        # Enable the next button just in case it was disabled before (e.g we reached the end of the photos
        # and THEN we changed the filter
        self.button_next_top.config(state='normal')
        self.button_next_bottom.config(state='normal')

        # If there is only 1 image (or no images) when clothes are filtered then disable the next button as well
        if len(self.mywardrobe.master_tops_list) <= 1:
            self.button_next_top.config(state='disabled')
        if len(self.mywardrobe.master_bottoms_list) <= 1:
            self.button_next_bottom.config(state='disabled')

    # function called when user right clicks a tops image
    def right_clicked_image_top(self, event):
        # Set image_type to be a top so we know we are editing tops
        self.image_type = 'top'

        print("right click top!")
        # Call the edit image function and tell it that you are editing a top item
        # Make sure it doesn't keep creating menus when you right click
        # If the menu already exists, then forget it an make a new one
        self.R1.deselect()
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
        self.R1.deselect()
        try:
            print("working")
            self.edit_categories.place_forget()
            self.edit_image_options()
        except Exception:
            self.edit_image_options()

    # function called when the user left clicks in the root (get rid of edit categories)
    def left_clicked(self, event):
        # if the edit categories option is present (user right clicked an image) then remove it
        # if the edit categories option was not present (the user just clicked the root for no reason) then do nothing
        try:
            self.edit_categories.place_forget()
        except Exception:
            pass

    # Function that creates the menu to edit image categories when you right click an image (called by right_clicked..)
    def edit_image_options(self):
        # Get the x and y coordinated of the cursor
        cursor_x = int(self.root.winfo_pointerx() - self.root.winfo_rootx())
        cursor_y = int(self.root.winfo_pointery() - self.root.winfo_rooty())

        # Place "edit_categories" menu that appears when you right click
        self.edit_categories.place(x=cursor_x, y=cursor_y)

        # Place the buttons that open the category editor onto the menu
        # (R1 = edit weather filters R2 = edit occasion filters)
        self.R1.pack(anchor="w", fill='x')
        self.R2.pack(anchor="w", fill='x')

    # Function that displays a new window to edit filters
    def category_editor(self):

        # Close the menu if you are coming from edit_image_options function
        try:
            self.edit_categories.place_forget()
        except AttributeError:  # If you are adding a new top/bottom then edit_categories doesnt exist
            pass

        # Open a new canvas that shows all the categories and asks which one you want to add
        self.editor = tk.Toplevel()

        # add title to window - If adding a new top/bottom then show all filters, otherwise choose weather/occasion
        # depending on what the selected to edit
        try:
            selection = self.edit_image_selection.get()
        except AttributeError:  # If you are adding a new top/bottom then edit_image_selection doesnt exist
            self.editor.title("Edit Categories")
        else:
            if self.edit_image_selection.get() == 'occasion':
                self.editor.title("Edit Occasion Categories")
            elif self.edit_image_selection.get() == 'weather':
                self.editor.title("Edit Weather Categories")

        # change the size of the window
        self.editor_canvas = tk.Canvas(self.editor, height=400, width=600)
        self.editor_canvas.pack()

        # Show the image of the selected top
        # Set the frame
        self.frame_image_edit = tk.Frame(self.editor, bg='#80c1ff')
        self.frame_image_edit.place(
            relx=0.1, rely=0.1, width=FRAME_WIDTH, height=FRAME_HEIGHT)

        if self.image_type == 'top':
            # Put the top image inside the frame (remember the image photo is saved in the original
            # top_image_label.image
            self.image_label = tk.Label(
                self.frame_image_edit, image=self.top_image_label.image)
            # Save a reference so that tkinter doesnt doesn't send it to the garbage collector
            # when the function closes (so the widget can still hold onto the image)
            self.image_label.image = self.top_image_label.image

        elif self.image_type == 'bottom':
            # Put the bottom image inside the frame (remember the image photo is saved in the original
            # bottom_image_label.image
            self.image_label = tk.Label(
                self.frame_image_edit, image=self.bottom_image_label.image)
            # Save a reference so that tkinter doesnt doesn't send it to the garbage collector
            # when the function closes (so the widget can still hold onto the image)
            self.image_label.image = self.bottom_image_label.image

        # Place the image
        self.image_label.place(x=0, y=0)

        # Get the image name
        if self.image_type == 'top':
            image_name = self.mywardrobe.master_tops_list[self.top_index]
        elif self.image_type == 'bottom':
            image_name = self.mywardrobe.master_bottoms_list[self.bottom_index]

        # Show the filters
        # If you are adding a new top/bottom then display all the filters (in the except clause)
        # If you are editing filters then only display the one you're editing (weather or occasion)
        try:
            selection = self.edit_image_selection.get()
        except AttributeError:  # If you are adding a new top/bottom then edit_image_selection doesnt exist
            self.frame_options_edit_weather = tk.Frame(self.editor)
            self.frame_options_edit_weather.place(
                relx=0.5, rely=0.1, width=FRAME_WIDTH, height=FRAME_HEIGHT)

            self.frame_options_edit_occasion = tk.Frame(self.editor)
            self.frame_options_edit_occasion.place(
                relx=0.7, rely=0.1, width=FRAME_WIDTH, height=FRAME_HEIGHT)

            # Weather filters
            self.hot_selection = tk.IntVar()
            self.warm_selection = tk.IntVar()
            self.windy_selection = tk.IntVar()
            self.rainy_selection = tk.IntVar()

            self.hot_filter = tk.Checkbutton(self.frame_options_edit_weather, text="Hot", variable=self.hot_selection,
                                             command=self.change_hot_filter)
            self.hot_filter.pack(anchor='w')

            self.warm_filter = tk.Checkbutton(self.frame_options_edit_weather, text="Warm",
                                              variable=self.warm_selection,
                                              command=self.change_warm_filter)
            self.warm_filter.pack(anchor='w')

            self.windy_filter = tk.Checkbutton(self.frame_options_edit_weather, text="Cold and Windy",
                                               variable=self.windy_selection, command=self.change_windy_filter)
            self.windy_filter.pack(anchor='w')

            self.rainy_filter = tk.Checkbutton(self.frame_options_edit_weather, text="Cold and Rainy",
                                               variable=self.rainy_selection, command=self.change_rainy_filter)
            self.rainy_filter.pack(anchor='w')

            # Get the filters currently applied to that image
            if 'hot' in image_name:
                self.hot_filter.select()
            if 'warm' in image_name:
                self.warm_filter.select()
            if 'windy' in image_name:
                self.windy_filter.select()
            if 'rainy' in image_name:
                self.rainy_filter.select()

            # Occasion filters
            self.work_selection = tk.IntVar()
            self.house_party_selection = tk.IntVar()
            self.town_selection = tk.IntVar()
            self.twenty_first_selection = tk.IntVar()
            self.everyday_selection = tk.IntVar()
            self.family_selection = tk.IntVar()

            self.work_filter = tk.Checkbutton(self.frame_options_edit_occasion, text="Work",
                                              variable=self.work_selection,
                                              command=self.change_work_filter)
            self.work_filter.pack(anchor='w')

            self.house_party_filter = tk.Checkbutton(self.frame_options_edit_occasion, text="House Party",
                                                     variable=self.house_party_selection,
                                                     command=self.change_house_party_filter)
            self.house_party_filter.pack(anchor='w')

            self.town_filter = tk.Checkbutton(self.frame_options_edit_occasion, text="Town",
                                              variable=self.town_selection,
                                              command=self.change_town_filter)
            self.town_filter.pack(anchor='w')

            self.twenty_first_filter = tk.Checkbutton(self.frame_options_edit_occasion, text="21st",
                                                      variable=self.twenty_first_selection,
                                                      command=self.change_twenty_first_filter)
            self.twenty_first_filter.pack(anchor='w')

            self.everyday_filter = tk.Checkbutton(self.frame_options_edit_occasion, text="Everyday",
                                                  variable=self.everyday_selection, command=self.change_everyday_filter)
            self.everyday_filter.pack(anchor='w')

            self.family_filter = tk.Checkbutton(self.frame_options_edit_occasion, text="Family",
                                                variable=self.family_selection,
                                                command=self.change_family_filter)
            self.family_filter.pack(anchor='w')

        else:
            self.frame_options_edit = tk.Frame(self.editor)
            self.frame_options_edit.place(
                relx=0.5, rely=0.1, width=FRAME_WIDTH, height=FRAME_HEIGHT)

            if self.edit_image_selection.get() == 'weather':
                self.hot_selection = tk.IntVar()
                self.warm_selection = tk.IntVar()
                self.windy_selection = tk.IntVar()
                self.rainy_selection = tk.IntVar()

                self.hot_filter = tk.Checkbutton(self.frame_options_edit, text="Hot", variable=self.hot_selection,
                                                 command=self.change_hot_filter)
                self.hot_filter.pack(anchor='w')

                self.warm_filter = tk.Checkbutton(self.frame_options_edit, text="Warm", variable=self.warm_selection,
                                                  command=self.change_warm_filter)
                self.warm_filter.pack(anchor='w')

                self.windy_filter = tk.Checkbutton(self.frame_options_edit, text="Cold and Windy",
                                                   variable=self.windy_selection, command=self.change_windy_filter)
                self.windy_filter.pack(anchor='w')

                self.rainy_filter = tk.Checkbutton(self.frame_options_edit, text="Cold and Rainy",
                                                   variable=self.rainy_selection, command=self.change_rainy_filter)
                self.rainy_filter.pack(anchor='w')

                # Get the filters currently applied to that image
                if 'hot' in image_name:
                    self.hot_filter.select()
                if 'warm' in image_name:
                    self.warm_filter.select()
                if 'windy' in image_name:
                    self.windy_filter.select()
                if 'rainy' in image_name:
                    self.rainy_filter.select()

            elif self.edit_image_selection.get() == 'occasion':
                self.work_selection = tk.IntVar()
                self.house_party_selection = tk.IntVar()
                self.town_selection = tk.IntVar()
                self.twenty_first_selection = tk.IntVar()
                self.everyday_selection = tk.IntVar()
                self.family_selection = tk.IntVar()

                self.work_filter = tk.Checkbutton(self.frame_options_edit, text="Work", variable=self.work_selection,
                                                  command=self.change_work_filter)
                self.work_filter.pack(anchor='w')

                self.house_party_filter = tk.Checkbutton(self.frame_options_edit, text="House Party",
                                                         variable=self.house_party_selection,
                                                         command=self.change_house_party_filter)
                self.house_party_filter.pack(anchor='w')

                self.town_filter = tk.Checkbutton(self.frame_options_edit, text="Town", variable=self.town_selection,
                                                  command=self.change_town_filter)
                self.town_filter.pack(anchor='w')

                self.twenty_first_filter = tk.Checkbutton(self.frame_options_edit, text="21st",
                                                          variable=self.twenty_first_selection,
                                                          command=self.change_twenty_first_filter)
                self.twenty_first_filter.pack(anchor='w')

                self.everyday_filter = tk.Checkbutton(self.frame_options_edit, text="Everyday",
                                                      variable=self.everyday_selection,
                                                      command=self.change_everyday_filter)
                self.everyday_filter.pack(anchor='w')

                self.family_filter = tk.Checkbutton(self.frame_options_edit, text="Family",
                                                    variable=self.family_selection,
                                                    command=self.change_family_filter)
                self.family_filter.pack(anchor='w')

                # Get the filters currently applied to that image
                if 'work' in image_name:
                    self.work_filter.select()
                if 'house party' in image_name:
                    self.house_party_filter.select()
                if 'town' in image_name:
                    self.town_filter.select()
                if '21st' in image_name:
                    self.twenty_first_filter.select()
                if 'everyday' in image_name:
                    self.everyday_filter.select()
                if 'family' in image_name:
                    self.family_filter.select()

        # Add a save button
        self.save_button = tk.Button(
            self.editor, text="Save", bg='light blue', command=self.close_editor)
        self.save_button.place(
            relx=0.7, rely=0.8, relwidth=0.1, relheight=0.075)

        # Show the Edit Weather Categories window
        self.editor.mainloop()
        # print(self.edit_image_selection.get())

    # Function called when save button is pressed that closes the editor (new_item_category_editor and category
    # editor functions)

    def close_editor(self):
        self.editor.destroy()

    # Function called when user wants to change the hot weather filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Weather Categories window
    def change_hot_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.hot_selection.get() == 1:
            self.add_filter('hot')
        if self.hot_selection.get() == 0:
            self.remove_filter('hot')

    # Function called when user wants to change the warm weather filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Weather Categories window
    def change_warm_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.warm_selection.get() == 1:
            self.add_filter('warm')
        if self.warm_selection.get() == 0:
            self.remove_filter('warm')

    # Function called when user wants to change the cold and windy weather filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Weather Categories window
    def change_windy_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.windy_selection.get() == 1:
            self.add_filter('windy')
        if self.windy_selection.get() == 0:
            self.remove_filter('windy')

    # Function called when user wants to change the cold and rainy weather filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Weather Categories window
    def change_rainy_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.rainy_selection.get() == 1:
            self.add_filter('rainy')
        if self.rainy_selection.get() == 0:
            self.remove_filter('rainy')

    # Function called when user wants to change the work occasion filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Occasion Categories window
    def change_work_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.work_selection.get() == 1:
            self.add_filter('work')
        if self.work_selection.get() == 0:
            self.remove_filter('work')

    # Function called when user wants to change the town occasion filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Occasion Categories window
    def change_town_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.town_selection.get() == 1:
            self.add_filter('town')
        if self.town_selection.get() == 0:
            self.remove_filter('town')

    # Function called when user wants to change the house party occasion filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Occasion Categories window
    def change_house_party_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.house_party_selection.get() == 1:
            self.add_filter('house party')
        if self.house_party_selection.get() == 0:
            self.remove_filter('house party')

    # Function called when user wants to change the 21st occasion filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Occasion Categories window
    def change_twenty_first_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.twenty_first_selection.get() == 1:
            self.add_filter('21st')
        if self.twenty_first_selection.get() == 0:
            self.remove_filter('21st')

    # Function called when user wants to change the everyday occasion filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Occasion Categories window
    def change_everyday_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.everyday_selection.get() == 1:
            self.add_filter('everyday')
        if self.everyday_selection.get() == 0:
            self.remove_filter('everyday')

    # Function called when user wants to change the family occasion filter on a clothing item (add or remove it)
    # Called when check button is pressed in Edit Occasion Categories window
    def change_family_filter(self):
        # Check if user is selecting (1) or deselecting (0) the filter and add/remove accordingly
        if self.family_selection.get() == 1:
            self.add_filter('family')
        if self.family_selection.get() == 0:
            self.remove_filter('family')

    # Function used to add a filter to a clothing image (called by change_..._filter functions above)
    def add_filter(self, added):
        # Get the image name
        if self.image_type == 'top':
            image_title = self.mywardrobe.master_tops_list[self.top_index]
        else:
            image_title = self.mywardrobe.master_bottoms_list[self.bottom_index]

        # Split the name into before the .jpg (or other extension) and the extension (this will exclude the '.')
        name_list = image_title.split(".")
        before_extension = name_list[0]
        extension = name_list[1]

        # Add the new category in between
        new_title = before_extension + ", " + added + "." + extension

        # Save the new name
        os.rename((self.file_path + "\\" + image_title),
                  (self.file_path + "\\" + new_title))

        # reload the clothes
        self.mywardrobe.load_wardrobe(self.file_path)

    # Function used to remove a filter from a clothing image (called by change_..._filter functions above)
    def remove_filter(self, removed):
        # Get the image name
        if self.image_type == 'top':
            image_title = self.mywardrobe.master_tops_list[self.top_index]
        else:
            image_title = self.mywardrobe.master_bottoms_list[self.bottom_index]

        # Create a list with 2 elements - the first is everything before the word top, the second is everything after
        new_name_list = image_title.split(removed)
        # the first part of the new name
        new_name_pt1 = new_name_list[0]
        # The second part of the new name
        new_name_pt2 = new_name_list[1]

        # Then remove the comma that came before the removed word
        index = new_name_pt1.rfind(",")
        new_name_pt1 = new_name_pt1[0:index]

        # Join the 2 parts together to form the new name
        new_name = new_name_pt1 + new_name_pt2

        # Save the new name
        os.rename((self.file_path + "\\" + image_title),
                  (self.file_path + "\\" + new_name))

        # reload the clothes
        self.mywardrobe.load_wardrobe(self.file_path)

    # Function called to add a new top to the wardrobe from within the app
    def new_top(self):
        # Set image_type to be a top so we know we are editing tops
        self.image_type = 'top'
        self.new_item()

    # Function used to add a new top to the wardrobe from within the app
    def new_bottom(self):
        # Set image_type to be a bottom so we know we are editing bottoms
        self.image_type = 'bottom'
        self.new_item()

    # Function used to add the item selected (called by new_top or new_bottom)
    def new_item(self):
        # Ask the user to select the top image from file explorer
        item_path = filedialog.askopenfilename()
        print(item_path)

        if item_path == "":
            return
        else:

            # Get the directory and the original image name
            index = item_path.rfind("/")
            directory = item_path[0:index + 1]  # including the /
            original_name = item_path[index + 1:]  # including the extension
            # print(directory)

            # Get the extension
            name_list = item_path.split(".")
            extension = name_list[1]

            # Name the top to the topx where x is the total number of tops in the wardrobe including the addition
            if self.image_type == "top":
                new_name = "top" + \
                    str(len(self.mywardrobe.all_tops) + 1) + "." + extension
            elif self.image_type == "bottom":
                new_name = "bottom" + \
                    str(len(self.mywardrobe.all_bottoms) + 1) + "." + extension
            # print(new_name)

            # Make a copy and move the file into the current wardrobe and rename it
            shutil.copyfile(item_path, (self.file_path + "\\" + new_name))

            # Load the image into the wardrobe
            self.mywardrobe.load_wardrobe()

            # Show the photo as the current selection
            if self.image_type == "top":
                self.top_index = len(self.mywardrobe.all_tops) - 1
                self.update_photo(self.mywardrobe.all_tops[self.top_index])

                # Disable the next button because this is the last photo
                self.button_next_top.config(state='disabled')

                # Enable the previous button if the list is greater than 1
                if len(self.mywardrobe.all_tops) > 1:
                    self.button_prev_top.config(state='normal')

            elif self.image_type == "bottom":
                self.bottom_index = len(self.mywardrobe.all_bottoms) - 1
                self.update_photo(
                    self.mywardrobe.all_bottoms[self.bottom_index])

                # Disable the next button because this is the last photo
                self.button_next_bottom.config(state='disabled')

                # Enable the previous button if the list is greater than 1
                if len(self.mywardrobe.all_bottoms) > 1:
                    self.button_prev_bottom.config(state='normal')

            # Show the edit weather categories options to add weather categories
            self.category_editor()

            # load the wardrobe again
            self.mywardrobe.load_wardrobe()

            # Show the edit occasion categories options to add occasion categories
            # self.R2.select()
            # self.R2.invoke()


'''
Things for the future:
Fix what happens if there are no options for the weather and occasion combination

Fix what happens when you delete a clothing item and add a new one because there could be 2 top6's
    - check all tops and all bottoms lists frequently to make sure there aren't duplicates

Maybe have multiple files/classes?? Organise the file better so different files have different functions

Make the app look cuter!!

Add a favourites category! maybe just a checkbox or something on its own below the weather and occasion

Find out how to get the current weather from a weather site (may need to input the time)
    - certain temperature ranges can correspond to different weather filters
    - Can read the temperature and automatically select a weather filter 
    - Have a button for "today"

Maybe you can choose a date in the future that you need an outfit for (and a time?) and it can tell you the weather 

Save outfits so you can look through pre assembled looks for specific occasions/weather types

Be able to delete items from the wardrobe from within the app (right click and remove)
    - this would be done by right clicking and going to a delete item option
    - A window will open saying are you sure you want to delete this item (could show the top)
    - Window has "delete" and "cancel" buttons
    - When the file is removed all the items after it decrease in number (e.g. if top6 was deleted then top7 becomes
      top6 and top8 becomes top7 etc.
      
DONE Be able to add an item to the wardrobe from within the app (go file, add item):
   DONE when you add the item you can choose:
    DONE 1. if its a top or bottom
    DONE 2. select which weather categories it falls under
    DONE 3. select which occasion categories it falls under
    DONE Then it is automatically added to the appropriate folder and named based on if its a top or bottom + 
         the length of the all tops list +1 (since you're adding a new item) + weather categories + occasion categories

DONE Be able to change the file path where the images are stored
- DONE Go to file, change directory and it will make you choose where "All Tops" and "All Bottoms" are located

DONE: Be able to edit the categories within the app
- DONE view the categories an item falls under and add/remove a category accordingly
    - DONE this would be done by right clicking and going to an edit categories option to display the current categories
    - DONE can either "add new" or "remove"
    - DONE add: then the title of the image gets edited to have the new category appended to it (title + ", " + category)
    - DONE remove: then the title of the image gets edited to remove the category
    
DONE When you first start the program it will ask you to choose the filepath. 
DONE Then it will remember it for next time.
DONE When you want a new file path you go to file - Load Wardrobe
            
'''
root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
