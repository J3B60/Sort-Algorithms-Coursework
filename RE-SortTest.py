import threading

#///////////////#
#/ Input Array /#
#///////////////#

A = [5]

#///////////////#

B = [] #Primary
C = [] #Secondary
D = [] #Min
E = [] #Max
Bx = [] #Reserved B
Cx = [] #Reserved C
R = [] #Result
n = 0 #Array Element
x = 0 #Number of unsorted elements
N = 0 #Number of NaNs

B = A

for x in range(0, len(A)):
    if (len(B) % 2 != 0):
        Bx += B[len(B)-1]
        del B[len(B)-1]
        Cx += C[len(C)-1]
        del C[len(C)-1]
    if (A[n] != A[n]):
        del A[n]
        N += 1
    else:
        if ():
            
print ('Input Array: ', A)
print ('Output Array: ', R)
print ('Number of NaNs: ', N)
