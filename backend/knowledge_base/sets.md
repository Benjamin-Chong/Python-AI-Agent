# Sets
- Set is a collection of unordered, un-indexed, distinct elements (no duplicates)
- Set allows us to use methods such as union, intersection, etc.

## Declaration
- `my_set = set()`
- OR can create a set with items inside of it. 
- Example:
```python
my_set = {1,2,3,4,5}
```

## Accessing an item
- Can access items using a loop to print out all of the items

## Adding To A Set
- add(your_item): adds one element
- update(your_item1, your_item2): allows you to add multiple elements at once (can be an iterable)

## Removing From A Set
- remove(your_item): will return errors if there is no item found. use try and except beforehand to prevent errors
- pop(): will remove an item in the list

## Clearing Items
- clear(): will clear all of the items in the set 

## Deleting The Entire Set
- del my_set

## Converting a list to a set
- converted = set(old_list)

## Joining sets
- first.union(second): returns a new set
- first.update(second): modifies the original set and does NOT create a new set