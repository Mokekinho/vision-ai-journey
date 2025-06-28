import numpy #é usado para gerenciar arrays em python, é uma forma mais rapidas que as listas, portanto é bom para grandes dados

#tutorial https://www.w3schools.com/python/numpy/numpy_intro.asp

def getting_started():
    arr = numpy.array([1,2,3,4,5,6,7,8,9])
    print(arr)
    print(numpy.__version__)



if __name__ == '__main__':
    fun_list = [getting_started]

    for fun in fun_list:
        fun()
        print("-" * 43)

