"""
Dynamic variables in Python are variables that are created and defined at runtime rather than at compile time.
This flexibility allows for more adaptable and general-purpose code, where variable names and types can be
determined during the execution of the program.

Understanding Dynamic Variables
Characteristics:
Runtime Creation: Variables can be created based on conditions or inputs received during program execution.
Flexible Names: Variable names can be constructed dynamically.
Flexible Types: Variable types can change at runtime.

Using globals() and locals()
globals(): This function returns a dictionary representing the global symbol table.
It can be used to create or modify global variables.

locals(): This function returns a dictionary representing the current local symbol table.
It can be used to access local variables within a function. However, modifications to this dictionary
don't affect local variables in the function's scope in CPython.
"""

# create a global variable dynamically
var_name = "dynamic_global_val"
globals()[var_name] = 100


# print(dynamic_global_val) # output=100

# Creating a local variable dynamically
def create_local():
    var_name1 = "dynamic_local_val"
    locals()[var_name1] = 200
    # This print won't work as expected because locals() doesn't modify the actual local scope
    # print(dynamic_local_var)


create_local()

# Using eval with untrusted input can be dangerous as it allows for execution of arbitrary code.
# Dynamically execute expressions
expression = "2+3+7"
result = eval(expression)
print(result)  # output=12

# Dynamically access and modify a variable
var_name2 = "x"
globals()[var_name2] = 10

expression1 = "x+10"
final = eval(expression1)
print(final)  # output=30
