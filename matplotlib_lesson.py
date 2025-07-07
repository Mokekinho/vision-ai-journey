import matplotlib
matplotlib.use('Qt5Agg') # uses pyqt to show
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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


def keyword_strings():
    data = {'a': np.arange(50), # Eixo X
            'c': np.random.randint(0, 50, 50), # 50 Cores dos pontos
            'd': np.random.randn(50)} # tamanho das bolinhas
    data['b'] = data['a'] + 10 * np.random.randn(50) # eixo Y
    data['d'] = np.abs(data['d']) * 100
    #Fois criado uma variedade de arrays


    #plot é grafico de linhas e o scatter é grafico de dispersão
    plt.scatter('a', 'b', c='c', s='d', data=data) # ao passar data = data é o mesmo que fazer plt.scatter(data['a'], data['b'], c=data['c'], s=data['d'])
    plt.xlabel('entry a')
    plt.ylabel('entry b')


    #usando pandas

    df = pd.DataFrame({
        'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.abs(np.random.randn(50)) * 100
    })

    # Coluna 'b' com ruído
    df['b'] = df['a'] + 10 * np.random.randn(50)

    # Plotando
    plt.scatter('a', 'b', c='c', s='d', data=df)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.title('Gráfico de dispersão com pandas')
    plt.show()


if __name__ == '__main__':
    print(matplotlib.__version__)
    keyword_strings()
