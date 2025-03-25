"""
Functions are declared using the following syntax:

Function Integer factorial(input as Integer)
    Variable ... //local variables here
    BeginFunction
        ... // write the code here
        Return ... //return an integer value
    EndFunction
"""

"""
The equivalent in python :
"""
def myFunction(input: int) -> int:
    # Here we declare local variables
    localVariable = 0  # Example initialization
    
    # Here we write the code that performs the function's task
    for i in range(1, input + 1):  # Example loop to calculate sum or factorial
        localVariable += i  # Example operation (sum in this case)
    
    # Return the result of the function
    return localVariable  # Returning the computed value


