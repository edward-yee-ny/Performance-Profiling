# Performance profiling

Performance profiling refers to the measurement of the performance of code. Performance can be measured in a number of areas, such as memory use, latency, etc. In this exercise, we focus on measuring execution time.

# Part 1: Measuring performance

We may think our code is fast, but how do we actually know?

We'll have to measure its performance.

## The `timeit` module

Reference: [timeit — Measure execution time of small code snippets](https://docs.python.org/3.7/library/timeit.html)

Python provides a `timeit` module that can measure the performance of code snippets:

```python
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
```

The above snippet is supposed to measure the time taken to call the `test()` function `n` times, and prints the time taken in seconds. Does it actually do that?

**Hint:** Look at the operations carried out in `test()`. Is it _only_ performing a linear search?

**Lesson:** Ensure that your function is only executing the operations you want to time.

If we want to test a function that takes parameters, we'll have to "wrap" it, because `timeit` will not help us pass arguments to the given function:

```python
import timeit

n = 100

data = list(range(n))

def search(n: int, target: int) -> int:
    """Test the performance of linear search for target on n elements"""
    for i, value in enumerate(data):
        if value == target:
            # index found
            return i

def test():
    search(1000, 777)

# Note that the function should be passed to `timeit.timeit` without '()'
# We don't want to call the function, instead we pass it to timeit.
# timeit will call the function and measure the time taken.
print("Time taken (s):", timeit.timeit(test, number=n))
```

**Your turn:** Try modifying the argument values that are passed to `search()`. How does this affect the time taken?

# Your task

You have learned that searching an array linearly takes an increasing amount of time as the number of elements increases. How does `search()` perform? Does the time taken for each call to `search()` increase when the input list grows larger?

Measure the performance of the `search()` function. Display your results as follows (or using any similarly suitable method):

```
 Array size  Time taken (μs) 
     0      2.1050000214017928
     1      1.1850061127915978
     2      1.2790042092092335
     3      1.0599978850223124
     4      1.2090022210031748
     5      1.6210033209063113
     6      1.0139992809854448
     7      1.2130039976909757
     8      0.9779978427104652
     9      1.1369993444532156
     10     1.0509975254535675
     11     1.0349976946599782
     12     1.3379976735450327
     13     0.872001692187041
     14     0.7019989425316453
     15     1.0000003385357559
    ...
```

## Questions

1. What do you notice about how `search()` behaves?
2. What are some possible sources of error in this measurement?


# Part 2: Performance of Sort & Search Algorithms

Set up `timeit` to measure the performance of your sort and search functions.

You need not measure the time for every possible array size; you may wish to measure with powers of 10, e.g. arrays of size 10, 100, 1000, ...

**Caveat 1:** You will need to start with a shuffled array if you want to measure typical execution time. You may wish to use the `random.shuffle()` function from the `random` module.

**Caveat 2**: If your sort function mutates the input array, ensure that you pass a copy of the original array so that the array size does not shrink or grow between runs. You can pass a copy of a list using `list.copy()` (note that this is an O(n) operation).

**Caveat 3:** Remember for each array size to run the function a few times and get the average time. `timeit` returns the total execution time for `n` runs.


# Part 3: Performance of Data Structures

Set up `timeit` to measure the performance of your data structure operations (linked list and binary search tree insertion & retrieval).

How does the time taken for each operation vary with the number of elements already in the data structure?

**Caveat:** You will need to add elements to the BST in random order, because adding sorted items to a BST will result in an unbalanced BST that essentially behaves like a linked list. You might wish to iterate through a shuffled list to do this.

**Caveat:** Remember that each insert operation should only be run once since the data structure size will change.


### lambda functions (not in syllabus; can skip)

It seems rather tedious to have to define a test function that is only used once. Fortunately, Python lets us create ad-hoc unnamed functions using the `lambda` keyword.

Another way to perform this wrapping using `lambda`:

```python
timeit.timeit(lambda: search(1000, 777), number=n)
```

The syntax `lambda: <expression>` gives a function that evaluates `<expression>` and returns its result. The above snippet will execute `search(1000, 777)` and return its result.
