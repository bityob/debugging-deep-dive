FROM python:3.9-slim

WORKDIR /app

RUN pip install flask remote-pdb pdbpp

COPY fifo_app.py .

CMD ["python", "fifo_app.py"]
