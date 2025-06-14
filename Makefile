VER = 1.6

docker_build:
	DOCKER_BUILDKIT=1 docker buildx build --platform linux/amd64 --push -t registry.digitalocean.com/fanclash/fanclash-admin:$(VER) .
