import numpy

# arrays

def arrays(arr):
    a = numpy.array(arr[::-1], float)
    return a

# reshape

arr = numpy.array(list(map(int, input().split())))
print(numpy.reshape(arr, (3,3)))

# transpose and flatten

n, m= list(map(int, input().split()))
l = numpy.array([input().strip().split() for i in range(n)], int)
arr = numpy.transpose(l)
print(arr)
print(l.flatten())

