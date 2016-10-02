'''
Created on Feb 28, 2016

@author: niko
'''

import colorsys


MIN_LEVEL = 0
MAX_LEVEL = 100


# http://stackoverflow.com/a/28134008/4419423
# @start : rgb tuple of initial color
# @end   : rgb tuple to fade into
# @time  : length of fade in ms
def fade_color(start, end, time = 1000):

# TODO:  hsv may not be the best. determine best color model for led lighting,
#        calculate step, and loop to fade

    normalized = (start[0] / 255, start[1] / 255, start[2] / 255)

    hsv = colorsys.rgb_to_hsv(*normalized)

    grayed_hsv = (hsv[0], 0.6, hsv[2])

    grayed_rgb = colorsys.hsv_to_rgb(*grayed_hsv)







class Light:

    # basic stuff
    address = None      # physical address of this light source
    name = None         # given name of this light
    description = None  # description of this light
    zone = None         # room in which this light is installed
    id = None           # numeric id of this light

    # level related
    min_level = 0       # minimum level
    max_level = 100     # maximum level
    level = 0           # current light level

    # color stuff

    color = (255, 255, 255)

    # functional stuff
    increment = 'debug'
    decrement = 'debug'
    set_level = 'debug'


    # register new light
    def __init__(self, address, name):

        self.address = address
        self.name = name

        self.get_level()
        self.get_color()

        print("new light registered!")


    # get current light level
    def get_level(self):

        print(self.level)

        # get level from device

        return self.level


    # set light level
    def set_level(self, level):

        self.level = max(min(self.min_level, level), self.max_level)

        self.get_level()


    # increase light level by one step
    def step_bright(self, step = 1):

        self.set_level(self.level + step)

        self.get_level()


    # decrease light level by one step
    def step_dim(self, step = 1):

        self.set_level(self.level - abs(step))

        self.get_level()


    # get current light color
    def get_color(self):

        print(self.color)

        # get color from device

        return self.color


    # set light color
    def set_color(self, rgb, blend = True):

        self.color = rgb




