numb1=int(input("enter number: "))
factorial=1 
if numb1 < 0:
    print("factorial not possible")
elif numb1 == 0:
    print("factorial is 1")
else:
    for i in range(1,numb1+1):
        factorial *= i    
    print(f"The factorial of {numb1} is {factorial}.")