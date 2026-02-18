
import ctypes

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int),
        ("height", ctypes.c_float)
    ]

def create_person():
    person_ptr = ctypes.pointer(Person())
    return person_ptr

def main():
    p = create_person()
    p.contents.name = b"John Doe"
    p.contents.age = 30
    p.contents.height = 5.9
    
    print(f"Name: {p.contents.name.decode()}")
    print(f"Age: {p.contents.age}")
    print(f"Height: {p.contents.height}")

if __name__ == "__main__":
    main()
