#5.5
n=int(input("enter a number"))
fact=1
if n <0:
    print("fact does not exist for nrgative number")
elif n==0:
    print("the fact of 0 is 1")
else:
    for i in range(1,n+1):
        fact *=i
    print(f"The factorial of {n} is: {fact}")
