# Rate My Realtor

Rate my realtor is an application where you can rate and create realtor profiles on demand. This application aims to stop the hassle of getting bad realtors. Rate them and find them all in one!


## Docker Initial Instructions:

### To ssh in the container:

```
docker exec -it "container name" /bin/bash
```

### To get the logs of the container

```
docker logs "container name" -f
```

### Allow permission to the mysql db before you can start working

```
docker exec -it "MYSQL container name" /bin/bash
```

```
mysql -u root -p
```

```
show databases;
```


Find the database you want to use and input at the bottom command

```
GRANT ALL PRIVILEGES ON `database name`.* TO 'web'@'%';
```

### Note: 'web'@'%' depends on the user you write on the application it self in settings.py

### After allowing permissions run the following:
```
docker exec -it "container name" /bin/bash
```

```
python manage.py migrate
```

### To restart the containers

```
docker-compose down
```
```
docker-compose up
```

### Once you have created the application make sure to set the environment variables - For security purposes only

```
heroku config:set DEBUG=False ALLOWED_HOSTS='*' 
heroku config:set SECRET_KEY='<SECRET KEY FROM ABOVE>'
```

## To do:

https://trello.com/b/lubOUyYw/rate-my-realtor


### References:

https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/
