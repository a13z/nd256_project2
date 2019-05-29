# Problem 1. LRU cache

In order to fulfill the requirements of this problem, that is, implement a cache 
structure with LRU functionality with O(1), I decided to use a double link list of double nodes which I had
 implemented in the practice lessons. This double list link is an attribute of the LRU_cache.
 
This double link list is accessed from a dictionary attribute named cache of the LRU_cache class.

Given a key/value pair to set, a node will be created at the end of the double list and
the key in the dictionary will point to the node created.

Given a key/pair to get, the value will be retrieve from the node in the double link list 
and this node will be moved to the end of the double link list. This is why a double link list
has been chosen, because the complexity to achieve this is O(1) since a node
has references to its previous and next nodes so it can be easily removed and
appended to the end of the double list.

_Note_ I decided to store the key in the node of the double linked list too, among with the value
for just one reason, when the capacity of the cache is full and the least
recent used node is evicted or deleted, I can get the key so I could delete it
from the cache dictionary too. Otherwise, this value will be kind of a zombie since
it will be out of the double linked list.

Complexity Big O is O(1) for set and get operations.

Space efficiency it will be O(n) being n the capacity of the cache.
