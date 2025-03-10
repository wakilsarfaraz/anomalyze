# Use Python 3.11 with preconfigured data science tools
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Set environment variables for better debugging/logging
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONPATH=/workspace/src

# Set working directory
WORKDIR /workspace

# Copy and install dependencies first (Leverages Docker caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /workspace

# Expose necessary ports
EXPOSE 8000

# Start FastAPI using Uvicorn with better process handling
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
