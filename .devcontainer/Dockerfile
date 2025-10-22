# syntax=docker/dockerfile:1

# Use Microsoft's official Dev Container Python 3.12 image as base
ARG VARIANT=3.12-bookworm
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# Avoid prompts from apt and set locale
ENV DEBIAN_FRONTEND=noninteractive

# Update and install essential development utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    wget \
    vim \
    openssh-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and basic Python build tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install commonly used Python dev tools and formatters
RUN pip install --no-cache-dir black flake8 pytest mypy poetry

# Create a non-root user for VS Code (matches devcontainer.json "remoteUser")
USER vscode

# Set workspace directory
WORKDIR /workspace

# Copy requirements if available and install them
COPY requirements.txt* ./
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Default shell session on container start
CMD ["bash"]
