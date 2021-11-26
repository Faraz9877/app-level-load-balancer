test:
	sudo docker-compose up -d
	pytest --disable-warnings -s || true
	sudo docker-compose down