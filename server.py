import asyncio
import logging
import sys
import websockets
from aiohttp import web
from pythonosc.osc_server import AsyncIOOSCUDPServer
import config
from dispatcher import dispatcher
from ws import register
from heartbeat import ping_device

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

async def osc_main():
    loop = asyncio.get_running_loop()
    server = AsyncIOOSCUDPServer((config.OSC_SERVER_IP, config.OSC_SERVER_PORT), dispatcher, loop)
    return await server.create_serve_endpoint()

async def ws_main():
    async with websockets.serve(register, "localhost", 8765) as server:
        await server.serve_forever()

async def handler(request):
    html = open('index.html', "r")
    return web.Response(text=html.read(), content_type='text/html')
async def http_main():
    server = web.Server(handler)
    runner = web.ServerRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 9000)
    await site.start()

async def heartbeat_main():
    await ping_device()

async def main():
    task1 = asyncio.create_task(osc_main())
    task2 = asyncio.create_task(ws_main())
    task3 = asyncio.create_task(heartbeat_main())
    task4 = asyncio.create_task(http_main())
    await asyncio.gather(task1, task2, task3, task4)

asyncio.run(main())
