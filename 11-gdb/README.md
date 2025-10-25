### build
```
docker buildx build --platform=linux/amd64 -t gdb .
```

### bash
```
docker run -it --rm --platform linux/amd64 gdb
```

### run on docker
```
.venv/bin/python debugging_with_gdb.py
```

### gdb on docker:
```
ls -la
gdb .venv/bin/python <core-file-name>
```
