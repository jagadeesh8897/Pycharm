def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "B is zero enter value other than 0"
a=int(input("enter A number: "))
b=int(input("Enter B Number: "))
print(divide(a,b))