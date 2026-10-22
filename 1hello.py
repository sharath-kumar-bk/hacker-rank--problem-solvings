name="sharath"          
me=[]
me.append((name))
print(me)


name="sharath"          
me=[]
me.append(sorted(name))
print(me)

name="sharath"          
me=[]
me.append(sorted(name))
me[0].reverse()
print(me)

name="sharath" 
name=list(name)
print(name)

name=("sharath")
print(type(name))


name=("sharath",)
print(type(name))

a=[2,3,3,4,3,21,20]
a.reverse()
print(a)

a = [1, 2]
a.append(3)
print(a)

a=[1,2]
a.append((3,))
print(a)
print(type(a))
print(type(a[2]))
print(type(a[2][0]))


def add(a,b,c):
    return(a+c)
c=add(2,4,3)
print(c)
print(type(c))

def func(a):
    print(type(a))
func("sharu")

def func(*a):
    print(type(a))
func()

a=[1,2]
a.append(3)
print(a)


a=[1,2]
a.insert(1,3)
print(a)


a=[1,2]
a.append((3,))
print(type(a[2]))
a=[1,2]
a.extend([3,4,5])
print(a)


a=[1,2]
a.pop(0)
print(a)

cs= lambda a: a*2
print(cs(2))

add=lambda a,b:a+b
print(add(3,4))

num=[2,4,3,5,6,3,7]
num.sort()
print(num)

num=[2,4,3,5,6,3,7]
num.sort(reverse=True)
print(num)

students=[
            {"name":"sharath","marks":34},
            {"name":"bharath","marks":45},
            {"name":"navina","marks":23}
]
for student in students:
    name =student["name"]
    mark =student["marks"]
    print(name,mark)

students=[
            {"name":"sharath","marks":34},
            {"name":"bharath","marks":45},
            {"name":"navina","marks":23}
]
students.sort(key= lambda student:student["marks"])
print(students)

students=[
            {"name":"sharath","marks":34},
            {"name":"bharath","marks":45},
            {"name":"navina","marks":23}
]
students.sort(key= lambda student:student["marks"], reverse=True)
print(students)

num=6
t=1
while num>=1:
   t=num*t
   num-=1
print(t)



x = 0
while x < 100:
    x += 2
    print(x)


    
x = 0
while x < 100:
    print(x)
    x += 2
print("===========")

x=1
while x<100:
    x+=3
print(x)

def factorial(n):
    if n==1:
        return 1
    return n *factorial(n-1)
print(factorial(4))


mul=lambda a,b:a*b
print(mul(2,3))

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
print(sum(5))

def sum(n):
    if n==1:
        return 1   
    print(sum(1))

num=[]
for i in range(1,10):
    num.append(i)
    num.sort(reverse=True)
print(num)

names=["sharath", "bharath","navin" ]
upper_names=[]
for index,name in enumerate(names):
    upper_names.append(name.upper())
print(upper_names)


names=["sharath", "bharath","navin" ]
upper_names=[name.capitalize() for name in names]
print(upper_names)

num=[1,2,3,4,5,6,7]
for i in range(0,len(num)-1,4):
    num[i],num[i+2]=num[i+2],num[i]
print(num)

num=[1,2,3,4,5,6]
for i in range(0,len(num)-1,2):
    num[i],num[i+1]=num[i+1],num[i]
print(num)

num=[1,2,3,4,5,6]
num=[nums*num for nums in num ]
print(num)
print("===============================================================================================================================")

num=[1,2,3,4,5,6]
num=[nums*num for nums in num ]
for i in range(0,len(num)-1,2):
    num[i],num[i+1]=num[i+1],num[i]
print(num)

x=1
y=1
z=1
result=[]
for i in range (x+1):
    for j in range(y+1):
        for k in range(z+1):
            result.append([i,j,k])
print(result)
print('======================================================')

x=4
y=4
result=[]
for i in range(x+1):
    for i in range(y+1):
        result.append(i)
print(result)
print("========================")
x=4
y=4
result=[]
for i in range(x+1):
    for i in range(y+1):
        result.append([i])
print(result)

for i in range(3):
    for j in range(3):
        print(i, j)
