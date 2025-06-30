import numpy #é usado para gerenciar arrays em python, é uma forma mais rápida que as listas, portanto é bom para grandes dados

#tutorial https://www.w3schools.com/python/numpy/numpy_intro.asp

def getting_started():
    arr = numpy.array([1,2,3,4,5,6,7,8,9])
    print(arr)
    print(numpy.__version__)

def creating_arrays():

    arr_list = [
        numpy.array([7, 8, 4, 97, 70, 10]),
        # da para usar coisas que não são lista, como, tuple or any array-like object
        numpy.array((1, 2, 3, 4, 5)),  # () é uma tupla em python
        numpy.array({1, 2, 3, 4, 5, 5}),  # {} é um set em python
        numpy.array([(1, 2), (3, 450), (1, 2)]), #array dentro de array, so funciona se tiver o mesmo tamanho e nao for e tipos diferentes
        numpy.array(42), # array de 0 dimensões, um escalar - 0D
        numpy.array([1,2,3]), # array de 1 dimensão, uma lista normal - 1D
        numpy.array([(1, 2), (3, 450), (1, 2)]), # 2D, e por aí vai
    ]
    for arr in arr_list:
        print(arr)

    arr = ([7, 8, 4, 97, 70, 10])
    print((type(arr))) #array it is called as ndarray, it is an object

    arr = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

    print(arr.ndim) #mostra a dimensão do array

    #it is possible to define the dimension of the array

    arr = numpy.array([1,2,3], ndmin = 5)
    print(arr)
    print(arr.ndim)

def array_indexing():

    arr = numpy.array([1,2,3,4])
    print(arr[0]) #equal to other languages

    print(arr[1] + arr [2])

    arr = numpy.array([[1,2], [3,4]])
    print(arr[0,1]) # que nem coordenada para acessar coisa de matriz
    print(arr[0][1]) # também da para acessar do jeito tradicional

    print(arr[0][-1]) # -1 representa o ultimo elemento
    print(arr[0][-2]) #quanto mais o número diminui anda da esquerda para direita

def array_slicing():
    arr = numpy.array([1,2,3,4,5,6,7,8,9])
    print(arr[1:5]) #we have a piece of the array, [start:end]
    print(arr[1:5:2]) # we have a piece of the array that jumps 2, [start:end:step]

    print(arr[2:]) # if we don't pass the end it'll be the end
    print(arr[:3])
    print(arr[2::2])

    print(arr[-3:-1])#it's ok to use negatives indexes, it works in the same way

    arr = numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    print(arr[1, 1:4]) # for 2D arrays

    arr = numpy.array([1,2,3,4,5])

    print(arr[1:4]) # the last one it is not included
    print(arr[1:])

def data_types():
    """
    Data Types in numpy

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
    """

    arr = numpy.array([1,2,3,4])

    print(arr.dtype) #shows the type of the content of the array

    arr = numpy.array((['avv', 'abb']))
    print(arr.dtype)

    arr = numpy.array([1,2,3,4], dtype= 'S')
    print(arr.dtype)

    #converting data type
    arr = numpy.array([1,2,3,4])
    new_arr = arr.astype('S') #makes a copy of the array with another type

    print(new_arr)
    print(new_arr.dtype)


def copy_as_view():
    arr = numpy.array([1,2,3,4])
    x = arr.copy() #makes a copy of the array, copy the content

    arr[0] = 12321

    print(arr)
    print(x)

    x = arr.view() #copy the reference of the original array

    arr[0] = 3
    print(arr)
    print(x)

    print(arr.base) #returns None because arr owns the data
    print(x.base) #returns the arr array because x doesn't own the data

def array_shape():
    arr = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr.shape) #returns the traditional (i,j), the number of lines, and columns

    arr = numpy.array([1, 2, 3, 4], ndmin=5)

    print(arr)
    print(arr.shape)

