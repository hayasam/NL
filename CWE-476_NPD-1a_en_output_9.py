
import ctypes

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int)
    ]

def create_person(name, age):
    person_ptr = ctypes.pointer(Person())
    person_ptr.contents.name = name.encode('utf-8') if name else None
    person_ptr.contents.age = age
    return person_ptr

def print_person(person_ptr):
    print(f"Name: {person_ptr.contents.name.decode('utf-8') if person_ptr.contents.name else 'None'}")
    print(f"Age: {person_ptr.contents.age}")

# Example usage
if __name__ == "__main__":
    p = create_person("Alice", 30)
    print_person(p)
