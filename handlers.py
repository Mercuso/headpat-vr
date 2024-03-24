from client import get_tcp_transport
from storage import storage
from serializers import serialize_collision_data

async def pat_left_handler(_, value):
    storage.lvalue = value
    transport = await get_tcp_transport()
    data = serialize_collision_data(storage)
    transport.write(data)
    await transport.drain()

async def pat_right_handler(_, value):
    storage.lvalue = value
    transport = await get_tcp_transport()
    data = serialize_collision_data(storage)
    transport.write(data)
    await transport.drain()
