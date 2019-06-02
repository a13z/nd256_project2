import os

def is_list(element):
    """
    Check if element is a Python list
    """
    return isinstance(element, list)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    new_files = []

    if os.path.isfile(path):
        if path.endswith(suffix):
            # print("Returning.. ", path)
            return path
    elif os.path.isdir(path):
        # print(os.listdir(path))
        for entry in sorted(os.listdir(path)):
            output = find_files(suffix,os.path.join(path, entry))
            # print("Output ", output)
            if is_list(output):
                new_files = new_files + output
            elif output is not None:
                new_files.append(output)
        if new_files != []:
            return new_files
        else:
            return None
    else:
        return None

def test_function(test_case):
    suffix = test_case[0]
    path = test_case[1]
    solution = test_case[2]

    print("Find files with extension %s in the %s directory" % (suffix, path))
    output = find_files(suffix, path)
    # print(output)
    if output == solution:
        print("Pass")
    else:
        print("False")

# Find all files with .c extension in ./testdir
path = './testdir'
suffix = '.c'
solution = ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
test_case = [suffix, path, solution]
test_function(test_case)

# Find all files with .py extension in ./testdir
path = './testdir'
suffix = '.py'
solution = None
test_case = [suffix, path, solution]
test_function(test_case)

# Find all files with empty extension in ./testdir
path = './testdir4'
suffix = ''
solution = None
test_case = [suffix, path, solution]
test_function(test_case)

# Find all files with .c extension in ./testdir4 which doesn't exist
path = './testdir4'
suffix = '.c'
solution = None
test_case = [suffix, path, solution]
test_function(test_case)
