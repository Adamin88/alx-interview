def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): The size of the Pascal's triangle.

    Returns:
        list of list of int: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

