# Functions
- used to modularize code and improves readibility

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
- in this version there are no parameters which means that there is no information that is fed into the function

## Function with parameters
- functions can be set with parameters in order to 'feed' information into the file.
- can have one or more parameters
- for example, you create a function that squares a number, you would want to call the function with your desired number.

## Default parameters
- we can set a default if no parameters are given
- Example:
```python
def my_function(x = 5):
    #code1
    #code2
    return ____ #choose what is returned
#calling a function
my_function()
```
- in this example, the function will default to x = 5 if the user does not give a number as a parameter