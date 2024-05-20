# 001 - Day 1 -Beginner - Working with Variables in Python to Manage Data

    ## Naming Rules
    - Can't start with numbers
    - Use underscores to use multiple words


# 002 - Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

    ## Strings
    - Index starts at zero
    - "Hello"[0] --> "H"

    ## Integer
    - 123
    - 123_000 underscores help make it readable

    ## Float
    3.14159

    ## Boolean
    True
    False

    ## Type Check
    type(variable_name) --> int, etc.

    ## Type Conversion
    str()
    int()
    float()

    ## Mathematical Operations
    +   = addition
    -   = subtraction
    *   = multiplication
    /   = Division (results in float)
    **  = To the power of

    ## Order of operations
    Follows PEMDAS

    ## More operations
    //  = Divide & Round to integer
    /=  = Divide byitself
    +=  = Add itself 
    -=  + subtract itself

    ## f-String
    allows mix of data types
    f("your score is {score}, your height is {height}")


# 003 - Day 3 - Beginner - Control Flow and Logical Operators

    ## If format
    if condition:
        do this
    else:
        do this

    ## Operators
    =   = checking something
    ==  = Equal to (if scenario)
    !=  = Not equal to
    %   = modulo

    ## Nested if
    if condition1:
        if subcondistion:
            do this
        else:
            do this
    else:
        do this

    # if / elif /else
    if condition1:
        do a
    elif confition 2:
        do b
    else:
        do this

    ## multiple ifs
    if condition1:
        do A
    if condition 2:
        do B
    if condition 3:
        do C

    ## Multiple Conditions
    and
    or
    not


    ## Lower Case formatting
    combined_names.lower()


    ## Count String Instances
    t = "String".count("t")


# Day 4 - Beginner - Randomisation and Python Lists

www.Askpython.com


## Random Library
import random
random_integer = random.randint(1,10)
random_float = random.random()
random_choice = random.choise(list/string)

## Modules
can import other files/variables
import file_name
print(file_name.variable_name)

## Lists
list = [item1, item2]
always square brackets
always seperated by commas

https://docs.python.org/3/tutorial/datastructures.html

## Nested List
list1 = ["A", "B", "C"]
list2 = ["D", "E", "F"]
list_all = [list1, list2]

# Day 5 - Beginner - Python Loops

    ## Loops
    exeucute the same code mutiple times

    For Loop

    ## For loop with lists
    fruits = ["Apple", "Peach","Pear"]
    for fruit in fruits:
        print(fruit)
    
    ## For Loop with Range
    for number in range(min, max, [optional - step]):
        print(number)
    
# Day 6 - Beginner - Python Functions & Karel

    ## Functions
    https://docs.python.org/3/library/functions.html 
    function()

    repeatable code

    def starts a function

    def my_function():
        print("Hello")
        print("Bye")
    
    my_function()


    ## While Loops

    while something_is_true:
        do something

    
# Day 7 - Beginner - Hangman


    ## Flow chart programming
