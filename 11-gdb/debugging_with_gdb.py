import ctypes


def crash():
    ctypes.string_at(0)


print("About to crash...")
crash()
print("Or not?")
