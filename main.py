import timeit

n = 100

def test() -> int:
    """Test the performance of linear search on 1000 elements"""
    data = list(range(1000))
    target = 777
    for i, value in enumerate(data):
        if value == target:
            # index found
            return i

# Note that the function should be passed to `timeit.timeit` without '()'
# We don't want to call the function, instead we pass it to timeit.
# timeit will call the function (without arguments) and measure the time taken.
print("Time taken (s):", timeit.timeit(test, number=n))
