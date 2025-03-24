"""
Write an algorithm that can display the following

  * 
 ***
*****
     
"""
height = int(input("Enter the number of rows of the triangle : "))
spaces = height - 1
for row in range(1,height+1):
    for column in range(1,spaces+1):
        print(" ",end="")
    spaces -= 1
    for column in range (1, ((2*row)-1)+1):
        print("*",end="")
    print()
