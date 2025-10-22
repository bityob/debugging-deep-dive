FROM python:3.13-slim

WORKDIR /app

RUN pip install flask remote-pdb pdbpp

COPY fifo_app.py .

CMD ["python", "fifo_app.py"]
