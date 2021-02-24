import threading
import math as mt
import statistics as st
#///////////////#
#/ Input Array /#
#///////////////#

A = []

#///////////////#

B = []      #Current Array
C = []      #New Array
pivot = 0   #Current Pivot position
NumP = 0    #Number of Pivots
x = len(A)  #Number of Elements Remaining
n = 0       #Element Position
NoNaN = 0   #Number of NaNs

NaNcounter(A[0])    #Check Selected values are valid/Not_NaN before getting a median
NaNcounter(A[mt.floor(len(A)/2)])
NaNcounter(A[len(A)-1])
pivot = st.median([A[0], A[mt.floor(len(A)/2)], A[len(A)-1]]) #To get a better start pivot
B = A   #Keep A for print
while (NumP != x):
    if (NaNcounter() != 1):
        if (B[n] < B[pivot]):
            C[]
def NaNcounter(x): #~~~Need to Check: Does x work as pass by reference?
    global NoNaN
    global n
    if (x != x):
        NoNaN += 1
        del x
        return 1
    else:
        return 0

###
#def NaNcounter():
#    global n
#    global B
#    global NoNaN
#    if (B[n] != B[n]):
#        NoNaN += 1
#        del B[n]
#        n += 1
###
