# Problem 6. Union and Intersection.

For this problem, it was required to use a linked list as a data structure
to return two lists, providing the set's union and intersection functions.

In order to optimise the algorithm, I created a helper function sort_list()
which returns a sorted list removing duplicate elements.

**sort_list(list) helper function**
I use this function to sort the list passed as arguments in both 
union and intersection functions.
I also used head and tail pointers to create the sorted list which
provides a complexity of Big O of O(1) when elements need to be added that
are either smaller than the first item in the list or higher than the last
item to the list.
For the elements we need to insert in the sorted list that are between
the first and last element of the sorted link, we need to iterate to find
the place to insert it.

The complexity of the Big O for the worst case scenario for the sort_list()
funcion is O(n) * O(n-2), so O(n*n)
 O(n) is to go through the original list
 O(n-2) is to go through the sorted list to insert elements in between
 head and tail. Minus 2 are the elements that will be inserted directly 
 in the sorted list 
The space complexity for the worst case scenario would be O(n) for the origin list
 and O(n) for the new sorted list, so O(2*n) which is O(n)
 
**Union function analysis**
The union function will get two lists which will be sorted by sort_list()
and then both new lists will be compared each other to create a new list
with the elements combined in both list.
 
The complexity of the Big O for the worst case scenario for the union()
function would be the O(n*n) from the sort_list() plus run through the 
new lists to combine them, O(n) for list1 and O(m) for the list two,
O(n+m). Total would be O(n*n) + O(n) + O(m)

The space complexity for the worst case scenario for the union 
would be the sum of O(n) for the origin list 1, O(m) for the origin list 2, O(n) for the sorted
list 1, O(m) for the sorted list 2 and O(n+m) for the union final list.

**Intersection function analysis**
The intersection function will get two lists which will be sorted by sort_list()
and then both new lists will be compared each other to create a new list
with the elements in common in both list.

The complexity of the Big O for the worst case scenario for the intersection()
function would be the O(n*n) from the sort_list() plus run through the 
new lists to combine them, O(n) for list1 and O(m) for the list two,
O(n+m). Total would be O(n*n) + O(n) + O(m)

The space complexity for the worst case scenario for the intersection 
would be the sum of O(n) for the origin list 1, O(m) for the origin list 2, O(n) for the sorted
list 1, O(m) for the sorted list 2 and O(n+m) for the union final list.
 
