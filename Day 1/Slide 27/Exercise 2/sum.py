"""
write an algorithm that asks an 
Integer and calculate the sum from 
0 to this Integer
"""
inputNumber = int(input("Enter a number: "))
sum = 0
for counter in range(0, inputNumber+1):
    sum += counter
print("The sum is: ", sum)
