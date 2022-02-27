import os
import re
import shutil

DIRECTORY = 'DIRECTORY'
FILES = 'FILES'
BOTH = 'BOTH'
PATHS = 'PATHS'
FILENAMES = 'FILENAMES'
REGEX = 'REGEX'
KEYWORD = 'KEYWORD'


def traverseFileTree(ft_node, dir_func=tuple(), file_func=tuple(), use_child_as_parameter=False):
    """
    Traverses a FileTree and performs a function to each node.

    :param use_child_as_parameter: Boolean that indicates whether the child variable should be passed into functions.
    :param ft_node: A FileTree object, from which to traverse.
    :param dir_func: A tuple in the format tuple(function, tuple(parameters)). Applies to directories (and files if one
     is not supplied for them).
    :param file_func: A tuple in the format tuple(function, tuple(parameters)). Applies to files (and directories if one
     is not supplied for them).
    """

    if not (dir_func or file_func):
        raise ValueError("Both function parameters cannot be empty.")

    output = []
    for child in ft_node.children:

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


def getAll(type_, ft_node):
    """
    Returns a list of directories or files, depending on type, contained in a directory and their descendants.

    :param type_: FILES or DIRECTORY
    :param ft_node: A FileTree node to work from
    :return: All the FileTree nodes of the type_ in and under the filetree provided
    """

    if type_ != DIRECTORY and type_ != FILES:
        raise ValueError(f"type_ must be '{DIRECTORY}' or '{FILES}', not '{type_}'")

    def checkIfItem(ft):
        if type_ == DIRECTORY and ft.is_directory:
            return ft
        elif type_ == FILES and not ft.is_directory:
            return ft

    # Will contain None values
    unfiltered_items = traverseFileTree(ft_node, dir_func=(checkIfItem,), use_child_as_parameter=True)

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


def graftDirectories(directories, source_dir, target_dir):
    """
    Takes a list of directories, and grafts them from their source directory to their target directory.

    :param directories: List of directories in source directory
    :param source_dir: Source directory
    :param target_dir: Target directory
    :return: Grafted directories
    """

    newDirectories = [graftItem(directory, source_dir, target_dir) for directory in directories]
    return newDirectories


def buildDirectories(directories):
    """
    Ensures all the directories are present, adding ones that are not.

    :param directories: Collection of directories to make/check
    """

    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def copyFiles(files, source_dir, target_dir, overwrite):
    """
    Copies the files to the target directory, checking if they already exist, overwriting them if told to.

    :param source_dir: Source directory; note, this is not the directory the files are in, but the directory from which
    the backup originates from
    :param overwrite: Boolean value to overwrite already present files or not
    :param target_dir: Target directory to which files will be copied
    :param files: Iterable collection of file paths to be copied
    """
    # Generate the new locations for each file
    new_file_paths = [graftItem(file, source_dir, target_dir) for file in files]

    # Copy files
    for i, new_file_path in enumerate(new_file_paths):
        if (not os.path.isfile(new_file_path)) or overwrite:  # If file doesn't exist or overwrite is true:
            shutil.copy(files[i], new_file_path)


def applyFilter(regex_filters, keyword_filters, path):
    """
    Checks whether a certain FileTree node satisfies all the regular expressions provided.

    :param keyword_filters: An iterable container containing keywordFilters to be applied
    :param regex_filters: An iterable container containing RegexFilters to be applied
    :param path: A path for the filters to be applied on
    :return: True if the node path satisfies each RegexFilter, False otherwise
    """

    def handleFilter(filter_, type_, path_):
        """
        Handles the logic of the filter and applies it to the item path provided.

        :param filter_: The filter object, either RegexFilter or KeywordFilter
        :param type_: The type of filter applied, either REGEX or KEYWORD
        :param path_: The path to be analysed
        :return: Whether or not this item should be copied according to the filter
        """
        # Validate type
        if type_ not in [REGEX, KEYWORD]:
            raise ValueError(f"type_ must be either {REGEX} or {KEYWORD}, got {type_}")

        # Decide whether to apply the filter to the filename or the full path
        if filter_.application == FILENAMES:
            str_to_use = os.path.basename(path_)
        else:
            str_to_use = path_

        # Decide whether the filter should be applied to the item according to whether it is a file or directory
        if (filter_.item_type != FILES and os.path.isdir(path_)) \
                or (filter_.item_type != DIRECTORY and os.path.isfile(path_)):
            # The filter applies to directories and the item is a dir OR
            #   the filter applies to files and the item is a file:

            # If the match is true and a whitelist is used, the result is true, or if the match is false and a
            # blacklist is used, the result is true; whitelist allows items that match it through, and blacklist allows
            # items that don't match it through.
            if type_ == REGEX:
                match = bool(re.match(filter_.regex, str_to_use))
                result = match is filter_.whitelist
            else:  # Type must be KEYWORD
                kw_in_str = filter_.keyword in str_to_use
                result = kw_in_str is filter_.whitelist
        else:
            # The regex does not apply to this item
            result = True

        return result

    results = []
    for regex_filter in regex_filters:
        results.append(handleFilter(regex_filter, REGEX, path))

    for keyword_filter in keyword_filters:
        results.append(handleFilter(keyword_filter, KEYWORD, path))

    return all(results)


def buildFilter(regex_filters, keyword_filters):
    """
    Builds the filter function to be passed to the FileTree constructors;
     the filter function has to have one parameter.

    :param regex_filters: Iterable container of RegexFilters
    :param keyword_filters: Iterable container of KeywordFilters
    :return: The filter function, which takes one argument, suitable for the FileTree constructor
    """

    def filter_(path):
        return applyFilter(regex_filters, keyword_filters, path)

    return filter_
