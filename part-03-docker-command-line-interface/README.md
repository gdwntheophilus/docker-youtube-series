
# Docker command line interface

- Execute below command to check docker infor
```bash
docker info
docker --version
(or)
docker -v
```

- Using existing containers
```bash
docker run --detach --interactive --tty --name myfirstcontainer alpine:latest
(or)
docker run -dit --name myfirstcontainer alpine:latest
```

- Entering into a container
```bash
docker exec -it <containerid> /bin/sh
```

- Dynamically running a command
```bash
docker run -it busybox:latest ping -c 6 localhost
```

- Docker help
```bash
docker --help
docker run --help
docker volume --help
docker image --help
docker build --help
```