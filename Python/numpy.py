import numpy

# arrays

def arrays(arr):
    a = numpy.array(arr[::-1], float)
    return a

# reshape



arr = numpy.array(list(map(int, input().split())))
print(numpy.reshape(arr, (3,3)))