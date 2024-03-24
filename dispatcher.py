import asyncio
from pythonosc.dispatcher import Dispatcher
import handlers

def wrap(func):
    def async_func(*args, **kwargs):
        loop = asyncio.get_running_loop()
        loop.create_task(func(*args, **kwargs))
    return async_func

dispatcher = Dispatcher()

dispatcher.map("/avatar/parameters/pat_left", wrap(handlers.pat_left_handler))
dispatcher.map("/avatar/parameters/pat_right", wrap(handlers.pat_right_handler))
