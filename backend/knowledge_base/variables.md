# Variables:
- a placeholder for data
- can be named almost anything

## Variable Naming Rules:
- must start with a letter or an underscore (no numbers)
- can only contain letters from the alphabet and 0-9 and _
- always case sensitive
- cannot be python keywords

## Data Types:
- there are many different types of data types. unlike other languages, there is no need to declare data types. they are assumed for you.
- these data types are used to hold different types of data such as numbers, letters, True / False, etc.
- int: used to hold numbers
- string: used to hold characters in a sentence format. must using '' or ""
- boolean: true or false only. usually used to hold the "state" of something
- float: used for decimals like 4.2 or 5.42.
- there are also other types that are more complex like complex, list, dict, tuple, but that is not included in our scope.

### Casting:
- converting a variable from one type to another type. 
- Example: converting an int to a string:
```python
number_in_int = 60
number_in_string = str(number_in_int) #will return '60' (note the quotes around the 60)