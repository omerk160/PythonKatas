def file_exceptions(file_path, op='r'):
    """
    Replaces ' ' by '_' in the given file_path.

    You have to except the MOST SPECIFIC exception and print an informative message for ALL potential file-related exceptions.
    The message must contain the exception name, e.g. RuntimeError, ZeroDivisionError, ...
    """
    try:
        with open(file_path, op) as file:
            content = file.read()
            content_modified = content.replace(' ', '_')
            return content_modified

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except IsADirectoryError as e:
        print(f"IsADirectoryError: {e}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except FileExistsError as e:
        print(f"FileExistsError: {e}")
    except OSError as e:
        print(f"OSError: {e}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == '__main__':
    print(file_exceptions('files/nonexistent_file.txt'))
    print(file_exceptions('files/somefile'))
    print(file_exceptions('files/'))
    print(file_exceptions('files/someotherfile', op='x'))
    print(file_exceptions('files/someotherfile'))

