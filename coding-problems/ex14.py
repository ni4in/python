#removing duplicates

a = ["1", 1, "1", 2]

print('solution 1 is {}'.format(list(set(a))))


#sol2 

from collections import OrderedDict

t = (OrderedDict.fromkeys(a))
print('solution 2 is {}'.format(list(a)))

#sol 3
new_list = []
for x in a:
    for y in a:
        if (x==y):
            continue
    new_list.append(x)

print('sol 3 is {}'.format(new_list))

#sol 4 

new_list = []
for x in a:
    if x not in new_list:
        new_list.append(x)

print('sol 4 is {}'.format(new_list))



