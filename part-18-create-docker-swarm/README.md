# How to create docker swarm

- How to get Manager instance
``` bash
ifconfig 
(or)
ipconfig getifaddr en0
```
- Execute below command in master instance
``` docker
docker swarm init --advertise-addr <MANAGER-IP>
```
- how to check if Swarm is active
``` docker
docker info # we will be able to see swarm active
```
- How we can join the cluster

```docker
docker swarm join --token SWMTKN-1-xxxxxxxxxxxxxxxxxx-2r1xbrq28heh2p3eorvp999r1 192.168.0.1:2377
docker
```
- If you have forgotten on how to get the token, run below command in the manager
```docker
docker swarm join-token worker
```
- How to check if the nodes are part of docker swarm

```docker
docker node ls
```