
import ctypes

class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int),
                ("name", ctypes.c_char_p)]

def create_person():
    person_ptr = ctypes.POINTER(Person)(Person())
    person_ptr.contents.status = 0
    person_ptr.contents.name = b"John"
    return person_ptr

# Alternative using malloc
def create_person_malloc():
    person_ptr = ctypes.cast(ctypes.create_string_buffer(ctypes.sizeof(Person)), 
                             ctypes.POINTER(Person))
    person_ptr.contents.status = 0
    person_ptr.contents.name = b"John"
    return person_ptr
