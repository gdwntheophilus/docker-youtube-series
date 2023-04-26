# Docker volumes

In this video we are going to see how we can create and docker images

## Docker volumes
### Named docker volumes
- Creating docker volumes
Below we are creating docker named volumes
```docker
docker volume create myvol
````

- Inspecting docker volumes
```docker 
docker volume inspect myvol
```
- how do we attach docker named volume 
```docker
docker run -dit -v myvol:/var/www/html/myvol myfirstimage
````

- How to verify 
```docker
docker exec -it <containerid> ls -lrt /var/www/html
```
-----------
### Unnamed volume
- we can create unabled volumes but mentioning the path 
```docker
docker run -p 80:80 -v /Users/godwin/docker/volumes/:/var/www/html myfirstimage
````

- How to verify 
```docker
docker exec -it <containerid> ls -lrt /var/www/html
```
