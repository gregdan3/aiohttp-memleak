build:
	docker compose build
up:
	docker compose up

bbuild:
	docker compose --profile buggy build
bup:
	docker compose --profile buggy up

lbuild:
	pdm sync
lup:
	pdm run ./aiohttp_example.py
