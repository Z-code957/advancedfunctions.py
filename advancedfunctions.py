#list comprehension
"""num = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in num if x%2==0]
print(even)"""

#dictionary comprehension
"""a = {x:x**2 for x in num }
print(a)"""

"""1.Hands-on Map
Outline:
Write a program to return the addition of numbers of two different lists.
 Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result."""

"""num1 = [1,2,3]
num2 = [4,5,6]
#print(num1 + num2)
add = map(lambda x,y:x+y,num1,num2)
print(list(add))
def square(num2):
    return num2 *num2
result = list(map(square,num2))
print(result)"""

"""2.Zip It!
Outline:
Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together,
 but 2nd list in reverse order 3. elements of two lists zipped into a dictionary"""

"""list1 = [10,20,30,40]
list2 = [50,60,70,80,90]
for i,j in zip(list1,list2[::-1]):
    print(i,j)
for i,j in zip(list1,list2):
    print(i,j)
newdict = {list1:list2 for list1,list2 in zip(list1,list2)}
print("{}".format(newdict))"""

"""3.That’s the exit
Outline:
Write a program where the value of i begins from 1 and goes to 10. 
When the value of i becomes 5, force the interpreter to exit the program."""

for i in range(10):
    if i==5:
        exit()
    print(i)