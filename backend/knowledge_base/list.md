# Lists
- Lists are one of the few collection data types
- Allows duplicate members
- Can be changed after creation (mutable)

## Declaration
- Can be declared in two ways: `my_list = []` or `my_list = list()`

## Accessing Using Index
- Lists are indexed at 0, which means that 0 is the first element
- Also can be accessed using negative index

## Slicing
- Refer back to the string.md for slicing
- Slicing rules are the exact same for lists
- Example:
```python
graphics_cards = ['3080 ti', '4070 ti', '5090']
sliced = [0:1] #returns 3080 ti and 4070 ti
```

## Modifying An Element
- can be done by using:
```python
my_list[0] = 'Changed'
```

## Adding To The List
- append() will add to the list (adds to the end)
- insert(index, your_insertion) 

## Removing From A List
- remove(item): removes an item matching the item
- pop(index): removes the item at the index (note: index is optional, will default to last element on the list) 
- del my_list[index]: used to remove an index or can be delete the list using del my_list
- clear(): method that can be used to clear all of the elements inside of the list
