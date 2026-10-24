print("utils module is loading")
print("Module name:", __name__)

def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(greet("Direct run"))
    print(add(10, 20))