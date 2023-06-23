#Solution 1
s=''
for i in range(0,26): 
    x = chr(ord('a') + i)
    s = s+' '+x 

print(s)  

#Solution 2

import string 

for letter in string.ascii_lowercase:
    print(letter)






