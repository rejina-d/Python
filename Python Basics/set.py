#sets in python
#set is an unordered collection of unique elements
#set is mutable

set1= {"hello","python",2,3,99,"hello"}
set2= {1,2,3,4,5}
print(set1)

#adding data to set
set1.add("551")
print(set1)

#union in set
set3= set1.union(set2)
print("union:", set3)
print("union:", set1 | set2)

#intersection in set
set4= set1.intersection(set2)
print("Intersection:", set4)
print("Intersection:", set1 & set2)

#difference in set
set5= set1.difference(set2)
print("difference:", set5)
print("difference:", set1 - set2)

#symmetric diff
set6= set1.symmetric_difference(set2)
print("symmetric diff:", set6)