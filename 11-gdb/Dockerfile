FROM ubuntu:22.04


RUN apt update && \
    apt install -y \
    libxml2-dev \
    libxmlsec1-dev \
    libxmlsec1-openssl \
    pkg-config \
    libtool \
    python3-dev \
    build-essential \
    gdb

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /opt/app

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY debugging_with_gdb.py .
