
### Manual

To build this container run in the folder of the `docker-compose`-file: 

1. `docker-compose up --build -d`
3. Open you favourite browser and go to [0.0.0.0]
4. To shutdown run `docker-compsose down`




#### Dockerfile

The static files are mounted wih the volumes of the `docker-compose` files! However if you change the static files make sure, you remove the volumes with `docker volumes prune` or run `docker-compsose down -v`. Those commands remove the volumes and if you run `docker-compose build` again the volumes will be mounted again correctly :smile: You can inspect all listed mounted files in the menu

#### Templates

To include the static files in your templates you can insert in e.g. in your header:
```css
<link rel="stylesheet" href="{% static 'demo/css/main.css' %} ">
```


#### Getting token
To get the token,
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"vuser","password":"vuser"}' http://0.0.0.0:80/api-token-auth/ 
```

If the user vuser does not exist, create it with

```

```


Sample query

```
curl -H "Authorization:Bearer <Token>" http://0.0.0.0/videos/?format=json
```


