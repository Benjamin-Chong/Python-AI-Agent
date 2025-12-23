# Dictionary
- think of a dictionary as a key value pair.
- for example, think of a city and state. both are paired together and are directly related

## Declaration
- dictionary = {}
- can also have inserted values. needs to be in this format: key:value

## Accessing dictionary items
- you can access items by refereing to its name, it will return the value associated with the key

## Adding items to a dictionary
- your_dictionary[your_key] = 'your_value'
- the same syntax is used to modify or update a key and its value

## Checking for keys
- use the in operator to check for the existence of a key

## Removing keys and values
- pop(your_key): removes the key and its value
- popitem(): removes the last item
- del your_key: removes an item with the key name

## Converting into a list
- your_dictionary.items(): changes the dictionary into a list of tuples (one value is the key and one is the pair)

## Clearing a dictionary
- clear()

## Deleting
- same as lists

## Copy
- we can use copy() to create another dictionary without interfering with the older dictionary

## Getting all keys as a list
- keys()

## Getting all the values as a list
- values()