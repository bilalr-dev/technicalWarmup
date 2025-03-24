"""
Write an algorithm that can display the following

*
**
***
**
*
"""
length = int(input("Enter the length of the triangle : "))
for i in range (1, length + 1):
    for j in range (1,i+1):
        print("*",end="")
    print()
for i in range(length-1,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()