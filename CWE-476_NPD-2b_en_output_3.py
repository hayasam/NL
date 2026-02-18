
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
def create_person_alt():
    person = Person()
    person.status = 0
    person.name = b"John"
    return person
