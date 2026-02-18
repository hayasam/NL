
import ctypes

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int)
    ]

def create_person(name, age):
    person_ptr = ctypes.pointer(Person())
    person_ptr.contents.name = name.encode() if isinstance(name, str) else name
    person_ptr.contents.age = age
    return person_ptr

# Example usage
if __name__ == "__main__":
    p = create_person("Alice", 30)
    print(f"Name: {p.contents.name.decode()}, Age: {p.contents.age}")
