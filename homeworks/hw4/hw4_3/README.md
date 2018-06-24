#### From the mongo shell:

```js
use blog
db.posts.drop()
```

#### From the mac or PC terminal window
```shell
mongoimport --drop -d blog -c posts posts.json
```