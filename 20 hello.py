s=("bharath" , "Sharath " , "charan")
new_s=tuple(
    w[:1] + w[1].upper() + w[2:] for w in s
)
print(new_s)

fruits = ["apple", "banana", "mango"]
print(fruits[0], len(fruits))



fruits = ["apple", "banana", "mango"]
x=fruits.pop()
print(x, fruits)


numbers=[4,5,2,7,9]
numbers.sort()
print( numbers)

numbers=[4,5,2,7,9]
numbers.reverse()
print(numbers)

numbers=[4,5,2,7,9,3,2,4,2]
print(numbers.count(2))

numbers=[4,5,2,7,9,3,2,4,2]
print(numbers.index(4))