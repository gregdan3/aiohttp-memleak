# aiohttp memtest

`aiohttp` has a memory leak, demonstrated in [issue #4833](https://github.com/aio-libs/aiohttp/issues/4833).

## Demonstration

`make build up` to see the issue in action. This will run every most recent Python version from 3.5 to 3.10, and output the results on your terminal.

There are also definitions for 3.4 and 3.11, but these both do not support this test (3.4 for syntax, 3.11 for `asyncio` changing its contract). You can `make bbuild bup` for these.
