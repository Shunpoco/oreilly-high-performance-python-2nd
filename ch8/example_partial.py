from functools import partial

# Ref: https://www.geeksforgeeks.org/partial-functions-python/
# https://docs.python.org/3/library/functools.html
# Partial functions allow us to fix a certain number of arguments of a function and generate a new function.

# A normal function
def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x

if __name__ == "__main__":
    # A partial function that calls f with
    # a as 3, b as 1 and c as 4.
    g = partial(f, 3, 1, 4)

    # Calling g() with x = 5
    print(g(5))

    # A partial function with b = 1 and c = 2
    h = partial(f, b=1, c=2)

    # Calling h() with a = 100, x = 2
    print(h(a=100, x=2))

    # below code causes error, because h(100, 2) try to inject 2 in b, but we already filled b
    # TypeError: f() got multiple values for argument 'b'
    # print(h(100, 2))
