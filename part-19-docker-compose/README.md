# Creating docker service
In this video we will see how we can create docker as a service

# we will need to install docker compose

- Redis Compose File

```docker
version: "3.9"
services:
  web:
    environment:
      - DEBUG=1
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
      - logvolume01:/var/log
    depends_on:
      - redis
  redis:
    image: redis
volumes:
  logvolume01: {}
```

- Run below command to start the docker compose file
``` docker 
docker compose up 
# if you want to run as demon or background process
docker compose -d up
```

# if we want to pass in environment file
```docker
version: "3.9"
services:
  web:
    env_file:
      - app.env
    environment:
      - DEBUG=1
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
      - logvolume01:${logpath}
volumes:
  logvolume01: {}
```

``` docker 
docker compose up 
# if you want to run as demon or background process
docker compose -d up
```


# if we want to pass in environment variable
```docker
version: "3.9"
services:
  web:
    environment:
      - DEBUG=1
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
      - logvolume01:${logfile}
volumes:
  logvolume01: {}
```


``` docker 
#export into environment variable
export logfile=/var/log/
docker compose up 
# if you want to run as demon or background process
docker compose -d up
```

- you can validate by providing below
```docker 
docker inspect <containerId>
```
