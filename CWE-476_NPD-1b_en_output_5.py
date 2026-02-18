
import ctypes

class person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

def allocate_person():
    p = ctypes.cast(ctypes.pointer(person()), ctypes.POINTER(person))
    p.contents.status = 0
    return p
