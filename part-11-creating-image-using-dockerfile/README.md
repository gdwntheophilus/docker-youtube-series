# Creating images using Dockerfile
In this tutorial we will be seeing how to create a image using docker file

# Sample Dockerfile
- Docker file sample for http server
```docker
ARG image=ubuntu
FROM ${image} 
ENV workdir=/var/www/html
RUN apt-get update 
RUN apt-get install -y apache2 
RUN apt-get install -y apache2-utils 
RUN apt-get clean 
WORKDIR ${workdir}
EXPOSE 80 
CMD ["apache2ctl", "-D", "FOREGROUND"]
```

![](DockerrunState.png)

- Docker command to build the file
``` bash
docker build -t myfirstimage .
```
- Docker command to run out image
``` bash
docker run -p 80:80 myfirstimage
```

- How can we pass build variable
``` bash
docker build -t myfirstimage --build-arg image=ubuntu .
```

- Attaching a volume and testing if appearing on browser
``` bash
docker run -p 80:80 -v /User/godwin/docker/volume:/var/www/html myfirstimage
```