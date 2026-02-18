
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

def access_person_members(person_ptr):
    print(f"Name: {person_ptr.contents.name.decode()}")
    print(f"Age: {person_ptr.contents.age}")

# Alternative approach using direct structure
def create_person_direct(name, age):
    p = Person()
    p.name = name.encode() if isinstance(name, str) else name
    p.age = age
    return p

# Example usage
if __name__ == "__main__":
    # Using pointer approach
    person_ptr = create_person("Alice", 30)
    access_person_members(person_ptr)
    
    # Using direct structure
    person = create_person_direct("Bob", 25)
    print(f"Name: {person.name.decode()}, Age: {person.age}")
