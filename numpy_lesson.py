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

if __name__ == '__main__':
    fun_list = [getting_started, creating_arrays, array_indexing, array_slicing, data_types]

    for fun in fun_list:
        fun()
        print("-" * 43)

