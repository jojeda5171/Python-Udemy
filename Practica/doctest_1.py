def suma(a, b):
    """Suma dos numeros
    >>> suma(1,2)
    3

    >>> suma(0,0)
    0

    >>> suma(-5,7)
    2

    """
    return a+b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
