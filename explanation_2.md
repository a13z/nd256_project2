# Problem 2. File Recursion

For this exercise, I decide to use recursion to get into the directories
I found being the base case when I find a file with the suffix provided.

Basically, I get the list of files and directories from the path given
and I sort that list. If I find a file with the suffix I return it, 
 otherwise if it is a directory I recursively get into it.
 
The complexity for the worst case scenario will be O(n) being n the number of
files or directories in the path given. 

The space complexity in the worst case scenario would also be O(n) being
 n the number of files, directories and subdirectories in the given path 


To answers to the points from the reviewer:

Yes, I understood the complexity would be linear and I tried to explain with
details when I said the complexity was O(n*m*p) being n files, m directories and
p subdirectories but this is an approximation of O(n) I believe and it is still
linear.
However, I do realise that I didn't explain it correctly and it is changed now.
Thank you.  