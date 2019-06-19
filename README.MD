To use docker:

To ssh in the container:

```docker exec -it "container name" /bin/bash```

To get the logs of the container

```docker logs "container name" -f ```

Allow permission to the mysql db before you can start working

```docker exec -it "MYSQL container name" /bin/bash```
```mysql -u root -p```
```show databases;```
Find the database you want to use and input at the bottom command
```GRANT ALL PRIVILEGES ON `databse name`.* TO 'web'@'%';```

Note: 'web'@'%' depends on the user you write on the application it self in settings.py

After allowing permissions run the following:

```docker exec -it "container name" /bin/bash```
```python manage.py migrate```

Restart the containers

```docker-compose down```
```docker-compose up```

Should be ready to go

References:

https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/
