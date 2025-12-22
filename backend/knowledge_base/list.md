# Lists
- lists are one of the few data types
- allows duplicate members

## Declaration
- list can be declared in two ways: my_list = [] or my_list = list()

## Accessing using index
- lists are indexed at 0, which means that 0 is the first element
- also can be accessed using negative index

## Slicing
- refer back to the string.md for slicing
- slicing rules are the exact same for lists.

## Modifying an  element
- can be done by using:
```python
my_list[0] = 'Changed'
```

## Adding to the list
- append() will add to the list (end)
- insert(index, your_insertion)

## Removing from a list
- remove(item): removes an item matching the item
- pop(index): removes the item at the index (note: index is optional, will default to last element on the list) 
- del my_list[index]: used to remove an index or can be delete the list using del my_list
- clear(): method that can be used to clear all of the elements inside of the list
