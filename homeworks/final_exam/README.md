#### From the mac or PC terminal window

1. For Question 1, 2
```shell
mongorestore --port <port number> -d enron -c messages <path to BSON file>
```

2. For Question 3
```shell
mongo final3-validate-mongo-shell.js
```

3. For Question 7
```
mongoimport --drop -d music -c albums albums.json
mongoimport --drop -d music -c images images.json
```