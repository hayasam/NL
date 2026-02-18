
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

def main():
    # Allocate and initialize a Person struct
    person = create_person("Alice", 30, 5.7)
    
    # Access struct members using pointer-like syntax
    print(f"Name: {person.contents.name.decode()}")
    print(f"Age: {person.contents.age}")
    print(f"Height: {person.contents.height}")

if __name__ == "__main__":
    main()
