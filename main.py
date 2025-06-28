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




if __name__ == '__main__':
    fun_list = [getting_started, creating_arrays]

    for fun in fun_list:
        fun()
        print("-" * 43)

