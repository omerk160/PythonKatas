def seven_boom(n):
    """
    This functions returns a list of all "Booms" for a 7-boom play starting from 1 to n
    """
    booms = []
    for i in range(1, n + 1):
        if i % 7 == 0 or '7' in str(i):
            booms.append(i)
    return booms


print(seven_boom(30))  # Expected [7, 14, 17, 21, 27, 28]

