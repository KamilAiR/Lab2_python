import numpy as np

arr = np.array([1, 2, 3, 4, 5]) #tablice
print(arr)

A = np.array([[1, 2, 3], [7, 8, 9]])
print(A)

A = np.array([[1, 2, 3],
              [7, 8, 9]])
print(A)

A = np.array([[1, 2, \
    3],
    [7, 8, 9]])
print(A)

v = np.arange(1,7)
print(v,"\n")

v = np.arange(-2,7)
print(v,"\n")

v = np.arange(1,10,3) # ostatni element mowi o skoku
print(v,"\n")

v = np.arange(1,10.1,3)
print(v,"\n")

v = np.arange(1,11,3)
print(v,"\n")

v = np.arange(1,2,0.1)
print(v,"\n")


v = np.linspace(1,3,4)
print(v)
v = np.linspace(1,10,4) # ostatni element mówi o tym ile ma byc elementow w liscie
print(v)

X = np.ones((2,3)) #macierz samych 1
Y = np.zeros((2,3,4)) # 2 talibce wypelnione zeram o wymiarach 3 na 4
Z = np.eye(2) #macierz z jedynkami na przekatnej
Q = np.random.rand(2,5) # macierz liczb losowych o wymiarach 2 na 5
print(Q)

print(X,"\n\n",Y,"\n\n",Z,"\n\n",Q)



#sklejanie
print( 'sklejanie')
A = np.ones((2,4))
X = np.zeros((2,2))
Z = np.eye((2))
U = np.block([[A], [X,Z]])

print(U)

V = np.block([[
    np.block([
        np.block([[np.linspace(1,3,3)],
                  [np.zeros((2,3))]])
        ,np.ones((3,1))])
            ],
    [np.array([100, 3, 1/2, 0.333])]] )
print(V)

#odwolywanie sie do elementow tablicy
print( V[0,2] )
print( V[3,0] )
print( V[3,3] )
print( V[-1,-1] )
print( V[-4,-3] )
print( V[3,:] )
print( V[:,2] )
print( V[3,0:3] )
print( V[np.ix_([0,2,3],[0,-1])] )
print( V[3] )

#usuwanie fragmentow macierzy i tablic

Q = np.delete(V, 2, 0)
print(Q)
Q = np.delete(V, 2, 1)
print(Q)

# sprawdzanie rozmiarow tablic

np.size(v)
np.shape(v)

# Operacje na macierzach

A = np.array([[1, 0, 0],[2, 3, -1],[0, 7, 2]] )
B = np.array([[1, 2, 3],[-1, 5, 2],[2, 2, 2]] )
print( A+B )
print( A-B )
print( A+2 )
print( 2*A )

MM1 = A@B #mnozenie macierzowe
print(MM1)
MM2 = B@A
print(MM2)

MT1 = A*B #mnozenie tablicowe
print(MT1)
MT2 = B*A
print(MT2)

DT1 = A/B # dzielenie tablicowe
print(DT1)

C = np.linalg.solve(A,MM1) #dzeielenie macierzowe
print(C) # porownaj z macierza B
x = np.ones((3,1))
b =  A@x
y = np.linalg.solve(A,b)
print(y)

