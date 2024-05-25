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

    ## Importing
    https://docs.python.org/3/reference/import.html
    import random (imports the whole module)
    from handman_words import word_list (imports part of the module)

# Day 8 - Beginner - Function Parameters & Caesar Cipher


def my_function(variable, variable2):
    do this with variable
    print(variable)

variable = parameter
actual value = argument


## positional argumeents
    def function (a, b, c)

can do function (c = 1, b = 2, 1 = 3) to do out of order

# Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction

## Dictionaries
key = word
value = defintiion

{Key: Value}
{"Bug": "An Error in code"
"Python": "A Snake"}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

## Retriving Items from dictionary
print(programming_dictionary["Bug"])

#Add items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create blank dictionary
empty_dictionary = {}

#Wipe existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

##Nesting

{
key: [List]
key2 :{Dictionary}

}

#Nesting a dictionary in a list
#useful if index needed
[{
    Key: [List],    
    Key2: {Dict}
},
{
    Key: Value,
    Key2: Value

# Day 10 - Beginner - Functions with Outputs

def my_function():
    result = 3 * 2
    return result

return gives the outputs

## Function with Outputs
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("FIRST","LAST"))

## Docstrings
documentation for user-crerated functions

def my_function(input)
"""This is my function. There is one input"""

