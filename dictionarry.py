d={7.88:'hhhh',55:'jj','a':'kk','[8,0]':'iii' }
print(d.keys())
print(d.values())
d[77]='hhhhhhhhhh'
print(d)
del d['a']
print(d)


sum=0
for i in range(10):
    sum=sum+i
    print(sum)