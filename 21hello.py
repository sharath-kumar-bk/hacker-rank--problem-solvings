age=input("enter your age:")
print(type(int(age)))

message=("i like java")
message=message.replace("java","python")
print(message)
print(message.find("p" ))

a=5
b=3
print (a&b)

a=(2,3)
b=(3,5)
c=(a[0]+a[1]+b[0]+b[1])
print(c)

a=[1,2,3,4]
print(a[0:3:-1])

a=(2)
print(a*10)
print(type(a))

a=[1,2,3,4]
print(a*2)
print(1*2+2*2+3*2+4*2)

fruits={"apple","banana","cherry"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)

a={1,2,3,4}
b={3,4,5,6}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)

a={1,2,3,4}
b={3,4,5,6}
print(sum(a))
print(sum(b))
print(sum(a)+sum(b))

a=[1,2,3,4]
a.append(5)
print(a)


a=[1,2,3,4]
print(a.append(5))
print(a)