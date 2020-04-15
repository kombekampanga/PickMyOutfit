import tkinter as tk
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

##############################  LIST CONTAINING ALL THE CLOTHING IMAGES  ###########################################
# list of all image names
'''
maybe in the future instead of loading all the lists here, we can have a function that gets the required images from
the right folder depending on which selection is made
Right now we are just making lists to see if this will work
'''

all_tops = ['top1.jpg', "top2.jpg", "top3.jpg", "top4.jpg", "top5.jpg", "top6.jpg", "top7.jpg", "top8.jpg", "top9.jpg",
            "top10.jpg"]
all_bottoms = ["bottom1.jpg", "bottom2.jpg", "bottom3.jpg", "bottom4.jpg", "bottom5.jpg", "bottom6.jpg", "bottom7.jpg",
               "bottom8.jpg", "bottom9.jpg"]

# Master lists - these will be updated in the program (when weather and/or occasions are selected)
# and used in the create_photo function to display the appropriate pictures
# To begin with these will show all the tops and bottoms because no selection has been made
master_tops_list = all_tops
master_bottoms_list = all_bottoms

################################  WEATHER AND OCCASION FILTER VARIABLES  ###########################################

# Weather and Occasion filter variables

# Weather and occasion lists - these will be updated in the filter function (when weather and/or
# occasions are selected) and then used to update the master lists accordingly
weather_tops_list = []
weather_bottoms_list = []
occasion_tops_list = []
occasion_bottoms_list = []

# lists of weather category titles
weather_categories = ['Show All','Hot', 'Warm', 'Cold and Windy', 'Cold and Rainy']
occasion_categories = ['Show All', 'Work', 'House Party', 'Town', '21st', 'Everyday', 'Family']

# Weather specified clothing
hot_tops = ['top1.jpg', 'top4.jpg', 'top6.jpg', 'top9.jpg']
hot_bottoms = ['bottom2.jpg', 'bottom5.jpg', 'bottom6.jpg', 'bottom9.jpg']

warm_tops = ['top1.jpg', 'top2.jpg', 'top5.jpg', 'top10.jpg']
warm_bottoms = ['bottom1.jpg', 'bottom3.jpg', 'bottom4.jpg', 'bottom7.jpg', 'bottom8.jpg', 'bottom9.jpg']

windy_tops = ["top3.jpg", "top2.jpg", "top5.jpg", 'top8.jpg', 'top10.jpg']
windy_bottoms = ['bottom1.jpg', 'bottom3.jpg', 'bottom4.jpg', 'bottom7.jpg', 'bottom8.jpg']

rainy_tops = ['top3.jpg', "top2.jpg", 'top5.jpg', 'top7.jpg', 'top8.jpg', 'top10.jpg']
rainy_bottoms = ['bottom1.jpg', 'bottom4.jpg', 'bottom7.jpg', 'bottom8.jpg']

# Occasion specified clothing
work_tops = ['top5.jpg', 'top8.jpg', 'top9.jpg']
work_bottoms = ['bottom8.jpg', 'bottom9.jpg']

house_party_tops = ['top1.jpg', 'top6.jpg', 'top10.jpg']
house_party_bottoms = ['bottom1.jpg', 'bottom2.jpg', 'bottom5.jpg', 'bottom6.jpg', 'bottom7.jpg']

town_tops = ['top2.jpg', 'top4.jpg']
town_bottoms = ['bottom5.jpg', 'bottom7.jpg']

twenty_first_tops = ["top2.jpg", "top4.jpg"]
twenty_first_bottoms = ["bottom2.jpg", "bottom4.jpg", "bottom7.jpg"]

everyday_tops = ['top1.jpg', 'top3.jpg', 'top5,jpg', 'top7.jpg', 'top10.jpg']
everyday_bottoms = ['bottom1.jpg', "bottom3.jpg", "bottom5.jpg", "bottom6.jpg", 'bottom7.jpg']

family_tops = ["top1.jpg", "top5.jpg", "top7.jpg", "top8.jpg", "top9.jpg"]
family_bottoms = ['bottom1.jpg', 'bottom2.jpg', 'bottom6.jpg', 'bottom7.jpg', 'bottom8.jpg', 'bottom9.jpg']

#######################################  OTHER VARIABLES  ###############################################




