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
]))

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
print(type(a[2
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

num=[6]
t=1
while num>=1:
   t=num*t
   num-=1
print(t)
