# Create Docker Images and Containers
In this tutorial we will be seeing on how to create Docker images and how we can run and create containers

### Create Docker Images

- Create the Dockerfile
``` docker
ARG image=ubuntu
FROM ${image}
ADD index.html /var/www/html/index.html
RUN apt-get update 
RUN apt-get install -y apache2 
RUN apt-get install -y apache2-utils 
RUN apt-get clean 
WORKDIR /var/www/html
EXPOSE 80 
CMD ["apache2ctl", "-D", "FOREGROUND"]
```

- Create Container or running Docker images

```docker
docker run -dit -p 80:80 myfirstimage
```

- Check if the container process is running

```docker
docker ps 
```
