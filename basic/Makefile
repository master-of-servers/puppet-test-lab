run:
	docker-compose up -d --force-recreate --build
	sleep 40
	docker exec -it basic-puppetagent /bin/bash -c "puppet agent -t --waitforcert=120"

destroy:
	docker-compose stop
	docker-compose rm -f
