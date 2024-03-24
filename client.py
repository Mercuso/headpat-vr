import asyncio
import time
from zeroconf.asyncio import (
    AsyncZeroconf,
)
import config

tcp_transport = None

async def get_patstrap_ip() -> str | None:
    info = await AsyncZeroconf().async_get_service_info("_http._tcp.local.", f"{config.DEVICE_MDNS_NAME}._http._tcp.local.")
    if not info:
        return None
    addresses = info.parsed_scoped_addresses()
    return addresses[0]

async def open_socket_connection():
    patstrap_ip = None
    while not patstrap_ip:
        patstrap_ip = await get_patstrap_ip()
        time.sleep(1)
    return await asyncio.open_connection(patstrap_ip, 8888)

async def get_tcp_transport():
    global tcp_transport
    if not tcp_transport or tcp_transport.is_closing():
        reader, writer = await open_socket_connection()
        tcp_transport = writer
    return tcp_transport