# Wardrobe class that contains the window for the clothes to be displayed
class WardrobeApp:
    def __init__(self, root):
        # make the wardrobe window/GUI
        self.root = root

        # create variables to hold which radio button is selected (to track which option is selected)
        # These variables hold the "label" text for each radio button, so its updated based on which one is clicked
        self.weather_selection = tk.StringVar()
        self.occasion_selection = tk.StringVar()

        # Index numbers to keep track of which top/bottom item we are looking at
        # So when we click next and previous we can move through the items
        self.bottom_index = 0
        self.top_index = 0

        # Create the details for the window
        self.create_frame()
        self.create_buttons()
        # self.CreateLabels()
        self.create_menu_buttons()

        # Upload the initial top and the bottom picture into the frame (indices initially = 0)
        self.create_photo(master_tops_list[self.top_index])
        self.create_photo(master_bottoms_list[self.bottom_index])

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
        for category in weather_categories:
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
        for category in occasion_categories:
            self.occasion_menu.add_radiobutton(label=category, variable=self.occasion_selection,
                                               command=self.occasion_selected)

        # add the menu feature to the menu button
        self.occasion_menubutton.config(menu=self.occasion_menu)
        # Place occasion menu button on the root
        self.occasion_menubutton.place(relx=0.05, rely=0.3)

    def create_photo(self, image_name):
        # load the image in
        load = Image.open(image_name)
        # Resize the image so it fits in the frame
        image_resized = load.resize((int(FRAME_WIDTH), int(FRAME_HEIGHT)), Image.ANTIALIAS)
        # Create the image so tkinter can read it
        photo = ImageTk.PhotoImage(image_resized)

        # check if the image is a top or bottom and put it in the appropriate frame
        # Place the image into a label so it can be displayed (tkinter rule)
        if "top" in image_name:
            image_label = tk.Label(self.frame_top, image=photo)
        elif "bottom" in image_name:
            image_label = tk.Label(self.frame_bottom, image=photo)

        # Save a reference so that tkinter doesnt doesn't send it to the garbage collector
        # when the function closes (so the widget can still hold onto the image
        image_label.image = photo

        # Place the image into the frame
        image_label.place(x=0, y=0)

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
        self.top_index = random.randint(0, len(master_tops_list) - 1)
        self.bottom_index = random.randint(0, len(master_bottoms_list) - 1)

        # Place the random top and bottom images on the screen
        self.create_photo(master_tops_list[self.top_index])
        self.create_photo(master_bottoms_list[self.bottom_index])

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
        if self.top_index == len(master_tops_list) - 1:
            self.button_next_top.config(state="disabled")
        else:
            self.button_next_top.config(state="normal")

        if self.bottom_index == len(master_bottoms_list) - 1:
            self.button_next_bottom.config(state='disabled')
        else:
            self.button_next_bottom.config(state="normal")

    # function to get the next photo
    def next_photo(self, item):

        # check if you're changing the top or bottom photo
        # and get the appropriate index and image list
        if item == 'top':
            index = self.top_index
            image_names = master_tops_list
        elif item == 'bottom':
            index = self.bottom_index
            image_names = master_bottoms_list

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
            self.create_photo(image_names[index])
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
            image_names = master_tops_list
        elif item == 'bottom':
            index = self.bottom_index
            image_names = master_bottoms_list

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
            self.create_photo(image_names[index])
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

    # function when weather filter is selected
    def weather_selected(self):
        self.filter('weather')

    # function when occasion filter is selected
    def occasion_selected(self):
        self.filter('occasion')

    # function to apply filter based on weather and/or occasion selection
    def filter(self, selection):
        global weather_tops_list
        global weather_bottoms_list
        global occasion_tops_list
        global occasion_bottoms_list
        global master_tops_list
        global master_bottoms_list

        # If the selection made was to filter the weather then get the appropriate list based on what weather
        # type was selected
        print("selection: " + selection)
        if selection == 'weather':
            print("working1")
            if self.weather_selection.get() == 'Show All':
                print("working2")
                weather_tops_list = all_tops
                weather_bottoms_list = all_bottoms
            elif self.weather_selection.get() == 'Hot':
                print("working3")
                weather_tops_list = hot_tops
                weather_bottoms_list = hot_bottoms
            elif self.weather_selection.get() == 'Warm':
                weather_tops_list = warm_tops
                weather_bottoms_list = warm_bottoms
            elif self.weather_selection.get() == 'Cold and Windy':
                weather_tops_list = windy_tops
                weather_bottoms_list = windy_bottoms
            elif self.weather_selection.get() == 'Cold and Rainy':
                weather_tops_list = rainy_tops
                weather_bottoms_list = rainy_bottoms
                print("length of weather tops: " + str(len(weather_tops_list)))


        # If the selection made was to filter the occasion then get the appropriate list based on what occasion
        # type was selected
        if selection == 'occasion':
            if self.occasion_selection.get() == 'Show All':
                occasion_tops_list = all_tops
                occasion_bottoms_list = all_bottoms
            elif self.occasion_selection.get() == 'Work':
                occasion_tops_list = work_tops
                occasion_bottoms_list = work_bottoms
            elif self.occasion_selection.get() == 'House Party':
                occasion_tops_list = house_party_tops
                occasion_bottoms_list = house_party_bottoms
            elif self.occasion_selection.get() == 'Town':
                occasion_tops_list = town_tops
                occasion_bottoms_list = town_bottoms
            elif self.occasion_selection.get() == '21st':
                occasion_tops_list = twenty_first_tops
                occasion_bottoms_list = twenty_first_bottoms
            elif self.occasion_selection.get() == 'Everyday':
                occasion_tops_list = everyday_tops
                occasion_bottoms_list = everyday_bottoms
            elif self.occasion_selection.get() == 'Family':
                occasion_tops_list = family_tops
                occasion_bottoms_list = family_bottoms

        # If both a weather and a occasion are selected
        # Check if specific weather and occasion filters are applied (not just show all)
        # Also have to check if a selection has been made because at the start self.weather_selection and
        # self.occasion_selection are empty
        if (self.weather_selection.get() != 'Show All') and (self.occasion_selection.get() != 'Show All') and \
                (self.weather_selection.get() != '') and (self.occasion_selection.get() != ''):
            # Empty the master_tops_list and fill it only with tops common to both the weather category
            # and the occasion category selected
            master_tops_list = []
            for top in occasion_tops_list:
                if top in weather_tops_list:
                    master_tops_list.append(top)

            master_bottoms_list = []
            for bottom in occasion_bottoms_list:
                if bottom in weather_bottoms_list:
                    master_bottoms_list.append(bottom)

        # Else if only an occasion is selected then update the master list to be clothes for that occasion
        elif (selection == 'occasion') and ((self.weather_selection.get() == 'Show All') or
                                            (self.weather_selection.get() == '')):
            # Update master list
            master_tops_list = occasion_tops_list
            master_bottoms_list = occasion_bottoms_list

        # Else if only a weather type is selected then update the master list to be clothes for that weather
        elif (selection == 'weather') and ((self.occasion_selection.get() == 'Show All') or
                                            (self.occasion_selection.get() == '')):
            print("working almost there")
            # Update master list
            master_tops_list = weather_tops_list
            master_bottoms_list = weather_bottoms_list
        print("length of master list: " + str(len(master_tops_list)))
        # Update indices to start from the beginning
        self.top_index = 0
        self.bottom_index = 0


        # check the list is empty, and if it is then add the empty picture so this is displayed
        if len(master_tops_list) == 0:
            master_tops_list.append('emptytop.jpg')
        if len(master_bottoms_list) == 0:
            master_bottoms_list.append('emptybottom.jpg')

        # Run create_photo to add the first photos to the frames
        self.create_photo(master_tops_list[self.top_index])
        self.create_photo(master_bottoms_list[self.bottom_index])

        # Make the previous buttons disabled as we are at the first image of the filtered images
        self.button_prev_top.config(state='disabled')
        self.button_prev_bottom.config(state='disabled')

        # Enable the next button just in case it was disabled before (e.g we reached the end of the photos
        # and THEN we changed the filter
        self.button_next_top.config(state='normal')
        self.button_next_bottom.config(state='normal')

        # If there is only 1 image (or no images) when clothes are filtered then disable the next button as well
        if len(master_tops_list) <= 1:
            self.button_next_top.config(state='disabled')
        if len(master_bottoms_list) <= 1:
            self.button_next_bottom.config(state='disabled')


