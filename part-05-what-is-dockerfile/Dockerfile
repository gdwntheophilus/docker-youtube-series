
ARG imagename
FROM ${imagename} 
LABEL "website.name"="geeksforgeeks website"
USER root
WORKDIR /
COPY test.txt /
ADD text.txt /
ENV author godwin
RUN apt-get update 
RUN apt-get install -y apache2 
RUN apt-get install -y apache2-utils 
RUN apt-get clean 
EXPOSE 80 

VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]
CMD ["apache2ctl", "-D", "FOREGROUND"]