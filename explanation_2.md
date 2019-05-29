# Problem 2. File Recursion

For this exercise, I decide to use recursion to get into the directories
I found being the base case when I find a file with the suffix provided.

Basically, I get the list of files and directories from the path given
and I sort that list. If I find a file with the suffix I return it, 
 otherwise if it is a directory I recursively get into it.
 
The complexity for the worst case scenario will be O(n*m*p) being n the number of
files, m the number of directories and p subdirectories in the path given. 
This could grow exponentially. 

The space complexity in the worst case scenario can also grow exponentially since
 it depends on the number of directories and subdirectories in the given path 
  This is when we use recursion and the amount of memory required will increase
  exponentially.
