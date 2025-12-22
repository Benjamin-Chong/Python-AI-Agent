# Strings
- text is a string data type.

## Creating a string
- can be a bunch of texts or one single character
- can be made using a single or double quote or triple quotes

## String concatination
- strings can be connected together.
- Example: connecting PC specs together:
```python
cpu = '7800X3D'
space = ' '
graphics_card = '3080 ti'
pc_specs = cpu + space + graphics_card #if printed, it will print out 7800X3D 3080 ti
```

## Escape sequences
- can be placed anywhere in a string
- \n: creates a new line
- \t: places a tab (8 spaces)
- \\: backlash. will give '\'
- \': single quote. will give '''
- \": double quotes. will give '"'

## String formatting
- can insert information into strings. 
- OLD FORMAT: Example: inserted_string = 'My PC has a %s as its graphics card and a %s as its CPU' %(graphics_card, cpu)
- %s: string
- %d: decimal
- %f: floating point decimal
- %xf: floating point with precision. replace the x with the amount of precision desired.
- NEW FORMAT: Example: inserted_string_new = 'My PC has a {} as its graphics card and a {} as its CPU'.format(graphics_card, cpu)
- f-Strings: Example: f'My PC has a {graphics_card} as its graphics card and a {cpu} as its CPU'

## Unpacking characters
- in python, characters can be accessed by simply using the assignnment operator
- you can also access them by index.

## Slicing characters:
- Example:
```python
graphics_card = '3080 ti'
series = [0:3] #will print only 3080
```
- you can also use the -1 to splice only the last index
- Reversing can be done simply by [::-1]
- you can also skip certain characters [::2]. this will keep every second character (including the first)

### String methods
- useful for making changes to strings
- a few useful are: capitalize(), title(), or swapcase()