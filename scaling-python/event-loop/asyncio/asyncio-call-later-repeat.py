# Runs every 1 seconds

import asyncio

loop = asyncio.get_event_loop()


def hello_world():
    loop.call_later(1, hello_world)
    print("Hello world!")


loop = asyncio.get_event_loop()
loop.call_later(1, hello_world)
loop.run_forever()
