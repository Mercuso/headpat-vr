import asyncio
import time
import logging
import json
from websockets.asyncio.server import broadcast
from storage import storage, WS_CONNECTIONS
from client import get_udp_transport, udp_client_protocol

def data_received_callback (data, addr):
    storage.last_hb_received_at_ts = time.time()
    logging.debug('[HB] Device replied')

async def ping_device():
    udp_client_protocol.register_data_received_callback(data_received_callback)
    while True:
        transport = await get_udp_transport()
        now = time.time()
        if transport:
            logging.debug('[HB] Ping device')
            transport.sendto(b'\x00')
            storage.last_hb_received_at_ts = 0.0
            await asyncio.sleep(4)
            if storage.last_hb_received_at_ts == 0.0:
                logging.debug('[HB] device is offline (no response in 4 sec)')
                if storage.is_device_online:
                    storage.is_device_online = False
                    broadcast(WS_CONNECTIONS, json.dumps({"type": "deviceStatus", "value": False}))
            else:
                if not storage.is_device_online:
                    storage.is_device_online = True
                    broadcast(WS_CONNECTIONS, json.dumps({"type": "deviceStatus", "value": True}))
                await asyncio.sleep(6)
        else:
            await asyncio.sleep(2)

