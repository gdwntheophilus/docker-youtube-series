# Install docker on a AWS EC2 server

In this video we will be seeing how to install docker in AWS EC2 instance

# Prerequisites
- This tutorial assumes you have a EC2 or a VM Server where you will be installing Docker

# Installation steps
- Connect to EC2 instance

```bash
ssh -i  docker-ec2-key-pair.pem ec2-user@ec2-3-89-91-252.compute-1.amazonaws.com
```

- Copy and run below commands on the EC2 instance
```bash
yum update -y 
yum -y install docker
systemctl start docker.service
```
