from colorama import init
from termcolor import colored
init()
print(colored('instruction !', 'red', 'on_blue' ))
from termcolor import colored
print(colored('operators :-', 'red', attrs=['bold']))
print(colored('for adding = +', 'blue', attrs=['bold']))
print(colored('for subtacting = -', 'blue', attrs=['bold']))
print(colored('for multipling = *', 'blue', attrs=['bold']))
print(colored('for divisoin = /', 'blue', attrs=['bold']))

def add(a,b):
    result=a+b
    print("a+b= ",result)

def sub(a,b):
    result=a-b
    print("a-b= ",result)

def mul(a,b):
    result=a*b
    print("a*b= ",result)

def div(a,b):
    result=a/b
    print("a/b= ",result)

a=int(input("enter the first number(a): "))
b=int(input("enter the second number(b): "))
op=input("enter the opperator: ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("invalid operator")
