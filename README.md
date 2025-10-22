# Debugging Deep Dive

## 01-ide

## 02-pdb

## 03-pdbpp

## 04-ipython
```
uv run jupyter
```

## 05-remote-pdb
```
# 1st shell
(cd 05-remote-pdb && docker build -t flask-debug .)
docker run -p 5555:5555 -p 4444:4444 flask-debug

# 2st shell
curl -X POST -H "Content-Type: application/json" -d '{"data": ["1", "two"]}' http://localhost:5555/process
```
