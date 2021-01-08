a=7
b=9
c=sum((a,b)) #built in function
print(c)

#user defined function
def function1(a,b):
    print("hello you are in function 1 ",a+b)
def function2(a,b):
    """this function will give you the average of two numbers a and b ; this line is not a comment.
    this line is known as DOC_STRING because this line is written as the first line of the
    function and you can acces this line from  print(function2.__doc__)  give a try and see . """
    average=(a+b)/2
    print("Average of ",a ,"and ",b ,"is :",average)

function1(3,8)
print(function1(5,7))
function2(4,6)
print(function2.__doc__)