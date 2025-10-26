FROM python:3.13-slim

WORKDIR /app

RUN apt update && apt install -y curl telnet

RUN pip install flask remote-pdb pdbpp

COPY app.py .

CMD ["python", "app.py"]
