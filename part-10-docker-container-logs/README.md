# Docker container Logs
In this tutorial we are going to see how we can see docker log information 

### Docker logs

- to understand docker logs we will create a image, below is the Docker file for our image

```dockerfile
FROM python
WORKDIR /apps
COPY run.py /apps/run.py
ENTRYPOINT [ "python","/apps/run.py"]
```
- we will build our image
```docker 
docker build -t myfirstimage .
```

- now we will run our image 
```docker 
docker run -dit myfirstimage 
``` 

- To check the logs we will use below command 
```docker 
docker logs <containerId> 
```

- now if you want to view the continious rolling log file 
```docker 
docker logs -f <containerId>
```