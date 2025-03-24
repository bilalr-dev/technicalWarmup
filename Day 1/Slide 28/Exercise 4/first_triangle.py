"""
Write an algorithm that can display the following

*
**
***
****
*****
"""
#I used the first method because it has a better 
#space complexity of 𝑂(1)
height = int(input("Enter the height of the triangle : "))
for i in range(1, height + 1):
    for j in range(1, i+1):
        print("*", end="")
    print()