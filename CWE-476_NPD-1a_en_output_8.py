
import ctypes

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int)
    ]

def create_person(name, age):
    person_ptr = ctypes.pointer(Person())
    person_ptr.contents.name = name.encode('utf-8') if isinstance(name, str) else name
    person_ptr.contents.age = age
    return person_ptr

def access_person(person_ptr):
    print(f"Name: {person_ptr.contents.name.decode('utf-8')}")
    print(f"Age: {person_ptr.contents.age}")

# Alternative using direct structure
class PersonDirect:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def create_person_direct(name, age):
    return PersonDirect(name, age)

def access_person_direct(person):
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
