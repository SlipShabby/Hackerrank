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


# array mathematics

n, m = map(int, input().split())
a, b = (numpy.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep = '\n')


# floor, ceil, rint

numpy.set_printoptions(legacy = '1.13')
arr = numpy.array(input().split(), float)

print(numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr),sep='\n')


# sum and prod 

n, m = map(int,input().split())
arr = numpy.array([input().split() for _ in range(n)],int)
print(numpy.prod(numpy.sum(arr,axis=0), axis = 0))


# min and max

n,m = map(int, input().split())
arr = numpy.array([input().split() for i in range(n)],int)
print(numpy.max(numpy.min(arr,axis = 1)))


# mean, var and std

# numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
arr = numpy.array([input().split() for i in range(n)], float)
print(numpy.mean(arr, axis = 1), numpy.var(arr,axis = 0), round(numpy.std(arr),11), sep='\n')

# dot and cross

n = int(input())
a = numpy.array([input().split() for i in range(n)],int)
b = numpy.array([input().split() for i in range(n)],int)
print(numpy.dot(a,b))

# inner and outer

a, b = numpy.array([input().split() for i in range(2)],int)
print(numpy.inner(a,b), numpy.outer(a,b), sep = '\n')


