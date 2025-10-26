## 05-remote-pdb

#### First shell
```
cd 05-remote-pdb
docker build -t flask-debug .
docker run --name flask-debug flask-debug
```

#### Second shell
```
docker exec -it flask-debug bash -c "until telnet 127.0.0.1 4444; do sleep 2; done"
```

#### Third shell
```
docker exec -it flask-debug bash
curl -X POST -H "Content-Type: application/json" -d '{"data": ["1", "two"]}' http://localhost:5555/process
```
