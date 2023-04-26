# Docker Swarm
In this video we are going to look into docker swarm 

![](swarm-diagram.png)

# Manager nodes
### Manager nodes handle cluster management tasks:

- maintaining cluster state
- scheduling services
- serving swarm mode HTTP API endpoints

# Worker nodes
Worker nodes are also instances of Docker Engine whose sole purpose is to execute containers. Worker nodes dont participate in the Raft distributed state, make scheduling decisions, or serve the swarm mode HTTP API.


- To check if docker swarm is active
```docker
docker node ls
```