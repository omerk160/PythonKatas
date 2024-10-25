class SortedDict(dict):
    """
    Implement SortedDict class which is a regular Python dictionary,
    but the keys are maintained in a sorted order

    Usage example:
    x = SortedDict()

    x['banana'] = 'ccc'
    x['apple'] = 'aaa'
    x['orange'] = 'bbb'

    list(x.keys())
    >> ['apple', 'banana', 'orange']

    list(x.values())
    >> ['aaa', 'ccc', 'bbb']

    list(x.items())
    >> [('apple', 'aaa'), ('banana', 'ccc'), ('orange', 'bbb')]
    """

    def __init__(self):
        super().__init__()
        self._sorted_keys = []

    def __setitem__(self, key, value):
        # Insert the item normally
        super().__setitem__(key, value)

        # Maintain the sorted list of keys
        if key not in self._sorted_keys:
            self._sorted_keys.append(key)
            self._sorted_keys.sort()

    def __delitem__(self, key):
        # Remove the item and update the sorted key list
        super().__delitem__(key)
        self._sorted_keys.remove(key)

    def keys(self):
        return iter(self._sorted_keys)

    def values(self):
        return (self[key] for key in self._sorted_keys)

    def items(self):
        return ((key, self[key]) for key in self._sorted_keys)


if __name__ == '__main__':

    if __name__ == '__main__':
        s_dict = SortedDict()
        s_dict['banana'] = 'ccc'
        s_dict['apple'] = 'aaa'
        s_dict['orange'] = 'bbb'



    print(list(s_dict.keys()))  # ['apple', 'banana', 'orange']
    print(list(s_dict.values()))  # ['aaa', 'ccc', 'bbb']
    print(list(s_dict.items()))  # [('apple', 'aaa'), ('banana', 'ccc'), ('orange', 'bbb')]