import asyncio
import logging
import sys
from pythonosc.osc_server import AsyncIOOSCUDPServer
import config
from dispatcher import dispatcher

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

async def main():
    loop = asyncio.get_running_loop()
    server = AsyncIOOSCUDPServer((config.OSC_SERVER_IP, config.OSC_SERVER_PORT), dispatcher, loop)
    return await server.create_serve_endpoint()

loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
loop.run_forever()
