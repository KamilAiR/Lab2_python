import numpy as np
#-------------------------------------------zad 3--------------------------------------------------------


a = np.arange(1,6)
b = np.arange(5,0, -1) # co 1 w dol
c = np.zeros([3,2], dtype = int) #tablica zer
d=2* np.ones((2,3),  dtype = int) # mnozac ones przez 2 bedziemy miec same 2-ki
e = np.linspace(-90,-70,3,dtype = int)
f=np.array([[10],[10],[10],[10],[10]])


X= np.block([[a],[b]])
B= np.block([[d],[e]])
C= np.block([[c,B]])
D= np.block([[X],[C]])
A= np.block([[D,f]])
#print(A)

#-------------------------------------------zad 4--------------------------------------------------------

B=A[1,:]+A[3,:]
#print(B)

#-------------------------------------------zad 5--------------------------------------------------------

C =(np.max(A,0)) # max w kolumnach
# np.max(A,1)) max w wirszach
#print(C)

#-------------------------------------------zad 6--------------------------------------------------------

D_1 = np.delete(B,0,0)
D= np.delete(D_1,4,0)
#print(D)

#-------------------------------------------zad 7--------------------------------------------------------

for x in range(0,4):
    if D[x] == 4:
        D[x] = 0;
#print(D)

#-------------------------------------------zad 8--------------------------------------------------------

for x in range(0,6):
    if C[x] == np.max(C):
        x_max=x
    elif C[x] == np.min(C):
        x_min=x

E = np.delete(C,[x_min,x_max] , 0)
#print(E)

#-------------------------------------------zad 9--------------------------------------------------------


lista=[]
for i in range(0,5):
    for j in range(0, 6):
        if A[i,j] == np.max(A):
            #w_max= i
            lista.append(i)
        elif A[i,j] == np.min(A):
            #w_min = i
            lista.append(i)

# print(A)
# print("-----------------------")
# print (lista)
# print("-----------------------")
# print(A[lista,:])


#-------------------------------------------zad 10--------------------------------------------------------

#print(D*E)
#print(D@E)

#-------------------------------------------zad 11--------------------------------------------------------

def funkcja(rozmiar):
    Z = np.random.randint(0, 10, [rozmiar, rozmiar])
    slad = 0
    for i in range(0, rozmiar):
        slad = slad + Z[i, i]
    return Z, slad

print(funkcja(5))
