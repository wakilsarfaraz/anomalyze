# Use Python 3.11 with preconfigured data science tools
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Set working directory
WORKDIR /workspace

# Ensure MongoDB data directory exists
RUN mkdir -p /var/lib/mongodb

# Expose necessary ports
EXPOSE 8000

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /workspace

# Start FastAPI using Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
