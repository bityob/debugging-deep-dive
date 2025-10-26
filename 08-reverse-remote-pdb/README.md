# 08-reverse-remote-pdb

First, deploy the lambda to AWS.

Then =>

First shell - Listen to incoming connections
```
nc -l 4444
```

Second shell - Tunnel local machine to the internet using `ngrok`
```
ngrok tcp 4444
```

Third shell - Trigger the lambda manually
```
sls invoke -f hello
```
