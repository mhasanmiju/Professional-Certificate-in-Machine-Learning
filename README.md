# Sorting Lists of Numbers in Python

This guide provides a variety of techniques for sorting lists of numbers in Python, catering to different scenarios and list sizes. Whether you need to sort small or large lists, Python has efficient built-in tools for the job.

## Contents
1. Different Ways to Sort a List of Numbers
   - Approach 1: Using `sorted()` for Quick Sorting
   - Approach 2: In-Place Sorting with `sort()`
   - Approach 3: Creating Sorted Copies with Slicing
   - Approach 4: Custom Sorting with Lambda Functions
   - Approach 5: Optimizing for Large Lists with `heapq`

## Different Ways to Sort a List of Numbers

### Approach 1: Using `sorted()` for Quick Sorting
The `sorted()` function is ideal when you want a new list sorted from the original, leaving the original list unchanged.
```python
numbers = [7, 3, 9, 2]
sorted_list = sorted(numbers)
print(sorted_list)  # Output: [2, 3, 7, 9]
```
### Approach 2: In-Place Sorting with `sort()`
The `sort()` method modifies the list directly, which can be more memory-efficient when a new list isn’t needed.
```python
numbers = [7, 3, 9, 2]
numbers.sort()
print(numbers)  # Output: [2, 3, 7, 9]
```
### Approach 3: Creating Sorted Copies with Slicing
Using slicing, you can create a sorted copy of a list without changing the original.
```python
numbers = [7, 3, 9, 2]
sorted_copy = numbers[:]
sorted_copy.sort()
print(sorted_copy)  # Output: [2, 3, 7, 9]
```
### Approach 4: Custom Sorting with Lambda Functions
For cases where sorting requires specific criteria, `sorted()` or `sort()` can take a `key` argument with a lambda function.

```python
numbers = [7, -3, 9, -2]
sorted_custom = sorted(numbers, key=lambda x: abs(x))
print(sorted_custom)  # Output: [-2, -3, 7, 9]
```
### Approach 5: Optimizing for Large Lists with `heapq`
For large datasets, the `heapq` module provides efficient sorting functions like `nsmallest()` and `nlargest()`.

```python
import heapq

numbers = [7, 3, 9, 2]
sorted_large_list = list(heapq.nsmallest(len(numbers), numbers))
print(sorted_large_list)  # Output: [2, 3, 7, 9]
```
