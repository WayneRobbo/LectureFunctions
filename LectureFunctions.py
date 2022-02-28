

def functionName(param1, param2):
    result = param1 + param2

    return result
#End of function


def say_hello():
    print("hello")
#end if function

#function call
say_hello()
#function call and paramters passed
print(functionName(10, 10))

def factorial_N(j):
    fact = 1
    for i in range(j):
        fact = fact * (i + 1)
    print("N! = ", fact)
#End of function

#Function call
n = int(input("enter factorial number"))
factorial_N(n)