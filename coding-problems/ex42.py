"""
Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)
"""

a = [1, 2, 3]
b = (4, 5, 6)

for i in range(len(a)):
    print(f"{a[i]+b[i]}")


#using zip 

for i,j in zip(a,b):
    print(i+j)