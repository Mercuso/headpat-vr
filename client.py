import asyncio
import time
import logging
from zeroconf.asyncio import (
    AsyncZeroconf,
)
import config

class ClientProtocol:
    def connection_made(self, transport):
        logging.info("Connection made")

    def datagram_received(self, data, addr):
        logging.debug(f"Recieved: {data.decode()}")

    def error_received(self, exc):
        logging.error("UDP socket error", exc_info=exc)

    def connection_lost(self, exc):
        logging.info("Connection closed")

udp_transport = None

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
    loop = asyncio.get_running_loop()
    return await loop.create_datagram_endpoint(
        lambda: ClientProtocol(),
        remote_addr=(patstrap_ip, 4210)
    )

async def get_udp_transport():
    global udp_transport
    if not udp_transport or udp_transport.is_closing():
        transport, _ = await open_socket_connection()
        udp_transport = transport
    return udp_transport
