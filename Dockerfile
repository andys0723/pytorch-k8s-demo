# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy your code
COPY ./distributed_demo.py /app/

# Install PyTorch CPU wheels (ARM-compatible)
RUN pip install --upgrade pip \
    && pip install --no-cache-dir torch torchvision

# Default command
CMD ["python", "distributed_demo.py", "&&", "tail", "-f", "/dev/null"]
