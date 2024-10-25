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
        pass

    def __setitem__(self, key, value):
        pass

    def items(self):
        raise NotImplemented()

    def values(self):
        raise NotImplemented()

    def keys(self):
        raise NotImplemented()


if __name__ == '__main__':

    s_dict = SortedDict()
    s_dict['a'] = None
    s_dict['t'] = None
    s_dict['h'] = None
    s_dict['q'] = None
    s_dict['b'] = None
    print(s_dict.items())
