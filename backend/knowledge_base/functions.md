# Functions
- Used to modularize code and improves readability

## Declaration:
- Example:
```python
def my_function():
    #code1
    #code2
    return ____ #choose what is returned
#calling a function
my_function()
```
- In this version there are no parameters which means that there is no information that is fed into the function

## Function With Parameters
- Functions can be set with parameters in order to 'feed' information into the file.
- Can have one or more parameters
- For example, you create a function that squares a number, you would want to call the function with your desired number.

## Default parameters
- Can set a default if no parameters are given
- Example:
```python
def my_function(x = 5):
    #code1
    #code2
    return ____ #choose what is returned
#calling a function
my_function()
```
- In this example, the function will default to x = 5 if the user does not give a number as a parameter