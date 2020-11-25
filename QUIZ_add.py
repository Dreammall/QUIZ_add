#!/usr/bin/env python
# coding: utf-8

# In[81]:


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
for P in plist:
    M = 10 - P
    if(P != L or P != G or M != L or M != G ):
         print("Mの値")
         print(M)
         print("Pの値")
         print(P)
         print("  ")
print("------------------------------")
        
print("Eの値")
for E in range(2,10):
    if(E != L or E != G or E != P or E != M ):
        print(E)
print("------------------------------")

pe1 = P+E+1

if(pe1 >= 10):
    A = pe1-10
    if((A+L+1) >= 10):
        R = A+L+1-10
else:
    A = pe1
    if((A+L) >= 10):
        R = A+L-10

print("Aの値")
if(A != O  or A != N or A != L or A != G or A != P or  A != M or A != E):
    print(A)
print("------------------------------")

print("Rの値")
if(R != O  or R != N or R != L or R != G or R != P and  R != M or R != E or R != A):
    print(R)


# In[ ]:




