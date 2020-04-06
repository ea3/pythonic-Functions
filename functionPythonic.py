def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
print(help(factorial))

fact = factorial
print(fact)
print(fact(5))

print(map(factorial, range(11)))
print(list(map(factorial, range(11))))
fruits = ['Manzana', 'Banana', 'Mango', 'Kiwi', 'Patilla', 'Meloconton']
print(sorted(fruits, key=len))


def reverse(word):
    return word[::-1]


print(sorted(fruits, key=reverse))

print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])
print(dir(factorial))


# Higher order functions in Python.

