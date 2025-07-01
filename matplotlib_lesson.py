import matplotlib
matplotlib.use('Qt5Agg') # uses pyqt to show
import matplotlib.pyplot as plt
import numpy as np

#For this file I'll study matplotlib from https://matplotlib.org/stable/tutorials/index.html

def first_plot():
    plt.plot([2, 2, 2, 4]) #create a line on the plot through the points
    plt.plot([2, 3, 4, 5]) # all points are based on y

    plt.plot([2, 2, 2, 4], [1, 2, 3,4]) # the first array is the x value, and the second is the y value
    #the y starts with the smallest value of the plots
    plt.ylabel('some numbers') #the y label
    plt.xlabel('other numbers')  #the x label
    plt.show() #shows the plot


def plot_style():
    """
    Colors:

    'b'	blue
    'g'	green
    'r'	red
    'c'	cyan
    'm'	magenta
    'y'	yellow
    'k'	black
    'w'	white

    Line Styles:

    '-'	solid line
    '--'	dashed line
    '-.'	dash-dot line
    ':'	    dotted line

    Marker Styles:

    '.'	point
    'o'	circle
    's'	square
    '^'	triangle up
    'v'	triangle down
    '<'	triangle left
    '>'	triangle right
    'd'	diamond
    'x'	x
    '+'	plus
    'p'	pentagon
    '*'	star
"""

    plt.plot([1,2,3],[3,2,1], 'r.')
    plt.plot([1, 2, 3], [4, 3, 2], 'm--p')

    plt.plot([1,2,1,1],[0,1,2,0], 'k')



    t = np.arange(0., 5., 0.2) # all lists are converted for np array, so, it is fair use np array directly
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^') # it 's posible  plot multiple lines in the same call
    plt.show()



if __name__ == '__main__':
    print(matplotlib.__version__)
    plot_style()
