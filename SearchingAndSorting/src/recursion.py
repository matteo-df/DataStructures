def get_fibonacci(position):
    """
    Implement a function recursively to get the desired Fibonacci sequence value.
    F(0)=0
    F(1)=1
    F(n)=F(n-1)+F(n-2)
    """

    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return get_fibonacci(position-1) + get_fibonacci(position - 2)
