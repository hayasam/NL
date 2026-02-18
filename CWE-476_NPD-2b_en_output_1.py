
import ctypes

class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int),
                ("name", ctypes.c_char_p)]

def create_person():
    person_ptr = ctypes.POINTER(Person)(Person())
    person_ptr.contents.status = 0
    person_ptr.contents.name = ctypes.c_char_p(b"John")
    return person_ptr

person = create_person()
