#!/usr/bin/env python
# coding: utf-8

# In[98]:


O = 1
N = 0

for L in range(2,9):
    print("Lの値")
    print(L)
    G = L + 1
    print("Gの値")
    print(G)
    print("  ")
print("------------------------------")
    
    
plist = [2,3,4,6,7,8]
# P ,M は L,G に等しくない
for P in plist:
    M = 10 - P
    if(P != L and M != L and P != G and M != G ):
         print("Mの値")
         print(M)
         print("Pの値")
         print(P)
         print("  ")
print("------------------------------")
        
# E はL,G,P,M に等しくない
print("Eの値")
for E in range(2,10):
    if(E != L and E != G and E != L  and M != G  ):
        print(E)
print("------------------------------")


if((P+E+1) >= 10):
    A = P+E+1-10
    if((A+L+1) >= 10):
        R = A+L+1-10
elif((P+E+1) < 10):
    A = P+E+1
    if((A+L) >= 10):
        R = A+L-10

print("Aの値")

if(A != O  and A != N and A != E):
    print(A)
print("------------------------------")

print("Rの値")
if(R != A):
    print(R)


# In[ ]:




