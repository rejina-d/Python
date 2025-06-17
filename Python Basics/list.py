#list in python
#list is a collection of items which can be of any data type
#list is denoted by square brackets []
#list is ordered collection of items which means that item at index 1 can be accessed directly
#list is changeable i.e we can add or remove items from list

list1= ['Hello', 'world', 'python', 1, 2, 3, 4.5]
list2= ['apple', 'banana', 'cherry']
#print(list1) #this will print the whole list

print(list1[1]) #this will print through index range
print(list1[2:5]) #this will print the first item in the list through range
print(list1[2:])
print(list1[:5])# printing through range from 5

list1.reverse() #this will reverse the list
print(list1) #this will print the whole list in reverse order

list1.append('Appended string')
print(list1) #this will print the whole list after appending

print(len(list1))

#printing using for loop
for item in list1:
    print(item, end= " ") #this will print each item in the list
    
 #sorting   
list2.sort(reverse=True)
print("sorted list:", list2) #this will print the list in reverse order