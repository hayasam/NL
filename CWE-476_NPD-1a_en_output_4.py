
import ctypes

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int),
        ("height", ctypes.c_float)
    ]

def create_person(name, age, height):
    person_ptr = ctypes.pointer(Person())
    person_ptr.contents.name = name.encode() if isinstance(name, str) else name
    person_ptr.contents.age = age
    person_ptr.contents.height = height
    return person_ptr

# Alternative using direct allocation
def create_person_alt(name, age, height):
    person = Person()
    person.name = name.encode() if isinstance(name, str) else name
    person.age = age
    person.height = height
    return ctypes.pointer(person)
