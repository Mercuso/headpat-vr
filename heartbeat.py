import asyncio
import time
from storage import storage
from client import get_udp_transport

last_hb_received_at_ts: float = 0.0 # seconds

def data_received_callback (data, addr):
    global last_hb_received_at_ts
    last_hb_received_at_ts = time.time()

async def ping_device():
    # ping device every 5 seconds before first response received
    # increase delay to 10 seconds after that
    # skip sending ping request if osc signal was received less than 5 seconds ago
    global last_hb_received_at_ts
    transport = await get_udp_transport()
    protocol = transport.get_protocol()
    protocol.register_data_received_callback(data_received_callback)
    while True:
        delay = 10 # default
        if transport:
            print(last_hb_received_at_ts is not None)
            now = time.time()
            if time.time() - last_hb_received_at_ts > delay:
                transport.sendto(b'\x00')
        await asyncio.sleep(delay)
