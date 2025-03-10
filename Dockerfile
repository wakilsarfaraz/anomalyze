# Use Python 3.11 with preconfigured data science tools
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Set environment variables for better debugging/logging
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONPATH=/workspace/src

# Set working directory
WORKDIR /workspace

# Install MongoDB tools
RUN apt update && apt install -y wget gnupg && \
    wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - && \
    echo "deb http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt update && \
    apt install -y mongodb-org-tools

# Copy and install dependencies first (Leverages Docker caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /workspace

# Copy environment file explicitly (ensures it's available inside the container)
COPY .env /workspace/.env

# Expose necessary ports
EXPOSE 8000

# Start FastAPI using Uvicorn with better process handling
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
