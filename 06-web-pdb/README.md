# 06-web-pdb

First shell -
```
docker run -it -p 4444:4444 -p 5555:5555 webpdb
```

Second shell -
```
uvx --from httpie http POST :4444/process data:='["1", "two"]'
```

Now, open browser to see the web pdb - http://localhost:5555
