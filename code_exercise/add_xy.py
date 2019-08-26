def add(x, y):
    """Return x plus y, optional"""
    return x + y
print("input x:")

a = input("> ")
a_int = int(a)

print("input y:")
b = input("> ")
b_int = int(b)
print("x + y = ", add(a_int,b_int))

