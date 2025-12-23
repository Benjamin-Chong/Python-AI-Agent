# Variables
- A name that refers to a value stored in memory
- Can be named almost anything, as long as naming rules are followed

## Variable Naming Rules
- Must start with a letter (a–z, A–Z) or an underscore (_)
- Can only contain letters, numbers (0–9), and underscores (_)
- Case-sensitive (`age` and `Age` are different)
- Cannot be Python keywords

## Data Types
- Python has many built-in data types
- Data types do not need to be explicitly declared
- Python infers them automatically
- Different data types represent different kinds of values (numbers, text, True / False, etc.)

- int: used to hold whole numbers (e.g., -3, 0, 42)
- string: used to hold text data and must be enclosed in single quotes ('') or double quotes ("")
- boolean: represents one of two values — True or False and is commonly used for conditions or state
- float: used to represent decimal (floating-point)

- Other built-in types exist (e.g., list, dict, tuple), but they are covered separately

### Casting
- Converting a value from one data type to another
- Example: converting an int to a string:

```python
number_in_int = 60
number_in_string = str(number_in_int)  # Will return '60'
```