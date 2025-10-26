### build
```
docker buildx build --platform=linux/amd64 -t gdb .
```

### bash
```
docker run -it --rm --platform linux/amd64 gdb
```

### run from docker bash
```
.venv/bin/python debugging_with_gdb.py
```

### gdb from docker bash
```
ls -la
gdb .venv/bin/python <core-file-name>
```
