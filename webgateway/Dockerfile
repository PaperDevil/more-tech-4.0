FROM python:3.10-slim as builder

WORKDIR /telemed

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt install nano && \
    apt install -y gcc python3-dev musl-dev libffi-dev

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

FROM python:3.10-slim

COPY --from=builder /opt/venv /opt/venv

WORKDIR /telemed
COPY . .

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/opt/venv/bin:$PYTHONPATH"