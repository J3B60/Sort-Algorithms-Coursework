import threading
import sys

########################
###Change Input Array###
########################

A = [1.4423423,1.664343,23.432344,334.6564,5.31,456.53,54.6432,56,7,56,7,867,86]

########################

n = 0   #Array Element
C = []  #Mins
D = []  #Maxs
B = []  #List of Reserved nums
M = []  #Array Temp Store MIN
N = []  #Array Temp Store MAX
Q = []  #First Reserve
R = []  #Result
MAX = None #Store MAX

if (len(A) == 0):
    print ("Empty String")
    sys.exit()

if (None in A):
    print ("Contains NULL")
    sys.exit()

def Compare(x, y):
    global C
    global D
    if (x > y):
        C += [y]
        D += [x]
    else:           #Including if equal
        C += [x]
        D += [y]
    print ("Min:", C)
    print ("Max:", D)

if (len(A)%2 != 0): #If Odd
    print ("Input Array Odd Length, Last Item Reserved")
    Q += [A[len(A)-1]] #Reserve
    del A[len(A)-1]

while (n != len(A)):  #Thread
        Compare(A[n], A[n+1])
        n += 2

while (len(C) != 1 and len(D) != 1):
    if (len(C)%2 != 0): #If Odd #Only need to check 1 of the lists since symmetrical (For cases such as 30/2=15, 6/2= 3, 10/2=5)
        print ("Processed Array Odd Length, Items Reserved")
        B += [C[len(C)-1]] #Reserve #Thread
        B += [D[len(D)-1]] #Reserve #Thread
        del C[len(C)-1]     #Thread
        del D[len(D)-1]     #Thread
    M = C                   #Thread
    N = D                   #Thread
    n = 0                   #Thread
    C = []                  #Thread
    D = []                  #Thread
    while (n != len(M)):    #Thread
        Compare(M[n], M[n+1])
        Compare(N[n], N[n+1])
        n += 2

R += C
MAX = D[0]
