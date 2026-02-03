print("------MENUS-----")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponentiation")
print("6.Modulex")
print("Enter your choice")
choice=int(input("Enter your choice:"))
if choice==1:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    addition()
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def exponent(a,b):
    return a**b
def modulex(a,b):
    return a%b

