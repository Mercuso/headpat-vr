import logging
import time
import json
from websockets.asyncio.server import broadcast
from client import get_udp_transport
from storage import Signal, storage, WS_CONNECTIONS
from serializers import serialize_collision_data

async def _send_data(value: float, side: str):
    if not storage.allow_signal_sending:
        return
    value = min(value, storage.max_intensity)
    if side == 'left':
        prev_lsignal = storage.lsignal
        if prev_lsignal and time.time() - prev_lsignal.sent_at_ts < 0.2:
            return
        storage.lsignal = Signal(value)
    elif side == 'right':
        prev_rsignal = storage.rsignal
        if prev_rsignal and time.time() - prev_rsignal.sent_at_ts < 0.2:
            return
        storage.rsignal = Signal(value)
    else:
        raise Exception('Invalid side codename')
    transport = await get_udp_transport()
    lvalue = storage.lsignal.value if storage.lsignal and not storage.lsignal.sent_at_ts else 0.0
    rvalue = storage.rsignal.value if storage.rsignal and not storage.rsignal.sent_at_ts else 0.0
    if transport:
        data = serialize_collision_data(lvalue, rvalue)
        logging.debug(f"[OSC Handler] Send pat_{side} value: {value}")
        logging.debug(f"[OSC Handler] Send data: {data}")
        transport.sendto(data)
        now = time.time()
        if storage.lsignal and storage.lsignal.sent_at_ts == 0.0:
            storage.lsignal.sent_at_ts = now
        if storage.rsignal and storage.rsignal.sent_at_ts == 0.0:
            storage.rsignal.sent_at_ts = now
    else:
        logging.debug(f"[OSC Handler] Cannot connect to device to send data")
    data = {
        "type": "signal", 
        "value": {
            "left": lvalue,
            "right": rvalue,
        }
    }
    broadcast(WS_CONNECTIONS, json.dumps(data))

async def pat_left_handler(_, value: float):
    await _send_data(value, 'left')

async def pat_right_handler(_, value: float):
    await _send_data(value, 'right')
