def calculate_pi():
    '''Calculates Pi using Gregory-Leibniz series.'''
    pi = (4/1)
    minus = True
    for i in range(3, 500000):
        if (i % 2) == 0: # even number
            continue
        else:
            if minus:
                pi -= (4/i)
                minus = not minus
            else:
                pi += (4/i)
                minus = not minus
    return pi

print(calculate_pi())