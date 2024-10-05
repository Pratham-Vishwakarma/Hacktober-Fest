import sys

sys.setrecursionlimit(10)
def recursive_function(n):
    while n<10:
        recursive_function(n)

print(recursive_function(10))
