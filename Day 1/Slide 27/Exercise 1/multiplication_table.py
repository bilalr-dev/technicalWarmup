inputNumber = int(input("Enter a number : "))
print(f"Table of {inputNumber}")
for counter in range(1,13):
    print(f"            {inputNumber} x {counter} = {inputNumber*counter}")