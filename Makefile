run:
	uv run fastapi dev src/main.py

docker-run:
	docker compose up --build --watch