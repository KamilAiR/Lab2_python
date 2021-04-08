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