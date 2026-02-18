
import ctypes

class person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

person_ptr = ctypes.pointer(person())
person_ptr.contents.status = 0
