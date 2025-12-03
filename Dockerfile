FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    chromium \
    chromium-driver \
    wget \
    curl \
    git \
    unzip \
    qemu-system-arm \
    qemu-utils \
    net-tools \
    iputils-ping \
    vim && \
    ln -sf /usr/bin/chromium /usr/bin/google-chrome && \
    pip3 install --upgrade pip && \
    pip3 install \
    requests \
    selenium \
    pytest \
    locust \
    urllib3 \
    pytest-html \
    pytest-xdist && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jenkins