def reshaping_array():
    arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    new_arr = arr.reshape(4, 3) # pass the i value and the j value, so it will  create an array with 4 lines, and 3 columns
    print(new_arr)

    new_arr = arr.reshape(2, 3, 2)

    print(new_arr)


    print(arr.reshape(2, 3, 2).base) #it returns arr because arr is the base of the view of the array arr.reshape()

    new_arr[0,0,0] = 10 # if the new array changes, the old changes too
    print(arr)

    new_arr = arr.reshape(2, 2, -1) # the numpy will calculate the last one dimension, you can do that for just one dimension

    print(new_arr)

    #THE NUMBER OF THE (I x J x K...) NEED TO BE EQUAL THE NUMBER OF THE ORIGINAL ELEMENTS

    arr = numpy.array([[1, 2, 3], [4, 5, 6]])

    new_arr = arr.reshape(-1) # creates a single line array

    print(new_arr)

    """"
    Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.
    """

def array_iterating():

    arr = numpy.array([1,2,3,4,5])

    for num in arr:
        print(num)

    arr = numpy.array([[1,2,3],[4,5,6]])

    for i in arr:
        print(i)

    for i in arr:
        for j in i:
            print(j)

    #at this moment it is the same thing as the other languages

    arr = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    for x in numpy.nditer(arr): # an easy way to iterate ofer the array
        print(x)

    arr = numpy.array([1, 2, 3])

    for x in numpy.nditer(arr, flags=['buffered'], op_dtypes=['S']): #op_dtypes changes the type of the element, it is b=necessary tha flag buffer because the function don't change the real value itself
        print(x)

    arr = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    for x in numpy.nditer(arr[:, ::2]): #whith diferente steps, it is the combination with slicing
        print(x)

    arr = numpy.array([1, 2, 3])

    for idx, x in numpy.ndenumerate(arr): #iterates returning the number and the index
        print(idx, x)

    arr = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    for idx, x in numpy.ndenumerate(arr):
        print(idx, x)


def ufunc_intro():

    #stands for universal functions, it vetorize the array, it is faster than simple interation.

    girl_ages = numpy.array([12,15,17,15,20, 22])

    boy_ages = numpy.array([30,27,20,10,11,45])

    print(numpy.add(girl_ages,boy_ages))


def create_own_unfunc():
    def average(x,y):
        return (x+y)/2

    average = numpy.frompyfunc(average, nin = 2 , nout = 1) #nin it is the number of arrays it is necessary for the input, and nout it is the number of arrays that is returned by the function

    girl_ages = numpy.array([12, 15, 17, 15, 20, 22])

    boy_ages = numpy.array([30, 27, 20, 10, 11, 45])

    print(average(girl_ages,boy_ages))

    print(type(average)) # see if it is an ufunc or not
    if type(average) == numpy.ufunc:
        print('average is ufunc')
    else:
        print('average is not ufunc')


def simple_arithmetic_ufunc():
    #I could use arithmetic operators + - * / directly between NumPy arrays

    x = numpy.array([3,3,3])
    y = numpy.array([3,2,2])

    print(x + y)

    print(numpy.add(x,y))
    print(numpy.subtract(y,x))
    print(numpy.multiply(y,x))
    print(numpy.divide(x,y))
    print(numpy.power(x,y))

    print(numpy.remainder(x,y))
    print(numpy.mod(x,y)) #both remainder and mod returns the mod operation

    print(numpy.divmod(x,y)) #returns to arrays, one it is the quotient and other the results

    x = numpy.array([-1,-1,-10])

    print( numpy.absolute(x))

if __name__ == '__main__':
    fun_list = [getting_started, creating_arrays, array_indexing, array_slicing, data_types, copy_as_view, array_shape, reshaping_array, array_iterating, ufunc_intro, create_own_unfunc, simple_arithmetic_ufunc]

    for fun in fun_list:
        fun()
        print("-" * 43)

