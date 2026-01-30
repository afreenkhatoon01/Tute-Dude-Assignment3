#task 1
def factorial(n):
    if n <0:
        print("factorial is not for negative numbers")
    if n==0 or n==-1:
        return 1
    else:
        return n*factorial(n-1)

if __name__=="__main__":
    num=int(input("Enter a number to find its factorial:"))
    result=factorial(num)
    print(f"The factorial of  {num} is {result}")

    #task 2
import math
num=int(input("Enter a number"))
log=math.log10(num)
print(f"The log base 10 of{num} is {log}")
sqrt=math.sqrt(num)
print(f"the square root of {num} is {sqrt}")
sin=math.sin (math.radians(num))
print(f"The sine of{num}is {sin}")