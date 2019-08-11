docker-compose stop
docker-compose rm -f
if [[ -f pwn.sh ]]; then
  rm pwn.sh
fi
