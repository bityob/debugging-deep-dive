# 07-fifo

First shell -
```
mkfifo fifo_stdin
mkfifo fifo_stdout
cat fifo_stdout & cat > fifo_stdin
```

Second shell -
```
uv run fifo_app.py
```

Third shell -
```
uvx --from httpie http POST :5555/process data:='["1", "two"]'
```
