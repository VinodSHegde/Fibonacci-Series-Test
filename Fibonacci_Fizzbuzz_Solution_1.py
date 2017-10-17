# Function to Check if the Number is Prime

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
    
# MATH Function for calculation   

import math 
t=int(input())                                        # Read User input for getting the range of series to be generated
a=math.sqrt(5)
for i in range(t+1):                                  # Generating T Fibonacci Number Series
    b=(1+a)/2                                         # To assist calculating Fibonacci Series
    c=(1-a)/2                                         # To assist Calculating Fibonacci Series 
    q=int((1/a)*((math.pow(b,i))-(math.pow(c,i))))    # Calculating Fibonacci Number at i
    if q>1:
        if(isPrime(q)):                               # Checks if the Generated Fib.No is Prime
            print("BuzzFizz")
        elif ((q%3)==0)|((q%5)==0):
            if((q%5)==0):
                print("Fizz",end="")
            if((q%3)==0):
                print ("Buzz", end=""),
            print("",end=" ")
        else:                                         # If Not Prime Number and Not Divisible by 3,5,15
            print("%d"%q)
    else:                                             # To generate initial 3 Fibonacci Numbers to ease further process
        print("%d"%q)
