import logging
from client import get_udp_transport
from storage import storage
from serializers import serialize_collision_data

async def pat_left_handler(_, value: float):
    storage.lvalue = value
    transport = await get_udp_transport()
    if transport:
        data = serialize_collision_data(storage)
        logging.debug(f"[OSC Handler] Send pat_left value: {value}")
        transport.sendto(data)
    else:
        logging.debug(f"[OSC Handler] Cannot connect to device to send data")

async def pat_right_handler(_, value: float):
    storage.rvalue = value
    transport = await get_udp_transport()
    if transport:
        data = serialize_collision_data(storage)
        logging.debug(f"[OSC Handler] Send pat_right value: {value}")
        transport.sendto(data)
    else:
        logging.debug(f"[OSC Handler] Cannot connect to device to send data")
