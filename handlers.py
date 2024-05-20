import logging
import time
from client import get_udp_transport
from storage import storage
from serializers import serialize_collision_data

async def _send_data(value: float, side: str):
    if time.time() - storage.last_sent_at_ts < 1:
        return
    if side == 'left':
        storage.lvalue = value
    elif side == 'right':
        storage.rvalue = value
    else:
        raise Exception('Invalid side codename')
    transport = await get_udp_transport()
    if transport:
        data = serialize_collision_data(storage)
        logging.debug(f"[OSC Handler] Send pat_{side} value: {value}")
        transport.sendto(data)
        storage.last_sent_at_ts = time.time()
    else:
        logging.debug(f"[OSC Handler] Cannot connect to device to send data")

async def pat_left_handler(_, value: float):
    await _send_data(value, 'left')

async def pat_right_handler(_, value: float):
    await _send_data(value, 'right')
