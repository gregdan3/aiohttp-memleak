build:
	docker compose build
run:
	docker compose run

lbuild:
	pdm sync
lrun:
	pdm run ./aiohttp_example.py
