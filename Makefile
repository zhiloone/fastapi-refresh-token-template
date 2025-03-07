run:
	uv run fastapi dev src/main.py

docker-run:
	docker compose up --build --watch

fix:
	uv run ruff check --fix

format:
	uv run ruff format