#!/usr/bin/env python
import logging
import requests
from memory_profiler import profile

_log = logging.getLogger(__name__)

LOG_FORMAT = (
    "[%(asctime)s] [%(filename)22s:%(lineno)-4s] [%(levelname)8s]    %(message)s"
)


def grab_data(url, session):
    with session.get(url) as response:
        data = response.content
    return data


@profile
def quicktest():
    url = "https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf"
    session = requests.Session()
    jobs_result = [grab_data(url, session) for _ in range(5)]
    if not all(jobs_result):  # sanity check
        _log.info("Something didn't give back data")
    session.close()


@profile
def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    try:
        quicktest()
        # memory usage should be back to normal
        _log.info("Completed example")
    except KeyboardInterrupt:
        _log.info("shutting down...")


if __name__ == "__main__":
    main()