'''
thinking about filtering:
when a selection is made it start from the beginning again:
At the start you have all the tops and all the bottoms and the previous and next buttons retrieve things from the 
all tops and all bottoms lists.
Maybe have one master list that changes depending on selections
So at the start: master top list = all tops
                 master bottom list = all bottoms
then if "hot" is selected then we can only include certain items
so master top list = hot tops
master bottom list = hot bottoms

then if everyday is also chosen then 
for top in master top list:
    if top in everyday top list:
        new master top list.append(top)
master top list = new master top list

Things to do:
- Change all "tops_list" references to say master_tops_list 
- Change all bottoms_list references to say master_bottoms_list
- Add appropriate global variables
- Remember to add Is_Occasion_selected = False and Is_Weather_selected = False global variables

def occasion_selected (When occasion is selected):
declare global top_index
declare global bottom_index
declare global master_top_list
declare global master_bottom_list
declare global Is_Occasion_selected
declare global occasion_tops_list
declare global occasion_bottoms_list
1. Is_Occasion_selected = True
2. Update occasion_tops_list = that occasion_tops
3. Update occasion_bottoms_list = that occasion_bottoms
4. Check if Is_Weather_selected = True
    If it is then:
        master_top_list = []
        for top in weather_tops:
            if top in occasion_tops_list:
                master_top_list.append(top)
        
        master_bottom_list = []
        for bottom in weather_bottoms:
            if bottom in occasion_bottoms_list:
                master_bottom_list.append(bottom)
    else:
        master_top_list = occasion_tops_list
        master_bottom_list = occasion_bottoms_list
        
5. Update top_index = 0
   Update bottom_index = 0
6. Run create_photo(master_top_list[top_index])
   Run create_photo(master_bottom_list[bottom_index]
7. top_prev_button.config(state = disabled)
   if len(master_top_list) == 1
        top_next_button.config(state = disabled)
8. same as 7 but with the bottoms
---------------------------------------------------------------
##################################################
NOTE: check if deselection settings are available
##################################################

def weather_selected (When weather is selected):
change is_weather_selected = True
then run filter('weather') 

def occasion_selected (when occasion is selected):
change is_occasion_selected = True
then run filter('occasion')

def filter(selection):
declare global top_index
declare global bottom_index
declare global master_top_list
declare global master_bottom_list
declare global Is_Weather_selected
declare global weather_tops_list
declare global weather_bottoms_list

1. if selection == 'weather':
     Update weather_tops_list = that weather_tops (self.config(label)[-1] somehow - includes the show all option
        maybe for title in list_of_weather_list_names
                if self.config(label)[-1] in title:
                    weather_tops_list = .....)
     Update weather_bottoms_list = that weather_bottoms
     
     Update master_tops_list = weather_tops_list
     Update master_bottoms_list = weather_bottoms_list
     
2. if selection == 'occasion':
    Update occasion_tops_list = that occasion_tops
    Update occasion_bottoms_list = that occasion_bottoms
    
    Update master_tops_list = occasion_tops_list
    Update master_bottoms_list = occasion_bottoms_list
    
3. if Is_Occasion_selected = True and Is_Weather_selected == True:
        master_top_list = []
        for top in occasion_tops:
            if top in weather_tops_list:
                master_top_list.append(top)
        
        master_bottom_list = []
        for bottom in occasion_bottoms:
            if bottom in weather_bottoms_list:
                master_bottom_list.append(bottom)
                
    elif Is_Occasion_selected
        master_top_list = occasion_tops_list
        master_bottom_list = occasion_bottoms_list
        
    elif Is_Weather_selected
        Update master_tops_list = weather_tops_list
        Update master_bottoms_list = weather_bottoms_list
        
        
4. Update top_index = 0
   Update bottom_index = 0
5. Run create_photo(master_top_list[top_index])
   Run create_photo(master_bottom_list[bottom_index]   
6. top_prev_button.config(state = disabled)
   if len(master_top_list) == 1
        top_next_button.config(state = disabled)
7. same as 7 but with the bottoms  
---------------------------------------------------------------------
def weather selected:
declare global top_index
declare global bottom_index
declare global master_top_list
declare global master_bottom_list
declare global Is_Weather_selected
declare global weather_tops_list
declare global weather_bottoms_list
1. Is_Weather_selected = True
2. Update weather_tops_list = that weather_tops
3. Update weather_bottoms_list = that weather_bottoms
4. Check if Is_Occasion_selected = True
    If it is then:
        master_top_list = []
        for top in occasion_tops:
            if top in weather_tops_list:
                master_top_list.append(top)
        
        master_bottom_list = []
        for bottom in occasion_bottoms:
            if bottom in weather_bottoms_list:
                master_bottom_list.append(bottom)
    else:
        master_top_list = weather_tops_list
        master_bottom_list = weather_bottoms_list
        
5. Update top_index = 0
   Update bottom_index = 0
6. Run create_photo(master_top_list[top_index])
   Run create_photo(master_bottom_list[bottom_index]   
7. top_prev_button.config(state = disabled)
   if len(master_top_list) == 1
        top_next_button.config(state = disabled)
8. same as 7 but with the bottoms  
  

'''

root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
