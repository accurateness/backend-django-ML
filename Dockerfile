# Base Image

FROM python:3.6


RUN apt-get update --allow-releaseinfo-change && apt-get install -y --no-install-recommends \
    tzdata \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /backend
COPY . /backend
RUN pip install -r requirements.txt

ARG DEFAULT_PORT=8000

EXPOSE ${DEFAULT_PORT}


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]