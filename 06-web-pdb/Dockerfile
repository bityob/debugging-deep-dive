FROM python:3.13-slim

WORKDIR /app

RUN pip install flask web-pdb

COPY web_pdb_app.py .

CMD ["python", "web_pdb_app.py"]
