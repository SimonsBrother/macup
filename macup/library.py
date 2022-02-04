import os
import re
import shutil

DIRECTORY = 'DIRECTORY'
FILES = 'FILES'


def traverseFileTree(file_tree, dir_func=tuple(), file_func=tuple(), use_child_as_parameter=False):
    """
    Traverses a FileTree and performs a function to each node.

    :param use_child_as_parameter: Boolean that indicates whether the child variable should be passed into functions.
    :param file_tree: A FileTree object, from which to traverse.
    :param dir_func: A tuple in the format tuple(function, tuple(parameters)). Applies to directories (and files if one
     is not supplied for them).
    :param file_func: A tuple in the format tuple(function, tuple(parameters)). Applies to files (and directories if one
     is not supplied for them).
    """

    if not (dir_func or file_func):
        raise ValueError("Both function parameters cannot be empty.")

    output = []
    for child in file_tree.children:

        if child.is_directory:  # Decides which function should be used
            function = dir_func if dir_func else file_func
        else:
            function = file_func if file_func else dir_func

        if use_child_as_parameter:  # Executes the function, handling what parameter is passed
            return_val = function[0](child)
        else:
            return_val = function[0](*function[1])

        output.append(return_val)

        if child.is_directory:  # The recursion must go on!
            output += traverseFileTree(child, dir_func, file_func, use_child_as_parameter)

    return output


def getAll(type_, file_tree):
    """
    Returns a list of directories or files, depending on type, contained in a directory and their descendants.

    :param type_: FILES or DIRECTORY
    :param file_tree: A FileTree node to work from
    :return: All the FileTree nodes of the type_ in and under the filetree provided
    """

    def checkIfItem(ft):
        if type_ == DIRECTORY and ft.is_directory:
            return ft
        elif type_ == FILES and not ft.is_directory:
            return ft

    # Will contain None values
    unfiltered_items = traverseFileTree(file_tree, dir_func=(checkIfItem,), use_child_as_parameter=True)

    # Removes None values
    items = list(filter(lambda item: item is not None, unfiltered_items))
    return items


def graftItem(item_path, source, target):
    """
    Removes the source part from an item path, and concatenates it onto target
    :param item_path: The file/directory to be grafted from source directory to target directory
    :param source: The source directory
    :param target: The target directory
    :return: The grafted directory
    """

    match = re.match(str(source) + r'(.*)', str(item_path))
    truncated_item_path = match.group(1)  # Contains the directory without the source
    return str(target) + truncated_item_path


def buildDirectories(directories):
    """
    Ensures all the directories are present, adding ones that are not.

    :param directories: Collection of directories to make/check
    :return: Nothing
    """

    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def copyFiles(files, source, target, overwrite):
    """
    Copies the files to the target directory, checking if they already exist, overwriting them if told to.

    :param source: Source directory; note, this is not the directory the files are in, but the directory from which
    the backup originates from
    :param overwrite: Boolean value to overwrite already present files or not
    :param target: Target directory to which files will be copied
    :param files: Collection of file paths to be copied
    :return:
    """
    # Generate the new locations for each file
    new_file_paths = [graftItem(file, source, target) for file in files]

    # Copy files
    for i, new_file_path in enumerate(new_file_paths):
        if (not os.path.isfile(new_file_path)) or overwrite:  # If file doesn't exist or overwrite is true:
            shutil.copy(files[i], new_file_path)
