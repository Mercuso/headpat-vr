import struct
from storage import Storage

def  serialize_collision_data(storage: Storage) -> bytes:
    data = (round(storage.lvalue*10) << 4) | round(storage.rvalue*10)
    return struct.pack('B', data)
