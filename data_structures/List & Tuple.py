"""
Python Programming Questions-LIST
Basic Level
1.Write a python program to create a list of integers and print it's elements.

ls = [35,22,10,64,55]
print(ls)



2.Write a program to find the sum and averages of all elements in a list.

ls = [35,22,10,64,55]
print( sum(ls) )
print( sum(ls)/len(ls) )



3.Write a program to find the largest and smallest element in a list.

ls = [35,22,10,64,55]
print( max(ls) )
print( min(ls) )



4.Write a python program to count the number of elements in a list without using len().

ls = [35,22,10,64,55]
count = 0
for e in ls:
    count +=1
print("Total number of elements :",count)



5.Write a program to reverse a list without using built-in functions

ls = [35,22,10,64,55]
print( ls[::-1])



6.Write a program to check if an element exists in a list.

ls = [35,22,10,64,55]
el = 22
for e in ls:
    if e==el:
        print("Exists")



7.Write a python program to remove duplicate elements from a list.

ls = [78,55,22,35,10,64,22,55]
ls2 = []
for e in ls:
    if e not in ls2:
        ls2.append(e)

print(ls2)
        


8.Write a program to sort a list in ascending and descending order.

ls = [35,62,40,10,77]
ls.sort()
print(ls)
ls.sort(reverse=True)
print(ls)



Intermediat Level
9.Write a program to merge two lists and remove duplicates.

ls = [35,41,20,60,12]
ls2 = [88,25,41,55,20]
ls.extend(ls2)
print(ls)
unique = []
for e in ls:
    if e not in unique:
        unique.append(e)
print(unique)




10.Write a program to find common elements between two lists.

ls = [36,52,41,78,94,10,57]
ls2 = [94,64,20,41,33,18,52]
for e in ls:
    if e in ls2:
        print(e)



11.Write a program to split a list into even and odd numbers.

ls = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for e in ls:
    if e%2==0:
        even.append(e)
    else:
        odd.append(e)
print("Even :",even,"\nOdd :",odd)


12.Write a program to rotate a list by n positions.
# Left-Rotation
ls = [10,20,30,40,50]
n = int(input("Enter The n Position : "))
for i in range(n):
    ls.insert(len(ls),ls[0])
    ls.pop(0)
print(ls)


# Right-Rotation
ls = [10,20,30,40,50]
n = int(input("Enter The n Position : "))
for i in range(n):
    ls.insert(0,ls[len(ls)-1])
    ls.pop(len(ls)-1)
print(ls)



13.Write a python program to find the second largest number in a list.

ls = [35,24,69,52,20,45]
ln1 = 0
ln2 = 0
for e in ls:
    if e>ln1:
        ln2 = ln1
        ln1 = e
    elif e>ln2 and e!=ln1:
        ln2 = e
print("Second Largest Number :",ln2)



14.Write a program to flatten a nasted list.

ls = [1,2,3,[4,5,6],7,8]
flatten = []
for e in ls:
    if isinstance(e,list):
        flatten.extend(e)
    else:
        flatten.append(e)
print(flatten)
    

15.Write a progaram to count frequency of each element in a list.

ls = [15,47,55,35,20,10,64,20,55]
freq = []
for e in ls:
    if e not in freq:
        freq.append(e)
print(freq)
for e in freq:
    print(e,":",ls.count(e))



16. Write a program to replace all negative numbers with zero in a list.

ls = [-1,2,8,-9,4,-6,5,-3,7]
ls2 = []
for e in ls:
    if e<0:
        ls2.append(0)
    else:
        ls2.append(e)
print(ls2)



Advanced Level
17.Write a program to remove all occurrences of a given element from a list

ls = [35,10,22,14,66,14,75,35,10]
print(ls)
ls2 = []
ge = int(input("Enter The Element to Remove : "))
for e in ls:
    if e!=ge:
        ls2.append(e)
print(ls2)



18. Write a program to check if a list is a palindrome.

ls = [1,2,3,2,1]
palin = []
for e in ls[::-1]:
    palin.append(e)
if palin==ls:
    print("Palindrome")
else:
    print("Not Palindrome")



19. Write a Python program to find missing numbers in a given list of consecutive integers.

ls = [1,2,4,5,6,7,8,10]  # it will work (but this is hard code)
missing = []
for e in range(1,11):
    if e not in ls:
        missing.append(e)
print("Missing Number :",missing)


ls = [1,2,4,5,6,7,8,10]   # (flexible code will fit in any list)
missing = []
for e in range(ls[0],ls[-1]+1):
    if e not in ls:
        missing.append(e)
print("Missing Number :",missing)



20. Write a program to perform element-wise addition of two lists. 

ls = [10,20,30,40,50]
ls2 = [5,5,5,5,5]
add = []
for i in range(len(ls)):
    add.append(ls[i]+ls2[i])
print(add)



21. Write a Python program to find the longest increasing subsequence in a list. 
22. Write a program to group elements based on frequency.

ls = [10,20,30,30,10,10,40,20,20,50]
print(ls)
blk = []
group = []
for e in ls:
    if e not in blk:
        blk.append(e)
        group.extend([e]*ls.count(e))
print(group)





#Python Programming Question - TUPLE
Basic Level

1.Write a Python program to create a tuple and print its elements.

t = (35,10,22,65,45)
print(t)



2.Write a program to find the length of a tuple.

t = (35,10,22,65,45)
print( len(t) )



3. Write a program to find the maximum and minimum element in tuple.

t = (35,10,22,65,45)
print( max(t) )
print( min(t) )



4.Write a program to convert a tuple into a list.

t = (14,78,95,25,55,20,98)
ls = list(t)
print(ls)



5.Write a program to check if an element exists in a tuple.

el = 10
t = (36,45,84,78,21,54,96)
if el in t:
    print("Exists")
else:
    print("Doesn't exists")




6.Write a program to count occurrences of an element in a tuple.

t = (12,52,41,78,96,33,22,33,33)
print(t.count(33))

# another way
t = (12,52,41,78,96,33,22,33,33)
element = int(input("Enter The Element : "))
count = 0
for e in t:
    if e==element:
        count += 1
print("Occurrences of ",element,"is",count)




Intermediat Level
7.Write a program to slice a tuple and display result.

t = (36,52,41,10,28,55,78)
print(t[1:6])



8.Write a program to find repeated elements in a tuple. 

t = (10,20,50,30,40,10,50)
repeated = []
for e in t:
    if e not in repeated and t.count(e)>1:
        repeated.append(e)
repeated_tuple = tuple(repeated)
print(repeated_tuple)



9.Write a program to merge two tuples. 

t1 = (10,20,30,40,50)
t2 = (60,70,80,90)
merge = t1+t2
print(merge)

# another way
t1 = (10,20,30,40,50)
t2 = (60,70,80,90)
l1 = list(t1)
l2 = list(t2)
l1.extend(l2)
print(tuple(l1))



10.Write a program to unpack elements of a tuple into variables. 

t = (10,20,30,40)
a,b,c,d = t
print(a)
print(b)
print(c)
print(d)



11.Write a Python program to sort a tuple. 

t = (35,10,20,64,45)
ls = list(t)
ls.sort()
t = tuple(ls)
print(t)



12. Write a program to convert a list of tuples into a dictionary.

ls = [(1,"Apple"),(2,'Banana'),(3,'Orange'),(4,'Guava')]
dictionary = dict(ls)
print(dictionary)



Advanced Level
13. Write a program to find the index of an element in a tuple. 

t = (12,52,41,78,63,51)
elmt = int(input("Enter The Element to Know Index Number : "))
if elmt in t:
    print(t.index(elmt))
else:
    print("Element not found!")



14. Write a program to remove an element from a tuple (without directly modifying it).

t = (10,20,30,40,50)
etr = int(input("Enter The Element to Remove : "))
temp_list = []
for e in t:
    if e!=etr:
        temp_list.append(e)
new_tuple = tuple(temp_list)
print(new_tuple)   



15. Write a program to find common elements between two tuples. 

t = (35,41,20,78,12)
t2 = (62,10,41,22,12)
common = []
for e in t:
    if e not in common and e in t2:
        common.append(e)

print(common)
    
        

16.Write a Python program to check if a tuple is a palindrome.     

t = (10,20,30,20,10)
if t==t[::-1]:
    print("Palindrome Tuple")
else:
    print("Not Palindrome Tuple")



17.Write a program to find the element with maximum frequency in a tuple.

t = (1,6,3,4,5,7,4,1,5,5,6)
temp = []
maxx = 0
value = 0
for e in t:
    if e not in temp:
        temp.append(e)
        if t.count(e)>maxx:
            maxx = t.count(e)
            value = e
print("The Element",value,"Frequence is",maxx)



18.Write a program to create a nested tuple and access its elements.

nasted_tuple = (1,2,3,(4,5,6),7,8,9)
print(nasted_tuple[0])
print(nasted_tuple[1])
print(nasted_tuple[2])
print(nasted_tuple[3])
print(nasted_tuple[3][0])
print(nasted_tuple[3][1])
print(nasted_tuple[3][2])
print(nasted_tuple[4])
print(nasted_tuple[5])
print(nasted_tuple[6])
"""

