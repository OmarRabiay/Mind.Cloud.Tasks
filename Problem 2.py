import numpy

K, M = map(int, input().split())
lists = []
maxs = []
squares = []
for i in range(K):  # Reads the lists and stores them
    a = numpy.array(list(map(int, input().split())))
    lists.append(a)
for i in range(K): # Finds the maximum of each list
    max = numpy.max(lists[i])
    maxs.append(max)
for i in range(K): # Calculates the square of each maximum
    square = maxs[i] * maxs[i]
    squares.append(square)
result = numpy.sum(squares) % M # Calculates the result
print(result)

