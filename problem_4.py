import time

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

class ActiveDirectory(object):

    def __init__(self, root):
        self.root = root

def search_group(root, group_name):
    """
    Return Group node if the group is found in the Active Directory.

    Args:
      root(obj): active directory root/parent
      group_name(class:Group): group name to find in the Active Directory
    """
    node = root

    if node is None:
        return False

    if node.get_name() == group_name:
        return node

    for group in node.get_groups():
        node = search_group(group, group_name)
        if node is not None:
            return node

def search_user(root, username):
    """
    Return True if user is found in active node if the group is found in the Active Directory.

    Args:
      root(obj): active directory root/parent
      username(string): group name to find in the Active Directory
    """
    node = root
    groups_user_belong = set()

    if node is None:
        return False

    if username in node.get_users():
        groups_user_belong.add(node.get_name())
        return True

    for group in node.get_groups():
        if search_user(group,username):
            groups_user_belong.add(group.get_name())
            groups_user_belong.add(node.get_name())
            return True

    return False

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    parent = active_directory.root

    group_found = search_group(parent, group)

    if group_found:
        return search_user(group_found, user)
    else:
        return False

def test_function(test_case):
    user = test_case[0]
    group = test_case[1]
    solution = test_case[2]

    print("User %s is in group %s or in any of its subgroups" % (user, group) if solution else \
              "User %s is NOT in group %s or in any of its subgroups" % (user, group))
    if is_user_in_group(user, group) == solution:
        print("Pass")
    else:
        print("Failed")

# load test data set

parent = Group("parent")
child = Group("child")
child2 = Group("child2")
child3 = Group("child3")

sub_child = Group("subchild")
sub_child2 = Group("subchild2")
sub_child3 = Group("subchild3")

child_user3 = "child_user3"
sub_child_user = "sub_child_user"
sub_child_user2 = "sub_child_user2"
sub_child_user3 = "sub_child_user3"

sub_child.add_user(sub_child_user)
sub_child2.add_user(sub_child_user2)
sub_child3.add_user(sub_child_user3)

child.add_group(sub_child)
child.add_group(sub_child2)

sub_child2.add_group(sub_child3)

child3.add_user(child_user3)

parent.add_group(child)
parent.add_group(child2)
parent.add_group(child3)

active_directory = ActiveDirectory(parent)

# Test case 1
user = "sub_child_user3"
group = "parent"
solution = True
test_case = [user, group, solution]
test_function(test_case)

# Test case 2
user = "sub_child_user3"
group = "child"
solution = True
test_case = [user, group, solution]
test_function(test_case)

# Test case 3
user = "sub_child_user3"
group = "child2"
solution = False
test_case = [user, group, solution]
test_function(test_case)

# Test case 4. Passing a child as a group
user = "sub_child_user2"
group = "sub_child_user3"
solution = False
test_case = [user, group, solution]
test_function(test_case)

# Test case 5
user = "sub_child_user2"
group = "subchild"
solution = False
test_case = [user, group, solution]
test_function(test_case)