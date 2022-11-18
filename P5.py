def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def main():
    while True:
        print("Enter 1 for addition: ")
        print("Enter 2 for subtraction: ")
        print("Enter 3 for multiplication: ")
        print("Enter 4 for division: ")
        print("Enter 5 for exiting: ")
        c=int(input("Enter your choice: "))
        if c==1:
            a=int(input("Enter number 1: "))
            b=int(input("Enter number 2: "))
            print("Sum= ",addition(a,b))
        elif c==2:
            a=int(input("Enter number 1: "))
            b=int(input("Enter number 2: "))
            print("Difference= ",subtraction(a,b))
        elif c==3:
            a=int(input("Enter number 1: "))
            b=int(input("Enter number 2: "))
            print("Product= ",multiplication(a,b))
        elif c==4:
            a=int(input("Enter number 1: "))
            b=int(input("Enter number 2: "))
            print("Result= ",division(a,b))
        elif c==5:
            break
        else:
            print("Wrong choice")
if __name__=="__main__":
    main()
            
