# Problem 4. Active Directory.

For this problem, apart from the Group class, I decided to create 
an Active Directory class which contains the link to the parent group. 

I have also created two helper methods, one to find a group in the Active
Directory and the other one to find a user in the group, or any of its childs, 
given as a parameter.

_Note_ I understood and assumed that, groups are unique in the Active
Directory, that is there are not two groups with the same name.
I also assumed that what it was required to do it was to find if a user
belongs to a given group or any of its childs.

The logic based on this is as follows, first I use search_group() 
function to find a if a group exists in the Active Directory and if so, 
I return the Group node.
From this Group node down, I start searching if username belongs to this group
or any of its child groups.

**search_group(root, group_name) helper function**
This function is used to find a group in the active directory. 

The worst case scenario Big O would be O(n) since we might need to 
traverse the whole tree to find a group.
Space complexity is O(n)

**search_user(root, username) helper function**
This function is used to find if a username exists from a given Group
 node passed as root parameter recursively.
This function uses a set to store the groups which the user belongs to. 

The worst case scenario Big O would be O(n) since we might need to 
traverse the whole tree to find a user, i.e. in case the group is parent
Space complexity is O(n)

