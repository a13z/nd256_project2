# Problem 3. Huffman coding

For this problem, I used a tree data structure since the Huffman coding
algorithm uses a tree to store and encode values based on their frequency.

In the tree data structure we store node objects.

**tree_traverse() helper function**
There is one helper function tree_traverse() which traverse the tree
recursively and populate the codes dictionary, used to map characters 
with the Huffman codes.
This helper function is used in the huffman_encoding() function.

Since it has to traverse the whole tree its worst case scenario Big O is
O(n). The space complexity is also O(n)

**huffman_encoding(data) function**
This function receives a string as an argument and does the following things:
1. Find the frequency for every character of the string.
2. Create a sorted list with frequencies found in step 1
3. Apply Huffman coding algorithm to create a tree data structure 
storing characters based on their frequencies. 
4. Encode the string with the Huffman code calculated.

_Note:_ This function does too many things which should be splitted into
different functions.

The worst case scenario Big O for this function is the sum of:
- for char to calculate frequencies is O(n)
- sorted() to sort the frequency list is O(log n)
- while freq_list loop is O(log n) since we are summing pair of elements from
 a list of frequencies and inside:
    - when freq_list has one element which only happens once:
        -traverse_tree() which populates codes dictionary used to encode
        O(n)
        -there is a for loop which is O(n)
        
Total worst case scenario Big O approx would be O(n)

The space complexity would be also O(n)

**huffman_encoding(data,tree) function**
This function receives a data string to decode and a tree as arguments 
and it loops through the string and decode a sequence of bits according
to the tree data structure.

The worst case scenario Big O for this function is O(n) since we have
to loop through the data string plus traverse the tree to the leaves
to find the char to decode which would be O(log n). Overall it would be
O (n log n)

The space complexity would be O (n)






