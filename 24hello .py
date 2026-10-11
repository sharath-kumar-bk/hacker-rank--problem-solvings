for i in range(1,5):        #printing numbers from 1 to 5
    print(i)
print("end")


for i in range(1,10):       #printing even and odd numbers from 1 to 10
    print(i)
    if i%2==0:
        print("even")
    else:
        print("odd")

for i in range(1,20,2):     #printing odd numbers from 1 to 20
    print(i)
print("end")

l=[2,4,5,6,4]      #using list comprehension
dl=[num*2 for num in l] 
print(dl)


l=[2,4,5,6,4]       #using list comprehension
dl=[num*num for num in l]
print(dl)


names=["sharath","bharath","charan"] # creating dictionary using for loop
d={}
for i in names:
    d[i] = len(i)
print(d)

names=["sharath","bharath","charan"] # creating dictionary using dictionary comprehension
d={name: len(name) for name in names}
print(d)


names=["sharath","bharath","charan"]        # creating dictionary using dictionary comprehension
marks=[25,50,75]
d={names[i]:marks[i] for i in range(len(names))}
print(d)

names=["sharath","bharath","charan"]        # creating dictionary using zip function
marks=[25,50,75,34]
d={name:mark for name,mark in zip(names,marks)}
print(d)

students_marks={              
    "ravi": 56,
    "sneha": 79,
    "charan": 78
}                                   # values of marks are increased by length of marks
students_marks={student:mark+len(str(mark)) for student,mark in students_marks.items()}
print(students_marks)


cities=["hyderabad","bangalore","chennai"]    # printing index of city name using enumerate function
for index, city in enumerate(cities):
    print(f"{index}: {city}")
print("===============")

cities=["hyderabad","bangalore","chennai"]  # printing index+length of city name  
for index, city in enumerate(cities):
    print(f"{index+len(city)}: {city}")


num=[]              #creating list using list comprehension
num=[i for i in range(1,10)]
print(num)

even_numbers=[]     #creating list of even numbers using list comprehension
even_numbers=[i for i in range(1,20)if i%2==0]
print(even_numbers)

numbers=input("enter the number:").split()
print(numbers*2)

names={
    "sharath":78,
    "bharat": 87,
    "charan": 76
}                                       #
names["ramesh"]=80
print(names)

names={
    "sharath":78,
    "bharat": 87,
    "charan": 76
}
names["bharat"]=80
print(names)

def greet():
    print("hello python")
greet()

i=5
while i<=10:
    i+=1
    print(i)

def tabel(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
tabel(2)
tabel(3)

def func(num):
    print(int(str(num*2)))
func(5)
print(type(func))

def func(num):
    return(int(str(num*2)))
a=100
c=a+func(5)
print(c)