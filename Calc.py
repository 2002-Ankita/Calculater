import math
print("\t___CALCULATOR___")
def sum(a,b):
    a = a+b
    return(a)
def sub(a,b):
    if a>b:
        a = a-b
        return(a)
    else:
        b = b-a
        return(b)
def mul(a,b):
    a = a*b
    return(a)
def div(a,b):
    q = a/b
    r = a%b    
    print("\nThe quotient is : %s" %q)
    print("\nThe remainder is : %s" %r)
def sqr(a):
    x = math.sqrt(a)
    return(x)
while True:
    print("\n\nChoose the operation you want to perform : ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SQUARE ROOT")
    print("\n\t6.EXIT")
    choice = int(input('enter your choice : '))
    if choice == 1:
        print("\n\nEnter the two numbers : ")
        num1 = int(input('enter the 1st number : '))
        num2 = int(input('enter the 2nd number : '))
        s=sum(num1,num2)
        print("\nThe sum is : %s"%s)
    elif choice == 2:    
        print("\n\nEnter the two numbers : ")
        num1 = int(input('enter the 1st number : '))
        num2 = int(input('enter the 2nd number : '))
        m=sub(num1,num2)
        print("\nThe difference is : %s"%m)
    elif choice == 3:    
        print("\n\nEnter the two numbers : ")
        num1 = int(input('enter the 1st number : '))
        num2 = int(input('enter the 2nd number : '))
        p=mul(num1,num2)
        print("\nThe product is : %s"%p)
    elif choice == 4:    
        print("\n\nEnter the two numbers : ")
        num1 = int(input('enter the 1st number : '))
        num2 = int(input('enter the 2nd number : '))
        d=div(num1,num2)
        print("\nThe division is : %s"%d)
    elif choice == 5:    
        print("\n\nEnter the numbers : ")
        num1 = int(input('enter the 1st number : '))
        r=sqr(num1)
        print("\nThe square is : %s"%r)
    else: 
        print("\nYou choose to exit.Bye....")
        break    
