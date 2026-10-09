for i in range(1,5):
    print(i)
print("end")


for i in range(1,10):
    print(i)
    if i%2==0:
        print("even")
    else:
        print("odd")

for i in range(1,20,2):
    print(i)
print("end")

l=[2,4,5,6,4]
dl=[]
for num in l:
    dl.append(num*2)
print(dl)


l=[2,4,5,6,4]
dl=[]
for num in l:
    print(num*num)


names=["sharath","bharath","charan"]
d={}
for i in names:
    d[i] = len(i)
print(d)

names=["sharath","bharath","charan"]
d={name: len(name) for name in names}
print(d)


names=["sharath","bharath","charan"]
marks=[25,50,75]
d={names[i]:marks[i] for i in range(len(names))}
print(d)

names=["sharath","bharath","charan"]
marks=[25,50,75,34]
d={name:mark for name,mark in zip(names,marks)}
print(d)