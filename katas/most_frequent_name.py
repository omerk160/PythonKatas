def most_frequent_name(file_path):
    """
    Receives a path to a file containing names (name in each line)
    The function should return the most frequent name in the file.

    You can assume file_path exists in the file system.
    """
    with open(file_path, 'r') as file:
        names = file.readlines()

        # Strip newline characters and whitespace from each name
        names = [name.strip() for name in names]

        # Dictionary to keep track of name counts
        name_counts = {}

        # Count the occurrences of each name
        for name in names:
            if name in name_counts:
                name_counts[name] += 1
            else:
                name_counts[name] = 1

        # Find the name with the highest count
        most_frequent = max(name_counts, key=name_counts.get)

        return most_frequent


if __name__ == '__main__':
    print(most_frequent_name('files/names.txt'))
