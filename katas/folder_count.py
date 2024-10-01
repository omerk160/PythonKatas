def count_folders(file_path):
    """
    Returns the number of folders in the given file path.
    `file_path` is a string representing the path to a file (either Windows or Linux format).
    """


# Example usage
file_path_1 = "C:\\Users\\Alex\\Documents\\project\\file.txt"
folders_count_1 = count_folders(file_path_1)
print(folders_count_1)  # 4 expected

file_path_2 = "/home/alex/projects/file.txt"
folders_count_2 = count_folders(file_path_2)
print(folders_count_2)  # 3 expected

"""
To complete this exercise:
--------------------------
Assume that the last part of the path is always a file and not a folder.


Exercise Breakdown:
-------------------
The `str.split(delimiter)` function allows you to break a string into a list of substrings based on a specified delimiter.
If no delimiter is specified, str.split(), the default is whitespace.
"""