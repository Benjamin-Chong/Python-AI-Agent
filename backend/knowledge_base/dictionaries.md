# Dictionary
- Think of a dictionary as a key value pair.
- Each key must be unique

## Declaration
- dictionary = {}
- Can also have inserted values. needs to be in this format: key:value
- Example:
```python
my_dict = {
    'city': 'Los Angeles',
    'state': 'CA'
}
```
## Accessing Dictionary Items
- Can access items by referring to its name, it will return the value associated with the key

## Adding Items To A Dictionary
- your_dictionary[your_key] = 'your_value'
- The same syntax is used to modify or update a key and its value

## Checking For Keys
- Use the in operator to check for the existence of a key
```python
'city' in my_dict  # True
```

## Removing Keys And Values
- pop(your_key): removes the key and its value
- popitem(): removes the last item
- del your_key: removes an item with the key name and its corresponding value

## Converting Into A List
- your_dictionary.items(): changes the dictionary into a list of tuples (one value is the key and one is the pair)

## Clearing a dictionary
- clear()

## Deleting
- same as lists

## Copy
- Can use copy() to create another dictionary without interfering with the older dictionary

## Getting all keys as a list
- keys()

## Getting all the values as a list
- values()