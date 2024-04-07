from client import get_udp_transport
from storage import storage
from serializers import serialize_collision_data

async def pat_left_handler(_, value: float):
    storage.lvalue = value
    transport = await get_udp_transport()
    data = serialize_collision_data(storage)
    transport.sendto(data)

async def pat_right_handler(_, value: float):
    storage.rvalue = value
    transport = await get_udp_transport()
    data = serialize_collision_data(storage)
    transport.sendto(data)
