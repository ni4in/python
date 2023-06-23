#dictionary filtering : filter all values greater than 1 

d = {"a": 1, "b": 2, "c": 3}

dd = {}
for key,val in d.items():
    if val<2:
        dd[key] = val
print(dd)

#dictionary comprehension 

d=dict((key,value) for key,value in d.items() if value <=1 ) 

#using filter function

f = d.items()

df = filter(lambda x:True if x[1]<= 1 else False ,f)
print(dict(df))


