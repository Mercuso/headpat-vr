import struct

def  serialize_collision_data(lvalue: float, rvalue: float) -> bytes:
    data = (round(lvalue*10) << 4) | round(rvalue*10)
    return struct.pack('B', data)
