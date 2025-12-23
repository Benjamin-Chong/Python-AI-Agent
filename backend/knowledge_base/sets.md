# Sets
- Set is a collection of unordered and unindexed distinct elements (no duplicates)
- Set allows us to use methods such as union, intersection, etc.

## Declaration
- my_set = set()
- or you can create a set with items inside of it. Example:
```python
my_set = {1,2,3,4,5}
```
## Accessing an item
- you can access items using a loop

## Adding to a set
- add(your_item)
- update(your_item1, your_item2): allows you to add multiple elements at once

## Removing from a set
- remove(your_item): will return errors if there is no item found. use try and except beforehand to prevent errors
- pop(): wiill remove an item in the list (random)

## Clearing items
- clear(): will clear all of the items in the set 

## Deleting the entire set
- same as tuples

## Converting a list to a set
- converted = set(old_list)

## Joining sets
- first.union(second)
- first.update(second)