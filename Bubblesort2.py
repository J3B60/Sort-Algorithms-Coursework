import random as rd
#/ Bubble Sort /#

#///////////////#
#/ Input Array /#
#///////////////#

A = ['P/\R',3,complex(3,6),float('NaN'),'g',float('inf'),4.32]

#///////////////#
print ("Input Array: ", A)
n = len(A)  #Number of elements remaining
swapped = False
i = 1       #Element in Array
NoNaN = 0   #Number of NaNs
R = A      #Result Array
while (n > 0):
    swapped = False
    while i < n:
        if R[i] != R[i]:
            del R[i]
            n -= 1
            NoNaN += 1 
        elif R[i-1] != R[i-1]:
            del R[i-1]
            n -= 1
            NoNaN += 1 
        else:
            if R[i-1] > R[i]:
                R[i], R[i-1] = R[i-1], R[i]
                swapped = True
            else:
                i += 1
    i = 1
    n -= 1
print ("Output Array: ", R)
print ("Number of NaNs: ", NoNaN)
