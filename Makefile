
local-start-docker-compose:
	 docker-compose -f ./docker/local/docker-compose.yaml --env-file .env up -d --build

start-test:
	cd tests && pytest
