#!/usr/bin/env python
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor

import aiohttp
from memory_profiler import profile

_log = logging.getLogger(__name__)

LOG_FORMAT = (
    "[%(asctime)s] [%(filename)22s:%(lineno)-4s] [%(levelname)8s]    %(message)s"
)


async def grab_data(url, session):
    async with session.get(url) as response:
        data = await response.read()
    return data


@profile
async def quicktest():
    url = "https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf"
    session = aiohttp.ClientSession()
    jobs = [grab_data(url, session) for _ in range(5)]
    jobs_result = await asyncio.gather(*jobs)
    if not all(jobs_result):  # sanity check
        _log.info("Something didn't give back data")
    await session.close()


@profile
def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(quicktest())
        # memory usage should be back to normal
        _log.info("Completed example")
    except KeyboardInterrupt:
        _log.info("shutting down...")
        loop.stop()


if __name__ == "__main__":
    main()
