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

a=[1,2]
a.append((3,))
print(type(a[2]))

def add(a,b,c):
    return(a+c)
c=add(2,4,3)
print(c)
print(type(c))

def func(a):
    print(type(a))
func("sharu")

def func(a,):
    print(type(a))
func()