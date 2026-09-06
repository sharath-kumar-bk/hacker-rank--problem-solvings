from unicodedata import name


def add(*numbers):
   return sum(numbers)

print(add(2,3,4,5,6))

def student_info(**details):
   for key,value in details.items():
      print(f"{key}: {value}")
student_info(name="sharath",age=25,marks=75,city="bangalore")

def add(a,b):
   return a+b
print(add(2,3))

add=lambda a,b: a+b
print(add(2,3))

double=lambda x: x*2
print(double(5))

student=[
   {"name":"sharath", "marks":75},
   {"name":"bharath", "marks":50},
   {"name":"charan", "marks":80}
]
student.sort(key=lambda x: x["marks"], reverse=True)
print(student)

def add(a,b):
   print(a+b)
   add(2,3)
   
def num(n):
   print(n)
   num(n-1)
   
num(5)