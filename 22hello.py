student={
    "name":"sharath",
    "age":"20",
    "college":"vvit",
    "branch":"cse-aiml"
}
print(student)   #accessing dictionory

student={
    "name":"sharath",
    "age":"20",
    "college":"vvit",
    "branch":"cse-aiml"
}

print(len(student))   #length of dictionary

print(student["name"])  #acccessung using key

student["year"]="1st"    #adding new key value pair
print(student) 

student.pop("age")            # removing a key-value pair
print(student)

del student["branch"]            # removing a key-value pair
print(student)

print(student.keys())   #printing all keys

print("name" in student)   #checking if key is present or not

print(student.values())   #printing all values

print((student.items()))   #printing all key-value pairs

print(student.get("name"))   #accessing value using get method

print(type(student))

student.clear()         #removing all key-value pairs
print(student)

