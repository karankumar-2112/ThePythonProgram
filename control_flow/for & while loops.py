"""
For Loop-Programming Questions
1.Write a program to print numbers from 1 to 100.

for i in range(1,100+1):
    print(i)




2.Write a program to print all even numbers between 1 and 50.

for i in range(1,50+1):
    if i%2==0:
        print(i)



3.Write a program to print the sum of first n natural numbers.

n = int(input("Enter n number : "))
add = 0
for num in range(1,n+1):
    add +=num
print("Sum of first n natural number :",add)




4.Write a program to print the multiplication table of a given number.
n = int(input("Enter A Number : "))
for i in range(1,10+1):
    print(n*i)




5.Write a program to print all element of a list

ls  = [21,23,65,47,50]
for el in ls:
    print(el)



6.Write a program to count the number of vowels in a string.

vowel = "aeiou".lower()
count = 0
for i in vowel:
    count+=1
    print(i)
print("Total Number of Vowels :",count)




7.Write a program to find the largest number in a list.

li = [63,54,78,12,51,84,30,43]
largest = 0
for x in li:
    if x>largest:
        largest = x
print(largest)



8.Write a program to print all prime numbers between 1 and 100.

for num in range(2,100+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)



9.Write a program to calculate the factorial of a number using a for loop.

num = int(input("Enter A Number : "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial of",num,":",fact)




10.Write a program to print the reverse of a string using a for loop.

st = "python"
reverse = ""
for i in st[-1:-7:-1]:
    reverse += i
print(reverse)

# another way to solve.
st = "DATA"
reverse = ""
for i in st:
    reverse = i+reverse
print(reverse)




WHILE Loop- Programming Questions
11.Write a program to print numbers from 1 to 50 using a while loop.

a = 1
while a<=50:
    print(a)
    a += 1


12.Write a program to print all odd numbers between 1 to 50.

a = 1
while a<=50:
    if a%2!=0:
        print(a)
    a += 1



13.Write a program to calculate the sum of digits of a number

num = 264
add = 0
a = 1
while a<=num:
    rem = num%10
    add = add+rem
    num = num//10
print(add)




14.Write a program to reverse a number using while loop.

num = int(input("Enter The Number : "))
reverse = 0
a = 1
while a<=num:
    rem = num%10
    reverse = reverse*10+rem
    num = num//10
print("Reverse of num :",reverse)




15.Write a program to find the factorial of a number using while loop.

num = int(input("Enter The Nubmer : "))
fact = 1
a = 1
while a<=num:
    fact = fact*a
    a +=1
print(fact)



16.Write a program to keep taking input from the user until the user enters 0.

num = 1
while num!=0:
    num = int(input("Enter Your Choice : "))
else:
    print("Bye")



17.Write a program to find the largest digits in a number.

num = int(input("Enter A Number : "))
largest = 0
a = 0
while num>a:
    rem = num%10
    if rem>largest:
        largest = rem
    num = num//10
print("Largest :",largest)




18.Write a program to check whether a number is palindrome.

num = int(input("Enter The Number : "))
copy = num
palin = 0
a = 1
while a<=num:
    rem = num%10
    palin = palin*10+rem
    num = num//10
if palin==copy:
    print("Palindrome")
else:
    print("Not Palindrome")



19.Write a program to print the Fibonacci series up to n terms.

num = int(input("Enter The Number : "))
a = 0
b = 1
count = 0
while count<num:
    c = a+b
    print(c)
    a = b
    b = c
    count +=1



20.Write a program to implement a number guessing game using while loop.

gn = int(input("Guess The Number : "))
num = 5
while num!=gn:
    gn = int(input("Wrong! Guess again : "))
else:
    print("Congratulations! You guessed it.")



Mixed (FOR+WHILE)
21.Write a program to print a number pattern using loops.

a = 1
while a<=5:
    for i in range(1,a+1):
        print(i,end="")
    print()
    a = a+1



22. Write a program to count the frequency of each character in a string.
23. Write a program to print all Armstrong numbers between 1 and 1000.
24. Write a program to simulate an ATM menu using a while loop.
25. Write a program to find the GCD of two numbers using loops.
"""

