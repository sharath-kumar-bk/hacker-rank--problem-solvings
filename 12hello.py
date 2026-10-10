pin= "1234"
trials=1
while trials<=3:
    input_pin=input(f"trial {trials} - Enter PIN: ")
    trials+=1
    enter_pin=input("Re-enter PIN: ")

    if input_pin==pin and enter_pin==pin:
         print("correct pin")
         break
    else:
         print("incorrect pin")
else:
     print("stop")
       


i=10
while i>=1:
    print(i)
    i-=1
print("haapy new year")

i=10
while i>=1:
     j=1
     while j<=i:
          print("sharath",end=" ")
          j+=1
     print()
     i-=1

i=10
for i in range(1,11):
     print(i)
print("end")

i=10
for i in range(1,11, 2):
     print(i)
print("end")

name=("sharath", "bharath", "naveen","sunil")
for names in name:
    print(f"{names} " * 2)

name=("sharath", "bharath", "naveen","sunil")
for i in range(len(name)):
    if i%2==0:
        print(f"{name[i]} " * 2)
    else:
        print(f"{name[i]}")

