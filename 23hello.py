marks=75 # Initialize the marks variable
if marks>=90:
    print("a")
elif marks>=70:
    print("b")
elif marks>=50:
    print("c")
else:
    print("fail")

day="sunday"         # Initialize the day variable
if day=="sunday" or day=="saturday":
    print("holiday")

age=20  # Initialize the age variable
if age>=18 and age<=20:
    print("major")

i=1 # Initialize the i variable
while i<=10:
    print(i)
    i+=1

fruits=["apple","banana","cherry"]       # Initialize the fruits list
for fruit in fruits:
    print(fruit)

name="sharath" # Initialize the name variable
for me in name:
    print(me)

for i in range(1,10):  # Initialize the range from 1 to 9
    if i == 6:
        break
    print(i)

for i in range (1,10): # Initialize the range from 1 to 9
    if i==6:
        continue
    print(i)


for i in range(1,11):
    for j in range(1,11):
        print(f"i={i} j={j} i*j={i*j}")

for i in range(1,11):  # 1 to 10th table
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")

for i in range(3):
    for j in range(2):
        print("Hello")