"""
Even if the recursive function is not 
the most efficient way to calculate the 
factorial of a number, and since we are
studying the functions declaration, I'll
use the recursive method

BEGIN
    FUNCTION Integer factorial(inputNumber as Integer)
        IF inputNumber < 0 THEN
            Write "Please enter a positive number"
            Return -1
        ELSE IF inputNumber = 0 OR inputNumber = 1 THEN
            Return 1
        ELSE
            Return inputNumber * factorial(inputNumber - 1)
        END IF
    END FUNCTION

    DO
        Write "Enter a number: "
        Read inputNumber
        IF inputNumber < 0 THEN
            Write "Please enter a positive number"
        END IF
    WHILE inputNumber < 0

    Write inputNumber, "! = ", factorial(inputNumber)
END


"""
def factorial(inputNumber: int) -> int:
    if inputNumber < 0:
        print("Please enter a positive number")
        return -1
    if inputNumber == 0 or inputNumber == 1:
        return 1
    else:
        return inputNumber * factorial(inputNumber - 1)
while True:
    try:
        inputNumber = int(input("Enter a number: "))
        if inputNumber >= 0:
            break
        else:
            print("Please enter a positive number")
    except ValueError:
        print("Please enter a valid number")

print(f"{inputNumber}! = {factorial(inputNumber)}")