print("hello world")

breakpoint(stdin=open("/tmp/fifo_stdin"), stdout=open("/tmp/fifo_stdout", "w"))

breakpoint()

print("EOF")
