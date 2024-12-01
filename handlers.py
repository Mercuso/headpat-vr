import logging
import time
import json
from websockets.asyncio.server import broadcast
from client import get_udp_transport
from storage import storage, WS_CONNECTIONS
from serializers import serialize_collision_data

async def _send_data(value: float, side: str):
    if time.time() - storage.last_sent_at_ts < 0.2 or not storage.allow_signal_sending:
        return
    if side == 'left':
        storage.lvalue = min(value, storage.max_intensity)
    elif side == 'right':
        storage.rvalue = min(value, storage.max_intensity)
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
    broadcast(WS_CONNECTIONS, json.dumps({"type": "signal", "value": {"left": storage.lvalue, "right": storage.rvalue}}))

async def pat_left_handler(_, value: float):
    await _send_data(value, 'left')

async def pat_right_handler(_, value: float):
    await _send_data(value, 'right')
