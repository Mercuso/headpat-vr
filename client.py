import asyncio
import logging
from zeroconf.asyncio import (
    AsyncZeroconf,
)
from zeroconf import NotRunningException
import config

class ClientProtocol:
    def connection_made(self, transport):
        logging.info("[UDP client] Connection made")

    def datagram_received(self, data, addr):
        logging.debug(f"[UDP client] Recieved: {data.decode()}")
        for cb in self._callbacks:
            cb(data, addr)

    def error_received(self, exc):
        logging.error("[UDP client] socket error", exc_info=exc)

    def connection_lost(self, exc):
        logging.info("[UDP client] Connection closed")

    _callbacks = []

    def register_data_received_callback(self, lambda_fn):
        if len(self._callbacks) > 10:
            raise Exception("Too many callbacks")
        self._callbacks.append(lambda_fn)

udp_transport = None

async def get_device_ip() -> str | None:
    try: 
        info = await AsyncZeroconf().async_get_service_info("_http._udp.local.", f"{config.DEVICE_MDNS_NAME}._http._udp.local.")
    except NotRunningException:
        logging.error('[mDNS] NotRunningException')
        info = None
    if not info:
        logging.debug('[mDNS] IP not found')
        return None
    addresses = info.parsed_scoped_addresses()
    return addresses[0]

async def open_socket_connection():
    device_ip = await get_device_ip()
    if not device_ip:
        return (None, None)
    loop = asyncio.get_running_loop()
    return await loop.create_datagram_endpoint(
        lambda: ClientProtocol(),
        remote_addr=(device_ip, config.DEVICE_PORT),
    )

async def get_udp_transport():
    global udp_transport
    if not udp_transport or udp_transport.is_closing():
        logging.debug('[TMP] NO TRANSPORT. opening connection')
        transport, _ = await open_socket_connection()
        udp_transport = transport
    return udp_transport
