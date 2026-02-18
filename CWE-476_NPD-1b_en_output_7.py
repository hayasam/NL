
import ctypes

class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

person_ptr = ctypes.pointer(Person())
person_ptr.contents.status = 0
