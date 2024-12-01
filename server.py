import asyncio
import logging
import sys
import websockets
from pythonosc.osc_server import AsyncIOOSCUDPServer
import config
from dispatcher import dispatcher
from ws import register

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

async def osc_main():
    loop = asyncio.get_running_loop()
    server = AsyncIOOSCUDPServer((config.OSC_SERVER_IP, config.OSC_SERVER_PORT), dispatcher, loop)
    return await server.create_serve_endpoint()

async def ws_main():
    async with websockets.serve(register, "localhost", 8765) as server:
        await server.serve_forever()

async def main():
    task1 = asyncio.create_task(osc_main())
    task2 = asyncio.create_task(ws_main())
    await asyncio.gather(task1, task2)

asyncio.run(main())
