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

# concantenate 

n,m,p = map(int,input().split())
ln = numpy.array([input().split() for i in range(n)], int)
lm = numpy.array([input().split() for i in range(m)], int)
print(numpy.concatenate((ln,lm), axis =0))

# ones and zeros

n = numpy.array(input().split(), int)
z = numpy.zeros((n),dtype = numpy.int)
o = numpy.ones(n, dtype=numpy.int)
print(z)
print(o)

# eye and identity

numpy.set_printoptions(legacy = '1.13')
n , m = map(int,input().split())
 
arr = numpy.eye(n, m, k = 0)
print(arr)


