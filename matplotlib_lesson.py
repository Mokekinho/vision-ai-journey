import matplotlib
matplotlib.use('Qt5Agg') # uses pyqt to show
import matplotlib.pyplot as plt

#For this file I'll study matplotlib from https://matplotlib.org/stable/tutorials/index.html

def first_plot():
    plt.plot([2, 2, 2, 4]) #create a line on the plot through the points
    plt.plot([2, 3, 4, 5]) # all points are based on y

    plt.plot([2, 2, 2, 4], [1, 2, 3,4]) # the first array is the x value, and the second is the y value
    #the y starts with the smallest value of the plots
    plt.ylabel('some numbers') #the y label
    plt.xlabel('other numbers')  #the x label
    plt.show() #shows the plot




if __name__ == '__main__':
    print(matplotlib.__version__)
    first_plot()

