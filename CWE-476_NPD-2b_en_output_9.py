
import ctypes

class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int),
                ("name", ctypes.c_char_p)]

def create_person():
    person_ptr = ctypes.POINTER(Person)(Person())
    person_ptr.contents.status = 0
    person_ptr.contents.name = b"John"
    return person_ptr

# Alternative implementation using direct struct access
class PersonDirect:
    def __init__(self):
        self.status = 0
        self.name = "John"

# Using ctypes for memory allocation similar to C
person_mem = ctypes.create_string_buffer(ctypes.sizeof(Person))
person_ptr = ctypes.cast(person_mem, ctypes.POINTER(Person))
person_ptr.contents.status = 0
person_ptr.contents.name = b"John"
