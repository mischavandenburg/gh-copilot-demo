def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a - b


def multiply(a, b):
    return a * b


def is_even(number):
    return number % 2 == 0


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print(f"Is 6 even? {is_even(6)}")

