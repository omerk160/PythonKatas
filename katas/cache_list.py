class CacheList(list):
    """
    Implement CacheList class which is a regular Python list,
    but it holds the last n elements only (old elements will be deleted)

    Usage example:
    x = CacheList(3)

    x.append(1)
    x.append(2)
    x.append(3)

    print(x)
    >> [1, 2, 3]

    x.append(5)
    print(x)
    >> [2, 3, 5]

    x.append(1)
    print(x)
    >> [3, 5, 1]
    """
    def __init__(self, cache_capacity=5):
        super().__init__()
        pass

    def append(self, element):
        pass

    def cache_capacity(self):
        """
        Return the cache capacity
        """
        pass


if __name__ == '__main__':
    c_list = CacheList(5)
    c_list.append(1)
    c_list.append(2)
    c_list.append(3)
    c_list.append(4)
    c_list.append(5)
    c_list.append(6)
    print(len(c_list))
    print(c_list)
