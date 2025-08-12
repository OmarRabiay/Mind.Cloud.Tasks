import numpy
import string

sympols = string.punctuation # Makes a list of symbols
result = "" 
N, M = map(int, input().split()) 

rows = []
for i in range(N): # Reads the input rows
    rows.append(list(input()))

mat = numpy.array(rows) # Converts the list to a numpy array

for j in range(M): # Replaces symbols in each column with spaces
    for i in range(N):
        if mat[i][j] in sympols:
            result += " "
        else:
            result += mat[i][j]

print(result) 