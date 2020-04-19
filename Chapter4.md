1. What is []?
The empty list value, which is a list that contains no items. This is similar to how ' ' is the empty string value.
2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
spam[2] = 'hello'
For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
3. What does spam[int(int('3' * 2) // 11)] evaluate to?
'd'
4. What does spam[-1] evaluate to?
'd'
5. What does spam[:2] evaluate to?
['a', 'b']
For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
6. What does bacon.index('cat') evaluate to?
1
7. What does bacon.append(99) make the list value in bacon look like?
[3.14, 'cat', 11, 'cat', True, 99]
8. What does bacon.remove('cat') make the list value in bacon look like?
[3.14, 'cat', 11, 'cat', True]
9. What are the operators for list concatenation and list replication?
The operator for list concatenation is +, while the operator for replication is *.
10. What is the difference between the append() and insert() list methods?
While append() will add values only to the end of a list, insert () can add them anywhere in the list.
11. What are two ways to remove values from a list?
The del statement and the remove() list method are two ways to remove value from a list.
12. Name a few ways that list values are similar to string values.
Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.
13. What is the difference between lists and tuples?
Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ) , while lists use the square brackets, [ and ].
14. How do you type the tuple value that has just the integer value 42 in it?
(42,)
15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
The tuple() and list() functions, respectively
16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
They contain references to list values.
17. What is the difference between copy.copy() and copy.deepcopy()?
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.
