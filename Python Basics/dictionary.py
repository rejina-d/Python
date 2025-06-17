#Dictionary in python
#A dictionary is a collection of key-value pairs
#It is mutable, meaning it can be changed after it is created

dict1={
    "name": "John",
    "age": 30,
    "city": "New York"
}

print (dict1) #printing the directory
print (dict1.keys()) #printing keys of dictionary
print (dict1.values()) #printing values of dictionary
print (dict1.items()) #printing key-value pairs of dictionary
print (dict1["age"])


for item in dict1.items():
    print(item) #printing items of dictionary
    
for keys, values in dict1.items():
    print(f"{keys}: {values}") #printing items of dictionary
    

#updating in dictionary
dict1["age"]=31

#updating values with update function
dict1.update({"age":31,"city":"Los Angeles"})

#get function in dictionary
print(dict1.get("name")) 

#set default function
dict.setdefault("Place:", "New York")

print("Dictionary after updating", dict1)

