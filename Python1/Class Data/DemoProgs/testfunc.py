"""Functions vs Main Programs

By definition, the main program begins with the first immediately
executable statement.  In this case, that is the statement x = 10.
Regardless of where a function is located in the source code, it is
separate from the main program.  In this example, we are testing the
location of the variable being passed from the main program to the
function.  In the main program, it is referenced simply as x.  In
the function, it is referenced as a_var.

The built-in function id gives us the location in memory of any object.
Here id is used to verify that the location of the variables x and a_var
are exactly the same.  In other words, these two variables point to
the  same object in memory.
"""

def testfunc(a_var):
    print('Func', id(a_var)) # print memory location of variable a_var
    return a_var**2

x = 10
print('Main', id(x)) # print memory location of variable x
z = testfunc(x)
print(z)

