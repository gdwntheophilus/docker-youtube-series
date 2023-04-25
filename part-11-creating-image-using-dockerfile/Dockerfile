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